#Ryan Lugo: RJL 10/22/21

q = int(input("What day is it?: "))
m = int(input("What Month number is it?: "))
j = int(input("What is the century?: "))
k = j % 100

day = "None"

# Couldn't figure out the issue, it would print out 6 not 7
day_formula = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7 + 1

if day_formula == 0:
    day = "Saturday"
elif day_formula ==1:
    day = "Sunday"
elif day_formula == 2:
    day = "Monday"
elif day_formula == 3:
    day = "Tuesday"
elif day_formula == 4:
    day = "Wednesday"
elif day_formula == 5:
    day = "Thursday"
elif day_formula == 6:
    day = "Friday"
else:
    print("Error",day_formula)

print(m,"/",q,"/",j,"was a",day,day_formula)