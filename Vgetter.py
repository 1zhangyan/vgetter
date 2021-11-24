import api_builder
from alive_progress import alive_bar

print("******************************************")
print("******************************************")
print("**************仅学习交流使用**************")
print("**************q+enter退出*****************")
print("******************************************")
mid = input("Please Input userId : ")
if mid == 'q':
    exit()
cid_bvid =  api_builder.get_user_cid_bvid(mid)
for cid in cid_bvid.keys():
    api_builder.video_download(cid_bvid[cid], cid)