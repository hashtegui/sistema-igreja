from sqlite3 import Error
import sqlite3

def create_connection(db_file):    
    con = None
    
    try:
        con = sqlite3.connect('./usuarios.db')  
    except Error as e:
        print(e)
    finally:
        if con:
            con.close()
            
def prepara_banco():
    '''
    CREATE TABLE IF NOT EXISTS pessoas(
        id integer auto_increment primary key,
        nome text not null,
        sobrenome text not null,
        sexo text not null,
        dt_nascimento text not null
    )
    '''