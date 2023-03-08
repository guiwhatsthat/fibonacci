import matplotlib.pyplot as plt

def fibonacci(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(b)
        temp = a + b
        a = b
        b = temp
    return result

fibonacci_sequence = fibonacci(20)

plt.plot(fibonacci_sequence)
plt.title('Fibonacci-Folge')
plt.xlabel('n')
plt.xticks(range(0, 21, 1))
plt.ylabel('Fibonacci(n)')
plt.show()