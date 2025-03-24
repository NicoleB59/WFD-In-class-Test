class Phone:
    def __init__(self, brand: str, model: str, year: int, price: float, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.color = color

    def print_attributes(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: {self.price}, Color: {self.color}")
        
    def update_brand(self, brand: str):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError("Brand must be a string.")

    def update_model(self, model: str):
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError("Model must be a string.")
    
    def update_year(self, year: int):
        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError("Year must be a int.")
    
    # The int was not working so I converted the number to a floating-point number.
    def update_price(self, price: float):
        if isinstance(price, (float, int)):
            self.price = float(price)
        else:
            raise ValueError("Price must be a float or integer.")
    
    def update_color(self, color: str):
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Color must be a string.")

# Creating instances
phone1 = Phone("Samsung", "Galaxy S21", 2021, 799.99, "Pink")
phone2 = Phone("Apple", "iPhone 11", 2020, 599.99, "Purple")

# calling print attributes
print(f"These are the current phones: ")
phone1.print_attributes()
phone2.print_attributes()

# updating the price of the attributes
phone1.update_price(749.99)
phone2.update_color("yellow")

# print updated attributes
print(f"These are the updated phones: ")
phone1.print_attributes()
phone2.print_attributes()

#Child class
class Smartphone(Phone):
    def __init__(self, brand: str, model: str, year: int, price: float, color: str, os: str, storage: int):
        super().__init__(brand, model, year, price, color)
        self.os = os
        self.storage = storage

    def print_attributes(self):
        super().print_attributes()
        print(f"OS: {self.os}, Storage: {self.storage}GB")

    def update_os(self, os: str):
        if isinstance(os, str):
            self.os = os
        else:
            raise ValueError("OS must be a string.")

    def update_storage(self, storage: int):
        if isinstance(storage, int):
            self.storage = storage
        else:
            raise ValueError("Storage must be an integer.")

# creating an instance for the smartphone with extra features shown.
print(f"These are the current phones: ")
smartphone1 = Smartphone("Apple", "iPhone 13", 2021, 999.99, "Pink", "iOS", 128)
smartphone2 = Smartphone("Apple","iPhone 11", 2020, 599.99, "Purple", "iOS", 64)

# print the attributes
smartphone1.print_attributes()
smartphone2.print_attributes()

# update the attributes
smartphone1.update_os("IOS 18")
smartphone2.update_storage(128)

# print updates attributes
print(f"These are the updated phones: ")
smartphone1.print_attributes()
smartphone2.print_attributes()

