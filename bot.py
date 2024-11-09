from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
from urllib.parse import quote
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    
except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from datetime import date
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
black = "\033[38;5;0m"
red = "\033[38;5;1m"
green = "\033[38;5;2m"
yellow = "\033[38;5;3m"
blue = "\033[38;5;4m"
magenta = "\033[38;5;5m"
cyan = "\033[38;5;6m"
light_gray = "\033[38;5;7m"
dark_gray = "\033[38;5;8m"
light_red = "\033[38;5;9m"
light_green = "\033[38;5;10m"
light_yellow = "\033[38;5;11m"
light_blue = "\033[38;5;12m"
light_magenta = "\033[38;5;13m"
light_cyan = "\033[38;5;14m"
white = "\033[38;5;15m"
grey_0 = "\033[38;5;16m"
navy_blue = "\033[38;5;17m"
dark_blue = "\033[38;5;18m"
blue_3a = "\033[38;5;19m"
blue_3b = "\033[38;5;20m"
blue_1 = "\033[38;5;21m"
dark_green = "\033[38;5;22m"
deep_sky_blue_4a = "\033[38;5;23"
deep_sky_blue_4b = "\033[38;5;24m"
deep_sky_blue_4c = "\033[38;5;25m"
dodger_blue_3 = "\033[38;5;26m"
dodger_blue_2 = "\033[38;5;27m"
green_4 = "\033[38;5;28m"
spring_green_4 = "\033[38;5;29m"
turquoise_4 = "\033[38;5;30m"
deep_sky_blue_3a = "\033[38;5;31m"
deep_sky_blue_3b = "\033[38;5;32m"
dodger_blue_1 = "\033[38;5;33m"
green_3a = "\033[38;5;34m"
spring_green_3a = "\033[38;5;35m"
dark_cyan = "\033[38;5;36m"
light_sea_green = "\033[38;5;37m"
deep_sky_blue_2 = "\033[38;5;38m"
deep_sky_blue_1 = "\033[38;5;39m"
green_3b = "\033[38;5;40m"
spring_green_3b = "\033[38;5;41m"
spring_green_2a = "\033[38;5;42m"
cyan_3 = "\033[38;5;43m"
dark_turquoise = "\033[38;5;44m"
turquoise_2 = "\033[38;5;45m"
green_1 = "\033[38;5;46m"
spring_green_2b = "\033[38;5;47m"
spring_green_1 = "\033[38;5;48m"
medium_spring_green = "\033[38;5;49m"
cyan_2 = "\033[38;5;50m"
cyan_1 = "\033[38;5;51m"
dark_red_1 = "\033[38;5;52m"
deep_pink_4a = "\033[38;5;53m"
purple_4a = "\033[38;5;54m"
purple_4b = "\033[38;5;55m"
purple_3 = "\033[38;5;56m"
blue_violet = "\033[38;5;57m"
orange_4a = "\033[38;5;58m"
grey_37 = "\033[38;5;59m"
medium_purple_4 = "\033[38;5;60m"
slate_blue_3a = "\033[38;5;61m"
slate_blue_3b = "\033[38;5;62m"
royal_blue_1 = "\033[38;5;63m"
chartreuse_4 = "\033[38;5;64m"
dark_sea_green_4a = "\033[38;5;65m"
pale_turquoise_4 = "\033[38;5;66m"
steel_blue = "\033[38;5;67m"
steel_blue_3 = "\033[38;5;68m"
cornflower_blue = "\033[38;5;69m"
chartreuse_3a = "\033[38;5;70m"
dark_sea_green_4b = "\033[38;5;71m"
cadet_blue_2 = "\033[38;5;72m"
cadet_blue_1 = "\033[38;5;73m"
sky_blue_3 = "\033[38;5;74m"
steel_blue_1a = "\033[38;5;75m"
chartreuse_3b = "\033[38;5;76m"
pale_green_3a = "\033[38;5;77m"
sea_green_3 = "\033[38;5;78m"
aquamarine_3 = "\033[38;5;79m"
medium_turquoise = "\033[38;5;80m"
steel_blue_1b = "\033[38;5;81m"
chartreuse_2a = "\033[38;5;82m"
sea_green_2 = "\033[38;5;83m"
sea_green_1a = "\033[38;5;84m"
sea_green_1b = "\033[38;5;85m"
aquamarine_1a = "\033[38;5;86m"
dark_slate_gray_2 = "\033[38;5;87m"
dark_red_2 = "\033[38;5;88m"
deep_pink_4b = "\033[38;5;89m"
dark_magenta_1 = "\033[38;5;90m"
dark_magenta_2 = "\033[38;5;91m"
dark_violet_1a = "\033[38;5;92m"
purple_1a = "\033[38;5;93m"
orange_4b = "\033[38;5;94m"
light_pink_4 = "\033[38;5;95m"
plum_4 = "\033[38;5;96m"
medium_purple_3a = "\033[38;5;97m"
medium_purple_3b = "\033[38;5;98m"
slate_blue_1 = "\033[38;5;99m"
yellow_4a = "\033[38;5;100m"
wheat_4 = "\033[38;5;101m"
grey_53 = "\033[38;5;102m"
light_slate_grey = "\033[38;5;103m"
medium_purple = "\033[38;5;104m"
light_slate_blue = "\033[38;5;105m"
yellow_4b = "\033[38;5;106m"
dark_olive_green_3a = "\033[38;5;107m"
dark_green_sea = "\033[38;5;108m"
light_sky_blue_3a = "\033[38;5;109m"
light_sky_blue_3b = "\033[38;5;110m"
sky_blue_2 = "\033[38;5;111m"
chartreuse_2b = "\033[38;5;112m"
dark_olive_green_3b = "\033[38;5;113m"
pale_green_3b = "\033[38;5;114m"
dark_sea_green_3a = "\033[38;5;115m"
dark_slate_gray_3 = "\033[38;5;116m"
sky_blue_1 = "\033[38;5;117m"
chartreuse_1 = "\033[38;5;118m"
light_green_2 = "\033[38;5;119m"
light_green_3 = "\033[38;5;120m"
pale_green_1a = "\033[38;5;121m"
aquamarine_1b = "\033[38;5;122m"
dark_slate_gray_1 = "\033[38;5;123m"
red_3a = "\033[38;5;124m"
deep_pink_4c = "\033[38;5;125m"
medium_violet_red = "\033[38;5;126m"
magenta_3a = "\033[38;5;127m"
dark_violet_1b = "\033[38;5;128m"
purple_1b = "\033[38;5;129m"
dark_orange_3a = "\033[38;5;130m"
indian_red_1a = "\033[38;5;131m"
hot_pink_3a = "\033[38;5;132m"
medium_orchid_3 = "\033[38;5;133m"
medium_orchid = "\033[38;5;134m"
medium_purple_2a = "\033[38;5;135m"
dark_goldenrod = "\033[38;5;136m"
light_salmon_3a = "\033[38;5;137m"
rosy_brown = "\033[38;5;138m"
grey_63 = "\033[38;5;139m"
medium_purple_2b = "\033[38;5;140m"
medium_purple_1 = "\033[38;5;141m"
gold_3a = "\033[38;5;142m"
dark_khaki = "\033[38;5;143m"
navajo_white_3 = "\033[38;5;144m"
grey_69 = "\033[38;5;145m"
light_steel_blue_3 = "\033[38;5;146m"
light_steel_blue = "\033[38;5;147m"
yellow_3a = "\033[38;5;148m"
dark_olive_green_3 = "\033[38;5;149m"
dark_sea_green_3b = "\033[38;5;150m"
dark_sea_green_2 = "\033[38;5;151m"
light_cyan_3 = "\033[38;5;152m"
light_sky_blue_1 = "\033[38;5;153m"
green_yellow = "\033[38;5;154m"
dark_olive_green_2 = "\033[38;5;155m"
pale_green_1b = "\033[38;5;156m"
dark_sea_green_5b = "\033[38;5;157m"
dark_sea_green_5a = "\033[38;5;158m"
pale_turquoise_1 = "\033[38;5;159m"
red_3b = "\033[38;5;160m"
deep_pink_3a = "\033[38;5;161m"
deep_pink_3b = "\033[38;5;162m"
magenta_3b = "\033[38;5;163m"
magenta_3c = "\033[38;5;164m"
magenta_2a = "\033[38;5;165m"
dark_orange_3b = "\033[38;5;166m"
indian_red_1b = "\033[38;5;167m"
hot_pink_3b = "\033[38;5;168m"
hot_pink_2 = "\033[38;5;169m"
orchid = "\033[38;5;170m"
medium_orchid_1a = "\033[38;5;171m"
orange_3 = "\033[38;5;172m"
light_salmon_3b = "\033[38;5;173m"
light_pink_3 = "\033[38;5;174m"
pink_3 = "\033[38;5;175m"
plum_3 = "\033[38;5;176m"
violet = "\033[38;5;177m"
gold_3b = "\033[38;5;178m"
light_goldenrod_3 = "\033[38;5;179m"
tan = "\033[38;5;180m"
misty_rose_3 = "\033[38;5;181m"
thistle_3 = "\033[38;5;182m"
plum_2 = "\033[38;5;183m"
yellow_3b = "\033[38;5;184m"
khaki_3 = "\033[38;5;185m"
light_goldenrod_2a = "\033[38;5;186m"
light_yellow_3 = "\033[38;5;187m"
grey_84 = "\033[38;5;188m"
light_steel_blue_1 = "\033[38;5;189m"
yellow_2 = "\033[38;5;190m"
dark_olive_green_1a = "\033[38;5;191m"
dark_olive_green_1b = "\033[38;5;192m"
dark_sea_green_1 = "\033[38;5;193m"
honeydew_2 = "\033[38;5;194m"
light_cyan_1 = "\033[38;5;195m"
red_1 = "\033[38;5;196m"
deep_pink_2 = "\033[38;5;197m"
deep_pink_1a = "\033[38;5;198m"
deep_pink_1b = "\033[38;5;199m"
magenta_2b = "\033[38;5;200m"
magenta_1 = "\033[38;5;201m"
orange_red_1 = "\033[38;5;202m"
indian_red_1c = "\033[38;5;203m"
indian_red_1d = "\033[38;5;204m"
hot_pink_1a = "\033[38;5;205m"
hot_pink_1b = "\033[38;5;206m"
medium_orchid_1b = "\033[38;5;207m"
dark_orange = "\033[38;5;208m"
salmon_1 = "\033[38;5;209m"
light_coral = "\033[38;5;210m"
pale_violet_red_1 = "\033[38;5;211m"
orchid_2 = "\033[38;5;212m"
orchid_1 = "\033[38;5;213m"
orange_1 = "\033[38;5;214m"
sandy_brown = "\033[38;5;215m"
light_salmon_1 = "\033[38;5;216m"
light_pink_1 = "\033[38;5;217m"
pink_1 = "\033[38;5;218m"
plum_1 = "\033[38;5;219m"
gold_1 = "\033[38;5;220m"
light_goldenrod_2b = "\033[38;5;221m"
light_goldenrod_2c = "\033[38;5;222m"
navajo_white_1 = "\033[38;5;223m"
misty_rose1 = "\033[38;5;224m"
thistle_1 = "\033[38;5;225m"
yellow_1 = "\033[38;5;226m"
light_goldenrod_1 = "\033[38;5;227m"
khaki_1 = "\033[38;5;228m"
wheat_1 = "\033[38;5;229m"
cornsilk_1 = "\033[38;5;230m"
grey_100 = "\033[38;5;231m"
grey_3 = "\033[38;5;232m"
grey_7 = "\033[38;5;233m"
grey_11 = "\033[38;5;234m"
grey_15 = "\033[38;5;235m"
grey_19 = "\033[38;5;236m"
grey_23 = "\033[38;5;237m"
grey_27 = "\033[38;5;238m"
grey_30 = "\033[38;5;239m"
grey_35 = "\033[38;5;240m"
grey_39 = "\033[38;5;241m"
grey_42 = "\033[38;5;242m"
grey_46 = "\033[38;5;243m"
grey_50 = "\033[38;5;244m"
grey_54 = "\033[38;5;245m"
grey_58 = "\033[38;5;246m"
grey_62 = "\033[38;5;247m"
grey_66 = "\033[38;5;248m"
grey_70 = "\033[38;5;249m"
grey_74 = "\033[38;5;250m"
grey_78 = "\033[38;5;251m"
grey_82 = "\033[38;5;252m"
grey_85 = "\033[38;5;253m"
grey_89 = "\033[38;5;254m"
grey_93 = "\033[38;5;255m"
default = "\033[38;5;256m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[0;33m",
    "\033[38;5;89m",
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]


