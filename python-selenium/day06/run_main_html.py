# 导包
import unittest

from tools.HTMLTestRunner import HTMLTestRunner

# 定义 测试套件
suite = unittest.defaultTestLoader.discover("./", pattern="02*.py")
# 执行
with open("./report/report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)
