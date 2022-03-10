from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def page():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def home():
    if request.method == 'POST':
        CRIM = float(request.form['CRIM'])
        ZN = float(request.form['ZN'])
        INDUS = float(request.form['INDUS'])
        CHAS = float(request.form['CHAS'])
        NOX = float(request.form['NOX'])
        RM = float(request.form['RM'])
        AGE = float(request.form['AGE'])
        DIS = float(request.form['DIS'])
        PTRATIO = float(request.form['PTRATIO'])
        B = float(request.form['PTRATIO'])
        LSTAT = float(request.form['LSTAT'])

        #load model
        filename = 'rnd_model.pickle'
        load = pickle.load(open(filename,'rb'))
        pred = load.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,PTRATIO,B,LSTAT]])
        return render_template('results.html',pred=pred[0])

if __name__ == '__main__':
    app.run(debug=True)


