import sqlite3


# Create DB for Card Info
conn = sqlite3.connect("card.db")
cur = conn.cursor()
conn.execute("CREATE TABLE card(card_id INTEGER, card_num TEXT, pin TEXT)")
cur.executemany(
    'INSERT INTO card VALUES (?, ?, ?)',
    [(10001, '0000-1234-5678', '0000'),
     (10002, '0000-9876-5432', '1111'),
     (10003, '1357-0000-1357', '2222')
     ]
)
conn.commit()
conn.close()


# Create DB for Account Info
conn = sqlite3.connect("account.db")
cur = conn.cursor()
conn.execute("CREATE TABLE account(account_id INTEGER, account_num TEXT, balance INTEGER)")
cur.executemany(
    'INSERT INTO account VALUES (?, ?, ?)',
    [(10001, '000-123-5678', 10000),
     (10002, '000-987-6543', 9800),
     (10003, '135-000-1357', 10)
     ]
)
conn.commit()
conn.close()