
#we can also do it altogether
name = input("Who is Joss?\n").title().strip()
#title() capitalizes first word of every letter

#strip is used to remove whitespaces
name = name.strip()

#capitalize only capitalizes the first letter of a single word
name = name.capitalize()

#split users name into multiple chunks
first , last = name.split(" ") #we can user multuple varible names to asign multiple values

print (name,"is Joss")
print ("His last name is",last)