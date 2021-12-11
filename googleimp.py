import json
from urllib.request import ProxyBasicAuthHandler, urlopen
import sqlite3
import re

con = sqlite3.connect('example.db')
cur = con.cursor()

total_item = 0
db_title = 0
db_author = 0
db_date = 0
db_isbn = 0
db_page_numb = 0
db_cover = 0
db_leng = 0

def se_menu ():
    global google_choice
    print ("Podaj parametr wedłóg którego chcesz wyszukać książkę:")
    print ("1.ISBN")
    print ("2.Tutuł")
    print ("3.Autor")
    print ("4.Wydawnictwo")
    print ("\n")

    google_choice = int(input())
    se_mode()

def autoinput ():
    global db_title, db_author, db_date, db_isbn, db_page_numb, db_cover, db_leng

    db_isbn = re.findall("\d+", db_isbn)[0]

    if len(db_title) > 29:
        db_title = db_title[0:29]

    elif len(db_author) > 29:
        db_author = db_author[0:29]
    
    elif len(db_isbn) < 13:
        db_isbn = db_isbn[0:10]

    elif len(db_leng) > 5:
        db_leng = db_leng[0:5]


    auto_addin ()
    se_menu ()

def auto_addin():
        global db_title, db_author, db_date, db_isbn, db_page_numb, db_cover, db_leng
        cur.execute ("INSERT INTO book4 (tytul,autor,data_publikacj,isbn,liczba_stron,jezyk_publikacji,okladka) values (?,?,?,?,?,?,?)",(db_title, db_author, db_date, db_isbn, db_page_numb, db_leng, db_cover))
    
        con.commit()
        
        print ("\n")
        print ("Nowa książka została dodana.")
        print ("\n")

def se_title_input ():
    global in_title
    in_title = input("Podaj tytuł ksiazki: ").strip()
    in_title = in_title.replace(" ","+")
    se_title ()

def se_title ():
    global total_item, db_title, db_author, db_date, db_isbn, db_page_numb, db_cover, db_leng

    api = "https://www.googleapis.com/books/v1/volumes?q=intitle:"+in_title
    
    response = urlopen(api)
    book_data = json.load(response)

    volume_info = book_data["items"][total_item]["volumeInfo"]
    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]

    print(f"Tytul: {volume_info['title']}")
    print(f"Autor: {prettify_author}")

    #Petla biorąca pod uwagę możliwość braku inforamcji o ilości stron przy danym tytule
    while True:
        try:
            print(f"Ilosc stron: {volume_info['pageCount']}")
            break
        except KeyError:
            print(f"Brak informacji o ilości stron.")
            break

    print(f"Data wydania: {volume_info['publishedDate']}")
    print(f"ISBN: ", volume_info.get('industryIdentifiers')[0]['identifier'])
    
   #Petla biorąca pod uwagę możliwość braku inforamcji o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['language']}")
            break
        except KeyError:
            print(f"Język brak informacji o języku w którym została napisana książka.")
            break

    #Petla biorąca pod uwagę możliwość braku miniatury o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['thumbnail']}")
            break
        except KeyError:
            print(f"Brak miniatury.")
            break

    print("\n***\n")
    

    print ("Jaką operację chcesz wykonać?")
    print ("\n")
    print ("1.Sprawdź nastęną książkę pasującą do wuszukiwanej frazy.")
    print ("2.Sprawdź poprzednią książkę pasującą do wuszukiwanej frazy.")
    print ("3.Dodaj tą książkę do bazy.")
    print ("4.Wyszukaj książkę przy pomocy innego parametru.")
    print ("5.Zakończ wyszukiwanie.")

    operacja_input = int(input())
    print ("\n")
    print ("\n")

    if  operacja_input == 1:
        total_item = total_item + 1 
        se_title ()
    elif operacja_input == 2:
        total_item = total_item - 1 
        se_title ()
    elif operacja_input == 3:
        db_title = volume_info['title']
        db_author = prettify_author
        db_date = volume_info['publishedDate']
        db_isbn = volume_info.get('industryIdentifiers')[0]['identifier']
        
        while True:
            try:
                db_cover = volume_info['thumbnail']
                break
            except:
                db_cover = ("Brak")
                break

        while True:
            try:
                db_leng = volume_info['language']
                break
            except:
                db_leng = ("Brak")
                break

        while True:
            try:
                db_page_numb = volume_info['pageCount']
                break
            except:
                db_page_numb = ("Brak")
                break
        autoinput ()

    elif operacja_input == 4:
        se_menu ()
    elif operacja_input >= 5:
        print ("Miłego dnia.")

