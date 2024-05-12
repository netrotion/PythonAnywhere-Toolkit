import requests

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.pythonanywhere.com',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Sec-WebSocket-Key': 'NJHcnjER1heATTRC20WxXA==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Upgrade': 'websocket',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Sec-WebSocket-Version': '13',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
}

response = requests.get('wss://consoles-11.pythonanywhere.com/sj/901/c9784j17/websocket', headers=headers)
print(response.text)