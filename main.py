import datetime as dt
from decimal import Decimal

goods = {
    "Хлеб": [
        {"amount": Decimal("1"), "expiration_date": None},
        {"amount": Decimal("1"), "expiration_date": dt.date(2024, 5, 25)},
    ],
    "Яйца": [
        {"amount": Decimal("2"), "expiration_date": dt.date(2024, 5, 28)},
        {"amount": Decimal("3"), "expiration_date": dt.date(2024, 5, 27)},
    ],
    "Вода": [{"amount": Decimal("100"), "expiration_date": None}],
}


def expire(items, in_advance_days=0):
    today = dt.date.today()
    expired_products = []

    for product, quantities in items.items():
        total_amount = sum(
            q["amount"] for q in quantities if q["expiration_date"] is not None
        )
        for quantity in quantities:
            if quantity["expiration_date"] is not None and (
                (quantity["expiration_date"] <= today and in_advance_days == 0)
                or (
                    quantity["expiration_date"]
                    <= today + dt.timedelta(days=in_advance_days)
                )
            ):
                expired_products.append((product, total_amount))
                break

    return expired_products


print(expire(goods))
# Вывод: [('Хлеб', Decimal('1'))]
print(expire(goods, 1))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
print(expire(goods, 2))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))]
