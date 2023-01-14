from flask import Flask, request, render_template,jsonify
from password_generator import passwords as generator

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def generate():


    len =request.form.get("len")
    
    if len:
         len = int(len)
    else:
        len=8

    password =generator(len)
    
   
    return render_template('index.html', value=password)


if __name__ == '__main__':
    app.run(debug=True)
