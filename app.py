from flask import Flask


app = Flask(__name__)



@app.route('/')
def index():
    return "The landing page"



@app.route('/inventory')
def get_items():
    pass



#Get a specific item
@app.route('/inventory/<int:id>')
def get_item():
    pass



@app.route('/inventory', methods=['POST'])
def post_item():
    pass




@app.route('/inventory/<int:id>', methods= ['PATCH'])
def update_item():
    pass


@app.route('/inventory/<int:id>', methods= ['DELETE'])
def remove_item():
    pass









if __name__ == "__main__":
    app.run(debug= True)