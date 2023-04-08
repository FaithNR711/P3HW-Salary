#CTI-110
#P3HW2- Salary
#Faith Rivera
#04/20/2023
#

# Ask the user to enter name of employee
name = input("Enter employee's name: ")

# Ask user to enter number of hours the employee worked this week
hours_worked = float(input("Enter number of hours worked: "))

# Ask user to enter employee's pay rate
pay_rate = float(input("Enter employee's pay rate: "))

# Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
if hours_worked > 40:
  overtime_hours = hours_worked - 40
  overtime_pay = overtime_hours * pay_rate * 1.5
else:
  overtime_hours = 0
  overtime_pay = 0

# Calculate amount employee should be paid for regular hours worked.
reg_hours_pay = (hours_worked - overtime_hours) * pay_rate

# Calculate Gross pay (total amount that should be paid to employee)
gross_pay = reg_hours_pay + overtime_pay

# Display employee's name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay
print("---------------------------------------------")
print("Employee's name:", name)
print("")
print("Hours Worked\tPay Rate\tOvertime\tOvertime Pay\tRegHour Pay\tGross Pay")
print("---------------------------------------------------------------------------------------------------------------------")
print("{:<14}\t${:<14}\t{:<9}\t${:<16.2f}\t${:<14.2f}\t${:<14.2f}".format(hours_worked, pay_rate, overtime_hours, overtime_pay, reg_hours_pay, gross_pay))
