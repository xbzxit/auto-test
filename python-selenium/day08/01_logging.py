# 导包
import logging

# 设置日志级别
# logging.basicConfig(level=logging.DEBUG)

# 设置修改默认的输入日志格式
fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fm)

# 调用 指定级别，输入日志信息
logging.debug("this is a debug...")
logging.info("this is a info...")
logging.warning("this is a warning...")
logging.error("this is a error...")
logging.critical("this is a critical...")
