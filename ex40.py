# build a dictionary - mystuff
# mystuff = {'apple': "I AM APPLES!"}
# print(mystuff['apple'])
# first exercise
'''
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
thing = MyStuff()
thing.apple()
print(thing.tangerine)
'''


class Song(object):

    def __init__(self, lyrics):
         self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
           print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
print("I'm trying to print: \"print(happy_bday.lyrics)\"")
print(happy_bday.lyrics)
# pass the lyrics to a variable
separate_variable = happy_bday.lyrics
# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

separate_variable2 = Song(separate_variable)
separate_variable2.sing_me_a_song()
