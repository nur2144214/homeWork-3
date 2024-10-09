class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        moneys = input("введите на счет деньги:")
        if moneys.isdigit():
            moneys = float(moneys)
            self._balance += moneys
        else:
            print("неправильный ввод")

    def _kill(self):
        self._balance = 0
        print("баланс обнулен")

    def __jackpot(self):
        self._balance *= 10
        print(f"Ваш баланс увеличился в 10 раз: {self._balance}")

    def combine_balance(self, other_bank):
        self._balance += other_bank.__balance
        print(f"Новый баланс: {self._balance}")


A = Bank("A", 50)
A.moneyX()


