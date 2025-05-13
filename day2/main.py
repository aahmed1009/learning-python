#----------------------------------------------------
# question1 
# def char():
#     x = input("Enter the string: ")
#     letter = input("Enter the letter to search on it: ")
#     positions=[]
#     for i in range(len(x)):
#       if x[i]==letter:
#         positions.append(i)
#       else:
#         continue
#     print(positions)
# char()    
#----------------------------------------------------
# question2
# def multiplication_table():
#   number=int(input("enter the number: "))
#   table=[]
#   for i in range(1,number+1):
#     row=[]
#     for j in range(1,i+1):
#       row.append(i*j)
#     table.append(row)
#     print(row)

# multiplication_table()      
    
      
    
  


#----------------------------------------------------
# question3    
# names=[]
# while True:
#   name=input("Enter the names & Enter stop to finish: ")
#   if name=='stop':
#     break
#   names.append(name)
# result = {}
# for name in names:
#   first=name[0].lower()
#   if first in result:
#     result[first].append(name)
#   else:
#     result[first]=[name]
# print(result)  
#lab 3 calculator
def area():
    shape = input("Enter shape (t for triangle, r for rectangle, s for square, c for circle): ")
    if shape == "t":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of triangle is", area)
    elif shape == "r":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        area = width * height
        print("Area of rectangle is", area)
    elif shape == "s":
        side = float(input("Enter side: "))
        area = side * side
        print("Area of square is", area)
    elif shape == "c":
        radius = float(input("Enter radius: "))
        pi = 3.14
        area = pi * radius * radius
        print("Area of circle is", area)
    else:
        print("Invalid shape")
area()

  