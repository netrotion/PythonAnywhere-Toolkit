import requests

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
    # 'Cookie': 'cookie_warning_seen=True; csrftoken=O0tJ0XJdDyKSIbd45FKwqcUxQPTVMeE7AKYFOLoeNEeIsWaQ8sffNFtrBnhtq7uk; sessionid=i4fabaffv7y1odttlfad0ffvsaqr83cq',
    'DNT': '1',
    'Origin': 'https://www.pythonanywhere.com',
    'Referer': 'https://www.pythonanywhere.com/user/hngl2808/files/home/hngl2808/mysite/123.py?edit',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'X-CSRFToken': '0TAgNWRyXLvZEES9dNzlkSx5ASN60FZfMD5cBKwz7RZPopPVgA44Hl6ZlqbEEyPs',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = "input=_pa_run(u'%2Fhome%2Fhngl2808%2Fmysite%2F123.py')%0A"

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/hngl2808/consoles/33744833/send_input/',
    cookies=cookies,
    headers=headers,
    data=data,
)