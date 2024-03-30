# Prolog
# Author: Marlee Hunter
# Email: mchu250@uky.edu


def main():
    
    
    # display title
    print('Union Risk Analysis by AFL-CIO Company Pay Ratios')
    print()
    
    # ask for number of companies
    companies = int(input('How many companies will be processed? '))
    print()
    
    # intialize accumulator
    total_ceo_pay = 0
    total_median_pay = 0
    
    # intialize loop
    for company in range(1, companies + 1):
        
        # display header
        print(f'Company {company} ----------')
        print()
        
        # ask for ticker
        ticker = input('   Ticker: ')
        
        # ask for median pay
        median_pay = int(input('   Median worker pay: '))
        
        # ask for ceo pay rate
        ceo_pay_rate = int(input('   CEO pay ratio: '))
        
        # calculate ceo pay 
        ceo_pay = ceo_pay_rate * median_pay
        
        # print header
        print('   --- Company Report ---')
        
        # determine ceo risk
        if ceo_pay > 200_000_000:
            ceo_risk = 5
        elif ceo_pay > 20_000_000:
            ceo_risk = 4
        elif ceo_pay > 2_000_000:
            ceo_risk = 3
        else:
            ceo_risk = 1
            
        # determine worker risk
        if median_pay < 5_000:
            worker_risk = 5
        elif median_pay < 10_000:
            worker_risk = 4
        elif median_pay < 20_000:
            worker_risk = 3
        else:
            worker_risk = 1
        
        # calculate company risk
        company_risk = ceo_risk * worker_risk
     
        
        # output company report
        print(f'   CEO Pay      ${ceo_pay / 1000000:.1f}M Risk {ceo_risk}')
        print(f'   Worker Pay      ${median_pay / 1000:.1f}K Risk {worker_risk}')
        print(f'   Company Risk {company_risk}')
        print()
        
        # accumulator pay for summary report
        total_ceo_pay += ceo_pay
        total_median_pay += median_pay
            
    # print report
    print()
    print('Summary Report ---------')
   
            
    if companies > 0:
        average_ceo_pay = total_ceo_pay / companies
        average_median_pay = total_median_pay / companies
    else:
        average_ceo_pay = 0
        average_median_pay = 0
    # print average ceo pay
    print(f'Average CEO pay            ${average_ceo_pay / 1000000:.1f}M')
    # print average median worker pay
    print(f'Average Median Worker pay  ${average_median_pay / 1000:.1f}K')
    
        
main()
    
    
    
    
    
    
    
    
    