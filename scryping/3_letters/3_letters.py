import os
import requests

def enable_vpn(proxy_host="192.168.1.53", proxy_port="54652"): # включение впн
    os.environ['HTTP_PROXY'] = f"socks5h://{proxy_host}:{proxy_port}" #тип прокси
    os.environ['HTTPS_PROXY'] = f"socks5h://{proxy_host}:{proxy_port}"
    # настройка протоколов запроса

def disable_vpn(): #выключение впн
    os.environ.pop('HTTP_PROXY', None)
    os.environ.pop('HTTPS_PROXY', None)

def send_request(): #отправка запроса
    response = requests.get("https://httpbin.org/ip", timeout=10)
    print(response.json())

send_request()
enable_vpn()
send_request()
disable_vpn()
send_request()

