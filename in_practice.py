def WAF(text):
    vowel = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowel:
            count += 1

    print(f"Number of vowels: {count}")
    
char = input("Write anything to check how many vowels are there: ")

WAF(char)


# num = int(input("Enter a number to check if it's even or odd: "))

# def WAF(num):
#     if num % 2 == 0:
#         print("The number is even!")
#     else:
#         print("The number is odd!")

# WAF(num)

# def calc_ft(sending_money): #parameter
#     after_tax = sending_money + (sending_money * 0.15)
#     print(after_tax)

# calc_ft(100) #argument


# st_roll = {101, 105, 102, 101, 108, 105, 110}
# print("The student roll numbers are: ", st_roll)

# em_records = [(101, "Alice", 50000), (102, "Bob", 65000), (103, "Charlie", 45000)]

# em_id = int(input("Enter your Employee ID: "))

# found = False
# for record in em_records:
#     if record[0] == em_id:
#         print(f"Here's the details: Employee ID: {record[0]}, Name: {record[1]}, Salary: {record[2]}")
#         found = True
#         break
# if not found:
#     print("Invalid Employee ID")



#List
# marks = (89,90,52,75,55)
# print(marks, len(marks))

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))

# for i in range(1, 1001):
#     if a % i == 0 and b % i == 0:
#         print(i)


# for i in range(1, 51):
#     if i == 15:
#         continue
#     if i % 3 == 0:
#         print(i)

# for i in range(1, 11):
#     print("57 * ",i, "=", 57 * i)


# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# for i in range(2, 11, 2):
#     print(i)




# i = 1
# while i <= 5:
#     print(i * "*")
#     i +=1


#name = "Bruce Wayne"

# #find
# print(name.find("yne")) # 0 index => position

#replace
# print(name.replace("Bruce Wayne", "Batman"))
# print(name.replace("Wayne", "man"))
# print(name.replace("yne", "ice"))

#check for updates
# print("W" in name) #True
# print("w" in name) #False

# pr1 = int(input("Bill-1: "))
# pr2 = int(input("Bill-2: "))
# pr3 = int(input("Bill-3: "))

# sum = pr1 + pr2 + pr3

# print("Total bill: ", sum)

# superName = input("Enter a Super Hero Name: ")

# print("S" in superName)
# print("s" in superName)

# marks = int(input ("Enter your marks: "))

# if marks >=80:
#     print('A')
# elif marks < 80 and marks >= 60:
#     print ('B')
# else: 
#     print('C')