from ATM.LocalRepoAccess import *
from ATM.LocalRepoAccountAction import *
from ATM.Message import *
from sys import exit

##### Enter Card #####

print_msg_enter_card()
card_num = input()
print()


##### Check PIN number #####

pin_check = False
wrong_cnt = 0

while wrong_cnt < 5:
    print_msg_enter_pin()
    input_pin = input()
    print()
    if is_pin_correct(card_num, input_pin):
        pin_check = True
        break
    else:
        print('Wrong PIN number. Please try again.', end='\n\n')
        wrong_cnt += 1
else:
    print_msg_freeze_acc()
    exit()


##### View Accounts #####

if pin_check:
    accounts = view_accounts(card_num)
    
    print('Your Accounts:')
    for idx, acc in enumerate(accounts, 1):
        print(f'[{idx}] {acc[1]}')
    print_msg_choose_acc()
    account_idx = int(input())-1
    print()


##### Account Actions #####

account_id = accounts[account_idx][0]
action = 0

while action != 9:
    print_msg_choose_action()
    action = int(input())
    print()

    # View Balance
    if action == 1:
        balance = view_balance(account_id)
        print(f'Your current balance is {balance} dollars.', end='\n\n')
    
    # Deposit
    elif action == 2:
        print_msg_enter_deposit_value()
        deposit_value = int(input())
        print()
        print('=== Processing Deposit... ===')
        print('=== Deposit Completed ===')
        deposit(account_id, deposit_value)
        balance = view_balance(account_id)
        print(f'Your current balance is {balance} dollars.', end='\n\n')
    
    # Withdrawl
    elif action == 3:
        print_msg_enter_withdrawl_value()
        balance = view_balance(account_id)
        withdraw_value = int(input())
        print()
        print('=== Processing Withdrawl... ===')
        
        if withdraw_value > balance:
            print_msg_withdrawl_error()
            print()
            continue
        else:
            withdraw(account_id, withdraw_value)
            print('=== Withdrawl Completed ===')
            balance = view_balance(account_id)
            print(f'Your current balance is {balance} dollars.', end='\n\n')

# End Program
print('End Program.\nThank you for using Bear Bank ATM.')
exit()
