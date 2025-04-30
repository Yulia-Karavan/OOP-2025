from abc import ABC, abstractmethod

class Item(ABC):
  def __init__(self, name, price):
    self.name = name
    self.price = price

  @abstractmethod
  def use(self):
    pass

  def __str__(self):
    return self.name
  
class Food(Item):
  def __init__(self, name, price, type):
    super().__init__(name, price)
    self.type = type

  def use(self):
    print(f" Ти з'їв {self.name}")
  
class Potion(Item):
  def use(self):
    print(f" Ти випив {self.name}")

class Wallet:
  def __init__(self, balance):
    self._balance = balance

  def get_balance(self):
    return self._balance 
  
  def add_money(self, amount):
    if amount > 0:
      self._balance += amount
      print(f"Баланс поповнено на {amount}. Новий баланс: {self._balance}")
    else:
      print("Помилка: сума поповнення повинна бути більша за 0!")

  def spend_money(self, amount):
    if self._balance >= amount:
      self._balance -= amount
      return True
    else:
      print(f"В тебе недостатньо грошей для покупки")
      return False

class Inventory:
  def __init__(self):
    self.items = []
  
  def add_items(self, item):
    self.items.append(item)

  def show_items(self):
    print("Твій інвентар: ")
    if len(self.items) == 0:
      print("  порожній")
    else:
      for i in self.items:
        print(f"  •{i}")
  
  def use_items(self):
    print("Використання предметів з твого інвентарю:")
    for item in self.items[:]:
      if isinstance(item, Food) and item.type == "овоч":
        continue
      item.use()
      self.items.remove(item)

class Player:
  def __init__(self, name, balance):
    self.name = name
    self.wallet = Wallet(balance) 
    self.inventar = Inventory()

  def buy(self, item):
    if self.wallet.spend_money(item.price):
      self.inventar.add_items(item)
      print(f"{self.name} купив {item.name}. Залишок: {self.wallet.get_balance()}")

  def use_inventory(self):
    self.inventar.use_items()

  def show_inventar(self):
    self.inventar.show_items()


apple = Food("Яблуко", 20, "фрукт")
potion_helth = Potion("Зілля здоров'я", 50)
pie = Food("Пиріг", 35, "страва")
potato = Food("Картопля", 10, "овоч")

player1 = Player("Yulia671", 100)

player1.buy(apple)
player1.buy(potion_helth)
player1.buy(pie)
player1.wallet.add_money(15)
player1.buy(pie)
player1.buy(potato)
print("-----------------")
player1.show_inventar()
player1.use_inventory()
player1.show_inventar()