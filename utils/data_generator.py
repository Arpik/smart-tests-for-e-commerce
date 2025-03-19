from faker import Faker
from .log_config import logger
import requests
import openai


class TestDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_ai_user(self):
        """Generate user data with AI, fallback to Faker if AI fails."""
        try:
            logger.info("Requesting AI-generated user data...")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt="Generate realistic user data in JSON format.",
                max_tokens=100
            )
            ai_data = response.choices[0].text.strip()
            logger.info("AI-generated user data received successfully.")
            return eval(ai_data)  # Convert JSON string to dictionary
        
        except Exception as e:
            logger.warning(f"AI data generation failed: {e}. Falling back to Faker.")
            return {

                "user_name": self.fake.user_name(),
                "first_name": self.fake.first_name(),
                "last_name": self.fake.last_name(),
                "email": self.fake.email(),
                "password": self.fake.password(length=12),
                "phone_number": self.fake.phone_number(),
                "address1": self.fake.address(),
                "address2": self.fake.secondary_address(),
                "zipcode": self.fake.zipcode(),
                "state": self.fake.state(),
                "phonenumber": self.fake.phone_number(),
                "city": self.fake.city(),
                "company":self.fake.company()
            }

    def generate_product(self):
        """Generate fake product data for e-commerce testing."""
        return {
            "product_name": self.fake.word().capitalize() + " " + self.fake.word().capitalize(),
            "price": round(self.fake.random_number(digits=2), 2),
            "category": self.fake.random_element(elements=["Electronics", "Clothing", "Home", "Beauty", "Sports"]),
            "stock": self.fake.random_int(min=1, max=100),
        }

