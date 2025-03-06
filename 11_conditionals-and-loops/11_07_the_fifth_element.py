# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

for num in range(1, 1001):
    if num % 5 == 0:
        print(num)