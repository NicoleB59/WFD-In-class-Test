from django.db import models

# Car Model
class Car(models.Model):
    serial_number = models
    make = models
    model = models
    color = models
    year = models
    for_sale = models

    def __str__(self):
        return f"{self.serial_number} {self.make} {self.model} {self.year} {self.for_sale}"
# Customer model
class Customer(models.Model):
    first_name = models
    last_name = models
    Phone_no = models
    Address = models
    City = models
    State = models
    Postal_code = models

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.Phone_no} {self.Address} {self.City} {self.State} {self.Postal_code}"

# sales_Invoice model
class sales_Invoice(models.Model):
    customer = models
    Date = models
    Car = models
    Customer = models
    Salesperson = models

    def __str__(self):
        return f"{self.customer} {self.Date} {self.Car} {self.Customer} {self.Salesperson}"

# salesperson model
class  salesPerson(models.Model):
    first_name = models
    last_name = models

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# serviceTicket model
class serviceTicket(models.Model):
    serviceTicket = models
    Car = models
    Customer = models
    DateRec = models
    Comment = models
    DateRecToCustomer = models

    def __str__(self):
        return f"{self.serviceTicket} {self.Car} {self.Customer}"

# serviceID model
class service_ID(models.Model):
    service_name = models
    Hourly_Rate = models

    def __str__(self):
        return f"{self.service_name} {self.Hourly_Rate}"

# parts model
class Parts(models.Model):
    Parts_number = models
    Description = models
    Purchase_price = models
    Retail_price = models

    def __str__(self):
        return f"{self.Parts_number} {self.Description} {self.Purchase_price}"

# parts used model
class parts_Used_ID(models.Model):
    Parts = models
    Service_ID = models
    Number_used = models
    Price = models

# service mechanic id model
class serviceMechanic_ID(models.Model):
    serviceTicket = models
    serviceMechanic_ID = models
    service_ID = models
    hours = models
    comment = models
    rate = models

    def __str__(self):
        return f"{self.serviceTicket} {self.Service_ID}"

# mechanic id model
class Mechanic_ID(models.Model):
    Last_name = models
    First_name = models











