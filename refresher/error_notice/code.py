# def devide(divided, divisor):
#     if divisor == 0:
#         print('Divisor cannot be zero (0.0)')
#         return 
#     return divided / divisor

def devide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be zero (0.0)')
    return divided / divisor

# grades = [77, 3, 12, 42] 
grades = []

print('Welcome to the average grade program') 
try:
    average = devide(sum(grades),len(grades))
    print(f'The average grade is {average}')
except ZeroDivisionError:
    print('There are no grades yet in your list')

# try:
    # average = devide(sum(grades),len(grades))

# except ZeroDivisionError as e:
    # print(e)
    # print('There are no grades yet in your list')

# else:
    # print(f'The average grade is {average}')
# finally:
#     print('Thanks!')


