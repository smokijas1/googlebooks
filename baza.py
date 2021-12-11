import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()


print ("\n")
def chekin ():

    cur.execute ('SELECT * FROM book4')
    records = cur.fetchall()

    print('{0: <30} {1: <30} {2: <16} {3: <13} {4: <14} {5: <6} {6: <30}'.format("Tytuł","Autor ","Data publikacji ","ISBN ","Liczba stron ","Język ","Okładka "))
    for row in records:
        print('{0: <30} {1: <30} {2: <16} {3: <13} {4: <14} {5: <6} {6: <30}'.format(row[0], row[1], row[2], row[3], row[4] ,row[5], row[6]))


print ("W bibliotece znajdują się następujące tytuły.")
print ("\n")
chekin ()
print ("\n")


