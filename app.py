
from flask import Flask, jsonify, abort, make_response, request
from models import books

app=Flask(__name__)
app.config['SECRET_KEY']="nininini"

# /api/v1/books/:

# Metoda GET zwracająca listę ksiazek:

@app.route('/api/v1/books/', methods=["GET"])
def book_list_api_v1():
    return jsonify(books.all())

# Metoda POST dodajaca nowe pozycje:

@app.route('/api/v1/books/', methods=["POST"])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book={
        'id': books.all()[-1]['id']+1,
        'title':request.json['title'],
        'autor':request.json.get('autor',''),
        'pages':request.json.get('pages',''),
        'description':request.json.get('description',''),
        'read': False
    }
    books.create(book)
    return jsonify({ 'book': book }), 201


# /api/v1/books/id:

# Metoda GET zwracajaca konkretne id:

@app.route('/api/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book=books.get(book_id)
    if not book:
        abort(404)
    return jsonify({ 'book ': book })

# Metoda DELETE usuwająca pozycje:

@app.route('/api/v1/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    result=books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({ 'result': result})

# Metoda PUT zmieniajaca zawartosc pozycji:

@app.route('/api/v1/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book=books.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data=request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'autor' in data and not isinstance(data.get('autor'), str),
        'pages' in data and not isinstance(data.get('pages'), int),
        'description' in data and not isinstance(data.get('description'), str),
        'read' in data and not isinstance(data.get('read'), bool)
    ]):
        abort(400)
    book={
        'id':data.get('id', book['id']),
        'title':data.get('title',book['title']),
        'autor':data.get('autor',book['autor']),
        'pages':data.get('pages',book['pages']),
        'description':data.get('description',book['description']),
        'read':data.get('read', book['read'])
    }
    books.update(book_id, book)
    return jsonify({ 'book':book })

# błędy:

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found','status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error':'bad request', 'sttaus_code':400}), 400)


if __name__=='__main__':
    app.run(debug=True)






