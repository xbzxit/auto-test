# 导包
import json


def read_json(filename):
    filepath = "../data/" + filename
    # 打开文件并调用 load方法
    with open(filepath, "r", encoding="utf-8")as f:
        return json.load(f)


if __name__ == '__main__':
    print(read_json("login.json"))
    """
        需求格式：[(),(),(),(),(),()]
        实际格式为：{"login_001":{}}
    """
    print("--" * 50)

    # 定义空列表
    arrs = []
    for data in read_json("login.json").values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("verify_code"),
                     data.get("expect_result"),
                     data.get("success")))
    print(arrs)
