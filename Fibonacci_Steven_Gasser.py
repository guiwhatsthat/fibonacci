# Berechnen der Fibonacci-Zahlen rekursiv
def fib_recursive(n):
    # Berechnet die n-te Fibonacci-Zahl rekursiv
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_recursive(n-1) + fib_recursive(n-2)
        return result
# fib_recursive mit n=10 aufrufen
for i in range(11):
    print(f"fib_recursive({i}) = {fib_recursive(i)}") 


# Funktion für die Berechnung der Anzahl aufrufe der rekursiven Funktion fib_recursive(n)
def fib_calls(n):
    global counter # Verwendung einer globalen Variable
    counter = 0 # Setzt den Zähler auf 0

    def fib_rec(n):
        global counter # Verwendung einer globalen Variable
        counter += 1 # Erhöht den Zähler um 1 bei jedem Aufruf

        if n <= 1:
            return n
        else:
            return fib_rec(n-1) + fib_rec(n-2)

    fib_rec(n) # Aufruf der rekursiven Funktion
    return counter # Gibt die Anzahl der Aufrufe zurück

# Gibt die Anzahl der Aufrufe der rekursiven Funktion fib(n) zurück
for i in range(11):
    print(f"Anzahl der Aufrufe der rekursiven Funktion fib({i}): {fib_calls(i)}")


# Funktion zur visuellen Darstellung des Zeitaufwandes von Fibonacci-Berechnungen in einer Rekursion 
import matplotlib.pyplot as plt

def plot_results(results):
    n_values = [result[0] for result in results]
    times = [result[1] for result in results]
    
    plt.plot(n_values, times)
    plt.title("Zeit vs. n in Fibonacci-Berechnungen")
    plt.xlabel("n")
    plt.ylabel("Zeit (in Sekunden)")
    plt.show()

results = [
    (30, 2.108395),
    (31, 3.377656),
    (32, 5.490332),
    (33, 8.829561),
    (34, 14.552251),
    (35, 23.228020),
    (36, 37.680425),
    (37, 61.124931),
    (38, 98.993207),
    (39, 159.598007),
    (40, 257.939955)
]

plot_results(results)

# Messung der Zeit für die Berechnung der Fibonacci-Zahlen (rekursiv)
import time

def time_fib_recursive(n):
    start_time = time.time()
    result = fib_recursive(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

for i in range(20, 41):
    result, elapsed_time = time_fib_recursive(i)
    print(f"fib_recursive({i}) = {result}, Zeit: {elapsed_time:.6f} Sekunden")



# effiziente Funktion (iterativ) zur Berechnung der Fibonacci-Zahlen
def fib_iterative(n):
    if n <= 0:
        return 0 # Wenn n kleiner oder gleich 0 ist, gib 0 zurück
    elif n == 1:
        return 1 # Wenn n gleich 1 ist, gib 1 zurück
    else:
        a = 0 # Initialisiere a mit dem Wert von fib(0)
        b = 1 # Initialisiere b mit dem Wert von fib(1)
        for i in range(2, n+1): # Iteriere von fib(2) bis fib(n)
            c = a + b # Berechne den aktuellen Wert von fib(i)
            a = b # Setze a auf den vorherigen Wert von b
            b = c # Setze b auf den aktuellen Wert von c
        return b # Gib den letzten berechneten Wert zurück


# Messung der Zeit für die Berechnung der Fibonacci-Zahlen (iterativ)
import time

def time_fib_iterative(n):
    start_time = time.time()
    result = fib_iterative(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

for i in range(10000, 10001):
    result, elapsed_time = time_fib_iterative(i)
    print(f"fib_iterative({i}) = {result}, Zeit: {elapsed_time:.6f} Sekunden")
