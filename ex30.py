
people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


''' or above decision process can be written:'''
def what_to_take(people, cars, trucks):
    if trucks >= people and trucks < cars:
        print ("Alright take trucks")
    elif trucks < people and cars >= people:
        print ("not enough trucks, take cars")
    else:
        print ("Can't fit everyone")
people = input("number of people: ")
cars = input("number of cars: ")
trucks = input("number of trucks: ")
what_to_take(people, cars, trucks)
