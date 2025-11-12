from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id":1, "name":"Promise me", "genre":"crime,mystery and suspense thriller"},
    {"id":2, "name":"The 48 laws of power", "genre":"self-help book"},
    {"id":3, "name":"The alchemist","genre":"adventure and fantasy"}
]

@app.route("/api/books")
def get_books():
    return jsonify (books),200 

@app.route("/api/books", methods=['POST'])
def create_books():
    data = request.get_json()
    new_id = len(books)+1
    new_book = {"id":new_id, "name":data["name"],"genre":data["genre"]}
    books.append(new_book)
    return jsonify(new_book), 200

@app.route("/api/books/<int:book_id>", methods = ['PATCH'])
def update_books(books_id):
    data = request.get_json()
    for book in books:
        if book['id']== books_id:
            book["name"]= data.get("name", book["name"])
            return jsonify(book), 200
        return jsonify ({"Error Message": "Book Not Found"}), 404
    
@app.route("/api/books/<string:genre>", methods = ['DELETE'])
def delete_books(genre):
    for book in books:
        if book['genre']== genre:
            books.remove(book)
            return jsonify({"Message": "Successfully deleted"}), 201
        return jsonify ({"Message": "unsuccessful"}), 404
    
@app.route("/api/books/<int:book_id>")
def get_books_id(books_id):
    for book in books:
        if book['id']== books_id:
            return jsonify(book), 200
        return jsonify ({"Message": "Not Found"}), 404
    
@app.route("/api/books/<book_name>")
def get_name(books_name):
    for book in books:
        if book["name"] == books_name:
            return jsonify(book), 200
        return jsonify ({"Message": "Book Not Found"}), 404

@app.route("/api/info")
def get_book_info():
    return jsonify()

#Run the server
if __name__ == "__main__":
    app.run(debug=True)
