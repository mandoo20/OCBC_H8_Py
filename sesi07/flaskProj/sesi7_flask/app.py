from  markupsafe import escape
from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Main'

# @app.route('/<name>')
# def hello(name):
#     return f'Hello, {escape(name)}!'

# @app.route('/hello')
# def hellow():
#     return f'Hello, World!'

#variable rules
@app.route('/user/<username>')
def show_user_profile(username):
 # show the user profile for that user
 return f'User {escape(username)}'
@app.route('/post/<int:post_id>')
def show_post(post_id):
 # show the post with the given id, the id is an integer
 return f'Post {post_id}'
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
 # show the subpath after /path/
 return f'Subpath {escape(subpath)}'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
 return render_template('hello.html', name=name)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#  if request.method == 'POST':
#     return do_the_login()
#  else:
#     return show_the_login_form()

# #static file - > bikin folder 'static'
# url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run(debug=True)