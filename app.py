from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
<<<<<<< Updated upstream
def home():
    return render_template("website.html")
=======
def index():
    return render_template("index.html")
>>>>>>> Stashed changes

@app.route('/record_input', methods=['POST'])
def record_input():
    input_variable = request.form.get('input_variable')
    print(f"Recorded input variable: {input_variable}")
    # Add your own processing logic here
    return f"Input variable recorded: {input_variable}"



if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
