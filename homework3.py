### Задание 3.1: Безопасный калькулятор

s = input('Введите уравнение\n')

try:
    if '*' in s:
        first, second = s.split('*')
        print(int(first)*int(second))
    elif '-' in s:
        first, second = s.split('-')
        print(int(first)-int(second))
    elif '+' in s:
        first, second = s.split('+')
        print(int(first)+int(second))
    elif '/' in s:
        first, second = s.split('/')
        if int(second) == 0:
            print('Деление на ноль')
        else:
            print(int(first)/int(second))
    else:
        print('Неизвестная операция')
except ValueError:
    print('Некорректный ввод')
except Exeption:
    print('Неизвестная ошибка')

### Задание 3.2: Чтение файла с обработкой ошибок

try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('Файл не найден')
except PermissionError:
    print('Отказано в доступе')
except UnicodeDecodeError:
    print('Ошибка в декодировании')
finally:
    print('Файл успешно закрыт')

### Задание 3.3: Кастомные исключения

class InsufficientFundsError(Exception):
    pass
class InvalidAccountError(Exception):
    pass
class TransactionLimitError(Exception):
    pass

def add_to_dict_immutable(d: dict, key, value):
    new_dict = d.copy()
    new_dict[key] = value
    return new_dict

class BankAccount:
    accounts = {}
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        BankAccount.accounts[self.account_number] = self
        self.transaction_count = 0
        self.transaction_limit = 100

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError('Недостаточно средств для снятия')
        if self.transaction_count >= self.transaction_limit:
            raise TransactionLimitError("Превышен лимит транзакций в месяц")
        self.transaction_count += 1


        self.balance -= amount

    def transfer(self, amount, target_account):
        if self.balance < amount:
            raise InsufficientFundsError('Недостаточно средств для перевода')
        if target_account.account_number not in BankAccount.accounts:
            raise InvalidAccountError('Неверный номер счёта')
        if self.transaction_count >= self.transaction_limit:
            raise TransactionLimitError("Превышен лимит транзакций в месяц")
        self.balance -= amount
        target_account.balance += amount
        self.transaction_count += 1