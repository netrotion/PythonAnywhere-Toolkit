from dateutil.relativedelta import relativedelta
from datetime import datetime
from time import sleep
import requests
import json
import os
TABS = "\t"*5
PREV_TABS = "\t"*4
BANNER = f"""{TABS}============================\n{TABS}|        PAW MANAGERS      |\n{TABS}============================\n"""



class paw:
    def __init__(self,user,password,session=None):
        if session == None:
            self.session = requests.Session()
        else:
            self.session = session
        self.user = user
        self.password = password
    
    def login(self):
        headers = {
            'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language'   : 'en-US,en;q=0.9,vi;q=0.8',
            'Content-Type'      : 'application/x-www-form-urlencoded',
            'Origin'            : 'https://www.pythonanywhere.com',
            'Referer'           : 'https://www.pythonanywhere.com/login/',
            'User-Agent'        : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        baseurl = 'https://www.pythonanywhere.com/login/'
        data = self.session.get(
            baseurl,
            headers=headers
        ).text

        csrftoken = data.split('csrfToken = "')[1].split('"')[0] #csfttoken -> cookie
        waretoken = data.split('csrfmiddlewaretoken" value="')[1].split('"')[0]  #waretoken -> data
        cookies = {
            'csrftoken': csrftoken
        }

        data = {
            'csrfmiddlewaretoken'       : waretoken,
            'auth-username'             : self.user,
            'auth-password'             : self.password,
            'login_view-current_step'   : 'auth',
        }

        response = self.session.post(
            'https://www.pythonanywhere.com/login/', 
            cookies = cookies, 
            headers = headers, 
            data    = data
        )

        data = response.text

        if 'Log in' in data:
            return {'status':False}
        return {'status':True,'session':self.session,"user":self.user,"password":self.password}
    
    def uptime(self):
        baseurl = f'https://www.pythonanywhere.com/user/{self.user}/webapps/#tab_id_{self.user}_pythonanywhere_com'
        headers = {
            'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language'   : 'en-US,en;q=0.9,vi;q=0.8',
            'Connection'        : 'keep-alive',
            'Referer'           : f'https://www.pythonanywhere.com/user/{self.user}/',
            'User-Agent'        : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        data = self.session.get(baseurl,headers=headers).text
        csrftoken = data.split('Anywhere.csrfToken = "')[1].split('"')[0]
        waretoken = data.split('csrfmiddlewaretoken" value="')[1].split('"')[0]

        cookies = {
            'web_app_tab_type'      : f'%23tab_id_{self.user}_pythonanywhere_com',
            'cookie_warning_seen'   : 'True',
            'csrftoken'             : csrftoken,
        }

        data = {
            'csrfmiddlewaretoken': waretoken,
        }

        response = self.session.post(
            f'https://www.pythonanywhere.com/user/{self.user}/webapps/{self.user}.pythonanywhere.com/extend',
            cookies = cookies,
            headers = headers,
            data    = data,
        )

        try:
            timepast = str(datetime.strptime(' '.join(response.text.split('<strong>')[1].split('<')[0].split(' ')[1:]), "%d %B %Y") - relativedelta(months=3)).split(' ')[0]
            now = str(datetime.now()).split(' ')[0]
            return {'status':True,'time':now,'last':timepast,'session':self.session}
        except:
            return  {'status':False}
    def get_data_space_value(self):
        main_menu = f"https://www.pythonanywhere.com/user/{self.user}/"
        quota_info = f"https://www.pythonanywhere.com/user/{self.user}/quota_information/"
        data = self.session.get(main_menu).text
        data1 = self.session.get(quota_info).json()
        cpu_usage = data.split("CPU Usage:")[1]
        cpu_percent_useed = cpu_usage.split('<span id="id_daily_cpu_usage_percent">')[1].split('<')[0] + r" % used"
        cpu_usage_seconds = cpu_usage.split('<span id="id_daily_cpu_usage_seconds">')[1].split('<')[0] + " of 100s"
        cpu_reset_time =    cpu_usage.split('<span id="id_daily_cpu_reset_time">')[1].split('<')[0] 
        dict_data = {
            "cpu" : {
                "cpu_percent_used" : cpu_percent_useed,
                "cpu_usage_seconds" : cpu_usage_seconds,
                "cpu_reset_time" : cpu_reset_time,
            },
            "storage": data1
        }
        return dict_data
    def start_login_and_uptime(self):
        response_login = self.login()
        if not response_login['status']:#neu false tra ve json false
            return response_login
        response_uptime = self.uptime()
        return response_uptime






class main:
    def __init__(self):
        self.user = ""
        self.password = ""
        self.is_login = False
        self.update_data()
        self.config_startup()
    def update_data(self):#cap nhat gia tri user
        self.cache = json.loads(open("dataset/cache.json","r",encoding="utf-8").read())
        self.user_data = json.loads(open("dataset/user.json","r",encoding="utf-8").read())

    def write_data(self):
        open("dataset/cache.json","w",encoding="utf-8").write(json.dumps(self.cache))
        open("dataset/user.json","w",encoding="utf-8").write(json.dumps(self.user_data))

    def get_user_infomation(self):
        return paw(self.user,self.password,self.session).get_data_space_value()

    def config_startup(self):
        self.cls()
        print(f"{PREV_TABS}>> Please wait while checking infomation...")
        if self.user_data != {"user": None, "password": None}:
            response = paw(self.user_data["user"],self.user_data["password"]).login()
            if response["status"]:
                print(f"{PREV_TABS}>> Success!")
                self.is_login = True
                self.user = response["user"]
                self.password = response["password"]
                self.session = response["session"]
                self.write_data()
                sleep(1)
                return
            else:
                print(f"{PREV_TABS}>> Failed, wrong username or password")
                sleep(1)
                return
    
    def cls(self):
        if os.name == "posix":
            cls_cmd = "clear"
        else:
            cls_cmd = "cls"
        os.system(cls_cmd)
        return print(BANNER) 
    def check_valid_choose(self,input,start,end):
        if not input.isnumeric():
            return False
        if int(input) not in range(start,end+1):
            return False
        return True 
    
    def home(self):
        def login():
            self.cls()
            user = input(f"{PREV_TABS}[users]>>")
            password = input(f"{PREV_TABS}[password]>>")
            print(f"{PREV_TABS}>>Please wait while login...")
            response = paw(user,password).login()
            if response['status']:
                self.is_login = True
                self.user_data["user"] = response["user"]
                self.user_data["password"] = response["password"]
                self.session = response["session"]
                self.write_data()
                print(f"{PREV_TABS}>>Login success!")
                return self.home()
            else:
                print(f"{PREV_TABS}Wrong infomation!")
                sleep(1)
                return login()
        def info():
            print(f"{PREV_TABS}>>Updated soon...")
            sleep(1)
            pass
        def uptime():
            self.cls()
            count = 0
            while True:
                try:
                    if paw(self.user,self.password,self.session).uptime():
                        count += 1
                        for i in range(86400*100,-1,-1):
                            s = f'{PREV_TABS}[Count: {count}][Time left : {round(i/100,5)}][>>To exit, press Ctrl + C]   '
                            print(s,end='\r')
                            sleep(0.01)
                    else:
                        print(f"{PREV_TABS}>>Failed to uptime")
                except KeyboardInterrupt:
                    print(f"{PREV_TABS}>>Exited uptime windows")
                    return self.home()
        def c_s():
            print(f"{PREV_TABS}>>Updated soon...")
            sleep(1)
            return self.home()
        def logout():
            self.is_login = False
            self.session = None
            self.user_data = {"user":None,"password":None}
            self.write_data()
            return self.home()
        func = {
            "is_login": {
                "1" : info,
                "2" : uptime,
                "3" : c_s,
                "4" : logout,
            },
            "is_not_login" : {
                "1" : login 
            }
        }
        self.cls()
        
        if not self.is_login:
            self.cls()
            print(f"{PREV_TABS}>>1. Log in")
            choosing = input(f"{PREV_TABS}[input number]-->")
            if self.check_valid_choose(choosing,1,1):
                return func["is_not_login"][choosing]()
            else:
                print(f"{PREV_TABS}Error!")
                sleep(1)
                return self.home()
        else:
            try:
                infom = self.get_user_infomation()
            except:
                print(f"{PREV_TABS}>>Network error!")
                return
            while True:
                self.cls()
                
                print(f"{TABS}============================")
                print(f"{TABS}          >> INFO <<")
                print(f"{TABS}Welcome user : {self.user}")
                print(f"{TABS}----------------------------")
                print(f"{TABS}CPU Usage : {infom['cpu']['cpu_percent_used']} - {infom['cpu']['cpu_usage_seconds']}")
                print(f"{TABS}CPU reset : {infom['cpu']['cpu_reset_time']} left")
                print(f"{TABS}----------------------------")
                print(f"{TABS}Storage : {infom['storage']['percent']} full")
                print(f"{TABS}Memory : {infom['storage']['used']} of your {infom['storage']['quota']} quota ")
                
                print(f"{TABS}============================")
                print(f"{PREV_TABS}>>1. Info")
                print(f"{PREV_TABS}>>2. Uptime")
                print(f"{PREV_TABS}>>2. Config storage")
                print(f"{PREV_TABS}>>4. Log out")
                choosing = input(f"{PREV_TABS}[input number]-->")
                if self.check_valid_choose(choosing,1,4):
                    return func["is_login"][choosing]()
                else:
                    print(f"{PREV_TABS}Error!")
                    sleep(1)
                    return self.home()
if __name__ == "__main__":
    
    try:
        running = main()
        running.home()
    except KeyboardInterrupt:
        os.system("cls") if os.name != "posix" else os.system("clear")
        print(BANNER)
        print(f"{TABS}>>Exited!")