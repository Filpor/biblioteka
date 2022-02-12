# biblioteka
Aplikacja potrafiąca zapisać listę książek, napisana z regułami API.

Struktura elementu json:

    "autor": "Autor Książki", 
    "description": "Opis Książki", 
    "id": "Identyfikator przypisywany autmoatycznie", 
    "pages": "Ilość Stron jako int", 
    "read": "Wartość bool zawierająca informację czy książka została przeczytana", 
    "title": "tytuł"
   
Aplikacja posiada nastęujące metody HTTP:

Pod Adresem: http://localhost:5000/api/v1/books/ :

1. GET - wyświetla wszystkie zapisane książki

2. POST - Dodająca nowe pozycje do listy

Pod Adresem: http://localhost:5000/api/v1/books/id :

1. GET - Wyświetlająca wybrany element id

2. DELETE - Usuwająca wybraną pozycję id z listy

3. PUT - Zmieniąjąca wybrane dane w pozycji id
    
