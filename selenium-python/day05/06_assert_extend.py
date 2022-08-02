"""
    目标断言扩展：
        两种实现方式：
            1. 使用unittest框架中的断言
            2. 使用python自带断言
"""
# 使用python自带断言 判断两个字符串是否相等
assert "hello" == "hello"
# 不相等
assert "hello" == "hello1" "出错啦啦啦！！！这俩不相等"

# 第二个字符串是否包含第一个字符串
assert "h" in "hello"
assert "ha" in "hello"

# 判断是否为True
assert True
assert False
# 0 为False ; 1为True
assert 0
assert 1