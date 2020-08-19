import requests;
import random;
from time import sleep
f1=open('C:/Users/不二哥01/Desktop/test.txt','r',True,'utf-8');
comment=f1.readlines();
f1.close();
f2=open('../tools/file/color_10_pureNumber.txt','r',True,'utf-8');
color=[];
color_list=f2.readlines();
f2.close();
for i in color_list:
    r=i.split('\n')[0];
    color.append(r);
Formdata={
'type':'1',
'oid':'188976760',
'msg':'666',
'bvid':'BV1LA411t7xm',
'progress':'1200',
'color':'7048739',
'fontsize':'25',
'pool':'0',
'mode':'1',
'rnd':'1597727590677637',
'plat':'1',
'csrf':'a3b9d9e9970d8b415885f1afab45ccda',

}
progress=int(Formdata['progress']);
headers={
'Accept':'*/*',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Origin':'null',
'Referer':'https://www.bilibili.com/video/BV1LA411t7xm?from=search&seid=3482607985346800825',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',

}
cookie={
'cookie':"_uuid=B4EF809E-3694-82C9-BB97-AEE6AD1D724B89093infoc; buvid3=26D790D4-958D-40B3-8221-CC5DE7B118DD138395infoc; CURRENT_FNVAL=16; DedeUserID=525327062; DedeUserID__ckMd5=cac2193c21107ccb; SESSDATA=7788010a%2C1612263445%2C77ea6*81; bili_jct=a3b9d9e9970d8b415885f1afab45ccda; bp_t_offset_525327062=420377685108720629; rpdid=|(k|mlm)Rkmk0J'ulmY~u~Jl|; LIVE_BUVID=AUTO2215973125406578; bp_video_offset_525327062=423899794515875204; finger=1295565314; sid=abaauv2a; PVID=2; bsource=search_baidu",
}
url='https://api.bilibili.com/x/v2/dm/post';
# status=requests.post(url,data=Formdata,headers=headers,cookies=cookie)
# print(status);
count=0;
for j in range(20):
   progress+=20;
   Formdata['progress']=str(progress);
   for i in range(10):
      sleep(5);
      Formdata['msg']=comment[i];
      Formdata['color']=random.choice(color);
    # rnd+=10000;
    # Formdata['rnd']=str(rnd);
      res=requests.post(url=url,data=Formdata,headers=headers,cookies=cookie);
      count+=1;
      print(str(count)+':'+str(res));

