"""Data models for customers, food products, orders, and menus."""

class Customer:
    def __init__(self, name: str) -> None:
        """Create a customer with a name and an empty purchase history."""
        self.name = name
        self.purchaseHistory = []


class Food_Product:
    def __init__(
        self, name: str, price: float, category: str, popularityRating: float
    ) -> None:
        """Create a food product with its identifying and display attributes."""
        self.name = name
        self.price = price
        self.category = category
        self.popularityRating = popularityRating


class Order:
    def __init__(self) -> None:
        """Create an empty order with a zero total cost."""
        self.items = []
        self.totalCost = 0

    def addItem(self, item: Food_Product) -> None:
        """Add a food product to the order."""
        self.items.append(item)

    def removeItem(self, item: Food_Product) -> float:
        """Remove one matching product, if present, and return the updated total."""
        if item in self.items:
            self.items.remove(item)
        return self.calculateTotal()

    def calculateTotal(self) -> float:
        """Recalculate and return the sum of the prices of all ordered items."""
        self.totalCost = sum(item.price for item in self.items)
        return self.totalCost


class Menu:
    def __init__(self) -> None:
        """Create a menu with no food products."""
        self.items = []

    def filterByCategory(self, category: str) -> list[Food_Product]:
        """Return menu products whose category exactly matches the argument."""
        return [item for item in self.items if item.category == category]

    def filterByPriceRange(
        self, minimum: float, maximum: float
    ) -> list[Food_Product]:
        """Return products priced inclusively between the supplied bounds."""
        return [item for item in self.items if minimum <= item.price <= maximum]

    def sortByPrice(self, descending: bool = False) -> list[Food_Product]:
        """Return products sorted by price, ascending unless descending is true."""
        return sorted(self.items, key=lambda item: item.price, reverse=descending)

    def sortByPopularity(self, descending: bool = True) -> list[Food_Product]:
        """Return products sorted by popularity, descending by default."""
        return sorted(self.items, key=lambda item: item.popularityRating, reverse=descending)

    def sortByName(self) -> list[Food_Product]:
        """Return products sorted alphabetically by name, ignoring case."""
        return sorted(self.items, key=lambda item: item.name.lower())


    #With the following code, it will follow its exact UML Diagram structure with all the 
    #capabailites and tools to show the relationships between the classes as defined in the UML diagram.