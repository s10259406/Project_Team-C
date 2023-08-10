# import your modules
import overheads, cash_on_hand, profit_loss

def main(option):

    '''
    - The function will return the highest overhead, surplus and deficit of both cash on hands & profit and loss
    - Required parameter: option
    '''
    
    # open the file in write mode
    with open('summary_report.txt', 'w') as file:
        
        if option == 'SURPLUS':
            # write some output to the file
            file.write('Scenario with SURPLUS\n')
            # call the module functions and write the results to the file
            file.write(f'{overheads.overheads_function("max_ovh")}')
            file.write(f'{cash_on_hand.coh_function("Surplus")}')
            file.write(f'{profit_loss.profitloss_function("Surplus")}')

        elif option == 'DEFICIT':
            # write some output to the file
            file.write('Scenario with DEFICIT\n')
            # call your module functions and write the results to the file
            file.write(f'{overheads.overheads_function("max_ovh")}')
            file.write(f'{cash_on_hand.coh_function("Deficit")}')
            file.write(f'{profit_loss.profitloss_function("Deficit")}')

# call main function with an option
main('SURPLUS')
# main('DEFICIT')