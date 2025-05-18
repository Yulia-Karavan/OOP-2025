import copy 

DOUGH_THIN = "тонке"
DOUGH_THICK = "товсте"

SAUCE_TOMATO = "томатний"
SAUCE_BBQ = "барбекю"

TOPPING_MOZZARELLA = "моцарела"
TOPPING_SALAMI = "салямі"
TOPPING_BACON = "бекон"
TOPPING_HAM = "шинка"


class Pizza():
  def __init__(self, name, dough, sauce, toppings, time):
    self.name = name
    self.dough = dough
    self.sauce = sauce
    self.toppings = toppings if toppings else []
    self.time = time

  def clone(self):
    return Pizza(self.name, self.dough, self.sauce, self.toppings.copy(), self.time)

  def __str__(self):
    toppings_list = ', '.join(self.toppings)
    return (f" Піцца: {self.name}\n"
            f"  - Тісто: {self.dough}\n"
            f"  - Соус: {self.sauce}\n"
            f"  - Начинка: {toppings_list}\n"
            f"  - Час приготування: {self.time} хв\n")

margarita = Pizza("Маргарита", DOUGH_THICK, SAUCE_TOMATO, [TOPPING_MOZZARELLA], 20)
print(margarita)

spicy_margarita = margarita.clone()
spicy_margarita.name = "Маргарита з салямі"
spicy_margarita.toppings.append(TOPPING_SALAMI)
print(spicy_margarita)

bbq_pizza = spicy_margarita.clone()
bbq_pizza.name = "BBQ Піцца"
bbq_pizza.sauce = SAUCE_BBQ
bbq_pizza.toppings.append(TOPPING_BACON)
print(bbq_pizza)

meat = copy.deepcopy(bbq_pizza)
meat.name = "м'ясна"
meat.toppings.append(TOPPING_HAM)
print(meat)