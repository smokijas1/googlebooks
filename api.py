from flask import *
import sqlite3

book4 = {}
records = 0
book_list = []

def biblioteka():
    global book4, records
    book4 = {}
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute ('SELECT * FROM book4')
    records = cur.fetchall()

    for i in records:
        book4 = {}
        book4["Title"] = i[0]
        book4["Author"] = i[1]
        book4["Date"] = i[2]
        book4["ISBN"] = i[3] , 
        book4["Page number"] = i[4] 
        book4["Language"] = i[5] 
        book4["Cover"] = i[6]
        book_list.append(book4)

app = Flask (__name__)

@app.route ('/api/lib', methods=['GET'])

def api_get_books4 ():
    biblioteka ()  
    return jsonify (book = book_list)



app.run(port=3000)
