import sqlite3


# Create DB for Card Info
conn = sqlite3.connect("card.db")
cur = conn.cursor()
conn.execute("CREATE TABLE card(card_id TEXT, card_num TEXT, pin TEXT)")
cur.executemany(
    'INSERT INTO card VALUES (?, ?, ?)',
    [('c001', '0000-1234-5678', '0000'),
     ('c002', '0000-9876-5432', '1111'),
     ('c003', '1357-0000-1357', '2222')
     ]
)
conn.commit()
conn.close()


# Create DB for Account Info
conn = sqlite3.connect("account.db")
cur = conn.cursor()
conn.execute("CREATE TABLE account(account_id TEXT, card_id TEXT, account_num TEXT, balance INTEGER)")
cur.executemany(
    'INSERT INTO account VALUES (?, ?, ?, ?)',
    [('acc001', 'c001', '000-123-5678', 10000),
     ('acc002', 'c001', '000-987-6543', 9800),
     ('acc003', 'c002', '135-000-1357', 10),
     ('acc004', 'c003', '246-789-1135', 200),
     ('acc005', 'c004', '110-113-1112', 3500)
     ]
)
conn.commit()
conn.close()