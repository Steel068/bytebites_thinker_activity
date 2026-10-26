Client Feature Request
We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

Candidate Class:
1. Customer
2. Food Product
3. Menu
4. Order
```mermaid
classDiagram
	class Customer {
		+String name
		+List~Order~ purchaseHistory
	}
	class FoodProduct {
		+String name
		+Decimal price
		+String category
		+float popularityRating
	}
	class Menu {
		+List~FoodProduct~ items
		+filterByCategory(category) List~FoodProduct~
	}
	class Order {
		+List~FoodProduct~ items
		+Decimal totalCost
		+calculateTotal() Decimal
	}

	Customer "1" --> "0..*" Order : purchase history
	Menu "1" o-- "0..*" FoodProduct : contains
	Order "1" --> "1..*" FoodProduct : selects
```