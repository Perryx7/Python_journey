class Car:
    def __init__(self, brand, model, available=True):
        self.brand = brand
        self.model = model
        self.available = available

    def rent(self):
        """Rent the car if available."""
        if self.available:
            self.available = False
            print(f"{self.brand} {self.model} has been rented ✅")
        else:
            print(f"{self.brand} {self.model} is not available ❌")

    def return_car(self):
        """Return the car and make it available again."""
        if not self.available:
            self.available = True
            print(f"{self.brand} {self.model} has been returned and is now available 🔄")
        else:
            print(f"{self.brand} {self.model} was already available")

    def get_info(self):
        """Display information about the car."""
        status = "Available" if self.available else "Rented"
        print(f"Car: {self.brand} {self.model} | Status: {status}")


# Create cars
cars = [
    Car("Toyota", "Corolla"),
    Car("Mercedes", "Class A"),
    Car("Ferrari", "488", available=False),
    Car("Porsche", "911"),
    Car("Lexus", "RX", available=False)
]

# Simulation
for c in cars:
    print(f"\nBefore rental: {c.brand} {c.model} | Available: {c.available}")
    c.rent()
    print(f"After rental: {c.brand} {c.model} | Available: {c.available}")
    c.get_info()
