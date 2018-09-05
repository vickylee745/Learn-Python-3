def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    if cheese_count > 19 and boxes_of_crackers > 20:
        # put a if condition: if many cheese and many crackers, print the following
        # If not enough cheese and crackers, skip printing the following:
        print("Man that's enough for a party!")
        print("Get a blanket.\n")


print("\nWe can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("\nWe can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("\nAnd we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# write a guessing game

def guess_number(num):
    print("Les't play a guessing game!\n")
    if num == 2:
        print("You Win\n")
    else:
        print('You Lose\n')

guess_number(1)
my_guess = 5
guess_number(my_guess)
guess_number(my_guess-3)
