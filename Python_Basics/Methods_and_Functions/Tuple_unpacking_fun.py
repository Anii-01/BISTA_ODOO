

stock_prices = [('abc',200),('def',300),('ghe',400)]   #packed tuple

for items in stock_prices:
    print(items)

for a,b in stock_prices:     #unpacking tuple
    print(a)

for a,b in stock_prices:
    print(b*10)



work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for name,hour in work_hours:
        if hour > current_max : 
            current_max = hour
            employee_of_month = name
        else:
            pass

    return (employee_of_month,current_max)

result = employee_check(work_hours)
print("The employee of month is: ", result)


name,hours = employee_check(work_hours)
print(name)
print(hours)

