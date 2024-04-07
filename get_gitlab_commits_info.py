'''
get gitlab project commits information.

Usage:
    - Import this module using `import mymodule`.
    - Use the functions provided by this module as needed.

Author: Lei Wang
Date: April 2, 2024
'''

__author__ = "王磊"
__copyright__ = "Copyright 2024 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"

import requests

# 替换为你的GitLab实例的URL
gitlab_url = "http://192.168.0.46"
# 替换为你的项目ID
project_id = "9"
# 替换为你的个人访问令牌
private_token = "glpat-oz5f75qQ5BtzcDshoAkz"

# 构建请求URL
url = f"{gitlab_url}/api/v4/projects/{project_id}/repository/commits"

# 设置请求头部，包括你的个人访问令牌
headers = {"PRIVATE-TOKEN": private_token}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 将响应内容从JSON格式解析为Python字典列表
    commits = response.json()
    # 打印Commits信息
    for commit in commits:
        print(f"Commit ID: {commit['id']}, Message: {commit['message']}, Committer: {commit['committer_name']}, Date: {commit['committed_date']}")
        print("#################################################")
        print("   ")
else:
    print(f"Failed to retrieve commits. Status code: {response.status_code}")
