# Write a program to find if a year is leap year or not.

n = int(input("Enter the year : "))

if(n%400==0):
    print(f"{n} is a leap year")
elif(n%4==0 and n%100!=0):
    print(f"{n} is a leap year")
else:
    print(f"{n} is not a leap year")