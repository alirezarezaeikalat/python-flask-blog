from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'alireza',
        'title': 'blog 1',
        'content': 'first post content',
        'date_posted': 'April 2020'   
    },
    {
        'author': 'ghasem',
        'title': 'blog shahadat',
        'content': 'second post',
        'date_posted': 'june 2020'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'ghasem')

if __name__ == '__main__':
    app.run(debug=True)