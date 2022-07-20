"""
    目标： 学习 logging底层 模块实现
        1. logger
"""

import logging

# 获取logger
logger = logging.getLogger()
# 设置级别
logger.setLevel(logging.INFO)

# 获取控制台 处理器
sh = logging.StreamHandler()
# 到文件 根据时间

# 将处理器添加到 logger
logger.addHandler(sh)

# 输入信息
logger.info("info")
logger.debug("debug")
