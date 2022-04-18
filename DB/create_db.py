import sqlite3

# Create DB
conn = sqlite3.connect("Bank.db")
cur = conn.cursor()
conn.executescript('''
                   CREATE TABLE card(
                       card_id TEXT NOT NULL,
                       card_num TEXT NOT NULL,
                       pin TEXT NOT NULL,
                       PRIMARY KEY(card_id)
                   );
                   
                   CREATE TABLE account(
                       account_id TEXT NOT NULL,
                       card_id TEXT NOT NULL,
                       account_num TEXT NOT NULL,
                       balance INTEGER NOT NULL,
                       FOREIGN KEY(card_id) REFERENCES card(card_id),
                       PRIMARY KEY(account_id)
                   );
                   
                   INSERT INTO card(card_id, card_num, pin) VALUES
                   ('c001', '0000-1234-5678', '0000'),
                   ('c002', '0000-9876-5432', '1111'),
                   ('c003', '1357-0000-1357', '2222');
                   
                   INSERT INTO account(account_id, card_id, account_num, balance) VALUES
                   ('acc001', 'c001', '000-123-5678', 10000),
                   ('acc002', 'c001', '000-987-6543', 9800),
                   ('acc003', 'c002', '135-000-1357', 10),
                   ('acc004', 'c002', '246-789-1135', 200),
                   ('acc005', 'c003', '110-113-1112', 3500);
                   
                   ''')
            
conn.commit()
conn.close()