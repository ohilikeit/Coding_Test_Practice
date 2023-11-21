from itertools import product

def calculate_sales(users, emoticons, discounts):
    # Initialize the count of subscribers and total sales
    subscribers = 0
    total_sales = 0

    # Go through each user
    for user in users:
        # Set the initial expense for the user to 0
        user_expense = 0
        # Go through each emoticon and calculate the expense for the current discount set
        for price, discount in zip(emoticons, discounts):
            discounted_price = price * (1 - discount / 100)
            # If the discount meets the user's requirement, add to their expense
            if discount >= user[0]:
                user_expense += discounted_price

        # If the user's expense exceeds their limit, they subscribe
        if user_expense >= user[1]:
            subscribers += 1
        else:
            total_sales += user_expense

    return subscribers, total_sales

def solution(users, emoticons):
    # Define the possible discounts
    possible_discounts = [10, 20, 30, 40]
    # This will hold the maximum number of subscribers and the corresponding sales
    max_subscribers = 0
    max_sales = 0

    # Generate all possible combinations of discounts for the emoticons
    for discounts in product(possible_discounts, repeat=len(emoticons)):
        # Calculate the sales and subscribers for the current discount set
        subscribers, sales = calculate_sales(users, emoticons, discounts)

        # If we have more subscribers than before, or equal subscribers but more sales, update the max values
        if subscribers > max_subscribers or (subscribers == max_subscribers and sales > max_sales):
            max_subscribers = subscribers
            max_sales = sales

    return [max_subscribers, max_sales]
