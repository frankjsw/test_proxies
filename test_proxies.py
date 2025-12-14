import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.exceptions import RequestException

TEST_URL = "https://ifconfig.me/ip"

def test_one(proxy_str: str, timeout: int = 8):
    """
    proxy_str: "ip:port"
    """
    host, port_str = proxy_str.split(":")
    port = int(port_str)

    proxies = {
        "http": f"socks5h://{host}:{port}",
        "https": f"socks5h://{host}:{port}",
    }

    start = time.time()
    try:
        resp = requests.get(TEST_URL, proxies=proxies, timeout=timeout)
        elapsed = time.time() - start
        if resp.status_code == 200:
            ip_text = resp.text.strip()
            print(f"[OK] {proxy_str} -> exit_ip={ip_text}, {elapsed:.2f}s")
            return {
                "proxy": proxy_str,
                "ok": True,
                "exit_ip": ip_text,
                "elapsed": elapsed,
                "error": None,
            }
        else:
            print(f"[BAD] {proxy_str} -> status={resp.status_code}")
            return {
                "proxy": proxy_str,
                "ok": False,
                "exit_ip": None,
                "elapsed": elapsed,
                "error": f"非 200 状态码：{resp.status_code}",
            }
    except RequestException as e:
        elapsed = time.time() - start
        print(f"[ERR] {proxy_str} -> {e}")
        return {
            "proxy": proxy_str,
            "ok": False,
            "exit_ip": None,
            "elapsed": elapsed,
            "error": str(e),
        }


def filter_proxy_pool(proxy_list, max_workers: int = 20):
    """
    多线程筛选整个代理池。
    proxy_list: ["ip:port", ...]
    """
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_proxy = {
            executor.submit(test_one, proxy): proxy for proxy in proxy_list
        }
        for future in as_completed(future_to_proxy):
            res = future.result()
            results.append(res)

    good = [r for r in results if r["ok"]]
    bad = [r for r in results if not r["ok"]]

    print("\n====== 筛选结果 ======")
    print(f"总计：{len(results)} 个代理")
    print(f"可用：{len(good)} 个")
    print(f"不可用：{len(bad)} 个")

    if good:
        print("\n可用代理列表：")
        for r in good:
            print(f"  {r['proxy']}  (出口IP: {r['exit_ip']}, {r['elapsed']:.2f}s)")

    return good, bad


if __name__ == "__main__":
    # 把你原来的 proxies_list 转换成 "ip:port" 格式
    raw_proxies_list = [
        "47.243.30.66:37469",
        "67.201.58.190:4145",
        "192.252.208.70:14282",
        "121.169.46.116:1090",
        "98.170.57.241:4145",
        "98.182.147.97:4145",
        "174.64.199.79:4145",
        "184.170.249.65:4145",
        "174.77.111.198:49547",
        "68.71.240.210:4145",
        "98.178.72.30:4145",
        "142.54.229.249:4145",
        "72.207.109.5:4145",
        "24.249.199.4:4145",
        "72.211.46.124:4145",
        "98.181.137.80:4145",
        "67.201.33.10:25283",
        "68.71.249.153:48606",
        "98.188.47.150:4145",
        "98.188.47.132:4145",
        "192.111.129.145:16894",
        "72.195.114.169:4145",
        "98.181.137.83:4145",
        "98.170.57.249:4145",
        "184.178.172.23:4145",
        "198.177.252.24:4145",
        "174.64.199.82:4145",
        "174.77.111.196:4145",
        "184.178.172.25:15291",
        "192.111.137.37:18762",
        "192.252.214.20:15864",
        "192.252.220.92:17328",
        "184.170.248.5:4145",
        "98.182.171.161:4145",
        "199.58.184.97:4145",
        "142.54.237.34:4145",
        "139.59.24.173:1080",
        "70.166.167.55:57745",
        "142.54.239.1:4145",
        "72.211.46.99:4145",
        "192.111.138.29:4145",
        "208.65.90.21:4145",
        "192.111.137.35:4145",
        "184.170.248.5:4145",
        "68.71.247.130:4145",
        "104.200.135.46:4145",
        "98.188.47.132:4145",
        "70.166.167.55:57745",
        "107.152.98.5:4145",
        "192.111.137.34:18765",
        "94.159.106.252:1080",
        "192.111.139.162:4145",
        "192.111.129.150:4145",
        "199.116.114.11:4145",
        "184.178.172.3:4145",
        "184.185.2.12:4145",
        "98.182.171.161:4145",
        "72.195.34.59:4145",
        "192.252.220.92:17328",
        "68.1.210.189:4145",
        "199.229.254.129:4145",
        "192.252.216.81:4145",
        "184.170.249.65:4145",
        "184.170.245.148:4145",
        "199.58.184.97:4145",
        "199.58.185.9:4145",
        "192.111.138.29:4145",
        "58.22.60.174:1080"

    ]

    good, bad = filter_proxy_pool(raw_proxies_list, max_workers=20)
