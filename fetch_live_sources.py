# coding=utf-8
import requests, time

# 在这里加入主接口和 CDN 备用接口
urls = [
    "http://api.hclyz.com/mf/json.txt",          # 主接口
    "https://cdn.jsdelivr.net/gh/json.txt"       # CDN 地址（你需要自己搭建或替换）
]

save_path = "live_sources.txt"
content = ""

for u in urls:
    try:
        response = requests.get(u, timeout=10)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            content = response.text
            print(f"成功抓取：{u}")
            break
        else:
            print(f"请求失败，状态码：{response.status_code} 来自 {u}")
    except Exception as e:
        print(f"抓取出错：{e} 来自 {u}")
        time.sleep(5)

if not content:
    content = "所有接口均失败\n"

with open(save_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 已保存到 {save_path}")
