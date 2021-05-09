# Напишите код с использованием наследования

class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a special dish")


myChef = Chef()
myChef.make_special_dish()


class ChineseChef(Chef):  # все  три функции тоже переходят сюда это и есть наследование от другого класса

    def make_fried_rice(self):
        print("Chef makes a fried rice")


myChinesChef = ChineseChef()
myChinesChef.make_fried_rice()
myChinesChef.make_salad()