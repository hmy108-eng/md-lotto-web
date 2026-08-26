# MD LOTTO 6/45 v3.1 MOBILE WEB — two-file deployment edition
# Upload only this file and requirements.txt to GitHub/Streamlit Community Cloud.
import base64 as _b64, zlib as _zlib, json as _json, tempfile as _tempfile, sys as _sys
from pathlib import Path as _Path
_EMBEDDED = 'eNrNfYt220ay4K9gMicDQAIhPmWbMrzHk3hmvOs4s3Zyb2ZpHh6IACVEIMAAoB7W1R/sF+w/7j9sPfoJgLKcO3PPzsMi+lHdXV1dXVVdXX3/zTZZ5WXTlCerVVZkzWoV7u6+mTvfrFbXaVVnZbFaOZHjTsJhOHQ/Fd8Ejq5yHq+vmrRuRJVNVW6d1Wqzb/ZVCtWy7a6sGicuirKJGwBVfypEWhUXSblVn8V+u7tz4topdoGzgzz4Cf/bJZ8KAlqvs91dWAOUWkI9z4pyi42LInYuADxPqxWlyQLlrsm22ee0koVkwuoi3qaqWJ1t9zl1V5Zb53FdZ5s7WaLZF1lxIXPhK13dpNnFZVMHzr+/efvXv/20evf2zx9ef/jHpwL/m6QbZxs368vVutwXjbcut+dlcJMVCMafVyngq3DytPDqVOT6f8Kfsogvoaxq6Fm62qZNla1rj76CJq4u0iY4L4t9Hb0vizSoyhv64c8/FQ785zJr6mhhdUHU8p1NWTlrJyscArbkCuW+ie7dc8CuO9/Gtx4C8AN3ssv3tTuv91vv8lU0obqXWFfkT638aSe/ATrIRT6mPHBr2cahzjsZEEDZONh10XP8D9DKFXRfzoLqO4+4M4Iz7P3C3VVqZt1lhE1Wf4jcAkC7VKPCGgTa101BTwB3Zj+AehMnznNvIyDeZw8uVS1vwgwm5ZagZQLaReqNglPfN7qP/9kCNkeIzFHgjovEnY8BmRX8nQDSmkt3Pg3cGf6dPZwB/d8h/mG92UDsXrdakL3H/C11epeEMIgi9rCngC49gu2iWj640EnR1HG0ycu4wYKLVqGlbzfDqKVagFX+IRC+LmtMGw2HwyOiZZwNX2RWZQZ5HlcYGOX9E+OD2xLrAdIV2TO7YOr3quIioHkNgDRXJbCpPN5Z9L6+LOu0iBZAC3HTpNsdkL9A5s1llqe01riQ/5JA8TSLsi/HMIahgeB11Ox3eerVsN7TBDsQ1vEWU+SUT099nHZfN3gcjSy6IgrlNufrsmiyYp9aBYzBdAmwuPMUf2DecOv7r8wqSB23ug2/pxHOCePdLi0SgGOhmzMlxm/i/GoFIG/iKvGSTQCMtGpWTRVnRTQZDhn/MNeQke6iEc0EMmNMg8Q0TaLT6SxgLK2IpdXRDLAaiKms0h2XNedwEgg+as0mkGVNcwnLLVtDs3lWNwLzRr8CRFCy8alLvr8YqD7NBWHRQk0ISQKUMcc8tmQTZnm5XsyhHLSIjFQmcQqznug+K+R6KZAjLP0uG3jmw2JmrixKh8yxzpyijswdyqPGjaW2TSJ7c+ISQVELzDP92+i1vngO8J9j6LiFZeO3wrf4a7NCROg2ESukh56226i1IW2TkJoPm5ImybdYNe5LMHhYPhFTQfiB/njYzSNkHMMh9hbLnNOMV+cJ/NUtIo5XGscGLbU5bnUu6bzVxUO8hCiu212/DTb5SrgGth8Hv03jIsrj7XkSO1fpXRBX1Zz5crELMdNb3BIfx0xIKuLC16seSi9NaLu0WqcwYXkatYEseGNfvoy2W/lbA4IRWoCqdA2bV1LFN6uidOeSkkUCbOogDQpBQUGjRBIWxAZMeSw9cOa0nTkVma1dDcuS1LAi6UWWZkGCQZkbPWQSiqzdPxj6HbBisrC7K0QL1ETkcP+D6hzGJYok2fXhYslByFiNMWDWYxRwRbPktFNyapR8pAmBG6Mio6bbhIERq7yFqd7mxASvNEmtruuVBu3OdY5qEtekOzc+HizWQgIBySrb9sJN1+F+l+AiuqfpZWGDpl0KHjTvJDJQMgsPlIhgKY0EjqArI/UhkcHaWOGWumgEuFZBbIdKPZhrBnYsySZgPPZGC3LZ93ET/6UClONSqpV0D0LqNqbpkIqVd95Ixib4MSRE0VDqDPcubXDufCjQCxoD7zZQMBQT9wp+9hGzH6JUjDJLXtZ12qn38ov1mgx3Y+7VAJseMCTuS5Kuszq7TiPMOeYckG4jpbmhflMHslgQzvxwdx3n+xQHK5OdNK9TZxQOzyApb+I64h5aXGFgd1WvClOdEagS/VWMS0wnc0k9euaW/kFGoMr3ZavKBgFqnijUIEQ3t2ewSoHboMtH0ttdugbxs79pzWskhFbT0/6mp483PX1C09PHm4Z0c7JWNIvIQWg5ERgJlydYY57q2mynW0lP2UEO1Tsdl2mMVLSiv0iJ7pzo0WVKBUKhv6C1ZviF/wZunV0UJFSudisiVdmLnQ08vc6StFinq3KzSpMLKHZelrm3exkOZyTRY1OvuAW7Jsj9UNp9c7vLyypuyuoudF47KCaCQJWtQRW9c7AX2QY+igZU6xoKYQYwmHqfN1J52FVluXHgf2yPge8UZN4Gl9SuvEmr0NXqt8FokSkDStdlvt8WpoAMmRZj5jllLmzOBKYoUlLlJBs3S3JaD9G0dp8qjXPgioK7M4QeEINO+yfdHh1oxSBnSezdLvdvGb8Dst5E+mDLXEm1D/4hvbgAQgRwjyprp4ayprW08TTIigL0D5TjIO95S5cYjVuq2nNDq7NUNrk/ffoG//vjvkkrZ1805R74cuJQa2dOGq8vseOQhw06dZoDJmpHqB3OvkaDWlkAbadxlWdoo8PukR46EEOjqnXIDf0u1fDrtUJeXXdtvRBtfklkWv48UdJCq/H7yXrbYZHl4H+epOoZ4gloOtEONbViDcS3kD2XYyRNd7kMgMmUVboiI1f0U7VPDRDnTWRRHVodTbJDhAu4vjV0w1DwO9FgUqXx+ysVXprBhSs+LTuXlrS6oikKH4Sk4RJ03BUyVA/V1XS9cJmocT0SUJC4yw1sRe5SNlYABtylKM20wTKJKmElnv1uORLmoEkv7oD1QkHIht3+MRuOnpPJsM0HToeHFr7FHiZDmw98BNi0+HnRBk5NCdn6Km0cMkEHuCENQMrLY9iYZJ9hkw2d96UaAtJ27TSXqTC8EDiLBeiK0b2eLveH753zOI9hCwapxTbKg5Yqc5aB435sqv0ad8gBSALXd93StSxgKRTuezLgDHAvjvODdSmX2vkO5igZxHiqknYLrjF3JXKtdv4eZ9BKE59nedbcHWpoB6XQmHSOBCc29vjiIrq/mmslISDFdQUbFn20FOuhMvAPlSl/+ED88YrM6wrTGv7C/Q4JIr5IB8i9gZL/c60ZgL/P6ABqkwF1CInvIPSwB35otBAabYSylX/VntFrSTTthqZF8YsGxC+ZCrHWr4GHyzy48bF6CuVTnCrPWFRZk25rr3MwQdaqf66t8WgyOv71ywbHlmFNMF0+NPhDdMjkyIcpfcdg/YZHNMhHSE6IHzwOWAgCWh5HI/pUVAQpyoDFBS2C4mxheKJ8Yc+idPGb0qdGuvitB/BHx1owcxDVTRG+XsMPEIXUeeJmn+fOdDZgGgDJvczPgIEyCKc8/zVlkT6p4N9aCFZZWYSG2b+8ftIMI+xVDYWijuX+semeTr442feKh6LyCWtRUjRzR0xR/Iu4HCURS0Sm0N2bYUh+JIjkC8QBRb9AGm0W9v8BlfSbyAndL16MUODY1k82jGPh/7zR2rQJC7z1cegvIa9ljLYN0FsawbZe0kFaD267tQWqe6sr1HeriazeatPD1ab91SxlRO8QxJNjss5fXEgObG4UuFg8ja+AZtaQ+WjdkBzkzgmY3P2MOmwkYQu8heuTJugYX1JR18YrlrSs9bFhrJ+2MgQKHr4kjIZ4WMo2ktpbGL3s7dUyiOs1DBl4X/SXOK9TP6zSOm1Y+/CSqtxJFcTyQEmg0a/3Pvm1LovAAU4G3QfR9DdgOekkcPDgFiV2+JVtU+HtsYubyzw7l+D+Dp8Kju2pIl1b0t/2ODeivvwM4yTegQKsXFT+9tNPf3/NaaLovsqhpUm4b7Icht9Ud7LsB/xA8f7Prz++WX3347uff3j/0YmchTqYCfgXmmfgdzHCf8b4zwT/meI/M/znFP6h4ydkN3//8PZ/WeB6nRn02ZDlBAF7k3tDCktN3z4AfPPLTx9eW/3jaa7jPK1X8RYFf+hAvAfdSdSFzzrdZqtW2jYu9lBRJgBsDdVEwqfix7/85e13b1+/W/33jz++X/384R0W8Zg63cum2dXzk5Obm5swuUSaSas72A/Cq+okb0CnOeEd8+918w4/3xabMkzK/1ZX68t3zZtdnUT3AsUw4v8E0PfpzWNwga5/ePvhw48fVq/fvcNBoM+VbKfellcvZuFF1lzuz8OsPGHaZ3NffRLneYgU7SoY717/9ObjT18JBreAupGQFFY/vPn487sOrO2BgTMwV/s9req0Ri8yz3cGr/Ri+MipghmCIt/K8DR7qe4iIn+PSAn0ThBogCjWDf6s0jjBv3hgUm42q028BlEqCp/1GBBQfgZWBtS8TlESiLzp+EUwAwV3NhzD/yfw/6kfoLdPeQNqPGySl2VSR7A2P6cF+lws3L+++clVDL8OiaA9hRVYE8aq9nAXxQGgbkoDwQ3GqvSkOrIxNFTDWtBG2J9r0D9fX4B6787dH8rPWZ7HJ7Nw6Hg/fD94h5PrXE/QKpzGQHZneCYMkwtS5h74q3vQxOK+Xq/THcKEbSgHsRSZ5wnxzCa9bU52OQqPRydHbmsTqPW0A9/PqJfJZm5tDgHRQFahMAnC/cW+3NdzB43jgu8jmZgVBIlssxpthNFirf29LGZILjZo94YMULCE/XqpTNwCAEhDcVanzr/hxvSmqsoKmNoPnOdIo7dzL0oDV2MAV2m6i8z2js2OWHz02GaC0vWn0yc8lEo2C4S8hKzdnaR5Bdbk7k/i6La1frFeopkP2CophNna48QgxWHXkUuYcP0wrpu7XeqBatruwSMDm3e9m9ASr1D4lA6sSzywkTgmRzC9i8m6+IH7sdfOPwAGetMuGWZ1EXsw0AKQ3EMB7tuCCNZRdZwkbfjIqw8qzMgyTPa8ONLkMcjfy1KOqNmBLGwJQSVRCMJIhSKUJSsCBkG4JO+Lx00GIIHXRSQ81bBWV3tCVlYXPqjZpw6KqbBo0MNx9DK6fQm6n97voVDbBNpdPBJ3wllVuN6CVMTGOoddpZTDyAOsLuyWWloKB0HRsl4UIBATIYVxg8aSQA48KgxLtHawEu5V1nhxcDAwyqHBQUvC2RTHN39sRFzu0DgMso3oDMqQdxWZHBZjpcNmhxvS8SBOEwA10S9Pj0x7FXYJ2xbNhduMjjk7yaBm+P7xyLdxYxaRyvEfItlOW7FmjihONgR9ISXJ8v4AvwyYHd+pw4yXECwIR3NfbmsxnwyXCtv2IRhvNqgEIJJ5g+9sObSloKVejCiJjN3JR2uKRD3NjeVukTxlBpI+/Cc92LfaSjq4jxTurbGy91XNp/bcKZBSXGiLEMTp7T7oAbADBfmF2/PhoqzRC4E63AvBcfUIxJm2TmifgUJZNBs16QrVG2pqJCoJwEjqfb2PohHlPQKbxVVm8HNQkyUMTOARhDTFT0PFZVwLDykkJlB0gR/yti13tAObIvqwK1k3yS688vzX4Cq9qw2/nQyIGWizWKeUi6RokhUZ2INrYv/nv/bYCQQYMsIjaOn9c93yD4+oA9fcfKf6xnKvFyA2XAzk4U43kSbb3ZSdnP/TWhZfmGMgchdXNfpObLJ1Blogyp7oO56XcTJH9AVSkwAxHWcdCfg/EAY7Dg9emcsd8rl/AkJw7+akgpHSfPNeKs/0owLhHDNIN6JCUshFaurC+bDJ/7FVkL5n9RuhiZ8ER/xOAZwoL4Hy7tWCeg5p1BnKpV9582crUQFgucA8lrDFAWOmrlvtbLDPzfuSlPkN91R/Nf+eFerrRv5u2WKvrZmlzkjbFS7ra9+3uCmJIyB1GJ2q0986SMWOgDJJHYABU+PvMjIdCSGDz95qid/3Jf4U+0e7jwZZQ2MBsAp/bohTt4Z9o0rDDezUuPgr99On5NgNoAoxEJAhuDQKEcvF/NQwvrZXDzbDq+dAO1DAAIHObrj/ASoZjUSxNoH3lkRZhoRV41tdpJEJB/DelVR/Lur9bkf7uiNXnoM2FdQgdyUowE59Ge+UnE1D68qZ1qalXIbxwzdtVMyy8bBnMR8Nl8HR0b2Q7uZFvziIbYBA+CBXADuxkcRn8OBNij5minNgg57oCVYIUJMA4QF/R6OxzSmEPoH+JLAmleHiTOveC/dDukmrtAIZ9AlmIGUNkYsTLYw5zVjhdO1W1hniXVvyjmpybZYgQoC3jRs5uEg5ZIsRRuIvmpRDmm20fEgZqS2a8aT18t2KTEKeH8gWTIEIDQXOG/qDF+bi2gH6ZTxKRrBx72WfUfZPtShHJPhhX2BPBRH+KAmP6Jwm09nEWQ7iqOMeu85/OG74awkyArfBN+PEprHNMG0FqpN3S7uEPbsmvSLpCO95orLbheIeS23Nb/u93xrqX5eYMZe0TUHRBoZ/J3Gjpz5+cYPi1DrJrjOkyzri2wCuSnB9XO8H94JT31bZs5fkpaOqd1Q98zYYaV2q6CIbjJaGo73L5xYL2yDcX0FadPXO0GcjpkmZE9C+7KUcfE+eAHyzlmVkn/AUMCvImsWoun9QU72wbdLL6GbNlTFZDq/HUK0LqjxVum3CVkU5o6XRQBWmZaXVZDWd8+rlyCKv12FhUvixPHD+DEUH6WaDxwdckdeUBHvn0JkDutYobi8cSHfxRWr52NjcqDJ4Iw2ox1b81VzoCRuyBzvy/SiYwf7+qT76v//nf7tBFaJF0jdPThmbqADQpkQ2APihRX/B61usa94BIUVSvasIBtM3DTOb13RQ1DHMPxFBZ4o1G9xNcmS/ve2JMogus3eTIfSux6Z6qJfiCOLJXRSiWyT7ZdG10rWtI8KFxa2NGRewgL92LSPSdKKvhZY37EOAR35eBaOke5pzqwPoBYON/wSjgD5vd9KIQ9KHVBID/5jveD7BxOYfe6a9KTC6VKXoVQn7lZfeor92cTG3rN9Vui2b1EqDXhuLV5iskDNLCL400mEiA5CXxgUta4OGqhNqq5M2RsEE6qIC0oGCwCy3ZRGlfMcZ/sWjS3YtgYFTolRhYOYX7Q2Vq+NoWpOUhuj5VCxBHG1Pn8zRYjGA7jXQIe6cutxX6xTtUnSI7JSF6UhDJhMQNwDEYj42DEi489Hk8cDY1vESk1Irqc+Y+4FQJlsGIbvMQSoEHhoXDnQemhU+r7hsN+zUnJQ3xUUF0mPoGnQCDDjb3K0aEG1gg2i0xIrWK4tiyFmSl3FLr22bsS7T9VWaRMMzkpgApSzKKqnWcExgy4ayP0FxDw0v7JgpTEy+sks9KpdCx6M+oZspwhd3aBeqtSjinKX0o+2YC9p0Ud50iQVQ9DHFQzIPWsXJkkM21c+ibYEUKLKuZj9Vhi1awqtUc9SoBXB3Ln4EOkvSKLpQyI62LVCqMJFGhoDYvMbQyByGTEDW9w343Fl3zn8X88nStErFTbnN1qubKmuAm9bXHRJDF4c5OjbYrAiTQ9AI0qIJt1dJBlyUPpgPB8RqVuWVadDeJEGz3UXSkQKq1fjb28FyyG4jgogpx+4KVOv9BhPdEKq4AcCPiFPrVpF6yjpc52WdepvE7xNGzDWAp0U4PoAXsNc6HSkGmL9idSlyv/3H4Nvt4NvEZeBVCpoJ6OxYB5uWAwFBMc/vbIkZilPvaOQ1VsHjiTrcF3lWXNG3RnsdXz+CbRjpf5gY75ukAAsQPnQAENwbKbsNxdree7ZePChXFf12P9kF5mldFcQR6d6BBPBkOgHmlMI0xEmyAtaZXafJChOQonEKxRQDDe1C4otMJB4RSZicG1wcE8RMwDTgl5gHqQBAdenbEwqXAZojXOH4bdo2oQtIPVDcE9b2AIsE2WbFbUSuoBTXJC3f9LIsCuhPut4DIt3vPrwBUc/5+f3b//nzG+ft++/f/IKHfCt5CPjje96hpPruq9OkFkl2ZuquWEvRi/+wQfRfMlUH5sHV0xQywaIU7qHwFyb77U72LEiLGn2x4nqdZWItIvJgLxsHMKIYlA1c8z4UXJfk++Xum83ged/aNBBBi8BERHvwxi5pDt6SsEzikcz8QXMYkURjwvagEV5DNNROf/0DWoUBWU0jdlzICXbPA6Go2dbsQAoLeqexRAISWxfWusXxLy1t8EO6gRV2ye7EonEgqE2a34WfhBj5hrRCvGGogpjglaysSJUCqXRH3I0Q1kDCqriBEMbOEqghjGn3SAeozSlSAOHUsD8UTY41kYaatJjjGtrkGV4MQ8umFJx0b+JzCrgEKqtsjkH/BCksf3338d9QLhOUgyFdkK3SpUm6XRZv8A6aYIy429f79TpNkzo0sdW3buhqAIhXpiYRFqC9NJ8j93WdxScfQUnKkXSlEB5pbk16qCY51kYtjUgcM1lOJoKqxFHXNm3iSGuw9j5olunTVqFbVgJJYUYl07RleJHYpofooE0CwMs8wBFK0MKXkP0GraaDVmXCza15kmB2QVyc0NDpMIHpUZq5CZsowOpB+YGuYUWzQAk+6qjLpGhTFv9Z8B8ptL6MuBvSUUeVbmlTjyit+gLAW1Bs9vkV29bz+ALkzdt43RCJsptI4LDcSaSOHBM/eLVQzwEJAgMYisPYg/YVcvMV4J89IqxBtM51hf7HyBva3jwazkseePc0UsxLZE0tH9oavRB4G4x6wlUJFBo3EQUSbUuBQaSgGz56K1EdxrTpVnTjX9G9Pt1HeMw/pbu/m46kHtuaYjo+/0M0Qg56kAT+EPXOao+mLTReyeWzQh7pz51RGN4zmAflGRE4F7CE7w927AHqHOyV5RH0KIW1NUSGRvrkYLR8TFs0iMn/om+T+46bhMW3K6Hb3V1P5QCziS+qlJV8475oyxgk7D89HDY6bBEQJEG7ftQrC7TcekTeolcBXX550tUhDKui7ACqDC2gBqsWPn3T08Snb5bWVCpNSK4fM48EuAjU6Ct3TjKoi/IRaAVxw8cqYt8FdZfNLu7c1Xz7mOfzTC94wh9dgmDbd5+bq0uyApSCAikftcgJOsArtSlOe5BIDxQelTsXsZ1ci1zdub31uS3OtNK7lDtv5fX0/Oio5esk6Ck4OpKVHzqGbIF2rtEvp7LRo+MoqIbdvjVozhrL9YenjYwSnAgddckqtlrHuIsJZxua987QVOMPvWeVXZOnNUJF2lrwPqBzto2xPYZyOilBt8ymLHN1gcM4T6q1K6BtlMN2bNvb6p/o6HkR76Ds+SCm/Dg4xxKfsx0fJ+I/i9F8aR6PnO/xBjZUwqAVOcg1xcvoMtNGQT4zwc+8DC6pxQW0Nhr6gTcaBWP8Ox4FE/w7GQVT/DuFvzN/aTpE0EUeaKX4djS0gePZOiCWAnKOzG6b2PQEgGBMKzCOonPz9tmaDi7v4/Paiwfn/kEohIWx/+APZraqb16wwvvD2BkaOazPJGGeKlK/HbeQAwR9nRatMlE0bBc76F2fw9Zk1n4ZjbttXGYXl1apV9F40ilFxMARWillgLvsF5pfoyfHeo+XRld46VLEawUiQqe7R+mIvA7x7hbQHddCAvRPZodbQxdDKo19pNLAKWD+VzzDqgd0uS1ey5g68fogSDpLZzJe3WfHowd3fi3O1K/tM3VB6/5D966alOhwFfY76NpSHhENSHMx8Jpo1L6Ets2//gqaEfFYxji+ytO4KsJdtktJ6RYlt/EVzJRIbJcFRbcq1yl70YoKHxu8llYlH2GTU3fLZA0EElerbZmkuazwrryg2EIfUhBh6DywVUlcF5Xl8/JihaGLAlA/1qt4v17hteX0CYGYPxV/efP6p58/vPkYLdzPXM0NXCmSI6UEmsQgA1fAajxUP2f652g4xGthwsgtGfoKXWI2kqG2L8+jkdjy0+ZcVNp/iYp6IXun9bxfFro/y+iXUH6EmyzPi9h7Fs5s6vpF3HeA6nR/VJluz/dZjkGFijRvR+MYzYYBLIhVltxakU9lmghFgLxQJHVVX5GhwhbgiPD4547+JbEmS1qughzBoBv6QMDyWxbSqIVlI8CB/7sjHOgmfgnT24ZOW6AVAHgnvxcjMtphRaHHsc6q+aERhhe7IkerAGA/jqatmSp2YVzHVRXfeb/4gfF1Z31JYDoINy0etWn/EeOVUHBqEfgl0vFF5iA1oG4AygIsCViq5+KCO5rZsvOKJWtUK3CV17iyKIQe7mO7uMpqyN0XG2CSodV1iyd49oL3/KC7oOleGcob0fPhMPguAqpV46E5X6W4JFhu6dAmxb/AL30BAK/NkQC7qWI6FY7C8UyiZF+nKv7FwOvWPjYa8OfLAyxY+W1vONLxYRhMD9DiY5ct6ibCdWLSOW5KMDxsBK/EnZxMaN0Ed4FaL+aqhTKAmpZLKx47ZL/tU6Aa/+VYeVyqZEU+kGvEbYyvQVGhaC0sQIt1wJWinupnDmzaEacusOOjQN4H4ET/yBsNrCnxfR/U4TMZkERAehmtMWY32/NE2qs13qegax5I25EkceByjffLggAsgzvxA08RsIvrHEQEKhmK4HIrInGsAdDRES4YLYNROngWjAb4B2qeg4yPlWHngmXunZ5MZzQBO2lDz3Nx8V5uM94dgwPFEesfzkfQfvt81kA065dM7ih3s+pH3ypgHat0OjM1gtnJ3Q4jv5WbFQfFkDHcrK3Q7HLn4oLodhtMngcujgCX9EoWcufnmA6fVEXFTpQFsdoAi7QaOUeBBa1H6JLcrER9efkifwlVYEA3sLnDggKV+qcUt2t0YCjzBDoGTCu+KEpkImcYg4kPDqxobMh8a5QL0KIuuAcGHnEf+oKIr7Z5XwwqK/SUWuA3sILLm2g6a0eVoubQTDpAyh3E6Jbr/PDObN55g7HmhHxTO0DAbPkv0bcIVnHtKIpw2AIAPLrWsar+6+PLrQgSGc2HAZQctPAwMLnlGVVR3FXXx234eLR8lAXS8iLbB61+GaQNuMSZSBdd6eGTGKtd1z05GZvOFcQy2+wSQQcGWCXiaDDdu4kG51NMsyfyeA+XCu4AObctIQX7IMQU3WpbWtGFjDJfDMx01yAbYxnhKyUUI0z3o3z0tnkyC1XCTTv+cMuHuXesRjRvzXjaTLYhZtbHorolmRMf0uFc4JMH2KZopCl3pyt8IoQ7jQzYI2RfoPQOe8VicDpfHo+0j1LI75qYPmgybs2DffCLyDm8DwdGgDHeBhYynBpsPHrCq4VG1dJ4mgOqLGmXsst2sdap9MV9S4cvpgArQlHqTEPeip97cMLO8764uCpmb89eI0Kv0pbj62Z4s1HtGLcVeavx+0OkcjMGLahIO9WCSKSDIl/FjlHk0a2pM3vqt3qgwvSKqLvvMDCulsLJsU+Oy4nXFSaKcLr7ArbFgr04+MiZTmwSuang3puhuREU87i4w12Kw12FbuAI0sJ/H1rGBPVK0e99VCnAt4YuhTL+BaNlbxwbocWLSGTderxWA1ZCRDE6qAJtq9cGIGN7NUaAiDU0SXbSFYYd80wtPaAYZOPhASX+UKyEL9kK5O8J2g3a0QtE4AgMXFDUGLdgKO+owIgjr4BWtY3iBL/7DAHMyTF6SBWNfLlB/tH5IEJw0Ms9MtItxbmE6dmCfI4LyImB8CAPYOJMAHaJdIQFBSSgBHbAb0KJkwVa/65kCLVl5A2gU8KkEqJp1MeYwlfebt2wCHAUTmbOsYNDkTjplBjNDsZdNWpO+moOnQFjCxb7uQecub8P48dagPZRifFUS7N2QwPEMkE+GrdEfahU5MjyYTtACgosBPkh49EMdqE2D8NZUtMlB7vzkDztaHhBpU9EOCYNLjgKMkfqGNbA14C0pxoWemkH0VNOR9QDy2wt7ihJMFJ9BW4T4Q17v/2QEeb4L1vQMTGMk8Q79HIRjQufLLKxSN0hiMZaFfHxjJh62IjCQZUBwJo7d+b8to8T9UH2XbPbasGKjhqiEBaVwW36ELL2gzG9OsDtfaEoqfLUly8UnHZURhZApW2aphR/4uEV54gecJ740LnUKOfRT/N6YisOowy9rCIxjoZGGMZxOxrvBF/IORSOt+/pJNZl/lpBjTuO9eno/UX6faH31AbG16CicZE6P3xPYShTfmdMc2oRvrd2krRew6DxCAHZGNav8agbo/gCAGFIiG+pHeRk1QW60xphKzfOZEBmr6kMbAlMA6ikDpCugVFmyA4v0mKfSXcnqgwccQCtw5I2Ql8C17mUXvjbFPotn8TKoQN0qNv17eoPsIgEi5GI2ptTHaBGpCYGhW1F23pzU7NJx/es1YqYRkK5kRGxX0WzYftCkmqzjp7MhETN5jbq24tN6mICFpwEJzeJFp0t3VsHAEsSkvGwnu7b0gRBpnR8jkg+W3Q7v11gwH626y+DKqV4xqYK+kfnf6QpbHDOeVWC7g7CGtAlKMXwCwNCX8MWy9ApGKeOZ8pnsLCEYKvkUE1MS2Ju60voCgX14q4t5jhjxB3p2ycdFt9144V2NJ4NfXkwajwXh5xvIpkXfkzNj7H8qNItq+iRatgSS5g5q1IqpIv15pzB+8hhIaOle8YfQN4R6Huj5+K75fyng+bQe4XmsZdqtX1qL1+xo8uJREUuqipr5s/rbtwG+ercunb+5NCbc7reFx6f627y/bF8d4xSizWvmc3vJn1ZxNZ3076safu6R5HejMnIsRsPaPrw5bX0ZsJpE0qbcNqU06aUNm3B0TF7HeAU2CI+ZKPYJBHqOchwwCzxcG2AT4WErVsyMJ3TcHiETYGgMwpn+HOCMs+Yfo7x53BypF9iNBZSd2oA3itJJz3IViQE/z+T1JWZpORhmwH2Af+Z2oYYrqADEtDgLPNCRJHvFamFu3LncS2KctNLacZW/6+adZplud/vxmLZTlTKRK5qlTK1zSYLF7Ahdv5loBLkhm8k8S6/jBRKW3CU0KQ2KihM0UU8OTvBmK5tmY8y4mUn7UtiOwjz0rJOH/BWZoeZcMCsBqMVSAPvMtq4PyKZ3staD7gJ31PVB4efwKzxiRkK5kt2Y7T8gbblqu5IoHJkALUjGS40i2gzhSVtg/ybNz/pb2/Axo0OI7/Bn268J0tPFpvdV2jJX6EQP/IesRKKKWB/ldVX4sVeFctSipaUCnsFFNGPueKXcxw5bO0VDiCTkbZa1f5g6h8Nw/FQ3vffbPqdfEBRNt17jOBuVIeiKM2pwWNo/9nM7gA2nUiXj4QuBFItaHo0VMfPfW486MMjoXinA9moKA0KBYAYPlOdQvfq4tuZ5SJDUalFx2b2ySZs26NwGGCubz6f/AT5xhJ9a/SjEiUW0pjb60e1JPOUcu0wnM6ZGSMkaewC9pGYyXWToJsgQB3JGUYLN+iixrVa6WSg4lCgLYM84CK5BPrsxMaS/hyhzsvtAny+KRsoDwqKXH0BWkCnhOlZgZv99iIycrVnA+Vw7e0FX1aQzwfjN51QX7wSQuuzcGZ5cPKRNho809udNwgns6PP3KGVOAnXeaDgox/QCUAdjPyjozG/noJ3guTUdweh/T38EzyIOEKT99EoPGUPTaMAnbJATRm0i/prdtfE/qJYRiEAUkM4xq4b3T6GVXjEvZNXIkHYz8vyar+L7sUl8JjjvVXhue9Lo7Y0xPimyx8ruNrp74HQjImd9361zmlzSqWiAvGtmEi14ymm1Yk7rxMVYJ+G6c7NLxFqnwfhzo0P846SCtcvNQN6shy0A78nmorkdGLVQKmF2cElLRqVCl00tQgMVq7IY0j0odzxBsKEf1InRCpiu0iSqN8370yAxBL3k/koGM/DF+NgSv+O5uHpLJjRv8M5zHRwiv8+LKC06FAOgs0hnzwJG8s8HTaUFrCl5yW5LnoFEP/JSds58kG1wqV5SQSi6omUVeodhT3ucfuT1UWJFlopcTAZ+ycvDHTKeGxEueFkeqSmhchfYfQ4HJ0eKRwco63O7KuRwA0Z3Nt67qFLUXYXlC2fKMYi5CWsWCvGwHm51H4srIn3k6tYswTSpP+lHXWBEuXhkGQbn6MFcl/O5BhMpk3t1vcD0CUNcccSUKknY3/Zg2w5Us04QUGQp0af2TSnbXAdZV2Osdfy03rYmcLdWK9whNPuOxww392XOMLRWL3FEY6fP6hnlwSo6BFmcSbOPKLHKYBtKVHvBJ6xpBWNBh2JyzTB4q7gicEuzIEuj/THsSpgDxzK0A+d30LC8ggTdDajY3lEf9vmQ5Z/5xaRcIf5QUTes+esC1DvgT4Ca3I4D8ekU6lQa8KMcpSCZVpHXO3p1FUwh4AyYq1uYT4lo/90W/LOtvucnS2+UviGXVmYc5T4/R1u3eilevgMS719qSq9x7v8+feQaCwQ9MDLNnfeBUUZF4ECAw6IJ1fFNpLSKpby/4S/REkjVOE2ik4VU3JHtYzgxln8fqeKIYyAdOFxkdiFddaksrOmOmvaXFpZE501U1kypYBVbgTY36IwDPyxykuPH29x9AShQZlsxo40GktMHDSAsh16wdR7wWztQg5U2v9Ig0XzcCTmD41icXGHHisYgITDcgnMroTdWJ6plVWSVtE9IRaP2RFnsJ8SgubAaxAb80lAQ59PAx7wfCYvZxOwVuPG9QrDo1WjwZSlQbbL68g4CTFE7gDdK0S3ydhAhTFUI57pU6xOTjHDP5KZPFpoAgwk8THt9aNQdrgSHb6q5+bYFtXSClOCGCdxgIoGhtG1mhNCoYJ/pidmgb9sEPQ2NIo31R8iRmqrA/6BiTumF5zVBPPnK6mf4trLvJ2trugV6vlhVlyv1snGC188m6G5LTJmxrTd8Dla/VvVoM+ot8OzwB1urieFDoTlsea8G3w+qlM/YIUx2B3Tp2+QJ7rQ4PN3GiVXS4N31fphO8JfR8LWJUGk1h/i3Tk6WzQcet25arTriyfLv5itM3cOfQKEXftm4F9VWYb/fWhDQeRzMD6rVTEn5sB63SxaUwrbU99MPwbGIM5VRVEPYSAmxQJ6zTV3hKyWKF4IRwauDVWjuUxh36GXjVd4iyHnszHlXp2kRbk1TlinM3W0KufKeCyReMrohCqZjygSjzntphPP8TT002DmH02e+92SxJWsklP/SH9OXqD9sltt1qk2aVWbtKp1tltyevgn7rRfYQfbmq8dWVdWDnuO1Otsd2c7gKwvszHsxPLddz35kvxyCoug722ImV086R6cqWOjX6RSsJfGuf755WqTVB6+L692A3K+k27+lMO2B+JR7JOs1YMoUt7b2rNLWuZ5S7M81M6Ip2LAiAXlghb8Gylk211z5xWqJTz0ipTxqDU+UBMD+p8/t/ebKDseneEdSNoTEEYg2ltky6PiBH/j+Te3DWlLvJgoWruO8/ZFCHJc+S0YBqMetU1cnQnYHbWOvDE+mROgR+hkOFT3qPliQGdKxabCl1iwCEWX22PQGbl/F4YRkvypdJAy8SJaN3xZv6EMzehxhbYbvEQpjsgS+4CMO6EcNhNjQ0YbGvV2MBoYoPBWOZkydRLbZaiscXSCo0E6wolGc6pn1FCnwGbaq2jMkLo0xRSKlq4z/fIANXi0I4uK3i1FKu+XvnI5UZCLuLBPb+6lTXKuzGsg1rhznhfQstF5BsRKO/GEodrgh7aRkdz+LvDZwNaplHFzUBj4JLKkbVXiR2X45gA68NBOh+auNjQ0ySZJuUEPrC7IV6NHgUqL6txTox6oBy5Oago+Av/yyNVLspIw6SRWrJLu29Fo4+QXLchgcxMQFv35UgbP5Ym4v8HQuWSGIvLUa4NhHPDz1SdHj74PbZpK9LpW/gp0Uv+l9bw2pX6QehvLjH1gvbVeEth1LCVCU07Qy2furBc7fj8S4cPvKDO1fZOX7Oi4LiI3aP/Im51Mp353xVChHl7Sd2/YVAjGZsc5BMN64UEtf9m/CKkhWon064vL8XPEpHaYzAx2cC1s9GorFSEb2YogWgx3dLuRGtZTS1qr0Q+15XQdxvH9CxBzQaQVzEHwgMCVfXTnKuKHm2cbWeBEptJNRfn7kfXWXXefW+xEcmMkA7K9Ee5xRwzcnbwuvLt+OHRqKghf7OIaHfxAlQsyweo3AWYZSSkBDyQFcH2b0++8QNN64nItXzfERxqsFy0X7FpOftz4z/Lws0D6Uh6eOOs1iq+9MPkND61Xa1l+xWa8m0S2fHpiSduTvi1Y79Xz9WP+dQk54sk31O7EBZqDq23it6mWiIcrhQhATYPSKOhFFPOVizVoIvYrFS8V9nrukvQsqmu5oCb/lMV0tRguaT1dLUbwY40/xku1tq7NdSW4yOT3ULc826fe/ReSOg7pMXJ/nOatnh+Oi7YwGgtUBxTiNL4Ce6RmcGYydBVpXa/ifZJ94aL4mVOe1yA1wB6i/JHxqc3W9W5jq5Hl+boDbEcM+3asXxKmmyyynGb5R0djxTt5CdjcU7kPxMmve3wUJLodH3nT6cnkBV3GZPioZoU1CJ2iUDDt+raKyxniwhpgDUTRuixWt+MVvQR1O4ZZFfUhEXYCCcxNNu58OjUJs20iIDELVAzWRd05esRi3NWsucMbFqsq/ZVni04+X6FXxIwH6IJekqU3qwT+cOU2bHFD4wfpTLqhB1KKNWikOJfkhXVG163LlE9Td1V5bYZPW9N7KOKGlTCgiNuKIog60A1M0Dau7pDlxvnuMo6gi0pftLw9ewQn4K519DWcu33nB1vEx6fgjziIMW79UPAMSqSOZhcFBWdCFkJ3bXZ1aFD+S4Jy6OqN6KQBvUHoIrkffvMV8PXN0o8KDofMNpyHT3jm5CWcgF8iRM6ermG7V/dleg6mU2Oi1P5XguL1qKfHGR9bJ5sFlkUBDj/p1SLDBeSMTpjlW0b5nScMrfW8/nbsd51FDq4tPO1G3UbqKKYjCef+Nhpamb/tAd0YMCwcDbtIpRovDtV4gTUofg1eJeQ5g68Qv9AIy9G2fRW3ynj5bdOOxNYyQTX74utcrR67V3Q4OggXUA7qspDtM4+U8O9v3v71bz+t3r3984fXH/4RoQHQiLnwTzrnROwrSGkH7Ox5F+yoF+zQADsWYEWNFszxrAtz2gtzZsAcMkw+xYvJ47oDeTLu6e2sB/LwuYY8nTFkVSjvATx8IuBJp8sPOqAGeQ96dEEhED4fYlHjRb5oIU/t1v6fRLZ2TqdaS+ld/nFbls2lvh2AJ2l4/7wGPlBhIMMLvCsgItU553vgMrB8cucSiJQHgDfFywoEGeAuLOLasTdw/V8eXVIHLrED2EX/eHJEGa+iSTtnNJZZ01aWEvb3RSqCh+hbBPRsjIi2MZ7q+yH2lZDR7PCNENx5RBCP562b9G8RuH2fX7valxvgwvUWhJ0At8tBkq7zGK82chcdilxS6cDB5Fma0JsMdEEf3aH5EiS9LrPHAAH6ARrYA/Y1CEl0EQCd47GQvmQigAsvA+wE3+Oo1UPWAC3BwCYwf9DTDV5uAb6BMi/0cY+2OUTBJmsO3P1oXcZ4qdB0/Lz7Csy9WwDiYR9T/CVwxUy5c5sPLXQZEO5Jn4Uy9w+By1MpLxYrDwp56191IDD7NTAIQDr21HigBVKT1n7sLjxwXA911Nof5cdqxn7dAYlF5BjRfbrX5VX+EyL8nHWkaw5lYBuEfg08xHRw49vWI3uA8nisE5EQmUDUul3FOFV3q/h03F4+9p0aWkf4zzEM62j07PhXa0UZv5XPzU3XN5+YFfbHj7jNOc/dAse3PI4sdkdqtn4CVnI/Y05wPtU5Lh8DA80wSDoH5p+hrtYi3XMKPHmIaOmcWJOrgGuTLP0RQgGu8xMSC2QQ83BdX6NgIGSIQD2uExSjoBgHxSQopkExC4pTPhH/VIzGoxfBeDg+HQyng9EoGAXjAHaN8fNg8iJAm8MIy8Aurco8hxJj+B8XmgbTSTA6pUIjVQgyT4MRZDynQsNgchq8oDJjUWY2GI6DaYAtPkNwsC1ORwCOCk10oRcAnMAMschkgt0ac3NTVQqKvKBC0INnoGthx8fPqdBMFQKoz7HYC+w6RkpEcFTmVJWBnk5Fz6FXp9j5KSPgmSiD/wMkjabYLxz9CNsbMaDnqhBAwP69oLHDuGZUigq9UIVgTCDpYNEXCGryDPvEuJwMdalnAfcccfcci6A6C0Ukup8BxhGVE+rVc2rveTDiQmNVCFFNcztiUFOcFOr3ZKIL4eziWBFJ2CH4QRM3maoykDMScMTQoP4zKiSx/XwwHAEen9H8zoiUsA0qc6rLPKce8bwxCiCFSz1TpbClIfVoIrGE9ESlnqtSOCJBcUgnhKfxGBbKw/8DE1/L6Q=='
_RUNTIME = _Path(_tempfile.gettempdir()) / "md_lotto_mobile_runtime_v31"
_marker = _RUNTIME / ".ready"
if not _marker.exists():
    _RUNTIME.mkdir(parents=True, exist_ok=True)
    _files = _json.loads(_zlib.decompress(_b64.b64decode(_EMBEDDED)).decode("utf-8"))
    for _rel, _txt in _files.items():
        _p = _RUNTIME / _rel
        _p.parent.mkdir(parents=True, exist_ok=True)
        _p.write_text(_txt, encoding="utf-8")
    _marker.write_text("v3.1", encoding="utf-8")
