from flask import Flask, render_template, request
from flask import render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'hi '+name

#map the path in the url to handler functions
@app.route('/hello2')
def hello_2():
   return 'hi hello'


@app.route('/')
@app.route('/index')
def index():
    name = 'Oneonta'
    return render_template('index.html', title='Welcome', username=name)



@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

def hello_3():
   return 'hello world'
app.add_url_rule('/hello3', 'hello3', hello_3)

if __name__ == '__main__':
   app.run()
   #app.run(debug = True)

