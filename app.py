from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)#object creation

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    book=db.Column(db.String(100),nullable=False)
    author=db.Column(db.String(100),nullable=False)
    price=db.Column(db.Float,nullable=False)


    def to_dict(self):
        return {
            "id":self.id,
            "book":self.book,
            "author":self.author,
            "price":self.price
        }


with app.app_context():
    db.create_all()

@app.route('/home')#path/URL
def home():#view
    name="naveenKumar"
    age = 21
    context={
        "name":name,
        "age": age
    }
    return render_template("homepage.html",**context)

@app.route('/contact')#path/URL
def contact():#view
    name="naveen"
    address="palamaner"
    context={
        "name":name,
        "address":address
    }
    return render_template("contact.html",**context)

@app.route('/about')#path/URL
def about():#view
    name="discription of the company"
    context={
        "name":name
    }
    return render_template("aboutus.html",**context)

@app.route('/')#path/URL
def master():#view

    return render_template("master.html")


#API Creation
@app.route('/api/books')
def get_books():
    books=Book.query.all()
    return jsonify([book.to_dict() for book in books])
    #data_type=type(books)
   #@ return data_type

@app.route('/api/books' , methods=['POST',])
def add_book():
        data = request.get_json()
        new_book = Book(id = data['id'], book=data['book'], author=data['author'], price= data['price'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201
        


if __name__== '__main__':
    app.run(debug=True)
