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

def main():
  name = input("Введіть ваше ім'я: ")
  player1 = Player(name, 100)

  shop_items = [Food("Яблуко", 20, "фрукт"), Potion("Зілля здоров'я", 50), Food("Пиріг", 35, "страва"),
                Food("Картопля", 10, "овоч")]

  while True:
    print("\n Меню: ")
    print("1. Купити предмет")
    print("2. Показати інвентар")
    print("3. Використати предмети")
    print("4. Поповнити гаманець")
    print("5. Показати баланс")
    print("0. Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
      for i, item in enumerate(shop_items):
        print(f"{i+1}. {item.name} - {item.price} монет")
      try:
        choice_item = int(input("Оберіть номер предмета: ")) - 1
        if 0 <= choice_item <= len(shop_items):
          player1.buy(shop_items[choice_item])
        else:
          print("Неправельний вибір")
      except ValueError:
        print("Виберіть число!")

    elif choice == "2":
      player1.show_inventar()
    
    elif choice == "3":
      player1.use_inventory()

    elif choice == "4":
      try:
        amount = int(input("Введіть суму поповнення: "))
        player1.wallet.add_money(amount)
      except ValueError:
        print("Виберіть число!")

    elif choice == "5":
      player1.wallet.get_balance

    elif choice == "0":
      break

    else:
      print("Невідома команда.")

if __name__ == "__main__":
  main()
