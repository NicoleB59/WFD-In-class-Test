import unittest
# For some reason my import is not working
from PartA.PartA import Phone, Smartphone

class TestPhoneMethods(unittest.TestCase):

    def setUp(self):
        self.phone1 = Phone("Samsung", "Galaxy S21", 2021, 799.99, "Pink")
        self.phone2 = Phone("Apple", "iPhone 11", 2020, 599.99, "Purple")
        self.smartphone1 = Smartphone("Apple", "iPhone 13", 2021, 999.99, "Pink", "iOS", 128)

    def test_is_instance_of_phone(self):
        self.assertIsInstance(self.phone1, Phone)

    def test_is_not_instance_of_phone(self):
        self.assertNotIsInstance(self.phone1, Smartphone)

    def test_objects_are_identical(self):
        phone_clone = Phone("Samsung", "Galaxy S21", 2021, 799.99, "Pink")
        self.assertEqual(self.phone1, phone_clone)

    def test_update_methods(self):
        self.phone1.update_price(749.99)
        self.phone1.update_color("Blue")
        self.assertEqual(self.phone1.price, 749.99)
        self.assertEqual(self.phone1.color, "Blue")

    def test_smartphone_update_methods(self):
        self.smartphone1.update_os("iOS 15")
        self.smartphone1.update_storage(256)
        self.assertEqual(self.smartphone1.os, "iOS 15")
        self.assertEqual(self.smartphone1.storage, 256)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
