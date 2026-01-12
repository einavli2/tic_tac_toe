def process_invoice_price(price):
    tax_rate = 0.17
    total_with_tax = price * (1 + tax_rate)
    rounded_price = round(total_with_tax, 2)
    return f"Total: {rounded_price}$"

raw_prices = [100.5, 20.0, 55.75, 200.0]
map_result = list(map(process_invoice_price, raw_prices))
print("Map Result (List):", map_result)


def is_special_number(n):
    is_even = n % 2 == 0
    is_greater_than_50 = n > 50
    is_divisible_by_5 = n % 5 == 0
    return is_even and is_greater_than_50 and is_divisible_by_5

numbers_list = [10, 60, 45, 100, 50, 80, 22]
filter_result = tuple(filter(is_special_number, numbers_list))
print("Filter Result (Tuple):", filter_result)

from functools import reduce
def aggregate_sales(accumulator, transaction):
    category = transaction['category']
    amount = transaction['amount']
    # Check if category exists, then add amount
    accumulator[category] = accumulator.get(category, 0) + amount
    return accumulator

sales_data = [
    {'category': 'Electronics', 'amount': 1000},
    {'category': 'Food', 'amount': 50},
    {'category': 'Electronics', 'amount': 500},
    {'category': 'Food', 'amount': 150}
]
reduce_result = reduce(aggregate_sales, sales_data, {})
print("Reduce Result (Dictionary):", reduce_result)