chontool = """
\033[1;39m
██╗░░██╗░█████╗░████████╗
██║░░██║██╔══██╗╚══██╔══╝
███████║██║░░██║░░░██║░░░
██╔══██║██║░░██║░░░██║░░░
██║░░██║╚█████╔╝░░░██║░░░
╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░

████████╗██████╗░███████╗░█████╗░
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗
░░░██║░░░██████╔╝█████╗░░██║░░██║
░░░██║░░░██╔══██╗██╔══╝░░██║░░██║
░░░██║░░░██║░░██║███████╗╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░
\033[1;39m┌────────────────── Tool Minh Tuan ──────────────────┐
\033[1;33m ➜ \033[1;39mDEV : Do Minh Tuan
\033[1;33m ➜ \033[1;39mFb : Minh Tuấn ᰔ Hdao丨Ctee.com
\033[1;33m ➜ \033[1;39mZalo Support : 0981381473
\033[1;33m ➜ \033[1;39mSupport : Minh Tuấn ᰔ
\033[1;33m ➜ \033[1;39mBypass : Antiban
\033[1;33m ➜ \033[1;39mTool Spam Ngôn                                          
\033[1;39m└────────────────────────────────────────────────────────┘
\033[1;39m ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻
       	\033[1;31m[\033[1;33m ✯ \033[1;31m] \033[1;34m>\033[1;31m>\033[1;32m> \033[1;39m[ \033[32;5;245m\033[1m\033[38;5;32mMinh Tuấn Luxury\033[1;38;5;39m ]\033[1;33m: \033[1;32m
\033[1;39m➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻ ➻
"""

