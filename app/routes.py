from app import app

@app.route('/')
def index():
    return "holla my niggas"

@app.route('/name')
def name():
    my_name= 'brian'
    return f'holla {my_name}'