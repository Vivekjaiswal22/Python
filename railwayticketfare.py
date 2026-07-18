print ("=============================== \n   Welcome To Indian Railways      \n===============================")
#print(" ")
print ("  Safe    Secure   Affordable")
print("")
print ("=============================== \n       Journey Details      \n===============================")

n = int(input("Enter number of passengers : "))

names = []
ages = []

for i in range (n) :
    print("Passenger Details")
    name = input("Enter passenger's name : ")
    names.append(name)
    age = int(input("Enter passenger's age : "))
    ages.append(age)

print("\nPassenger Details")

for i in range(n):
    print("Passenger", i + 1, ":", names[i], "(", ages[i], ")")

start = input("From : ")
end = input("To : ")

Class = input("Enter your choice (1st ac, 2nd ac, 3rd ac, sleeper, general) : ").strip().lower()

clas = ["1st ac","2nd ac", "3rd ac", "sleeper","general"]
price = [500,400,300,200,100]

index = clas.index(Class)
amount = price[index]

total_fare = amount * n 
print(total_fare)
print("Your total fare for your journey is :", total_fare)
print("Have a safe and happy journey.")