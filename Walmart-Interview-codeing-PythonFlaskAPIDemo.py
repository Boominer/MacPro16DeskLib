from flask import Flask, jsonify, request

"""
1. @app.route decorator router, using http methods
2. Reuqest to retrive the json input data
3. jsonify() convert data into json responses 
4. Http status code:    
    200 OK – everything fine
    201 Created – new resource made
    400 Bad Request – your request is broken
    401 Unauthorized – you need to log in
    403 Forbidden – you don’t have permission
    404 Not Found – doesn’t exist
    500 Internal Server Error – server crashed
5. Request - improtant object in Flask
    
    def upload():
        query = request.args.get("query")/('limit')   # get the data from URL, ex: search?query=python?limit=10
        form = request.form.get("user")               # when your POSTed data comes from HTML forms
        data = request.get_json()                     # json body, parses 
        data = request.data                           # raw boday, deserialization the XML
        file = request.files["file"]                  # file.save("/tmp/uploaded_file")
        token = request.headers.get("Authorization")  # Access any incoming HTTP headers, Authentication token or centent negotiation
        session_id = request.cookies.get('session_id')
        method = request.method == "POST"

        return {
            "query": query,
            "json": data,
            "filename": file.filename,
            "token": token
        }
6. next(iteration, default = None)
    -- if there is a match, it returns the first matching book dict 
    -- if there is no match, returns the default, None

7. good API design principals 
    The top 7 tips:
    1) Use clear naming.
    2) Ensure reliability through idempotency.
    3) Add versioning for backward compatibility.
    4) Add pagination for response.
    5) Use clear query strings for sorting.
    6) Security should not be an afterthought. Use api-headers for passing in tokens.
    7) Keep cross-resource references simple.
    8) Rate limiting


"""


# Initialize Flask app
app = Flask(__name__)   # FFF

# Sample data (in-memory storage)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# GET all books
@app.route('/books', methods=['GET'])  ## methods
def get_books():
    return jsonify(books)

# GET book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):                  ### get_book 
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT/update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(data)         # python built-in dicitonary update method, ignore the new fields
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404    # 404

# DELETE/delete a book by id
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books = [b for b in books if b['id'] != book_id]
        # books.remove(book)    
        # # index = next(( i for i, b in enumerate(books) if b['id'] == book_id) , None)
        # del books[index]
        return {'message':'Deleted'}
    else:
        return {'message':'Book not found'}, 404

# Run the app
if __name__ == '__main__':    # == 
    app.run(debug=True)

