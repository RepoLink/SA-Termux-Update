#  android phone အသုံးပြုပြီး service accounts လုပ်နည်း
## Guide:
- YouTube Link: [Create Service Accounts Tutorial](https://youtu.be/qvPuFFrBD2c)
------
- [x] အရင်ဆုံး Termux ကို မိမိဖုန်းထဲ install လုပ်ပါ။Termux ကို ​အောက်ကပုံ နိပ်ပြီး downloadလုပ်ပါ
[![](https://telegra.ph/file/f302ba135e2cc33b23194.gif)Termux Download](https://drive.google.com/uc?export=download&id=1jnx0F3onc_vzaIMaUEqRh5zJPaAbBrsb)

install လုပ်ပီးရင် Termux ကိုဖွင့်လိုက်ပါ
​အောက်က CMD ​တွေ ရိုက်ထည့်ပါ
```
termux-setup-storage
```
```
pkg update
```
```
pkg upgrade 
```
```
pkg install git
```
```
pkg install python
```
```
pip install --upgrade pip
```
```
mkdir /sdcard/MyTermux/ -p
```
```
cd /sdcard/MyTermux
```
```
git clone <<< repolink >>>
```
```
cd /sdcard/MyTermux/ဖိုင်နာမည်ရိုက်ရန်
```
<<< ဒီအဆင့်ထိ ပထမတစ်ခေါက် Termux စ Run တဲ့အချိန်လုပ်ပေးရမှာ
နောက်ထပ် SA တွေ လုပ်တဲ့အချိန်ဆို မလိုတော့ပါ >>>
```
pip3 install -U -r requirements.txt
```
credentials.json file ကို [Google Console](https://console.cloud.google.com/?pli=1)မှာပြုလုပ်ပါ

```
python3 gen_sa_accounts.py --quick-setup -1
```
```
cd accounts
```
```
python3 emails.py
```
```

[Bulk Rename & Group Pro v1.63 (Paid) APK.apk]
```

https://drive.google.com/file/d/1SrgNZAO8BFnQGLKkQL6tsjERFdJmF1cS/view?usp=drivesdk

