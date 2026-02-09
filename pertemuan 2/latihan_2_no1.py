def fizzbuzz_plus(n):
    for N in range(1, n+1):
        if N % 3 == 0 and N % 5 == 0:
            print("FizzBuzz")
            
        elif N % 3 == 0:
            print("Fizz")
            if N % 7 == 0:
                print("Fizz" + "Seven")
            
        elif N % 5 == 0:
            print("Buzz")
            
        elif N % 7 == 0:
            print("Seven")

        else:
            print(N)
        

fizzbuzz_plus(21)