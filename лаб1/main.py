# гра в якій можна купляти предмети і використовувати їх
from abc import ABC, abstractmethod

class Item(ABC):
  def __init__(self, name, price = 0):
    self.name = name
    self.price = price

  @abstractmethod
  def use(self):
    pass
  
class Food(Item):
  def use(self):
    print(f" Ти з'їв {self.name}")
  
class Potion(Item):
  def use(self):
    print(f" Ти випив {self.name}")

class Player:
  def __init__(self, name, balance):
    self.name = name
    self._balance = balance
    self.inventar = []

  def buy(self, item):
    if self._balance >= item.price:
      self._balance -= item.price
      self.inventar.append(item)
      print(f"{self.name} купив {item.name}. Залишок: {self._balance}")
    else:
      print(f"В тебе недостатньо грошей щоб купити {item.name}")

  def get_balance(self):
    return self._balance
  
  def use_items(self):
    print("Використання предметів з твого інвентарю:")
    while self.inventar:
      item = self.inventar.pop(0)
      item.use()
    print("Твій інвентар порожній")
  

apple = Food("Яблуко", 20)
potion_helth = Potion("Зілля здоров'я", 50)
pie = Food("Пиріг", 35)

player1 = Player("Raf", 100)

player1.buy(apple)
player1.buy(potion_helth)
player1.buy(pie)
print(f"Залишок грошей: {player1.get_balance()}")
print("-----------------")
player1.use_items()