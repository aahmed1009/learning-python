# question1
# bill = 47.28
# tip = bill * 0.15
# total = bill + tip
# share = total / 2
# print("Each person needs to pay=",share)

#----------------------------------------------------
# question2 Ask the user for two numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# result = num1 / num2
# print("The result is=", result)
#----------------------------------------------------
# question3
# word1 = "How"
# word2 = "do"
# word3 = "you"
# word4 = "like"
# word5 = "}{"
# word6 = "so"
# word7 = "far?"
# print(word1, word2, word3, word4, word5, word6, word7)
#----------------------------------------------------
# question4
# word1 = "How"
# word2 = "do"
# word3 = "you"
# word4 = "like"
# word5 = "}{"
# word6 = "so"
# word7 = "far?"
# word7 = word7.replace("?", "!")

# print(word1, word2, word3, word4, word5, word6, word7)

#----------------------------------------------------
# question5
# statement = input("Enter a statement: ")
# length = len(statement)
# print("The length of your statement is:", length)
#----------------------------------------------------
# question6
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose operation:")
print("+  Add")
print("-  Subtract")
print("* Multiply")
print("/  Divide")
choice = input("Enter choice (+, -, *, /): ")
if choice == "+":
    print("Result:", num1 + num2)
elif choice == "-":
    print("Result:", num1 - num2)
elif choice == "*":
    print("Result:", num1 * num2)
elif choice == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid choice")
