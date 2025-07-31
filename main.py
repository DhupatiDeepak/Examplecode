#print("Hello deepak deva")

# name  = "Deepak dude poi"
# print("the name is :" +name)
# print(f"the name is {name} welcome")



# print("Deepak\n\t"*100)
# numb = 1
# numb2 = 5.66
# name = 'Deepak deva'
# is_published = True
# print(numb,numb2,name,is_published)
# print(numb + numb2 , name , is_published)
#
# name = input("what is your name: ")
# print("my name is :"+ name)

# colour =  input("what is your favourite colour ? ")
# number = int(input("what is you fav number ? "))
# name  = input("what is your name ? ")
# percentage = input("what is the percentage of you attendance ? ")
#
# print(name + " fav colour is" + colour + " fav number is" , number , " percentage is " , percentage)


# birth_year = int(input("enter the year you born"))
# age  = 2025 - birth_year
# print("the age is ", age)

# numb = 9
#
# print("the  numb is " + numb)


# name = "raju"

# print("the  numb is " + name)

# lbs = int(input("enter the weight in lbs "))
# kg  = lbs *0.45
# print("the weight in kgs ",kg)

# name  = 'hi this is Deepak "nani" dude'
# # print(name)
# print(name[5])
# print(name[0:28])
# print(name[:5])
# print(name[5:])

# print("*\t$\t#\t%"*1600)

# Diamond pattern in Python

n = 7  # Height of the diamond (should be odd for symmetry)

for i in range(n):
    if i <= n // 2:
        print(" " * (n // 2 - i) + "* " * (i + 1))
    else:
        print(" " * (i - n // 2) + "* " * (n - i))
