#way 1
def hello():
      print("Hello!")


name = input("What's your name? ")
hello()
print(name)

#way 2
def hello():
      print("Hello!",name)


name = input("What's your name? ")
hello()



# way 3


def hello(to):
      print("Hello!",to)


name = input("What's your name? ")
hello(name)

#we can also set default values if the user doesn't give any input such as


def hello(to = "World"):
      print("Hello!",name)


name = input("What's your name? ")
hello()
# print(name)




