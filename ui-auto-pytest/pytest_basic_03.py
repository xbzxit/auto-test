# www.pytest.org
# pip install pytest

# 测试类形式


# 类名以Test开头
import pytest


class TestDemo(object):

    def test_method1(self):
        print("method1")

    # 方法名以 test开头
    def test_method2(self):
        print("method2")


if __name__ == '__main__':
    pytest.main(['-s', 'pytest-basic_03.py'])

