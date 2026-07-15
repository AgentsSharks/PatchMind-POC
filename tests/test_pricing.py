from bookstore.pricing import PricingService


pricing = PricingService()


def test_normal_customer():
    assert pricing.calculate_total(100, 2, False) == 200


def test_student_discount():
    assert pricing.calculate_total(100, 2, True) == 180