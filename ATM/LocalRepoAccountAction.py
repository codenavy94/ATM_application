import sqlite3

class AccountAction:
    
    def __init__(self, card_num):
        self.card_num = card_num
        self.conn = sqlite3.connect("DB/Bank.db")
        self.cur = self.conn.cursor()
        
    def see_balance():
        pass

    def deposit():
        pass

    def withdraw():
        pass