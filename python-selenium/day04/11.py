import time

num = 11
num2 = "11"
print("num的值为：%d" % num)
# 报错
print("num的值为：%d" % num2)
# 正确
# print("num的值为：%r" %num2)

print("hello: {}".format(time.strftime("%Y_%m_%d %H_%M_%S")))
