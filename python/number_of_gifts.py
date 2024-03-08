# ----------------------- TASK -------------------------------
#   Leo's girlfriend asked him to buy a gift list during his next trip, now he wants to know how many of them will he be able to buy.

#   Write a function to help Leo out. The first parameter of the function is Leo's budget; 
#   the second one is an array containing the price of each gift. You should return an integer representing the maximum amount of gifts Leo can buy.

#   EXAMPLE:
#     Maximum budget: 20
#     Gift List: [13, 2, 4, 6, 1]
#     Should return 4.


# --------------------- APPROACH ----------------------------
#   1. Create a function called howManyGifts that takes 2 parameters, the first paramter is the maxBudget, and the second one is the gifts
#   2. Declare 2 variables that contain the sum of the gifts (sumOfAllGifts) and the gifts to buy (giftsToBuy). The sumOfAllGifts is a number and the giftsToBuy is an array
#   3. Loop throuhg the gifts and calculate the sum of all the gifts
#   4. Compare if sumOfAllGifts is less or equal to the maxBuget, if so, push the gifts to the giftsToBuy, otherwise do nothing
#   5. Return the length of the giftsToBuy


# --------------------- SOLUTION ------------------------------

def how_many_gifts(max_budget, gifts):
    gifts.sort()
    gifts_to_buy = []
    sum_of_gifts = 0
    
    for gift in gifts:
        if sum_of_gifts + gift <= max_budget:
            sum_of_gifts += gift
            gifts_to_buy.append(gift)
    
    return len(gifts_to_buy)

# Example usage:
max_budget = 50
gifts = [20, 30, 10, 5, 15]
print(how_many_gifts(max_budget, gifts))  # Output: 3
