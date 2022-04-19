import inspect

def print_msg_enter_card():
    msg = 'Enter your card number\n(ex) 0000-1234-5678\n>>'
    print(msg, end = ' ')

def print_msg_enter_pin():
    msg = 'Enter your PIN number\n(ex) 0000\n>>'
    print(msg, end = ' ')

def print_msg_freeze_acc():
    msg = 'You have entered wrong PIN number for 5 times.\n\
        Please visit Bear Bank to regain access to your accounts.'
    print(msg)
    
def print_msg_choose_acc():
    msg = inspect.cleandoc('''
    Choose account number. (ex) 1
    >>''')
    print(msg, end = ' ')
    
def print_msg_choose_action():
    msg = inspect.cleandoc('''
    Choose Account Action:
    ======================
    [1] View Balance
    [2] Deposit Money
    [3] Withdraw Money
    
    [9] End Program
    ======================
    >>''')
    print(msg, end = ' ')

def print_msg_enter_deposit_value():
    msg = inspect.cleandoc('''
    Enter deposit amount:
    >>''')
    print(msg, end = ' ')
    
def print_msg_enter_withdrawl_value():
    msg = inspect.cleandoc('''
    Enter withdrawl amount:
    >>''')
    print(msg, end = ' ')

def print_msg_withdrawl_error():
    msg = inspect.cleandoc('''
    There is not enough money in the account.
    Please try again.''')
    print(msg)