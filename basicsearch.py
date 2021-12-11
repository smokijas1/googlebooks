import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

serch_parameter = 0

print ("Witaj w wyszukiwarce.")
print ("Podaj parametr wedłóg którego chcesz wyszukać:")
print ("1.Tytuł")
print ("2.Autor")
print ("3.Język")
print ("4.Data publikacji")

serch_parameter = int(input())

def searchin ():
    global serch_parameter
    if serch_parameter == 1:
        print ("Podaj autora dzieła.")
        user_update = input ()
        cur.execute("SELECT * FROM book4 WHERE tytul=?", (user_update,))
        records = cur.fetchall()
    
    elif serch_parameter == 2:
        print ("Podaj tytuł dzieła.")
        user_update = input ()
        cur.execute("SELECT * FROM book4 WHERE autor=?", (user_update,))
        records = cur.fetchall()

    elif serch_parameter == 3:
        print ("Podaj język dzieła.")
        user_update = input ()
        cur.execute("SELECT * FROM book4 WHERE jezyk_publikacji=?", (user_update,))
        records = cur.fetchall()
    
    elif serch_parameter == 4:
        print ("Podaj date wydania działa.")
        user_update = input ()
        cur.execute("SELECT * FROM book4 WHERE data_publikacj=?", (user_update,))
        records = cur.fetchall()
    elif serch_parameter > 4:
        print ("Zły parametr, spróbuj jeszcze raz.")
        searchin ()

    print('{0: <30} {1: <30} {2: <16} {3: <13} {4: <14} {5: <6} {6: <30}'.format("Tytuł","Autor ","Data publikacji ","ISBN ","Liczba stron ","Język ","Okładka "))
    for row in records:
        print('{0: <30} {1: <30} {2: <16} {3: <13} {4: <14} {5: <6} {6: <30}'.format(row[0], row[1], row[2], row[3], row[4] ,row[5], row[6]))

searchin ()