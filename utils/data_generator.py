from faker import Faker


class TestDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_user(self):
        """Generate a fake user with realistic attributes."""
        return {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
            "password": self.fake.password(length=12),
            "phone_number": self.fake.phone_number(),
            "address": self.fake.address(),
        }

    def generate_product(self):
        """Generate fake product data for e-commerce testing."""
        return {
            "product_name": self.fake.word().capitalize() + " " + self.fake.word().capitalize(),
            "price": round(self.fake.random_number(digits=2), 2),
            "category": self.fake.random_element(elements=["Electronics", "Clothing", "Home", "Beauty", "Sports"]),
            "stock": self.fake.random_int(min=1, max=100),
        }
