# Author- Marlee Hunter


'''
Purpose: Finding pi by Monte Carlo
Pre-conditions: Input the number of darts (int)
Post-conditions: Output the time taken (float), approximation for pi (float), and the error for the approximation (float)

'''

# import libraries
import random
from time import process_time


def main():
    
    # display title
    print('Estimating pi with the Monte Carlo method\n')
    
    # initialize accumulator
    inside_circle = 0
    
    # start time
    start_time = process_time()
    
    # input number of darts 
    darts = int(input('How many darts for this simulation? '))
    print()
    
    # initialize loop
    for dart in range(darts):
        
        # get random x cordinate
        x_cordinate = random.random()
        
        # get random x cordinate
        y_cordinate = random.random()      
        
        # checks if its inside the circle
        if x_cordinate ** 2 + y_cordinate ** 2 <= 1:
                inside_circle += 1 
                
    # records end time
    end_time = process_time()
    
    # division against 0
    if darts <= 0:
        elapsed_time = 0   
        pi_approx = 0
    else:           
    # find ratio the pi approxmination
        pi_approx = (inside_circle / darts) * 4
    
    # find elapsed time
    elapsed_time = end_time - start_time
    
    # print elapsed time
    print(f'Time taken: {elapsed_time:.3f} seconds')
        
    # convert seconds to minutes and seconds if it exceeds one minute
    if elapsed_time > 60:
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"or {minutes} minutes and {seconds} seconds")    
 
    # print the approximation of pi
    print()
    print(f"Approximation to pi is {pi_approx:.9f}")    
    
    # print and calculate error for the approximation
    error = 3.141592654 - pi_approx
    print()
    print(f'Error for this Approximation: 3.141592654 - {pi_approx:.9f} = {error:.9f}')
 
    
main()
    
