# ATM_application
This is a simple ATM application which allows users to make several account actions.  
A user can view their balance, deposit to or withdraw from his/her own account according to the following steps.

1) Enter card number. (ex. 0000-1234-5678)
2) Enter PIN number. (ex. 0000)
3) If PIN is correct, the user can make one of the following actions:
    - [1] View Balance
    - [2] Make Deposit
    - [3] Make Withdrawl
    - [9] End Program

- If a wrong PIN number is inserted for 5 times in a row, a user will be given the following warning and the program will end automatically.  
```
You have entered wrong PIN number for 5 times.
Please visit Bear Bank to regain access to your accounts.
End Program.
```

## How to Run the Application
1. Set your cwd to the root directory of the repository.

```cmd
C:\Desktop\YOUR_DIR_NAME\ATM_application>
```

2. Execute ```main.py``` python file.

```
C:\Desktop\YOUR_DIR_NAME\ATM_application> python main.py
```

3. Enter valid card number for the follwing direction:  
(The program presupposes that the input is always a valid card number.)

```
Enter your card number
(ex) 0000-1234-5678
>> 0000-1234-5678
```

4. Enter valid PIN number for the following direction:

```
Enter your PIN number
(ex) 0000
>> 0000
```

5. If the PIN is correct, the application will show you a list of accounts you have as follows.  
Choose one of the accounts you would like make actions for.

```
Your Accounts:
[1] 135-000-1357
[2] 246-789-1135
Choose account number. (ex) 1
>> 1
```

6. If choose one of the accounts, you can choose one of the actions you would like to make:

```
Choose Account Action:
======================
[1] View Balance
[2] Deposit Money
[3] Withdraw Money

[9] End Program
======================
>> 2
```

7. For ```[2] Deposit Money``` and ```[3] Withdraw Money``` options, the program will ask the user to enter deposit/withdrawl amount as follows.  
Moreover, the program will return an error message if the withdrawl amount entered by the user is bigger than the account balance.

```
Enter deposit amount:
>> 1000
```
```
Enter withdrawl amount:
>> 500
```
```
=== Processing Withdrawl... ===
There is not enough money in the account.
Please try again.
```

8. The program will continue to run until the user enters ```9``` for ending the program.

