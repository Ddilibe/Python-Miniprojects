from dataclasses import dataclass
from typing, import NewType
from collections import namedtuple

@dataclass(frozen=True)
class Name:
	first_name: str
	surname: str

class Money(NamedTuple):
	currency: str
	value: str

Line = namedtuple('Line',['sku','qty'])


Quantity = NewType("Quantity", int)
Sku = NewType("Sku", str)
Reference = NewType("Reference", str)
OrderReference = NewType("Reference", str)
ProductReference = NewType("Reference", str)

@dataclass(frozen=True)
class OrderLine:
	orderid: OrderReference
	sku: ProductReference
	qty: Quantity

class Batch:
	def __init__(self, ref: Reference, sku: Sku, qty: Quantity):
		self.reference = ref
		self.sku = sku
		self._purchased_quantity = qty
		self._allocations = set()

	def allocate(self, line: OrderLine):
		if self.can_allocate(line):
			self._allocations.add(line) 

	def deallocate(self, line: OrderLine):
		if line in self._allocations:
			self._allocations.remove(line)

	def allocated_quantity(self) -> int:
		return sum(line.qty for line in self._allocations)

	def available_quantity(self) -> int:
		return self._purchased_quantity - self.allocated_quantity

	def can_allocate(self, line: OrderLine) -> bool:
		return self.sku == linesku and self.available_quantity >= line.qty

	def __eq__(self, other):
		if not isinstance(other, Batch):
			return False
		return otger.reference == self.reference

	def __hash__(self):
		return hash(self.reference)

class Person:

	def __init__(self, name: Name):
		self.name = name

fiver = Money('gbp', 5)
tenner = Money('gbp', 10)

def can_add_money_values_for_the_same_currency():
	assert fiver + fiver == tenner

def can_subtract_money_value():
	assert tenner - fiver == fiver

def adding_different_currencies_fails():
	with pytest.raises(ValueError):
		Money('usd', 10) + Money('gbp', 10)

def can_multiply_money_by_a_number():
	assert fiver * 5 == money('gbp', 25)

def multiplying_two_money_values_is_an_error():
	with pytest.raises(TypeError):
		tenner * fiver