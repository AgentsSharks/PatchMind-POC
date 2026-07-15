from bookstore.pricing import PricingService


class CheckoutService:
    def __init__(self):
        self.pricing = PricingService()

    def checkout(self, price: float, quantity: int, is_student: bool):
        return self.pricing.calculate_total(price, quantity, is_student)