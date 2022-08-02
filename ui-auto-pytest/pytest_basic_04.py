# www.pytest.org
# pip install pytest

# 函数形式
import pytest


def test_fun():
    print("测试函数")


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_basic_04.py'])

