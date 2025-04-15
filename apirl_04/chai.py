from abc import ABC,abstractmethod
class Chai(ABC):
    @abstractmethod
    def __init__(self,name,base_price,quantity_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_stock=quantity_stock
    def calculate_price():
        pass
    def display_info():
        pass
class MasalaChai(Chai):
     def __init__(self,name,base_price,quantity_stock):
         super().__init__(self,name,base_price,quantity_stock)
         self.base_price+=10
     def calculate_price(base_price):
         return self.base_price
     def display_info():
         print(f"Name: {self.name} | Price per cup:{self.base_price} | Stock:{self.quantity_stock}")
class GingerChai(Chai):
     def __init__(self,name,base_price,quantity_stock):
         super(). __init__(self,name,base_price,quantity_stock)
         self.base_price+=8
     def calculate_price(base_price):
        return self.base_price

     def display_info():
        print(f"Name: {self.name} | Price per cup:{self.base_price} | Stock:{self.quantity_stock}")
class ELachiChai(Chai):
    def __init__(self,name,base_price,quantity_stock):
         super(). __init__(self,name,base_price,quantity_stock)
         self.base_price+=12
    def calculate_price(base_price):
        return self.base_price
    def display_info():
        print(f"Name: {self.name} | Price per cup:{self.base_price} | Stock:{self.quantity_stock}")
class ChaiInventory():
    def __init__(self):
        self.inventory=[]
    def add_chai(self,chai):
        self.inventory.append(chai)
    def show_inventory(self):
        for chai in self.inventory:
            print(f"Name: {chai.name} | Price per cup:{chai.base_price} | Stock:{chai.quatity_stock}")
    def get_total_inventory_value(self):
        total_value=sum(chai.calulate_price for char in self.inventory)
        return total_value
inventory = ChaiInventory()

chai1 = MasalaChai("Masala Chai", 20, 50)
chai2 = GingerChai("Ginger Chai", 18, 40)
chai3 = ElaichiChai("Elaichi Chai", 25, 30)

inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()

print("Total Inventory Value: ₹", inventory.get_total_inventory_value())    
