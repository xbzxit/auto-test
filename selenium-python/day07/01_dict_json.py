"""
    目标：将python中的字典转为 json字符串
    案例：data = {"name":"张三", "age":18}
    操作：
        1. 导包  import json
        2. 调用dumps()方法 将字典转换为 json字符串
    注意：
        json中：还有一个方法 dump()写入json，勿要选错；
"""

# 导包
import json

"""将字典转换为json字符串"""
# 定义 字典
# data = {"name":"张三", "age":18}
# 调用dumps进行转换json字符串
# print("转换之前的数据类型：", type(data))
# d2 = json.dumps(data)
# print("转换之后的数据类型：", type(d2))
# print(d2)

"""
    目标：将字符串转为json
    方法：loads() 将字符串转为字典
    注意：load() 此方位为读取json方法，千万别写错了。
"""

# 定义 字符串
data = '{"data":"张三", "age":18}'
# 注意错误写法 ，属性名必须使用双引号
# data = "{'data':'张三', 'age':18}"
print("转之前：", type(data))
# 转换
d3 = json.loads(data)
print("转之后：", type(d3))
