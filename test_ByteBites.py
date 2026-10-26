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


class TestCustomer(unittest.TestCase):
    def test_customer_starts_with_empty_purchase_history(self):
        customer = Customer("Jordan")
        self.assertEqual(customer.name, "Jordan")
        self.assertEqual(customer.purchaseHistory, [])


class TestFoodProduct(unittest.TestCase):
    def test_product_stores_all_attributes(self):
        product = Food_Product("Taco", 4.5, "Entree", 4.8)
        self.assertEqual(
            (product.name, product.price, product.category, product.popularityRating),
            ("Taco", 4.5, "Entree", 4.8),
        )


class TestOrder(unittest.TestCase):
    def test_order_starts_empty_with_zero_total(self):
        order = Order()
        self.assertEqual(order.items, [])
        self.assertEqual(order.totalCost, 0)

    def test_add_items_and_calculate_total(self):
        order = Order()
        taco = Food_Product("Taco", 4.5, "Entree", 4.8)
        tea = Food_Product("Tea", 2.0, "Drink", 4.2)
        order.addItem(taco)
        order.addItem(tea)

        self.assertEqual(order.items, [taco, tea])
        self.assertEqual(order.calculateTotal(), 6.5)
        self.assertEqual(order.totalCost, 6.5)

    def test_remove_item_updates_total(self):
        order = Order()
        taco = Food_Product("Taco", 4.5, "Entree", 4.8)
        tea = Food_Product("Tea", 2.0, "Drink", 4.2)
        order.addItem(taco)
        order.addItem(tea)

        self.assertEqual(order.removeItem(taco), 2.0)
        self.assertEqual(order.items, [tea])

    def test_remove_missing_item_preserves_order_and_total(self):
        order = Order()
        taco = Food_Product("Taco", 4.5, "Entree", 4.8)
        soup = Food_Product("Soup", 3.0, "Entree", 4.0)
        order.addItem(taco)

        self.assertEqual(order.removeItem(soup), 4.5)
        self.assertEqual(order.items, [taco])

    def test_remove_last_item_returns_zero(self):
        order = Order()
        taco = Food_Product("Taco", 4.5, "Entree", 4.8)
        order.addItem(taco)

        self.assertEqual(order.removeItem(taco), 0)
        self.assertEqual(order.totalCost, 0)


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
        self.taco = Food_Product("Taco", 4.5, "Entree", 4.8)
        self.salad = Food_Product("salad", 6.0, "Entree", 4.2)
        self.tea = Food_Product("Tea", 2.0, "Drink", 4.2)
        self.burger = Food_Product("Burger", 8.0, "Entree", 4.9)
        self.menu.items = [self.taco, self.salad, self.tea, self.burger]

    def test_filter_by_category_matches_exactly(self):
        self.assertEqual(
            self.menu.filterByCategory("Entree"),
            [self.taco, self.salad, self.burger],
        )
        self.assertEqual(self.menu.filterByCategory("entree"), [])

    def test_filter_by_price_range_includes_endpoints(self):
        self.assertEqual(
            self.menu.filterByPriceRange(2.0, 6.0),
            [self.taco, self.salad, self.tea],
        )

    def test_filter_by_price_range_with_no_matches(self):
        self.assertEqual(self.menu.filterByPriceRange(10.0, 12.0), [])

    def test_sort_by_price_ascending_and_descending(self):
        self.assertEqual(
            self.menu.sortByPrice(),
            [self.tea, self.taco, self.salad, self.burger],
        )
        self.assertEqual(
            self.menu.sortByPrice(descending=True),
            [self.burger, self.salad, self.taco, self.tea],
        )

    def test_sort_by_popularity_default_and_ascending(self):
        self.assertEqual(
            self.menu.sortByPopularity(),
            [self.burger, self.taco, self.salad, self.tea],
        )
        self.assertEqual(
            self.menu.sortByPopularity(descending=False),
            [self.salad, self.tea, self.taco, self.burger],
        )

    def test_sort_by_name_ignores_case(self):
        self.assertEqual(
            self.menu.sortByName(),
            [self.burger, self.salad, self.taco, self.tea],
        )

    def test_sorting_does_not_reorder_menu_items(self):
        original_items = self.menu.items.copy()
        self.menu.sortByPrice()
        self.menu.sortByPopularity()
        self.menu.sortByName()
        self.assertEqual(self.menu.items, original_items)


if __name__ == "__main__":
    unittest.main()
