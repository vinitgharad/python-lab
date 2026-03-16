name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
dept = input("Enter department: ")
basic = float(input("Enter basic salary: "))

DA = 0.92 * basic
HRA = 0.58 * basic
TA = 0.30 * basic
LIC = 500

salary = basic + DA + HRA + TA - LIC

print("Employee Name:", name)
print("Employee ID:", emp_id)
print("Department:", dept)
print("Total Salary:", salary)