# Programming exercises chapter 8
import math

def fibonachi():
    n = int(input("Enter the nth number you want (negative number to quit): "))
    n1, n2 = 1, 1
    count = 0
    if n < 0:
        quit()

    while n >= 0:
        if n == 0:
            print("Invalid Input")
        elif n == 1:
            print(n1)
        else:
            while count < n:
                print(n1)
                nth = n1 + n2
                # Update values
                n1 = n2
                n2 = nth
                count += 1
        n = int(input("Enter the nth number you want (negative to quit): "))
        n1, n2 = 1, 1
        count = 0
       
    
def double_val():
    start_val = float(input("Enter the initial investment: "))
    interest = float(input("Enter the yearly interest (apr): "))
    end_val = start_val
    year = 0
    while end_val < (start_val * 2):
        end_val = end_val * (1 + interest)
        year += 1
        print(end_val)
        print(year)
    print("It took", year, "years to double the value.")


def syracuse():
    try:
        num = int(input("Enter any positive integer: "))
        count = 0
        num_list = []
        
        while num < 0:
            print("Number was not a positive integer.")
            num = int(input("Enter any positive integer: "))
        
        num_list.append(num)
        while num != 1:
            if (num % 2) == 0:
                num = num / 2
                count += 1
                num_list.append(num)
            else:
                num = 3 * num + 1
                count += 1
                num_list.append(num)
                
        print("\nIt took", count, "times to get to 1")
        print("Here is the list:")
        print(num_list)
    except ValueError:
        print("Input was not an integer.")
    except:
        print("\nUnkown Error")
        
def is_prime():
    print("Function to find all prime numbers including the input.")
    num = int(input("Enter a number: "))
    num_list = []
    prime = False

    for num in range(0, num + 1):
        if num > 1:
            # Iterate from 2 to sqrt of num
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
            
            else:
                print(num)
                num_list.append(num)
                prime = True

    if prime:
        print(num_list)
    else:
        print(num, "is not a prime number")
        
# The goldbach conjecture asserts that every number is the sum of two prime numbers
def goldbach():
    primes = []
    success = False
    num = int(input("\nEnter a positive even number: "))
    if num < 0:
        print("\nIncorrect Input: must be positive")
        again(goldbach)
    elif (num % 2) != 0:
        print("\nIncorrect Input: not an even number")
        again(goldbach)
    else:
        primes = prime(num)
        #print(primes)
        for i in range (0,len(primes)):
            first_num = primes[i]
            #print("i:",primes[i])
            for j in range (0, len(primes)):
                #print("j",primes[j])
                second_num = primes[j]
                if first_num + second_num == num:
                    success = True
                    print("Success")
                    print(first_num,"+",second_num,"=", num)
                #else:
                    #print("Fail")
        if not success:
            print("Something went wrong")
        again(goldbach)

def prime(num):
    primes = []
    prime = False
    for num in range (0, num + 1):
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
                prime = True

    if prime:
        print("There were primes")
    else:
        print("There were no primes")
    return primes


def again(function_name):
    ans = input("Run Again? (y/n): ")
    if "y" in ans:
        function_name()
    else:
        quit()


####
####
#fibonachi()
#double_val()
#syracuse()
#is_prime()
goldbach()