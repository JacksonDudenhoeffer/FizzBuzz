#num is theholder for the printed number and tested for fizzbuzz
for num in range(1, 101):
    #output is the holder for what will be printed
    output = ""
    #tests for a number divisible by 3
    if num % 3 == 0:
       output += "Fizz"
    #tests for a number divisible by 5
    if num % 5 == 0:
        output += "Buzz"
    #output is printed
    print(output)
