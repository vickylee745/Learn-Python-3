'''
# people = str("20")
# default is stored as number:
people = 20
cats = 30
dogs = 15
# what = (people == 20)
# print(what)

if people < cats:
    print ("Too many cats! The world is doomed!")
# can use else instead of if People >= cats:
else:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")
else:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are equal to dogs.")


# 2nd part of exercise

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
'''

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
