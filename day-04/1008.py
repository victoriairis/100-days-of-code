#salario

number, wrkd_hrs, pay_hr = input().split()

number = int(number)
wrkd_hrs = int(wrkd_hrs)
pay_hr = float(pay_hr)

print("number ="+str(number))
print("salary ="+str(float(wrkd_hrs * pay_hr)))