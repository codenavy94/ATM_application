import sqlite3

class Access:
    
    def __init__(self, card_num):
        self.card_num = card_num
        self.conn = sqlite3.connect("DB/Bank.db")
        self.cur = self.conn.cursor()
    
    def is_pin_correct(self, input_pin):
        query = f"SELECT pin\
                  FROM card\
                  WHERE card_num = '{self.card_num}'"
        self.cur.execute(query)
        correct_pin = self.cur.fetchone()[0]
        return correct_pin == input_pin
    
    def view_accounts(self):
        query = f"SELECT account_id, account_num, balance\
                  FROM card\
                  INNER JOIN account ON card.card_id = account.card_id\
                  WHERE card.card_num = '{self.card_num}'"
        self.cur.execute(query)
        accounts = self.cur.fetchall()
        self.conn.close()
        return accounts