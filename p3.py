def play():
    print('Welcome, this program can calculate Liquidity Ratio.')
play()    
def run():
    num1 = int(input('Current Assets:'))
    num2 = int(input('Inventory:'))
    num3 = int(input('Current Liabilities:'))
    print('{} - {} / {} ='.format(num1, num2, num3))
    print(num1 - num2 / num3)    
    cal_again()
def cal_again():
    C = input('If you want to run this program again press Y for yes, if not press N for no:')

    if C.upper() == 'Y':
        run()
    elif C.upper() == 'N':
        print('Bye')
run()        