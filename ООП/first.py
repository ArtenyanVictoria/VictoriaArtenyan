# 14. Продолжение тринадцатой задачи… создать метод show_inf, который будет печатать информацию,
# которая содержится в в словаре information. При том печатать таким образом:
#     1. name       	 ===> 	 None
#     2. last_name  	 ===> 	 None
#     3. years      	 ===> 	 None
#     4. city       	 ===> 	 None
#     5. passport   	 ===> 	 None

# 15. Продолжение четырнадцатой задачи… создать метод change_info, который может принимать от нуля, до пяти аргументов,
# у всех них стоит по умолчанию значение None, и если мы указываем этот аргумент, то его изменяем, изменяем в словаре
# эти данные


class Bank:
    def __init__(self, name=None, last_name=None, years=None, city=None, passport=None):
        self.__information = {}
        self.__information['name'] = name
        self.__information['last_name'] = last_name
        self.__information['years'] = years
        self.__information['city'] = city
        self.__information['passport'] = passport

    def show_inf(self):
        lst = list(self.__information.keys())
        for i in range(1, 6):
            if lst[i - 1] not in self.__information:
                print(f"{i}. {lst[i - 1]} " + ' ' * (20 - len(str(i)) - len(lst[i - 1])) + '===>' + '     ' + 'None')
            else:
                print(f"{i}. {lst[i - 1]} " + ' ' * (20 - len(str(i)) - len(lst[i - 1])) + '===>' + '     ' + self.__information[lst[i - 1]])




