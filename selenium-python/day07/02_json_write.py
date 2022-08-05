"""
    目标：写入json
    案例：
        1. data = {"name":"tom", "age":18}
        2. data = {"name":"李四", "age":18}
    操作：
        1. 导包 json
        2. 方法 dump(写什么内容,忘哪里写)
    注意：
        1. 写入操作  w
        2. 写入方法：dump()而不是dumps()
"""
# 导包
import json

# 定义 写的内容
# data = {"name": "tom", "age": 18}
data = {"name": "32", "age": 1318}
# 获取文件流 并 写入数据
"""
    ensure_ascii：设置编码格式-解决中文问题；
"""
with open("data/write.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
