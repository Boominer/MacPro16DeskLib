from flask import Flask,jsonify, request 
app = Flask(__name__)
books = [
    {'id':1,'title':'book1'}
    ,{'id':2,'title':'book2'}
]
@app.route('/books',methods=['GET'])
def get_books()
    return jsonify(books)

@app.route('/books/<int:id>',methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if books['id']==book_id), None)
    if book:
        return jsonify(book)
    else:
        return {'message':'not found'}, 404

@app.route('/books',methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id':len(books)+1
        'title':data['title']
    }
    books.append(book)
    return jsonify(new_bok), 201

@app.route()