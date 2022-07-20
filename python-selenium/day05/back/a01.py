
class Test02:
    def test001(self):
        print("test001被执行")

    def test002(self):
        print("test002被执行")


# 调试语句 一般要写在 if __name__ == '__main__': 之后


if __name__ == '__main__':
    print("__name__变量的值为：", __name__)
    print("调试语句，Test02类被执行啦")