clear()
runbanner(chontool)
idcanspam=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập Cái ID Thúi Của Mày Vô :{vang} ')
file_list = []
while True:
    ck=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Quăng 🍪 Của Mày Vào :{vang} ')
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
    except:
        print(f'{do}🍪 sai kìa tk ngu!!')   
runbanner(chontool)
lol = input(f"{xanhnhat}Bạn có muốn spam nhiều nội dung không {trang}({tim}y{vang}/{tim}n{trang}): {vang}")
if lol.lower() == "y":
      stt = 0
      loz = int(input(f"{xanhnhat}Bạn muốn spam bao nhiêu nội dung: "))
      while True:
        stt += 1
        name_files=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập file chứa nội dung thứ {stt} của bạn (ex: nd.txt) :{vang} ')
        file_list.append(name_files)
        if stt == loz:
          break
elif lol.lower() == "n":
      name_file=input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập file chứa nội dung của bạn (ex: nd.txt) :{vang} ') 
      file_list.append(name_file)
data_list = []
yn=str(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}bạn muốn spam mãi mãi không :> {trang}({vang}y{trang}/{vang}n{trang}) :{vang} '))
params = {
    "icm": '1',
}
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"247",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
}  
if yn.lower() == 'y':
      delay=int(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      clear()
      while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for selected_file in file_list:
              with open(selected_file, "rb") as file:
                  nds = file.read()
                  #data_list.append(ndss.decode('utf-8'))
            #for ndss in data_list:
              data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nds.decode('utf-8')}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"
              response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
              print(f"\033[1;33m[ {light_blue}{ngay_hom_nay}{vang}-{light_blue}{thang_nay}{vang}-{light_blue}{nam_} {vang} ] | {light_blue}UID BOX: {idcanspam}{vang}")
              idelay(delay)
        except Exception as e:
          print(f"    {light_blue}| Trạng Thái :{light_blue}Thành Công")
          time.sleep(10)

elif yn.lower() == 'n':
      soluong = int(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập số tin nhắn muốn gửi :{vang} '))
      delay=int(input(f'\033[1;97m[\033[1;33m✯\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 10s) :{vang} '))
      for i in range(soluong):
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for name_file in file_list:
              with open(name_file , "rb") as file:
                nds = file.read()
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nds.decode('utf-8')}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"
              response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
              i = i + 1
              print(f"\033[1;33m[ {light_blue}{ngay_hom_nay}{vang}-{light_blue}{thang_nay}{vang}-{light_blue}{nam_} {vang} ] | {light_blue}UID BOX: {idcanspam}{vang}")
              idelay(delay) 
        except Exception as e:
          print(f"    {light_blue}| Trạng Thái : {light_blue}Thành Công")
          time.sleep(10)
else:
    print(f"{do}Vui lòng điền đúng")  