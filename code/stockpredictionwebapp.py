# Making an executable

# Imports
import joblib
import pickle
from flask import Flask, request, jsonify, render_template


# Create an instance (our app)
#app = Flask(__name__)
app = Flask(__name__, template_folder='../templates/')

gnb_one = joblib.load('../model/gnb_one.pkl')
spacyload = joblib.load('../model/spacy.pkl')

@app.route('/', methods=['GET', 'POST'])

@app.route('/predict')
def predict():
    return render_template('prediction.html')

@app.route('/predicted', methods=['GET', 'POST'])
def predicted():
    if request.method == 'POST':
        headline_input = request.form['input']

        vec_tokens = []
        for token in spacyload.pipe([headline_input]):
            vec_tokens.append(token.vector)
            
        predicted_token = gnb_one.predict([vec_tokens[0]])[0]
        
        predicted_token = "the stock ending the day in green" if predicted_token == 1 else "the stock ending the day in red" 
       
        return render_template("predicted.html", content=headline_input, prediction=predicted_token)
    
@app.route('/bye')
def bye():
    return render_template('bye.html')

if __name__ == '__main__':
    app.run(debug=True)
