# Programming exercises chapter 8

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
    print("This")

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
        


####
####
#fibonachi()
#double_val()
syracuse()