_sys.path.insert(0, str(_RUNTIME))
import os as _os
_os.environ.setdefault("MD_LOTTO_DATA_DIR", str(_RUNTIME / "data"))

from pathlib import Path
import os, threading, time
import pandas as pd
import streamlit as st
import plotly.express as px
from md_lotto.data import load_csv,sync_history,save_sqlite,dataset_status,save_sync_status,load_sync_status
from md_lotto.stats import number_stats,pair_stats,triple_stats,structure_summary,randomness_audit,fdr_summary
from md_lotto.optimizer import optimize_games
from md_lotto.backtest import walk_forward,summarize_backtest,nested_walk_forward,strategy_tournament
from md_lotto.simulation import monte_carlo,theoretical_single_game
from md_lotto.ml import train_evaluate,walk_forward_ml

st.set_page_config(page_title='MD LOTTO 6/45',page_icon='🎯',layout='wide',initial_sidebar_state='collapsed')
ROOT=Path(__file__).parent
DATA_DIR=Path(os.getenv('MD_LOTTO_DATA_DIR', str(ROOT/'data')))
DATA_DIR.mkdir(parents=True,exist_ok=True)
path=DATA_DIR/'lotto_history.csv'; db=DATA_DIR/'lotto.db'; sp=DATA_DIR/'sync_status.json'
bundled=ROOT/'data'/'lotto_history.csv'
if not path.exists() and bundled.exists() and bundled.resolve()!=path.resolve(): path.write_bytes(bundled.read_bytes())
_SYNC_LOCK=threading.Lock()

