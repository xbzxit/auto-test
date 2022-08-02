# www.pytest.org
# pip install pytest

# 函数形式
import pytest


class TestDemo(object):


    def setup(self):
        print("setup")

    def test_method(self):
        print("method")

    def teardown(self):
        print("teardown")


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_basic_05.py'])
