def calculate_sum(*args):

    sum = 0

    if(len(args) == 0):
        return sum
    else:
        for i in args:
            sum += i
        return sum


num = input("Enter the number ('or done to finish')")

numbers = []

while num != "done":
    numbers.append(int(num))
    num = input("Enter the number ('or done to finish')")


print(calculate_sum(*tuple(numbers)))
