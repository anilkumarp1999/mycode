import datetime
day = int(input("Enter the day :"))
month = int(input("Enter the month :"))
year = int(input("Enter the year :"))
x = datetime.date(year,month,day)

last_digits = year%100

a = last_digits//4
b = a + day

if month == 1:
    k_v = 1
    c = b + k_v
    print(c)
elif month == 2:
    k_v = 4
    c = b + k_v
    print(c)
elif month == 3:
    k_v = 4
    c = b + k_v
    print(c)
elif month == 4:
    k_v = 0
    c = b + k_v
    print(c)
elif month == 5:
    k_v = 2
    c = b + k_v
    print(c)
elif month == 6:
    k_v = 5
    c = b + k_v
    print(c)
elif month == 7:
    k_v = 0
    c = b + k_v
    print(c)
elif month == 8:
    k_v = 3
    c = b + k_v
    print(c)
elif month == 9:
    k_v = 6
    c = b + k_v
    print(c)
elif month == 10:
    k_v = 1
    c = b + k_v
    print(c)
elif month == 11:
    k_v = 4
    c = b + k_v
    print(c)
elif month == 12:
    k_v = 6
    c = b + k_v
    print(c)

if year in range(1700,1799):
    ke_v = 4
    m = c + ke_v
    print(m)
elif year in range(1800,1899):
    ke_v = 2
    m = c + ke_v
    print(m)
elif year in range(1900,1999):
    ke_v = 0
    m = c + ke_v
    print(m)
elif year in range(2000,2099):
    ke_v = 6
    m = c + ke_v
    print(m)



r = (m+last_digits)%7

if r == 0:
    print("Saturday")
elif r == 1:
    print("Sunday")
elif r == 2:
    print("Monday")
elif r == 3:
    print("Tuesday")
elif r == 4:
    print("Wednesday")
elif r == 5:
    print("Thursday")
elif r == 6:
    print("Friday")



print(b)
print(a)
print(last_digits)
print(x)