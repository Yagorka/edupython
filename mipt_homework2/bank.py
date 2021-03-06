class Value():
    def __init__(self):
        # print("init", self)
        self.val = None

    def __set__(self, obj, val):
        # print(self, obj, val) объекты Value, Account и значение передаваемое
        self.val = val * (1 - obj.commission)

    def __get__(self, obj, objtype):
        # print(self, obj, objtype) Value object, Account object, <class '__main__.Account'>
        return int(self.val)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == "__main__":
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)
