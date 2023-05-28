
#Similarly for decimal numbers we can use float() to convert the strings to numbers

x = float(input("Whats the value of x? "))
y = float(input("Whats the value of y? "))

#by default all inputs are strings thats why we need to convert it into integer by using float() function

z = x + y

z = round(z)

# we can also use the round() function to round a particular number to the nearest int

print(z)

# if we need to format the output then we can use the other printing way as follows

print(f"{z:,}") #by putting this format print(f"{z:,}") we have got the output as 10,000 not 10000 as earlier


    