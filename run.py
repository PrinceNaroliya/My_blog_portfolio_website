from flask import Flask, render_template, request, url_for, redirect, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy 
from flask_ckeditor import CKEditor, CKEditorField 
from werkzeug.utils import secure_filename 
import os 
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)

# Config
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['CKEDITOR_PKG_TYPE'] = 'full'

# Extensions
db = SQLAlchemy(app)  
ckeditor = CKEditor(app)

# Ensure folder
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Model
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def home():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).limit(3).all()
    return render_template('home_page.html', blogs=blogs)

@app.route('/blog_post', methods = ['GET','POST'])
def blog_post():
    if request.method == 'POST':
        title = request.form.get('title')
        image = request.files.get('image')
        content = request.form.get('content')

        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image_path = os.path.join('static/images', filename)
            image.save(image_path)

            image_path = filename
        else:
            image_path = None

        new_blog = Blog(
            title = title,
            image = image_path,
            content = content
        )
        db.session.add(new_blog)
        db.session.commit()
    return render_template('blog_post.html')

@app.route('/blog/<int:id>')
def blog(id):
    blog = Blog.query.get_or_404(id)
    blogs = Blog.query.all()
    return render_template('blog.html', blog = blog, blogs = blogs)

@app.route('/blog_page')
def blog_page():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).all()
    return render_template('/blog_page.html', blogs = blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phonenumber = request.form.get('phonenumber')
        message = request.form.get('message')

        new_contact_message = ContactMessage (
            firstname = firstname,
            lastname =  lastname,
            email = email,
            phonenumber = phonenumber,
            message = message
        )

        db.session.add(new_contact_message)
        db.session.commit()
    return render_template('contact.html')

@app.route('/blog_detail_page')
def blog_detail_page():
    blogs = Blog.query.all()
    return render_template('blog_detail_page.html', blogs = blogs)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/contact_message_details')
def contact_message_details():
    new_messages = ContactMessage.query.all()
    return render_template('contact_message_details.html', new_messages = new_messages)

@app.route('/delete_blog/<int:id>', methods = ['GET','POST'])
def delete_blog(id):
    blog = Blog.query.filter_by(id = id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('blog_detail_page'))

@app.route('/delete_contact_message/<int:id>', methods = ['GET','POST'])
def delete_contact_message(id):
    contact_message = ContactMessage.query.filter_by(id = id).first()
    if contact_message:  
        db.session.delete(contact_message)
        db.session.commit()
    else:
        print(f"Contact message with id {id} not found.")
    return redirect(url_for('contact_message_details'))

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route("/google18a9e13cfb4bc401.html")
def google_verify():
    return send_from_directory("static", "google18a9e13cfb4bc401.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False)