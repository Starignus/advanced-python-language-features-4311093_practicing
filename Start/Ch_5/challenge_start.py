# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
#   dryclean is a boolean - If Tru add 5.00 
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

test_order_2 = [[
    ["shirt", "L", True, False],
    ["pants", "M", False, True],
    ["dress", "M", False, True],
    ["cover", True, "L"],
    ["whites", 5.25],
    ["darks", 12.5],
    ["pants", "S", False, False],
    ["jacket", "L", False, True],
    ["shirts and jeans", 28.0],
    ["comforter", False, "L"],
    ["shirt", "L", True, True]
]]

# TODO: process each order
def calc_order_price(order_contents):
    # set the initial variables for the totals
    total_price = 0.0

    # Your code to calculate the total price goes here
    for item in order_contents:
        print(f"Processing item: {item}")
        match item:
            # Dry Clean case with pattern matching and guards
            # Instructor code: case "shirt" | "pants" | "jacket" | "dress" as garment, size, starch, same_day:
            case [garment, size, starch, same_day] if garment in ["shirt", "pants", "jacket", "dress"]:
                price = 12.95
                if starch:
                    price +=2.00
                if same_day:
                    price += 10.00
                total_price += price 
            # Wash and Fold case with pattern matching and guards
            # Instructor code: Make sure it is a strng so --> 
            # case str() as desc, weigth:
            case [description, weight] if isinstance(weight, (int, float)) and isinstance(description, str):
                if weight > 15:
                    total_price += weight * 4.95 * 0.9
                else:
                    total_price += weight * 4.95
            # Blankets case with pattern matching and guards
            # Instructor code: case "comforter" | "cover" as type, dryclean, size:
            case [type, dryclean, size] if type in ["comforter", "cover"]:
                total_price += 25.00
                if dryclean:
                    total_price += 5.00
            case _:
                print(f"invalid item: {item}")

    # then return the result rounded to 2 places
    return round(total_price,2)

# for order in test_orders:
#     print(f"Order 1: {order}")
#     print(f"Order total: ${calc_order_price(order)}")
    
# print() 

for order in test_order_2:
    # print(f"Order 2: {order}")
    print(f"Order total: ${calc_order_price(order)}")