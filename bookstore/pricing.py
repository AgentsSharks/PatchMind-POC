class PricingService:
    STUDENT_DISCOUNT = 0.10

    def calculate_total(self, price: float, quantity: int, is_student: bool) -> float:
        total = price * quantity
        return total