#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    self._discount = discount

  @property
  def total(self):
    return self._total

  @total.setter
  def total(self, total):
    self._total = total

  @property
  def items(self):
    return self._items

  @items.setter
  def items(self, items = []):
    self._items = items
  
  @property
  def last_transaction_price(self):
    self.last_transaction_price = 0
  @property
  def last_transaction_amount(self):
    self.last_transaction_amount = 0

  def add_item(self, new_item, price, amount = 1):
    for item in range(amount):
      self._items.append(new_item)
    self._total += price * amount
    self._last_transaction_price = price
    self._last_transaction_amount = amount
  
  def apply_discount(self):
    if self._discount == 0:
      print("There is no discount to apply.")
    else:
      self._total = self._total - (self._total * (self._discount )/ 100)
      print("After the discount, the total comes to $" + str(int(self._total)) + '.')

  def void_last_transaction(self):
    self._total = self._total - (self._last_transaction_price * self._last_transaction_amount)
    self._items.pop()