st.markdown("""
<style>
.block-container{padding-top:.65rem;padding-bottom:2.5rem;max-width:1180px}
[data-testid="stHeader"]{background:rgba(0,0,0,0)}
[data-testid="stMetric"]{border:1px solid rgba(128,128,128,.18);padding:.8rem;border-radius:16px;background:rgba(127,127,127,.04)}
.hero{padding:1rem 1.05rem;border-radius:20px;background:linear-gradient(135deg,rgba(255,77,93,.14),rgba(70,130,255,.10));border:1px solid rgba(128,128,128,.15);margin:.2rem 0 1rem}
.hero h1{margin:0;font-size:2rem;line-height:1.15}.hero p{margin:.45rem 0 0;color:#9aa0a6;font-size:.95rem}
.status-ok{padding:.65rem .8rem;border-radius:14px;background:rgba(46,160,67,.12);border:1px solid rgba(46,160,67,.28)}
.status-warn{padding:.65rem .8rem;border-radius:14px;background:rgba(245,158,11,.12);border:1px solid rgba(245,158,11,.28)}
.lotto-row{display:flex;gap:.72rem;flex-wrap:wrap;align-items:center;margin:.72rem 0 1.15rem;padding:.18rem .06rem .55rem;perspective:900px}
.ball{
  --c1:#f6c515;--c2:#d99b00;--c3:#8b5c00;
  position:relative;width:56px;height:56px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;
  font-weight:900;font-size:1.12rem;letter-spacing:-.02em;color:#fff;text-shadow:0 1px 1px rgba(0,0,0,.72),0 0 4px rgba(0,0,0,.28);
  background:
    radial-gradient(circle at 33% 24%,rgba(255,255,255,.98) 0 5%,rgba(255,255,255,.54) 6%,rgba(255,255,255,0) 22%),
    radial-gradient(circle at 38% 34%,var(--c1) 0 25%,var(--c2) 57%,var(--c3) 100%);
  border:1px solid rgba(255,255,255,.52);
  box-shadow:
    inset 7px 9px 13px rgba(255,255,255,.28),
    inset -10px -13px 16px rgba(0,0,0,.36),
    inset 0 0 0 3px rgba(255,255,255,.08),
    0 2px 0 rgba(255,255,255,.16),
    0 9px 14px rgba(0,0,0,.34),
    0 15px 22px rgba(0,0,0,.16);
  transform:translateZ(0);isolation:isolate;
}
.ball::before{content:"";position:absolute;left:11%;top:9%;width:38%;height:22%;border-radius:50%;background:linear-gradient(180deg,rgba(255,255,255,.92),rgba(255,255,255,.10));filter:blur(.15px);transform:rotate(-28deg);opacity:.88;z-index:-1}
.ball::after{content:"";position:absolute;left:12%;right:12%;bottom:-8px;height:10px;border-radius:50%;background:rgba(0,0,0,.34);filter:blur(5px);z-index:-2}
.b1{--c1:#ffd94a;--c2:#f2b400;--c3:#9e6400}
.b2{--c1:#62b7ff;--c2:#247ff0;--c3:#0b3f98}
.b3{--c1:#ff7b78;--c2:#ef3f49;--c3:#921d2b}
.b4{--c1:#c5cbd3;--c2:#7f8792;--c3:#3f4650}
.b5{--c1:#69d876;--c2:#36a84b;--c3:#176127}
.bonus{width:58px;height:58px;box-shadow:inset 7px 9px 13px rgba(255,255,255,.30),inset -10px -13px 16px rgba(0,0,0,.38),inset 0 0 0 3px rgba(255,255,255,.11),0 0 0 3px rgba(255,255,255,.20),0 0 0 6px rgba(255,206,84,.36),0 10px 18px rgba(0,0,0,.40),0 0 20px rgba(255,206,84,.18)}
.bonus-label{display:inline-flex;align-items:center;justify-content:center;font-weight:900;color:#b6bac2;font-size:1.35rem;margin:0 .02rem;text-shadow:0 1px 2px rgba(0,0,0,.5)}
.game-card{padding:.8rem;border:1px solid rgba(128,128,128,.18);border-radius:16px;margin:.5rem 0;background:rgba(127,127,127,.035)}
.game-title{font-weight:800;margin-bottom:.35rem}.small-note{font-size:.83rem;color:#8f949b}.section-title{font-size:1.16rem;font-weight:800;margin:.55rem 0 .4rem}
.stButton>button{border-radius:12px;font-weight:700}
@media(max-width:768px){.block-container{padding-left:.72rem;padding-right:.72rem;padding-top:.45rem}.hero h1{font-size:1.55rem}.hero p{font-size:.86rem}.ball{width:47px;height:47px;font-size:1rem}.bonus{width:49px;height:49px}.lotto-row{gap:.48rem}[data-testid="stMetric"]{padding:.65rem}.stButton>button{width:100%;min-height:2.85rem}h2{font-size:1.3rem!important}h3{font-size:1.1rem!important}div[data-testid="stDataFrame"]{font-size:.78rem}}
</style>
""",unsafe_allow_html=True)

