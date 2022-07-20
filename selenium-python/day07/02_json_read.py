"""
    目标：读取json
    案例：
        读取 data/write.json
    操作：
        1. 导包 json
        2. 方法 load(文件流)
    注意：
        1. 写入操作  r
        2. 写入方法：load()而不是loads()
"""
# 导包
import json

# 打开要读取的文件流 并调用 load方法
with open("data/write.json", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
