import sqlite3

conn = sqlite3.connect("DB/Bank.db")

def cursor():
    return sqlite3.connect("DB/Bank.db").cursor()
    
def view_balance(account_id):
    c = cursor()
    query = f"SELECT balance\
              FROM account\
              WHERE account_id = '{account_id}'"
    c.execute(query)
    balance = c.fetchone()[0]
    c.connection.close()
    return balance

def deposit(account_id, deposit_value):
    balance = view_balance(account_id)
    new_value = balance + deposit_value
    c = cursor()
    query = f"UPDATE account\
              SET balance = {new_value}\
              WHERE account_id = '{account_id}'"
    c.execute(query)
    c.connection.commit()
    c.connection.close()

def withdraw(account_id, withdraw_value):
    balance = view_balance(account_id)
    new_value = balance - withdraw_value
    c = cursor()
    query = f"UPDATE account\
              SET balance = {new_value}\
              WHERE account_id = '{account_id}'"
    c.execute(query)
    c.connection.commit()
    c.connection.close()