def se_isbn_input ():
    global isbn
    isbn = input("Podaj numer ISBN: ").strip()
    se_isbn ()

def se_isbn ():
    global total_item, db_title, db_author, db_date, db_isbn, db_page_numb, db_cover, db_leng
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn"+isbn
    
    response = urlopen(api)
    book_data = json.load(response)

    volume_info = book_data["items"][total_item]["volumeInfo"]
    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]

    print(f"Tytul: {volume_info['title']}")
    print(f"Autor: {prettify_author}")

    #Petla biorąca pod uwagę możliwość braku inforamcji o ilości stron przy danym tytule
    while True:
        try:
            print(f"Ilosc stron: {volume_info['pageCount']}")
            break
        except KeyError:
            print(f"Brak informacji o ilości stron.")
            break

    print(f"Data wydania: {volume_info['publishedDate']}")
    print(f"ISBN: ", volume_info.get('industryIdentifiers')[0]['identifier'])
    
   #Petla biorąca pod uwagę możliwość braku inforamcji o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['language']}")
            break
        except KeyError:
            print(f"Język brak informacji o języku w którym została napisana książka.")
            break

    #Petla biorąca pod uwagę możliwość braku miniatury o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['thumbnail']}")
            break
        except KeyError:
            print(f"Brak miniatury.")
            break

    print("\n***\n")
    

    print ("Jaką operację chcesz wykonać?")
    print ("\n")
    print ("1.Sprawdź nastęną książkę pasującą do wuszukiwanej frazy.")
    print ("2.Sprawdź poprzednią książkę pasującą do wuszukiwanej frazy.")
    print ("3.Dodaj tą książkę do bazy.")
    print ("4.Wyszukaj książkę przy pomocy innego parametru.")
    print ("5.Zakończ wyszukiwanie.")

    operacja_input = int(input())
    print ("\n")
    print ("\n")

    if  operacja_input == 1:
        total_item = total_item + 1 
        se_isbn ()
    elif operacja_input == 2:
        total_item = total_item - 1 
        se_isbn ()
    elif operacja_input == 3:
        db_title = volume_info['title']
        db_author = prettify_author
        db_date = volume_info['publishedDate']
        db_isbn = volume_info.get('industryIdentifiers')[0]['identifier']
        
        while True:
            try:
                db_cover = volume_info['thumbnail']
                break
            except:
                db_cover = ("Brak")
                break

        while True:
            try:
                db_leng = volume_info['language']
                break
            except:
                db_leng = ("Brak")
                break

        while True:
            try:
                db_page_numb = volume_info['pageCount']
                break
            except:
                db_page_numb = ("Brak")
                break
        autoinput ()

    elif operacja_input == 4:
        se_menu ()
    elif operacja_input >= 5:
        print ("Miłego dnia.")

def se_author_input ():
    global authors
    authors = input("Podaj autora ksiazki: ").strip()
    authors = authors.replace(" ","+")
    se_author ()    

def se_author ():
    global total_item, db_title, db_author, db_date, db_isbn, db_page_numb, db_cover, db_leng
    api = "https://www.googleapis.com/books/v1/volumes?q=inauthor:"+authors
    response = urlopen(api)
    book_data = json.load(response)

    volume_info = book_data["items"][total_item]["volumeInfo"]
    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]

    print(f"Tytul: {volume_info['title']}")
    print(f"Autor: {prettify_author}")

    #Petla biorąca pod uwagę możliwość braku inforamcji o ilości stron przy danym tytule
    while True:
        try:
            print(f"Ilosc stron: {volume_info['pageCount']}")
            break
        except KeyError:
            print(f"Brak informacji o ilości stron.")
            break

    print(f"Data wydania: {volume_info['publishedDate']}")
    print(f"ISBN: ", volume_info.get('industryIdentifiers')[0]['identifier'])
    
   #Petla biorąca pod uwagę możliwość braku inforamcji o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['language']}")
            break
        except KeyError:
            print(f"Język brak informacji o języku w którym została napisana książka.")
            break

    #Petla biorąca pod uwagę możliwość braku miniatury o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['thumbnail']}")
            break
        except KeyError:
            print(f"Brak miniatury.")
            break

    print("\n***\n")
    

    print ("Jaką operację chcesz wykonać?")
    print ("\n")
    print ("1.Sprawdź nastęną książkę pasującą do wuszukiwanej frazy.")
    print ("2.Sprawdź poprzednią książkę pasującą do wuszukiwanej frazy.")
    print ("3.Dodaj tą książkę do bazy.")
    print ("4.Wyszukaj książkę przy pomocy innego parametru.")
    print ("5.Zakończ wyszukiwanie.")

    operacja_input = int(input())
    print ("\n")
    print ("\n")

    if  operacja_input == 1:
        total_item = total_item + 1 
        se_author  ()
    elif operacja_input == 2:
        total_item = total_item - 1 
        se_author  ()
    elif operacja_input == 3:
        db_title = volume_info['title']
        db_author = prettify_author
        db_date = volume_info['publishedDate']
        db_isbn = volume_info.get('industryIdentifiers')[0]['identifier']
        
        while True:
            try:
                db_cover = volume_info['thumbnail']
                break
            except:
                db_cover = ("Brak")
                break

        while True:
            try:
                db_leng = volume_info['language']
                break
            except:
                db_leng = ("Brak")
                break

        while True:
            try:
                db_page_numb = volume_info['pageCount']
                break
            except:
                db_page_numb = ("Brak")
                break
        autoinput ()

    elif operacja_input == 4:
        se_menu ()
    elif operacja_input >= 5:
        print ("Miłego dnia.")

