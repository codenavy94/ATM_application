from ATM import LocalRepoAccess, LocalRepoAccountAction

init_msg = 'Enter Your Card Number\n\
            (ex) 0000-1234-5678\n\
            >> '
input_card_num = input(init_msg)
user = LocalRepoAccess.Access(input_card_num)

##### Check PIN number #####

pin_check = False

pin_msg = 'Enter Your PIN Number\n\
           (ex) 0000\n\
           >> '
wrong_cnt = 0

while wrong_cnt < 5:
    input_pin = input(pin_msg)
    if user.is_pin_correct(input_pin):
        pin_check = True
        break
    else:
        print('Wrong PIN Number. Try Again.')
        wrong_cnt += 1
else:
    print('You have entered wrong PIN Number for 5 times.\n\
           Please visit Bear Bank to regain access to your accounts.')


##### View Accounts #####

if pin_check:
    accounts = user.view_accounts()
    

    
##### Account Actions #####

