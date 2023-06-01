#Maxine Silverman 
#Food-O-Matic 


import random
firsts = ["local", "roasted", "grilled", "garlic mashed", "oven dried", "spiced", "stewed", "assorted", "iced", "sliced", "braised", "free-range", "baby", "teriyaki glazed", "steamed"]
seconds = ["cauliflower", "tilapia fillet", "pork loin", "green beans", "basmati rice", "rainbow carrots", "fingerling potatoes", "three color squash", "potatoes", "eggplant", "drumstick", "short rib", "duck breast", "eye round of beef", "baguette"]
thirds = ["with fennel", "gratin", "bengali style", "with peas", "pizza", "with balsamico", "with garlic and olive oil", "with pigeon peas", "with minted yogurt", "soup, chutney", "salad", "with tropical fruit salsa", "over sticky rice", "au jus"]

first_price = [5, 3, 3, 2, 3, 4, 5, 4, 3, 2, 2, 2, 3, 4, 5 ]
second_price = [5, 3, 8, 5, 4, 4, 6, 5, 5, 8, 8, 9, 9, 8, 7 ]
third_price = [2, 3, 2, 2, 4, 2, 2, 3, 2, 3, 4, 3, 4, 2, 3]

while True:
    items = input("How many items would you like? Enter stop to end. ")
    used = []

    if items.lower() == "stop":
        break
    elif items.isnumeric():
        if int(items) <= len(firsts):
            for item in range(int(items)):
                while True:
                    first = random.choice(firsts)
                    second = random.choice(seconds)
                    third = random.choice(thirds)
                    meal = f"{first} {second} {third}"
                
                    if meal not in used: 
                        print(f"Item {item+1} is: {meal}. Your cost for this item is ${first_price[firsts.index(first)] + second_price[seconds.index(second)] + third_price[thirds.index(third)]}")
                        used.append(meal)
                        break
        else:
            print(f"Please enter a number less than {len(firsts)}")
    else:
        print("Please enter a valid number!")



