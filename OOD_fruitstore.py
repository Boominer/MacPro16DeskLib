class Fruit: 
    def __init__(self, name: str, base_price: float, strategy: None):
        self.name = name 
        self.price = base_price
        self.strategy = strategy or PricingStrategy()

    def get_description(self):
        return f'{{self.name} at price: {self.base_price}}'

    def get_price(self):
        return self.strategy.calculate_price(self.base_price)

class Banana(Fruit):
    def __init__(self, price:float):
        super().__init__('Banana', price)

class Apple(Fruit):
    def __init__(self, price:float):
        super().__init__('Apple', price)

class FruitStore:
    def __init__(self):
        self.inventory = []

    def add_fruit(self, fruit:Fruit):
        self.inventory.append(fruit)

    def get_all_fruits(self):
        return [fruit.get_description() for fruit in self.inventory]

# Factory pattern
class FruitFactory:
    @staticmethod 
    def create_fruit(name: str, price:float):
        if name.lower() == 'banaa':
            return Fruit('banaa',price)
        elif name.lower() == 'apple':
            return Fruit('apple', price)
        else:
            return Fruit(name, price)

# strategy pattern 
class PricingStrategy:
    def calculate_price(self, base_price:float) -> float:
        return base_price 
    
class SeasonalDiscount(PricingStrategy):
    def calculate_price(self, base_price:float) -> float:
        # 20% off for the hot seasonal discount 
        return base_price * 0.8

class BonusDiscount(PricingStrategy):
    def calculate_price(self, base_price:float) -> float:
        # apply a fixed bonus discount 
        base = super().calculate_price(base_price)
        return base - 2 

