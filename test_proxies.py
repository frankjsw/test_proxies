import requests
from requests.exceptions import RequestException

# 代理列表
proxies_list = [
    "socks5://47.243.30.66:37469",
    "socks5://67.201.58.190:4145",
    "socks5://192.252.208.70:14282",
    "socks5://121.169.46.116:1090",
    "socks5://98.170.57.241:4145",
    "socks5://98.182.147.97:4145",
    "socks5://174.64.199.79:4145",
    "socks5://184.170.249.65:4145",
    "socks5://174.77.111.198:49547",
    "socks5://68.71.240.210:4145",
    "socks5://98.178.72.30:4145",
    "socks5://142.54.229.249:4145",
    "socks5://72.207.109.5:4145",
    "socks5://24.249.199.4:4145",
    "socks5://72.211.46.124:4145",
    "socks5://98.181.137.80:4145",
    "socks5://67.201.33.10:25283",
    "socks5://68.71.249.153:48606",
    "socks5://98.188.47.150:4145",
    "socks5://98.188.47.132:4145",
    "socks5://192.111.129.145:16894",
    "socks5://72.195.114.169:4145",
    "socks5://98.181.137.83:4145",
    "socks5://98.170.57.249:4145",
    "socks5://184.178.172.23:4145",
    "socks5://198.177.252.24:4145",
    "socks5://174.64.199.82:4145",
    "socks5://174.77.111.196:4145",
    "socks5://184.178.172.25:15291",
    "socks5://192.111.137.37:18762",
    "socks5://192.252.214.20:15864",
    "socks5://192.252.220.92:17328",
    "socks5://184.170.248.5:4145",
    "socks5://98.182.171.161:4145",
    "socks5://199.58.184.97:4145",
    "socks5://142.54.237.34:4145",
    "socks5://139.59.24.173:1080",
    "socks5://70.166.167.55:57745",
    "socks5://142.54.239.1:4145",
    "socks5://72.211.46.99:4145",
    "socks5://192.111.138.29:4145",
    "socks5://208.65.90.21:4145",
]

# 测试目标URL
test_url = "https://www.google.com"

# 设置代理检查
def check_proxy(proxies):
    try:
        # 尝试连接 Google，设置更长的超时时间并跳过SSL证书验证
        response = requests.get(test_url, proxies=proxies, timeout=10, verify=False)
        
        if response.status_code == 200:
            print(f"代理 {proxies['http']} 可用")
        else:
            print(f"代理 {proxies['http']} 不可用，HTTP状态码：{response.status_code}")
    except RequestException as e:
        print(f"代理 {proxies['http']} 不可用，错误信息：{e}")

def main():
    for proxy in proxies_list:
        # 设置代理
        proxies = {
            "http": proxy,
            "https": proxy,
        }
        
        # 调用测试函数
        check_proxy(proxies)

if __name__ == "__main__":
    main()
