# Определение класса Account
class Account:
    # Метод инициализации класса
    def __init__(self, owner, balance=0):
        self.owner = owner  # Сохранение владельца счета как публичного атрибута
        self.__balance = balance  # Инициализация баланса как приватного атрибута

    # Метод для добавления средств на счет
    def deposit(self, amount):
        self.__balance += amount  # Увеличение баланса на указанную сумму
        print(f"Added {amount} to the balance")  # Вывод сообщения о депозите

    # Метод для снятия средств со счета
    def withdraw(self, amount):
        if amount > self.__balance:  # Проверка достаточности средств на счете
            print("Not enough funds")  # Вывод сообщения об ошибке при недостаточности средств
            return
        self.__balance -= amount  # Уменьшение баланса на указанную сумму
        print(f"Withdrew {amount} from the balance")  # Вывод сообщения о снятии

    # Метод для получения текущего баланса
    def get_balance(self):
        return self.__balance  # Возвращает текущий баланс

# Создание экземпляра класса Account с именем владельца "John" и начальным балансом по умолчанию (0)
acc = Account("John")

# Вызов метода deposit для добавления 100 единиц на счет
acc.deposit(100)
# Вывод текущего баланса с использованием метода get_balance
print(acc.get_balance())

# Вызов метода withdraw для снятия 50 единиц со счета
acc.withdraw(50)
# Вывод текущего баланса после снятия
print(acc.get_balance())
