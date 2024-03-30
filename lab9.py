# Author- Marlee Hunter

'''
Purpose: This program gets two times from input then compares them down to the second. Prints if they are equal, greater, or the same,
Pre-conditions: Get the 2 times in hours(int), minutes(int), and seconds(int)
Post-conditions:  Returns the first and second time then says if the time are greater equal or less than the other time

'''

def time_compare(hour1, minute1, second1, hour2, minute2, second2):
    '''
    Purpose: Compares the hours minutes and seconds then returns a value after each comparison
    Pre-conditions: hour1, minute1, second1, hour2, minute2, and second2 are all (int)
    Post-conditions: Returns the var number (1, 2, or 0)
    '''   
   # Comparing hours 
    if hour1 < hour2:
        var = 1
    elif hour1 > hour2:
        var = 2
    else: # Hours are the same so compare minutes
        if minute1 < minute2:
            var = 1
        elif minute1 > minute2:
            var = 2
        else: # Minutes are the same so compare seconds
            if second1 < second2:
                var = 1
            elif second1 > second2:
                var =  2 
            else:
                var = 0 # Times are the same
    return var
            
def time_print(hours, minutes, seconds):
    '''
    Purpose: Prints leading 0s if needed and semi colons between the hours, minutes, and seconds
    Pre-conditions: Using hours, minutes, and seconds (all int) 
    Post-conditions: Prints the time with a leading 0 infront if only 1 digit with colon seperating them
    '''
    # Checks if hours is less than 10
    if hours < 10:
        print("0", end="")
    print(hours, end=":")
        
    # Checks if minutes is less than 10
    if minutes < 10:
        print("0", end="")
    print(minutes, end=":")
    
    # Checks if seconds is less than 10
    if seconds < 10:
        print("0", end="")
    print(seconds)
    
def main():
    
    # Print title
    print('Tough times never last, but tough teams do\n')
    
    # Print intput for hour1
    hour1 = int(input("Enter first hours or -1 to stop: ")) 
    
    # Gets inputs only if number is not equal to -1
    while hour1 != -1:
        
        minute1 = int(input("Enter first minutes: "))
        second1 = int(input("Enter first seconds: "))
        # Get the second input
        hour2 = int(input("Enter second hours: "))
        minute2 = int(input("Enter second minutes: "))
        second2 = int(input("Enter second seconds: "))    
        print()

        # Print times
        print(f"   First time: ", end="")
        time_print(hour1, minute1, second1)
        print(f"   Second time: ", end="")
        time_print(hour2, minute2, second2)

        # Compare the times and print results
        result = time_compare(hour1, minute1, second1, hour2, minute2, second2)
        
        # Compares the results then prints the result
        if result == 0:
            print("   The times are the same\n")
        elif result == 1:
            print("   First time happens before second time\n")
        else:
            print("   First time happens after second time\n")
        
        # Print input for hour1 after loop is run     
        hour1 = int(input("Enter first hours or -1 to stop: "))

main()
    
