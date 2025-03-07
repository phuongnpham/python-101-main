# Print out every prime number between 1 and 1000.
for num in range(1, 1001):
    if num < 2:
        continue
    
    prime = True

    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")