def ball_class(n): return 'b1' if n<=10 else 'b2' if n<=20 else 'b3' if n<=30 else 'b4' if n<=40 else 'b5'
def balls_html(nums,bonus=None):
    parts=[f'<span class="ball {ball_class(int(n))}">{int(n)}</span>' for n in nums]
    if bonus is not None: parts += ['<span class="bonus-label">+</span>',f'<span class="ball {ball_class(int(bonus))} bonus">{int(bonus)}</span>']
    return '<div class="lotto-row">'+''.join(parts)+'</div>'
def pct(v,d=2):
    try:return f'{float(v)*100:.{d}f}%'
    except:return '-'
def render_backtest_summary(s):
    c=st.columns(4); c[0].metric('테스트 회차',f"{int(s.get('tests',0)):,}"); c[1].metric('MD 평균 최고 적중',f"{s.get('md_best_mean',0):.2f}개"); c[2].metric('랜덤 평균 최고 적중',f"{s.get('random_div_best_mean',0):.2f}개"); c[3].metric('우위 근거','있음' if s.get('evidence_of_edge') else '없음')
    st.caption(f"승 {s.get('head_to_head_wins',0)} · 패 {s.get('losses',0)} · 무 {s.get('ties',0)} · Sign test p={s.get('sign_test_p_value',1):.4f}")
    if 'md_realized_roi' in s:
        a,b,c=st.columns(3); a.metric('총 구매비',f"₩{s.get('md_total_cost',0):,.0f}"); b.metric('과거 지급액',f"₩{s.get('md_total_payout',0):,.0f}"); c.metric('과거 ROI',pct(s.get('md_realized_roi',0),1))

