# Sample dataset: List of dictionaries representing sales records
sales_data = [
    {"id": 1, "product": "Laptop", "region": "North", "amount": 1200},
    {"id": 2, "product": "Mouse", "region": "South", "amount": 25},
    {"id": 3, "product": "Keyboard", "region": "North", "amount": 75},
    {"id": 4, "product": "Laptop", "region": "East", "amount": 1300},
    {"id": 5, "product": "Mouse", "region": "North", "amount": 20},
    {"id": 6, "product": "Monitor", "region": "West", "amount": 300},
    {"id": 7, "product": "Laptop", "region": "South", "amount": 1150},
    {"id": 8, "product": "Keyboard", "region": "West", "amount": 80},
    {"id": 9, "product": "Monitor", "region": "North", "amount": 320},
    {"id": 10, "product": "Mouse", "region": "East", "amount": 30}
]

def group_sales_data(data, key_field):
    """
    Groups sales data by a specific field (e.g., 'region' or 'product').
    Returns a dictionary where keys are the group names and values are lists of records.
    """
    grouped_data = {}
    for record in data:
        key = record.get(key_field)
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(record)
    return grouped_data

def print_grouped_stats(grouped_data):
    """
    Prints the total sales amount for each group.
    """
    for group_name, records in grouped_data.items():
        total_sales = sum(r['amount'] for r in records)
        count = len(records)
        print(f"{group_name}: ${total_sales} (Count: {count})")

# 1. Group by Region
print("--- Sales by Region ---")
sales_by_region = group_sales_data(sales_data, "region")
print_grouped_stats(sales_by_region)

# 2. Group by Product
print("\n--- Sales by Product ---")
sales_by_product = group_sales_data(sales_data, "product")
print_grouped_stats(sales_by_product)
