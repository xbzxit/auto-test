# www.pytest.org
# pip install pytest

# 测试类形式


# 类名以Test开头
class TestDemo(object):

    def test_method1(self):
        print("method1")

    # 方法名以 test开头
    def test_method2(self):
        print("method2")

# 命令行执行 pytest -s pytest_basic_01.py


