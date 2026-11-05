import os
import urllib.request
import json

# 从环境变量读取 Token，绝不硬编码在代码里
token =os.getenv("GITHUB_TOKEN")
if not token:
    print("错误：未找到 GITHUB_TOKEN 环境变量！")
    exit(1)

# 替换成你自己的用户名和仓库名
REPO_OWNER = "jameshexu"
REPO_NAME = "pat-practice"

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
req = urllib.request.Request(url)
req.add_header("Authorization", f"Bearer {token}")
req.add_header("Accept", "application/vnd.github+json")

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(f"成功拉取！当前仓库有 {len(data)} 个 Issue。")
except Exception as e:
    print(f"请求失败，Token 可能无效或权限不足: {e}")
