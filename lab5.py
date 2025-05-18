from abc import ABC, abstractmethod

class OperationStrategy(ABC):
  @abstractmethod
  def execute(self, atm):
    pass

class WithdrawCash(OperationStrategy):
  def __init__(self, amount):
    self.amount = amount

  def execute(self, atm):
    if self.amount <= atm.cash:
      print(f"Видано {self.amount} грн.")
      atm.cash -= self.amount
    else:
      print("Недостатньо коштів у банкоматі.")
    atm.set_state(WaitingForCardState())

class CheckBalance(OperationStrategy):
  def execute(self, atm):
    print(f"Кеш: {atm.cash} грн.")
    atm.set_state(WaitingForCardState())


class ATMState(ABC):
  @abstractmethod
  def insert_card(self, atm):
    pass

  @abstractmethod
  def enter_pin(self, atm, pin):
    pass

  @abstractmethod
  def select_operation(self, atm, operation):
    pass

class WaitingForCardState(ATMState):
  def insert_card(self, atm):
    print("Картку вставлено. Введіть пін код")
    atm.set_state(CheckingPinState())

  def enter_pin(self, atm, pin):
    print("Ви не вставили картку.")

  def select_operation(self, atm, operation):
    print("Ви не вставили картку.")

class CheckingPinState(ATMState):
  def insert_card(self, atm):
    print("Картку уже вставлено.")

  def enter_pin(self, atm, pin):
    if pin == "1234":
      print("Правильний PIN. Оберіть операцію.")
      atm.set_state(SelectingOperationState())
    else:
      print("Невірний PIN.")

  def select_operation(self, atm, operation):
    print("Спочатку введіть PIN.")

class SelectingOperationState(ATMState):
  def insert_card(self, atm):
    print("Картку уже вставлено.")

  def enter_pin(self, atm, pin):
    print("PIN вже введено.")

  def select_operation(self, atm, operation):
    atm.set_strategy(operation)
    print("Виконується...")
    atm.perform_operation()


class ATM:
  def __init__(self, initial_cash):
    self.cash = initial_cash
    self.state = WaitingForCardState()
    self.strategy = None

  def set_state(self, state):
    self.state = state

  def set_strategy(self, strategy):
    self.strategy = strategy

  def perform_operation(self):
    self.strategy.execute(self)

  def insert_card(self):
    self.state.insert_card(self)

  def enter_pin(self, pin):
    self.state.enter_pin(self, pin)

  def select_operation(self, operation):
    self.state.select_operation(self, operation)


atm = ATM(initial_cash=1000)

atm.insert_card()
atm.enter_pin("1234")
atm.select_operation(WithdrawCash(300))

print("------")

atm.insert_card()
atm.enter_pin("1234")
atm.select_operation(CheckBalance())
atm.select_operation(WithdrawCash(7))