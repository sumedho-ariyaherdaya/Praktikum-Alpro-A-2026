def fizzbuzz_plus(n):
    for n in range(22):
        print(n)
        if n % 3 and n % 5:
            print("FizzBuzz")
        if n % 3:
            print("Fizz")
        if n % 5:
            print("Buzz")
        if n % 7:
            print("Seven")
        else:
            print(n)
        
fizzbuzz_plus("21")