import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

def addin ():

    cur.execute ("INSERT INTO book4  (tytul,autor,data_publikacj,isbn,liczba_stron,jezyk_publikacji,okladka) values (?,?,?,?,?,?,?)",(title, author, date, isbn, page_numb, leng, cover,))
    
    con.commit()


def auto_addin():
     if __name__=="__main__":
        cur.execute ("INSERT INTO book4  (tytul,autor,data_publikacj,isbn,liczba_stron,jezyk_publikacji,okladka) values (?,?,?,?,?,?,?)",(db_title, db_author, db_date, db_isbn, db_page_numb, db_cover, db_leng,))
    
        con.commit()
        print ("\n")
        print ("Nowa książka została dodana.")
        print ("\n")


print ("Witaj w systemie dodawania książek do bazy Śmigowski.")
print ("Przygotuj: tytuł książki, autora książka, data publikacji, numer ISBN, liczba stron, link do okładki i język publikacji.")
print ("\n")


def user_input ():
    global title, author, date, isbn, page_numb, cover, leng
    
    print ("Podaj tytuł książki.")
    title = input()
    print ("\n")

    print ("Podaj autora książki.")
    author = input()
    print ("\n")

    print ("Print podaj datę publikacji.")
    date = input()
    print ("\n")

    print ("Podaj numer ISBN.")
    isbn = input()
    print ("\n")

    print ("Podaj liczbę stron.")
    page_numb = input()
    print ("\n")

    print ("Podaj link do okładki książki.")
    cover = input ()
    print ("\n")

    print ("Podaj język publikacji.")
    leng = input ()
    print ("\n")

    if len(title) > 29:
        title = title[0:29]

    elif len(author) > 29:
        author = author[0:29]
    
    elif len(date) > 9:
        date = date[0:9]
    
    elif len(isbn) > 13:
        isbn = isbn[0:13]

    elif len(page_numb) > 5:
        page_numb = page_numb[0:5]

    elif len(leng) > 5:
        leng = leng[0:5]




user_input ()
addin ()

print ("Nowa książka została dodana.")