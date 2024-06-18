from abc import ABC, abstractmethod

# Interface PizzaComponent
class PizzaComponent(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass

# Implementação concreta de PizzaComponent
class BasePizza(PizzaComponent):
    def get_description(self) -> str:
        return "Pizza base"

    def cost(self) -> float:
        return 5.00

# Decorador abstrato
class PizzaDecorator(PizzaComponent):
    def __init__(self, pizza: PizzaComponent):
        self._pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass

# Decoradores concretos
class Massa(PizzaDecorator):
    def __init__(self, pizza: PizzaComponent):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Massa"

    def cost(self) -> float:
        return self._pizza.cost() + 1.00

class Molho(PizzaDecorator):
    def __init__(self, pizza: PizzaComponent):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Molho"

    def cost(self) -> float:
        return self._pizza.cost() + 0.50

class Queijo(PizzaDecorator):
    def __init__(self, pizza: PizzaComponent):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Queijo"

    def cost(self) -> float:
        return self._pizza.cost() + 1.50

class Pepperoni(PizzaDecorator):
    def __init__(self, pizza: PizzaComponent):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Pepperoni"

    def cost(self) -> float:
        return self._pizza.cost() + 2.00

class Azeitona(PizzaDecorator):
    def __init__(self, pizza: PizzaComponent):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Azeitona"

    def cost(self) -> float:
        return self._pizza.cost() + 1.00

class Cogumelo(PizzaDecorator):
    def __init__(self, pizza: PizzaComponent):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Cogumelo"

    def cost(self) -> float:
        return self._pizza.cost() + 1.50

# Classe principal Pizzeria para fazer pedidos
class Pizzeria:
    def order_pizza(self) -> PizzaComponent:
        pizza = BasePizza()
        pizza = Massa(pizza)
        pizza = Molho(pizza)
        pizza = Queijo(pizza)
        pizza = Pepperoni(pizza)
        pizza = Azeitona(pizza)
        pizza = Cogumelo(pizza)
        return pizza

# Exemplo de uso
pizzeria = Pizzeria()
pizza = pizzeria.order_pizza()
print(pizza.get_description())
print(f"Total cost: ${pizza.cost():.2f}")
