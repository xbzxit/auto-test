# 导包
import unittest

# 定义 测试套件
suite = unittest.defaultTestLoader.discover("./")
# 执行
with open("./report/report.txt", "w", encoding="utf-8") as f:
    unittest.TextTestRunner(stream=f, descriptions="跳过测试报告演示", verbosity=2).run(suite)