@st.cache_data(ttl=1800,show_spinner=False)
def cloud_sync_tick(_bucket):
    with _SYNC_LOCK:
        try:
            d,ss=sync_history(path,verify_official_count=3); save_sqlite(d,db); save_sync_status(ss,sp); return ss
        except Exception as e:return {'ok':False,'error':str(e),'using_cached_data':path.exists()}

startup_status=cloud_sync_tick(int(time.time()//1800)); st.session_state['startup_sync_status']=startup_status
if not path.exists(): st.error('데이터 파일을 준비하지 못했습니다. 잠시 뒤 다시 실행해 주세요.'); st.stop()
df=load_csv(path); status=dataset_status(df); ns=number_stats(df); latest=df.iloc[-1]; ss=st.session_state.get('startup_sync_status') or load_sync_status(sp)

st.markdown('<div class="hero"><h1>🎯 MD LOTTO 6/45</h1><p>과거 데이터·확률·조합 최적화를 연구하는 개인용 분석 도구</p></div>',unsafe_allow_html=True)
if ss.get('ok'): st.markdown(f'<div class="status-ok">✅ <b>데이터 정상</b> · 1회~{status.get("max_draw")}회 · 자동 동기화 확인</div>',unsafe_allow_html=True)
else: st.markdown('<div class="status-warn">⚠️ <b>온라인 최신 확인 실패</b> · 마지막 검증 데이터를 사용 중입니다.</div>',unsafe_allow_html=True)
nums=[int(latest[f'n{i}']) for i in range(1,7)]; bonus=int(latest.bonus)
st.markdown(f'<div class="section-title">제 {int(latest.draw_no)}회 최신 당첨번호</div>',unsafe_allow_html=True); st.markdown(balls_html(nums,bonus),unsafe_allow_html=True)
a,b,c,d=st.columns(4); a.metric('분석 회차',f'{len(df):,}'); b.metric('최신 회차',f'{int(latest.draw_no)}회'); c.metric('최신 추첨일',latest.draw_date.strftime('%Y-%m-%d')); d.metric('1등 확률','1 / 8,145,060')
st.caption('모든 특정 6개 조합의 1등 추첨확률은 동일합니다. MD Score는 당첨확률이 아닙니다.')

with st.sidebar:
    st.header('데이터 관리'); st.success(f"최신 {status.get('max_draw')}회까지 확인") if ss.get('ok') else st.warning('온라인 최신 확인 실패'); st.caption('누락 없음' if status.get('complete_from_draw1') else '일부 회차 누락 가능')
    if st.button('🔄 지금 최신 데이터 확인',use_container_width=True):
        cloud_sync_tick.clear(); new_ss=cloud_sync_tick(int(time.time()//1800)); st.session_state['startup_sync_status']=new_ss; st.rerun()
    st.caption('동기화 실패 시 기존 검증 데이터는 보존됩니다.')

if not status['complete_from_draw1']: st.error(f"현재 데이터가 {status['min_draw']}~{status['max_draw']}회만 있습니다.")
tabs=st.tabs(['대시보드','번호 분석','Pair/Triple','추천 조합','시뮬레이션','백테스트','고급 검증','AI 진단','ROI','도움말'])

with tabs[0]:
    st.subheader('데이터 상태'); audit=randomness_audit(df); struct=structure_summary(df); c=st.columns(4); c[0].metric('전체 회차',f"{status['draws']:,}"); c[1].metric('연속 데이터','정상' if status['contiguous'] else '점검 필요'); c[2].metric('당첨금 데이터','있음' if status.get('has_prize_data') else '없음'); c[3].metric('균등성 검정','특이점 없음' if audit.get('p_value',0)>=.05 else '검토 필요')
    st.caption(f"번호합 평균 {struct.get('sum_mean',0):.1f} · 10~90% 범위 {struct.get('sum_q10',0):.0f}~{struct.get('sum_q90',0):.0f} · 흔한 홀수 개수 {struct.get('odd_mode','-')}개")
    fig=px.bar(ns,x='number',y='count_all',hover_data=['count_20','count_100','current_gap','z_score'],labels={'number':'번호','count_all':'전체 출현'}); fig.update_layout(margin=dict(l=0,r=0,t=15,b=0),height=360); st.plotly_chart(fig,use_container_width=True)
    with st.expander('통계 진단 설명'): st.write('균등성 검정은 과거 출현빈도 치우침을 점검하는 감사 도구입니다. 미래 예측력을 의미하지 않습니다.'); st.write(f"보정 χ² p-value: {audit.get('p_value',1):.4f}")
with tabs[1]:
    view=ns[['number','count_all','count_20','count_50','count_100','count_300','current_gap','mean_gap','z_score']].copy(); view.columns=['번호','전체','최근20','최근50','최근100','최근300','현재 미출현','평균 간격','Z-score']; st.dataframe(view,use_container_width=True,hide_index=True); st.caption('Hot/Cold와 Gap은 과거 상태를 설명할 뿐 “나올 차례”를 의미하지 않습니다.')
with tabs[2]:
    st.info('다중 비교 착시를 줄이기 위해 Benjamini–Hochberg FDR 보정을 사용합니다.')
    if st.button('🔬 전체 FDR 검정 실행',use_container_width=True):
        with st.spinner('검정 중...'): f=fdr_summary(df)
        c=st.columns(4); c[0].metric('Pair 검사',f"{f.get('pair_tests',0):,}"); c[1].metric('Pair 유의',f"{f.get('pair_fdr_significant',0):,}"); c[2].metric('Triple 검사',f"{f.get('triple_tests',0):,}"); c[3].metric('Triple 유의',f"{f.get('triple_fdr_significant',0):,}")
    ps=pair_stats(df,with_tests=True).head(50).copy(); ps['번호쌍']=ps.apply(lambda r:f"{int(r.a):02d}-{int(r.b):02d}",axis=1); st.dataframe(ps[['번호쌍','count','expected','lift','fdr_q_value']].rename(columns={'count':'출현','expected':'기대','lift':'배율','fdr_q_value':'FDR q'}),use_container_width=True,hide_index=True)
    ts=triple_stats(df,min_count=2,with_tests=True).head(50).copy(); ts['번호 3개']=ts.apply(lambda r:f"{int(r.a):02d}-{int(r.b):02d}-{int(r.c):02d}",axis=1); st.dataframe(ts[['번호 3개','count','expected','fdr_q_value']].rename(columns={'count':'출현','expected':'기대','fdr_q_value':'FDR q'}),use_container_width=True,hide_index=True)
with tabs[3]:
    c1,c2=st.columns(2); game_count=c1.slider('게임 수',5,20,10,key='opt_games'); pool=c2.slider('후보 Pool',12,30,20)
    if st.button('🎯 추천 조합 만들기',type='primary',use_container_width=True):
        with st.spinner('조합 최적화 중...'): st.session_state['md_games']=optimize_games(df,ns,games=game_count,pool_size=pool,sample_combos=20000)
    games=st.session_state.get('md_games')
    if games is not None and len(games):
        for i,row in games.iterrows(): st.markdown(f'<div class="game-card"><div class="game-title">GAME {i+1:02d} · MD Score {float(row.get("md_score",0)):.1f}</div>{balls_html(row.combo)}<div class="small-note">새 Pair {int(row.get("new_pairs",0))} · Triple {int(row.get("new_triples",0))} · Quad {int(row.get("new_quads",0))}</div></div>',unsafe_allow_html=True)
        cov=games.attrs.get('coverage',{}); c=st.columns(3); c[0].metric('고유 Pair',cov.get('unique_pairs',0)); c[1].metric('고유 Triple',cov.get('unique_triples',0)); c[2].metric('고유 Quad',cov.get('unique_quads',0))
    else: st.info('「추천 조합 만들기」를 누르세요.')
with tabs[4]:
    sims=st.select_slider('가상 추첨 횟수',[10000,50000,100000,500000],value=100000)
    if st.button('🎲 시뮬레이션 실행',use_container_width=True):
        games=st.session_state.get('md_games')
        if games is None or not len(games): games=optimize_games(df,ns,games=10,sample_combos=12000)
        with st.spinner(f'{sims:,}회 가상 추첨 중...'): r=monte_carlo(games.combo.tolist(),sims)
        c=st.columns(3); c[0].metric('가상 추첨',f"{r['simulations']:,}회"); c[1].metric('1회 이상 당첨',pct(r['any_prize_probability'],3)); c[2].metric('평균 당첨 티켓',f"{r['mean_winning_tickets']:.4f}")
        labels={'1st':'1등','2nd':'2등','3rd':'3등','4th':'4등','5th':'5등','none':'미당첨'}; st.dataframe(pd.DataFrame([{'최고 결과':labels[k],'확률':pct(v,4)} for k,v in r['best_rank_probability'].items()]),use_container_width=True,hide_index=True)
with tabs[5]:
    tests=st.slider('최근 테스트 회차',10,150,30,10,key='bt_tests')
    if st.button('📈 백테스트 실행',use_container_width=True):
        with st.spinner('검증 중...'): st.session_state['last_bt']=walk_forward(df,start_train=300,max_tests=tests,sample_combos=2500,random_reps=100)
    bt=st.session_state.get('last_bt')
    if bt is not None and len(bt): render_backtest_summary(summarize_backtest(bt)); st.caption('우위 근거가 없으면 랜덤보다 낫다고 해석하지 않습니다.');
with tabs[6]:
    mode=st.radio('검증 방식',['Nested Walk-forward','Strategy Tournament'],horizontal=True)
    if mode=='Nested Walk-forward':
        nt=st.slider('Outer 테스트 회차',5,40,12,key='nested_tests')
        if st.button('🧪 Nested 검증 실행',use_container_width=True):
            with st.spinner('검증 중...'): bt=nested_walk_forward(df,start_train=360,max_tests=nt,inner_draws=16,sample_combos=1000,random_reps=60)
            render_backtest_summary(summarize_backtest(bt)); st.dataframe(bt,use_container_width=True,hide_index=True)
    else:
        if st.button('🏁 전략 토너먼트 실행',use_container_width=True):
            with st.spinner('전략 비교 중...'): tour=strategy_tournament(df,start_train=300,max_tests=30,sample_combos=1400)
            st.dataframe(tour,use_container_width=True,hide_index=True)
with tabs[7]:
    c1,c2=st.columns(2)
    if c1.button('시간순 Holdout',use_container_width=True):
        r=train_evaluate(df)
        if r.get('available'):
            c=st.columns(3); c[0].metric('AUC',f"{r['roc_auc_out_of_sample']:.3f}"); c[1].metric('Model Log-loss',f"{r['log_loss_out_of_sample']:.4f}"); c[2].metric('기본보다 우수','예' if r['beats_constant_logloss'] else '아니오')
    if c2.button('완전 Walk-forward',use_container_width=True):
        with st.spinner('회차별 재학습 중...'): r=walk_forward_ml(df,start_train=300,max_tests=30)
        if r.get('available'):
            rows=r.pop('rows',[]); c=st.columns(3); c[0].metric('테스트',r['tests']); c[1].metric('평균 AUC',f"{r['mean_auc']:.3f}"); c[2].metric('평균 Top6 적중',f"{r['mean_top6_hits']:.2f}개"); st.caption(f"평균 Log-loss {r['mean_log_loss']:.4f} · 기본 {r['mean_baseline_log_loss']:.4f}")
with tabs[8]:
    if status.get('has_prize_data'):
        st.info('실제 과거 등위별 당첨금을 이용한 연구용 백테스트입니다. 미래 수익을 보장하지 않습니다.')
        if st.button('💰 ROI 백테스트 실행',use_container_width=True):
            with st.spinner('계산 중...'): bt=walk_forward(df,start_train=300,max_tests=50,sample_combos=1800,random_reps=80)
            render_backtest_summary(summarize_backtest(bt))
    else: st.warning('현재 데이터에 등위별 당첨금 필드가 없습니다.')
    probs=theoretical_single_game(); labels={'1st':'1등','2nd':'2등','3rd':'3등','4th':'4등','5th':'5등'}; st.dataframe(pd.DataFrame([{'등위':labels[k],'확률':pct(v,6),'약 1 / N':f"1 / {round(1/v):,}"} for k,v in probs.items()]),use_container_width=True,hide_index=True)
with tabs[9]:
    st.markdown('''**권장 사용 순서**\n1. 상단의 데이터 정상 표시 확인\n2. 번호 분석과 Pair/Triple로 과거 상태 확인\n3. 백테스트·고급 검증·AI 진단으로 랜덤 기준선과 비교\n4. 마지막에 추천 조합 생성 및 시뮬레이션\n\n**중요**\n- 모든 특정 6개 조합의 1등 확률은 같습니다.\n- Hot/Cold, Gap, Pair, Triple은 과거 통계일 뿐 미래를 보장하지 않습니다.\n- MD Score는 당첨확률이 아닙니다.''')
    st.caption('MD LOTTO 6/45 · Final Mobile UI')
