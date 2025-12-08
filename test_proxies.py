import requests
import time
import warnings
from requests.exceptions import RequestException
from urllib3.exceptions import InsecureRequestWarning

# 忽略 SSL 证书验证警告
warnings.simplefilter('ignore', InsecureRequestWarning)

# 测试 URL
test_url = 'https://www.google.com'

def check_proxy(proxies):
    try:
        # 发送请求，跳过证书验证
        response = requests.get(test_url, proxies=proxies, timeout=10, verify=False)
        
        # 检查响应状态码
        if response.status_code == 200:
            print(f"代理 {proxies['http']} 可用")
        else:
            print(f"代理 {proxies['http']} 不可用，HTTP状态码：{response.status_code}")
    
    except RequestException as e:
        print(f"代理 {proxies['http']} 不可用，错误信息：{e}")
    
    # 如果返回 429 错误码，表示请求频率过高
    if response.status_code == 429:
        print(f"代理 {proxies['http']} 被限流，等待一段时间后重试...")
        time.sleep(60)  # 等待 1 分钟
        check_proxy(proxies)  # 重新调用函数重试

# 示例代理列表
proxies_list = [
    {"http": "socks5://47.243.30.66:37469", "https": "socks5://47.243.30.66:37469"},
    {"http": "socks5://67.201.58.190:4145", "https": "socks5://67.201.58.190:4145"},
    {"http": "socks5://192.252.208.70:14282", "https": "socks5://192.252.208.70:14282"},
    {"http": "socks5://121.169.46.116:1090", "https": "socks5://121.169.46.116:1090"},
    {"http": "socks5://98.170.57.241:4145", "https": "socks5://98.170.57.241:4145"},
    {"http": "socks5://98.182.147.97:4145", "https": "socks5://98.182.147.97:4145"},
    {"http": "socks5://174.64.199.79:4145", "https": "socks5://174.64.199.79:4145"},
    {"http": "socks5://184.170.249.65:4145", "https": "socks5://184.170.249.65:4145"},
    {"http": "socks5://174.77.111.198:49547", "https": "socks5://174.77.111.198:49547"},
    {"http": "socks5://68.71.240.210:4145", "https": "socks5://68.71.240.210:4145"},
    {"http": "socks5://98.178.72.30:4145", "https": "socks5://98.178.72.30:4145"},
    {"http": "socks5://142.54.229.249:4145", "https": "socks5://142.54.229.249:4145"},
    {"http": "socks5://72.207.109.5:4145", "https": "socks5://72.207.109.5:4145"},
    {"http": "socks5://24.249.199.4:4145", "https": "socks5://24.249.199.4:4145"},
    {"http": "socks5://72.211.46.124:4145", "https": "socks5://72.211.46.124:4145"},
    {"http": "socks5://98.181.137.80:4145", "https": "socks5://98.181.137.80:4145"},
    {"http": "socks5://67.201.33.10:25283", "https": "socks5://67.201.33.10:25283"},
    {"http": "socks5://68.71.249.153:48606", "https": "socks5://68.71.249.153:48606"},
    {"http": "socks5://98.188.47.150:4145", "https": "socks5://98.188.47.150:4145"},
    {"http": "socks5://98.188.47.132:4145", "https": "socks5://98.188.47.132:4145"},
    {"http": "socks5://192.111.129.145:16894", "https": "socks5://192.111.129.145:16894"},
    {"http": "socks5://72.195.114.169:4145", "https": "socks5://72.195.114.169:4145"},
    {"http": "socks5://98.181.137.83:4145", "https": "socks5://98.181.137.83:4145"},
    {"http": "socks5://98.170.57.249:4145", "https": "socks5://98.170.57.249:4145"},
    {"http": "socks5://184.178.172.23:4145", "https": "socks5://184.178.172.23:4145"},
    {"http": "socks5://198.177.252.24:4145", "https": "socks5://198.177.252.24:4145"},
    {"http": "socks5://174.64.199.82:4145", "https": "socks5://174.64.199.82:4145"},
    {"http": "socks5://174.77.111.196:4145", "https": "socks5://174.77.111.196:4145"},
    {"http": "socks5://184.178.172.25:15291", "https": "socks5://184.178.172.25:15291"},
    {"http": "socks5://192.111.137.37:18762", "https": "socks5://192.111.137.37:18762"},
    {"http": "socks5://192.252.214.20:15864", "https": "socks5://192.252.214.20:15864"},
    {"http": "socks5://192.252.220.92:17328", "https": "socks5://192.252.220.92:17328"},
    {"http": "socks5://184.170.248.5:4145", "https": "socks5://184.170.248.5:4145"},
    {"http": "socks5://98.182.171.161:4145", "https": "socks5://98.182.171.161:4145"},
    {"http": "socks5://199.58.184.97:4145", "https": "socks5://199.58.184.97:4145"},
    {"http": "socks5://142.54.237.34:4145", "https": "socks5://142.54.237.34:4145"},
    {"http": "socks5://139.59.24.173:1080", "https": "socks5://139.59.24.173:1080"},  # 这个代理是不可用的
    {"http": "socks5://70.166.167.55:57745", "https": "socks5://70.166.167.55:57745"},
    {"http": "socks5://142.54.239.1:4145", "https": "socks5://142.54.239.1:4145"},
    {"http": "socks5://72.211.46.99:4145", "https": "socks5://72.211.46.99:4145"},
    {"http": "socks5://192.111.138.29:4145", "https": "socks5://192.111.138.29:4145"},
    {"http": "socks5://208.65.90.21:4145", "https": "socks5://208.65.90.21:4145"}
]

# 遍历代理列表进行检查
for proxy in proxies_list:
    check_proxy(proxy)
