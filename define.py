import requests
from requests import Session
import os
from threading import Thread
cookies = {
    'cookie_warning_seen': 'True',
    'csrftoken': 'O0tJ0XJdDyKSIbd45FKwqcUxQPTVMeE7AKYFOLoeNEeIsWaQ8sffNFtrBnhtq7uk',
    'sessionid': 'i4fabaffv7y1odttlfad0ffvsaqr83cq',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Origin': 'https://www.pythonanywhere.com',
    'Referer': 'https://www.pythonanywhere.com/user/hngl2808/files/home/hngl2808/mysite',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'X-CSRFToken': 'hDEIWLASAPvfHhfiP6038cVaaqCaFI3x3n9EKzfTKVZ5r2c4STvMvFu4VY0IjBTK',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
session = Session()
session.cookies.update(cookies)
session.headers.update(headers)
#-----------------------------------------------------action

#deleted
# data = {
#     'action': 'delete_file',
# }

# response = requests.post(
#     'https://www.pythonanywhere.com/user/hngl2808/files/home/hngl2808/mysite/add_user.png',
#     data=data,
# )
######################write_data

# content_to_write = open("main.py",'r',encoding='utf-8').read()

# file = "123.py"
# data = {
#     'new_contents': content_to_write,
# }

# response = session.post(
#     f'https://www.pythonanywhere.com/user/hngl2808/files/home/hngl2808/mysite/{file}',
#     data=data,
# ).json()
# print(response)


#console api
# url = 'https://www.pythonanywhere.com/api/v0/user/hngl2808/consoles/33744833/get_latest_output/'
# url_input = 'https://www.pythonanywhere.com/api/v0/user/hngl2808/consoles/33744833/send_input/'



# prev_mess = ""
# while True:
#     try:
#         response = session.get(url).json()
#         if response == {'detail': 'Not found.'}:
#             print('>>session closed!')
#             break
#         response = response['output']
#     except:
#         print('>>network error!')
#         continue
#     os.system('cls')
#     print(response)
#     command = input('[send_messages]-->')
#     data = f"input={command}%0A"
#     response = session.post(
#         url_input,
#         data=data
#     )
#show console list
# url = "https://www.pythonanywhere.com/api/v0/user/hngl2808/consoles/"
# response = session.get(url).json()
# id = response[0][id]
# console_url = response[0]['console_url']
# console_frame_url = response[0]['console_frame_url']
#start console and remote
def thread(session):

    console_url =f'https://www.pythonanywhere.com/user/hngl2808/consoles/{console_id}/'
    frame = f'https://www.pythonanywhere.com/user/hngl2808/consoles/{console_id}/frame/'
    sharees_url = f'https://www.pythonanywhere.com/user/hngl2808/consoles/{console_id}/get_sharees'
    info_url = f'https://consoles-7.pythonanywhere.com/sj/info'
    for i in range(10):
        load_console = session.get(console_url,timeout=60)
        load_frame = session.get(frame,timeout=60)
        load_sharees = session.get(sharees_url,timeout=60)
        load_info = session.get(info_url)

url = 'https://www.pythonanywhere.com/user/hngl2808/consoles/bash/new'
response = session.post(url).text
console_id = response.split("Bash console ")[1].split("<")[0]


Thread(target=thread,args=(session,)).start()
url = f'https://www.pythonanywhere.com/api/v0/user/hngl2808/consoles/{console_id}/get_latest_output/'
url_input = f'https://www.pythonanywhere.com/api/v0/user/hngl2808/consoles/{console_id}/send_input/'



prev_mess = ""
while True:
    try:
        response = session.get(url).json()
        if response == {'detail': 'Not found.'}:
            print('>>session closed!')
            break
        response = response['output']
    except:
        print(response)
        print('>>network error!')
        continue
    os.system('cls')
    #input(list(response))
    if "$" not in response[-8]:
        print(response)
        continue
    command = input(response)
    
    data = f"input={command}%0A"
    response = session.post(url_input,data=data)