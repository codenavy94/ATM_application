import sqlite3

class Access:
    
    def __init__(self, card_num):
        self.card_num = card_num
        self.conn = sqlite3.connect()
    
    def is_pin_correct(self, pin):
        conn = sqlite3.connect("DB/card.db")
        cur = conn.cursor()
        query = f"SELECT pin FROM card WHERE card_num = {self.card_num}"
        cur.execute(query)
        correct_pin = cur.fetchone()[0]
        conn.close()
        return correct_pin == pin
    
    def view_accounts(self):
        conn = sqlite3.connect("DB/account.db")
        cur = conn.cursor()
        query = f"SELECT account_num FROM card\
                  INNER JOIN account ON card.card_id = account.card_id\
                  WHERE card.card_num = {self.card_num}"