# ```python
# #print("Hello deepak deva")

# # name  = "Deepak dude poi"
# # print("the name is :" +name)
# # print(f"the name is {name} welcome")



# # print("Deepak\n\t"*100)
# # numb = 1
# # numb2 = 5.66
# # name = 'Deepak deva'
# # is_published = True
# # print(numb,numb2,name,is_published)
# # print(numb + numb2 , name , is_published)
# #
# # name = input("what is your name: ")
# # print("my name is :"+ name)

# # colour =  input("what is your favourite colour ? ")
# # number = int(input("what is you fav number ? "))
# # name  = input("what is your name ? ")
# # percentage = input("what is the percentage of you attendance ? ")
# #
# # print(name + " fav colour is" + colour + " fav number is" , number , " percentage is " , percentage)


# # birth_year = int(input("enter the year you born"))
# # age  = 2025 - birth_year
# # print("the age is ", age)

# # numb = 9
# #
# # print("the  numb is " + numb)


# # name = "raju"

# # print("the  numb is " + name)

# # lbs = int(input("enter the weight in lbs "))
# # kg  = lbs *0.45
# # print("the weight in kgs ",kg)

# # name  = 'hi this is Deepak "nani" dude'
# # # print(name)
# # print(name[5])
# # print(name[0:28])
# # print(name[:5])
# # print(name[5:])

# # print("*\t$\t#\t%"*1600)

# # Diamond pattern in Python

# # n = 7  # Height of the diamond (should be odd for symmetry)
# #
# # for i in range(n):
# #     if i <= n // 2:
# #         print(" " * (n // 2 - i) + "* " * (i + 1))
# #     else:
# #         print(" " * (i - n // 2) + "* " * (n - i))

# # Prime number program in Python

# # num = int(input("Enter a number to check if it is prime: "))

# # if num > 1:
# #     for i in range(2, int(num ** 0.5) + 1):
# #         if (num % i) == 0:
# #             print(num, "is not a prime number")
# #             break
# #     else:
# #         print(num, "is a prime number")
# # else:
# #     print(num, "is not a prime number")

# # # Print all prime numbers up to a limit
# # limit = int(input("Enter the limit to print all prime numbers up to: "))
# # print("Prime numbers up to", limit, "are:")
# # for n in range(2, limit + 1):
# #     for i in range(2, int(n ** 0.5) + 1):
# #         if n % i == 0:
# #             break
# #     else:
# #         print(n, end=" ")
# # print()
# #
# # # Print all even numbers up to a limit
# # even_limit = int(input("Enter the limit to print all even numbers up to: "))
# # print("Even numbers up to", even_limit, "are:")
# # for n in range(2, even_limit + 1, 2):
# #     print(n, end=" ")
# # print()
# #
# # # Print a star pyramid pattern
# # rows = int(input("Enter the number of rows for the star pattern: "))
# # for i in range(1, rows + 1):
# #     print(" " * (rows - i) + "* " * i)

# // Singleton pattern in C++
# #include <iostream>
# using namespace std;

# class Singleton {
# private:
#     static Singleton* instance;
#     // Private constructor to prevent instancing
#     Singleton() {
#         cout << "Singleton instance created." << endl;
#     }
# public:
#     static Singleton* getInstance() {
#         if (instance == nullptr) {
#             instance = new Singleton();
#         }
#         return instance;
#     }
#     void showMessage() {
#         cout << "Hello from Singleton!" << endl;
#     }
# };

# // Initialize pointer to zero so that it can be initialized in first call to getInstance
# Singleton* Singleton::instance = nullptr;

# int main() {
#     Singleton* s1 = Singleton::getInstance();
#     s1->showMessage();

#     // Try to get another instance
#     Singleton* s2 = Singleton::getInstance();
#     if (s1 == s2) {
#         cout << "Both are the same instance." << endl;
#     }
#     return 0;
# }

# #include <iostream>

# Check if a number is prime


# Print all prime numbers up to a limit
limit = int(input("Enter the limit to print all prime numbers up to: "))
print("Prime numbers up to", limit, "are:")
for n in range(2, limit + 1):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
print()

import numpy as np

#
# # Print all even numbers up to a limit
# even_limit = int(input("Enter the limit to print all even numbers up to: "))
# print("Even numbers up to", even_limit, "are:")
# for n in range(2, even_limit + 1, 2):
#     print(n, end=" ")
# print()
#
# # Print a star pyramid pattern
# rows = int(input("Enter the number of rows for the star pattern: "))
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "* " * i)

# // Singleton pattern in C++
# #include <iostream>
# using namespace std;

# class Singleton {
# private:
#     static Singleton* instance;
#     // Private constructor to prevent instancing
#     Singleton() {
#         cout << "Singleton instance created." << endl;
#     }
# public:
#     static Singleton* getInstance() {
#         if (instance == nullptr) {
#             instance = new Singleton();
#         }
#         return instance;
#     }
#     void showMessage() {
#         cout << "Hello from Singleton!" << endl;
#     }
# };

# // Initialize pointer to zero so that it can be initialized in first call to getInstance
# Singleton* Singleton::instance = nullptr;

# int main() {
#     Singleton* s1 = Singleton::getInstance();
#     s1->showMessage();

#     // Try to get another instance
#     Singleton* s2 = Singleton::getInstance();
#     if (s1 == s2) {
#         cout << "Both are the same instance." << endl;
#     }
#     return 0;
# }

# #include <iostream>
