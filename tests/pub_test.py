import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food 

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink('Whisky', 5.00, True, 1)
        self.drink2 = Drink('Irn Bru', 2.00, False, 0)
        self.drink3 = Drink('Beer', 4.00, True, 1.50)
        self.food = Food("Crisps", 1.00, 0.5)
        self.pub = Pub('The Prancing Pony', 100.00, [self.drink1, self.drink2, self.drink3], [self.food, self.food])
       
    def test_pub_has_name(self):
        self.assertEqual('The Prancing Pony', self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(3, len(self.pub.drinks))

    def test_pub_finds_drink(self):
        self.assertEqual(self.drink2, self.pub.find_drink_by_name('Irn Bru'))
        self.assertEqual(None, self.pub.find_drink_by_name('Water'))

    def test_pub_can_add_drink(self):
        self.drink = Drink('Wine', 4.50, True, 2.00)
        self.pub.add_drink(self.drink)
        self.assertEqual(True, self.drink in self.pub.drinks)

    def test_pub_can_remove_drink(self):
        self.pub.remove_drink('Whisky')
        self.assertEqual(2, len(self.pub.drinks))
    
    def test_pub_has_foods(self):
        self.assertEqual(2, len(self.pub.foods))

    def test_pub_finds_food(self):
        self.assertEqual(self.food, self.pub.find_food_by_name('Crisps'))
        self.assertEqual(None, self.pub.find_food_by_name('Cake'))

    def test_pub_can_add_food(self):
        self.food = Food('Peanuts', 1.50, 1.00)
        self.pub.add_food(self.food)
        self.assertEqual(True, self.food in self.pub.foods)

    def test_pub_can_remove_food(self):
        self.pub.remove_food('Crisps')
        self.assertEqual(1, len(self.pub.foods))

    def test_get_id_young(self):
        self.customer_young = Customer("JP O'Reilly", [], 10.00, 17, 0)
        self.assertEqual (False, self.pub.get_id (self.customer_young))
        
    def test_get_id_old(self):
        self.customer_old = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27, 4)
        self.assertEqual (True, self.pub.get_id (self.customer_old))

    def test_pub_can_sell_drink_old_alco(self):
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27, 4)
        self.pub.sell_drink(self.customer, 'Beer')
        self.assertEqual(3, len(self.customer.stomach))
        self.assertEqual(2.00, self.customer.wallet)
        self.assertEqual(104.00, self.pub.till)
        self.assertEqual(False, self.drink3 in self.pub.drinks)

    def test_pub_can_sell_drink_old_soft(self):
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27, 4.00)
        self.pub.sell_drink(self.customer, 'Irn Bru')
        self.assertEqual(3, len(self.customer.stomach))
        self.assertEqual(4.00, self.customer.wallet)
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(False, self.drink2 in self.pub.drinks)

    def test_pub_can_sell_drink_young_alco(self):
        self.customer = Customer("JP O'Reilly", [], 10.00, 17, 0)
        self.pub.sell_drink(self.customer, 'Beer')
        self.assertEqual(0, len(self.customer.stomach))
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(True, self.drink3 in self.pub.drinks)

    def test_pub_can_sell_drink_young_soft(self):
        self.customer = Customer("JP O'Reilly", [], 10.00, 17, 0)
        self.pub.sell_drink(self.customer, 'Irn Bru')
        self.assertEqual(1, len(self.customer.stomach))
        self.assertEqual(8.00, self.customer.wallet)
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(False, self.drink2 in self.pub.drinks)

    def test_pub_can_sell_drink_too_poor(self):
        self.customer = Customer("JP O'Reilly", [], 1.00, 30, 0)
        self.pub.sell_drink(self.customer, 'Beer')
        self.assertEqual(0, len(self.customer.stomach))
        self.assertEqual(1.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(True, self.drink3 in self.pub.drinks)

    def test_pub_can_sell_drink_doesnt_exist(self):
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27, 4)
        self.pub.sell_drink(self.customer, 'Water')
        self.assertEqual(2, len(self.customer.stomach))
        self.assertEqual(6.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(3, len(self.pub.drinks))

    def test_pub_can_sell_drink_too_drunk(self):
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27, 8.00)
        self.pub.sell_drink(self.customer, 'Irn Bru')
        self.assertEqual(2, len(self.customer.stomach))
        self.assertEqual(6.00, self.customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(True, self.drink2 in self.pub.drinks)

    def test_pub_can_sell_food(self):
        self.food = Food("Crisps", 1.00, 0.5)
        self.customer = Customer("Stephen O'Reilly", [self.drink1, self.drink2], 6.00, 27, 8.00)
        self.pub.sell_food(self.customer, "Crisps")
        self.assertEqual(5.00, self.customer.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(7.5, self.customer.drunkeness)
        