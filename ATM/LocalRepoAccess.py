import sqlite3
import os.path

conn = sqlite3.connect("DB/Bank.db")

def cursor():
    return sqlite3.connect("DB/Bank.db").cursor()

def is_pin_correct(card_num, input_pin):
    c = cursor()
    query = f"SELECT pin\
              FROM card\
              WHERE card_num = '{card_num}'"
    c.execute(query)
    correct_pin = c.fetchone()[0]
    c.connection.close()
    return input_pin == correct_pin

def view_accounts(card_num):
    c = cursor()
    query = f"SELECT account_id, account_num, balance\
              FROM card\
              INNER JOIN account ON card.card_id = account.card_id\
              WHERE card.card_num = '{card_num}'"
    c.execute(query)
    accounts = c.fetchall()
    c.connection.close()
    return accounts