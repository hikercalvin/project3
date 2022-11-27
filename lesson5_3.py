print(__name__)
print(type(__name__))
print(__file__)
#一個專案內的主執行的py檔，必須要使用__name__的判斷式
if __name__ == '__main__':
    print("這是整個專案內，被PYTHON執行的主要執行檔")