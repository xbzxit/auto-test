"""
    目标： 学习 logging底层 模块实现
        1. logger
"""
# 注意以后导logging包，不在使用此方式
# import logging

# 导包时 导入 import logging.handlers 推荐：原因 logging是包名，导入包名时会自动执行包下面的__init__文件，所以这样导入，相当于导入 logging
# handlers为模块名称
import logging.handlers

# 获取logger
# logger = logging.getLogger()

# 修改名称

logger = logging.getLogger("admin")

# 设置级别
logger.setLevel(logging.INFO)

# 获取控制台 处理器
sh = logging.StreamHandler()
# 到文件 根据时间切割
th = logging.handlers.TimedRotatingFileHandler(filename="./log/logtime.log",
                                               when="S",
                                               interval=1,
                                               backupCount=3)

# 设置 处理器 级别 扩展 设置未error级别，那么只有error级别信息才会写入文件
th.setLevel(logging.ERROR)

# 添加格式器
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
fm = logging.Formatter(fmt)

# 将格式器 添加到处理器中
sh.setFormatter(fm)
th.setFormatter(fm)

# 将 控制台处理器添加到 logger
logger.addHandler(sh)
logger.addHandler(th)

# while True:
#     sleep(1)
#     # 输入信息
#     logger.info("info")
#     logger.debug("debug")


logger.info("info")
logger.debug("debug")
logger.error("error")
logger.warning("warning")
