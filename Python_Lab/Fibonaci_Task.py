n = 7
fibonacci = [0,1]

for i in range(0, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(fibonacci[i], end=" ")

else:
    print("\nFibonacci sequence up to", n, "terms:", fibonacci)