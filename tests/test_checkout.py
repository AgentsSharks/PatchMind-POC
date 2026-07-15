from bookstore.checkout import CheckoutService


checkout = CheckoutService()


def test_checkout():
    assert checkout.checkout(50, 2, False) == 100