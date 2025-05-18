from abc import ABC, abstractmethod

class IProduct(ABC):
  @abstractmethod
  def cost(self): pass

  @abstractmethod
  def name(self): pass

class Product(IProduct):
  def __init__(self, name, price):
    self._name = name
    self._price = price

  def cost(self):
    return self._price

  def name(self):
    return self._name

class CompoundProduct(IProduct):
  def __init__(self, name):
    self._name = name
    self._items = []

  def add(self, item: IProduct):
    self._items.append(item)

  def cost(self):
    return sum(item.cost() for item in self._items)

  def name(self):
    return self._name

  def describe(self):
    print(f"\n Піца: {self.name()}")
    for item in self._items:
        print(f" - {item.name()}: {item.cost()} грн")
    print(f" Вартість: {self.cost()} грн")

class Kitchen:
  def prepare_pizza(self, pizza):
    print(f"\n Замовленна піца готується")
    pizza.describe()

class Waiter:
  def take_order(self, client_name, pizza):
    print(f"\n Офіціант приймає від клієнта '{client_name}' замовлення'")

  def serve_pizza(self, client_name, pizza):
    print(f"Офіціант подає '{pizza.name()}' клієнту '{client_name}'")

class PizzaMenu:
  def get_mozarella_pizza(self):
    dough = CompoundProduct("Тісто")
    dough.add(Product("Борошно", 10))
    dough.add(Product("Вода", 5))
    dough.add(Product("Сіль", 0.5))

    sauce = Product("Соус томатний", 20)

    topping = CompoundProduct("Сирна начинка")
    topping.add(Product("Моцарела", 40))
    topping.add(Product("Томати", 10))

    pizza = CompoundProduct("Моцарелла")
    pizza.add(dough)
    pizza.add(sauce)
    pizza.add(topping)

    return pizza

  def get_meat_pizza(self):
    dough = CompoundProduct("Тісто")
    dough.add(Product("Борошно", 10))
    dough.add(Product("Яйце", 5))
    dough.add(Product("Олія", 5))
    dough.add(Product("Сіль", 0.5))

    sauce = Product("BBQ Соус", 30)

    topping = CompoundProduct("Начинка")
    topping.add(Product("Салямі", 20))
    topping.add(Product("Бекон", 20))
    topping.add(Product("Шинка", 20))

    pizza = CompoundProduct("М'ясна піца")
    pizza.add(dough)
    pizza.add(sauce)
    pizza.add(topping)

    return pizza

class PizzaOrderingFacade:
  def __init__(self):
    self.kitchen = Kitchen()
    self.waiter = Waiter()
    self.menu = PizzaMenu()

  def order_pizza(self, client_name, pizza_type):
    if pizza_type == "моцарелла":
        pizza = self.menu.get_mozarella_pizza()
    elif pizza_type == "м'ясна":
        pizza = self.menu.get_meat_pizza()
    else:
        print("Такої піци немає в меню.")
        return

    self.waiter.take_order(client_name, pizza)
    self.kitchen.prepare_pizza(pizza)
    self.waiter.serve_pizza(client_name, pizza)


facade = PizzaOrderingFacade()
facade.order_pizza("Yulia", "моцарелла")