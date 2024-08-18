import sqlite3
import hashlib

class SecurityHandler:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('users.db')
            self.create_users_table()
        except sqlite3.Error as e:
            print(e)
    
    def create_users_table(self):
        '''
        Creates tables of the database
            if it already exists, it doesn't create it again
        '''
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def close_connection(self):
            self.conn.close()
        
    def create_user(self, username, password):
        '''
        Taking a users username and password and inserting them into the table
            the password is hashed so that it is protected
        '''
        c = self.conn.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute('INSERT INTO users VALUES (?,?)', (username, hashed_password))
        self.conn.commit()
        print("User created sucessfully")
        
    def login_user(self, username, password):
        '''
        Checking if the username and password are in the tables through a query
        '''
        c = self.conn.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute('SELECT * FROM users WHERE = ? AND password = ?', (username, hashed_password))
        user = c.fetchone() #if no match, return None
        return user is not None #if not None, then return True

    def reset_database(self):
        print("Resetting the database")
        c = self.conn.cursor()
        c.execute('DROP TABLE users')
        self.create_users_table()
        self.close_connection()
        

