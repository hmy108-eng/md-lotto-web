from __future__ import annotations
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, roc_auc_score
from .stats import number_stats

FEATURES=['z_score','current_gap','mean_gap','count_20','count_50','count_100']

def _features_at(df):
    ns=number_stats(df).sort_values('number')
    X=ns[FEATURES].copy()
    X['mean_gap']=X.mean_gap.fillna(7.5)
    return X.to_numpy(float)

def build_panel(df,start_train=150,end_idx=None,feature_cache=None):
    end_idx=len(df) if end_idx is None else min(end_idx,len(df))
    X=[]; y=[]; draw_ids=[]
    for idx in range(start_train,end_idx):
        if feature_cache is not None and idx in feature_cache:
            feat=feature_cache[idx]
        else:
            feat=_features_at(df.iloc[:idx])
            if feature_cache is not None:
                feature_cache[idx]=feat
        target={int(df.iloc[idx][f'n{i}']) for i in range(1,7)}
        X.append(feat)
        yy=np.zeros(45,dtype=np.int8)
        yy[np.fromiter(target,dtype=int)-1]=1
        y.append(yy)
        draw_ids.extend([idx]*45)
    if not X:
        return np.empty((0,len(FEATURES))),np.array([]),np.array([])
    return np.vstack(X),np.concatenate(y),np.asarray(draw_ids)

def _model():
    return make_pipeline(StandardScaler(),LogisticRegression(max_iter=500,C=.5,solver='lbfgs'))

def train_evaluate(df,start_train=150,max_training_draws=500,test_fraction=.25):
    use=df.iloc[-(max_training_draws+start_train):].reset_index(drop=True) if len(df)>max_training_draws+start_train else df.reset_index(drop=True)
    st=min(start_train,max(50,len(use)//3))
    cache={}
    X,y,draw_ids=build_panel(use,st,feature_cache=cache)
    if len(np.unique(y))<2 or len(np.unique(draw_ids))<20:return {'available':False}
    unique=np.unique(draw_ids); cut=unique[max(1,int(len(unique)*(1-test_fraction)))-1]
    train=draw_ids<=cut; test=draw_ids>cut
    model=_model().fit(X[train],y[train])
    p=np.clip(model.predict_proba(X[test])[:,1],1e-7,1-1e-7)
    base=np.repeat(6/45,len(p))
    ll=float(log_loss(y[test],p)); bll=float(log_loss(y[test],base))
    return {'available':True,'train_rows':int(train.sum()),'test_rows':int(test.sum()),
            'roc_auc_out_of_sample':float(roc_auc_score(y[test],p)),
            'log_loss_out_of_sample':ll,'baseline_log_loss':bll,
            'logloss_delta_vs_baseline':ll-bll,'beats_constant_logloss':bool(ll<bll)}

def walk_forward_ml(df,start_train=300,max_tests=30,training_window=450):
    rows=[]; indices=list(range(start_train,len(df)))[-max_tests:]
    for idx in indices:
        hist_start=max(0,idx-training_window-start_train)
        hist=df.iloc[hist_start:idx+1].reset_index(drop=True)
        local_test=len(hist)-1
        local_start=min(start_train,max(100,local_test//2))
        cache={}
        X,y,dids=build_panel(hist,local_start,end_idx=local_test,feature_cache=cache)
        if len(np.unique(dids))<20:continue
        model=_model().fit(X,y)
        xt=_features_at(hist.iloc[:local_test])
        target={int(hist.iloc[local_test][f'n{i}']) for i in range(1,7)}
        yt=np.zeros(45,dtype=np.int8); yt[np.fromiter(target,dtype=int)-1]=1
        p=np.clip(model.predict_proba(xt)[:,1],1e-7,1-1e-7)
        base=np.repeat(6/45,45)
        rows.append({'draw_no':int(hist.iloc[local_test].draw_no),
                     'log_loss':float(log_loss(yt,p)),
                     'baseline_log_loss':float(log_loss(yt,base)),
                     'auc':float(roc_auc_score(yt,p)),
                     'top6_hits':int(yt[np.argsort(p)[-6:]].sum())})
    if not rows:return {'available':False,'tests':0,'rows':[]}
    ll=np.array([r['log_loss'] for r in rows]); bl=np.array([r['baseline_log_loss'] for r in rows])
    return {'available':True,'tests':len(rows),'mean_log_loss':float(ll.mean()),
            'mean_baseline_log_loss':float(bl.mean()),
            'mean_delta_vs_baseline':float((ll-bl).mean()),
            'beats_baseline_draws':int((ll<bl).sum()),
            'mean_auc':float(np.mean([r['auc'] for r in rows])),
            'mean_top6_hits':float(np.mean([r['top6_hits'] for r in rows])),
            'rows':rows}