def se_pub_input ():
    global publisher
    publisher = input("Podaj autora ksiazki: ").strip()
    publisher = publisher.replace(" ","+")
    se_pub () 

def se_pub ():
    global total_item, db_title, db_author, db_date, db_isbn, db_page_numb, db_cover, db_leng
    api = "https://www.googleapis.com/books/v1/volumes?q=inpublisher:"+publisher
    response = urlopen(api)
    book_data = json.load(response)

    volume_info = book_data["items"][total_item]["volumeInfo"]
    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]

    print(f"Tytul: {volume_info['title']}")
    print(f"Autor: {prettify_author}")

    #Petla biorąca pod uwagę możliwość braku inforamcji o ilości stron przy danym tytule
    while True:
        try:
            print(f"Ilosc stron: {volume_info['pageCount']}")
            break
        except KeyError:
            print(f"Brak informacji o ilości stron.")
            break

    print(f"Data wydania: {volume_info['publishedDate']}")
    print(f"ISBN: ", volume_info.get('industryIdentifiers')[0]['identifier'])
    
   #Petla biorąca pod uwagę możliwość braku inforamcji o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['language']}")
            break
        except KeyError:
            print(f"Język brak informacji o języku w którym została napisana książka.")
            break

    #Petla biorąca pod uwagę możliwość braku miniatury o języku przy danym tytule
    while True:
        try:
            print(f"Język: {volume_info['thumbnail']}")
            break
        except KeyError:
            print(f"Brak miniatury.")
            break

    print("\n***\n")
    

    print ("Jaką operację chcesz wykonać?")
    print ("\n")
    print ("1.Sprawdź nastęną książkę pasującą do wuszukiwanej frazy.")
    print ("2.Sprawdź poprzednią książkę pasującą do wuszukiwanej frazy.")
    print ("3.Dodaj tą książkę do bazy.")
    print ("4.Wyszukaj książkę przy pomocy innego parametru.")
    print ("5.Zakończ wyszukiwanie.")

    operacja_input = int(input())
    print ("\n")
    print ("\n")

    if  operacja_input == 1:
        total_item = total_item + 1 
        se_pub ()
    elif operacja_input == 2:
        total_item = total_item - 1 
        se_pub ()
    elif operacja_input == 3:
        db_title = volume_info['title']
        db_author = prettify_author
        db_date = volume_info['publishedDate']
        db_isbn = volume_info.get('industryIdentifiers')[0]['identifier']
        
        while True:
            try:
                db_cover = volume_info['thumbnail']
                break
            except:
                db_cover = ("Brak")
                break

        while True:
            try:
                db_leng = volume_info['language']
                break
            except:
                db_leng = ("Brak")
                break

        while True:
            try:
                db_page_numb = volume_info['pageCount']
                break
            except:
                db_page_numb = ("Brak")
                break
        autoinput ()

    elif operacja_input == 4:
        se_menu ()
    elif operacja_input >= 5:
        print ("Miłego dnia.")

def se_mode():
    if google_choice == 1:
        se_isbn_input ()
    elif google_choice == 2:
        se_title_input ()
    elif google_choice == 3:
        se_author_input ()
    elif google_choice == 4:
        se_pub_input ()
    elif google_choice > 4:
        print ("Błąd, spróbuj ponownie.")
        se_menu ()  

print ("Witaj w wyszukiwrce książek Google Books!")
print ("\n")

se_menu ()

  