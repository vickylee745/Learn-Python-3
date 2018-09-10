
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
