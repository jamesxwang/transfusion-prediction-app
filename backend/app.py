from flask import Flask, request, jsonify
import pickle
import joblib
import pandas as pd
import numpy as np
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')

def predict_probabilities(input_data):
    keys = [
        "Age",
        "Height(cm)",
        "Weight(cm)",
        "BMI",
        "Atrial Fibrillation",
        "Left Ventricular Enlargement",
        "Treated Hypertension",
        "Diabetes mellitus",
        "Anemia",
        "Cerebrovascular diseases",
        "NYHA classification",
        "ASA classification",
        "Extracorporeal circulation priming volume (mL)",
        "Red Blood Cell (RBC, 10^12/L)",
        "White Blood Cell(WBC, 10^9/L)",
        "Hemoglobin (Hb, g/dL)",
        "Hematocrit (HCT, %)",
        "Platelet Count (PLT, 10^9/L)",
        "Serum creatinine(Scr,mol/L )",
        "Total protein(TP, g/L)",
        "Albumin(ALB, g/L)",
        "Globulin(GLO, g/L)",
        "Alanine Transaminase (ALT, U/L)",
        "Aspertate Aminotransferase(AST, U/L)",
        "Prothrombin(PT, s)",
        "INR International Normalized Ratio(INR)",
        "Left ventricular ejection fraction(LVEF, %)",
        "Gender_female",
        "Gender_male",
        "Blood Type_A",
        "Blood Type_AB",
        "Blood Type_B",
        "Blood Type_O",
        "Extracorporeal circulation priming volume/Body Mass Index"
    ]
    obj = {}
    for key in keys:
        obj[key] = 0
    inputJSON = pd.read_json(json.dumps(input_data), orient='index')
    for col in inputJSON.columns:
        obj[col] = inputJSON.loc[0][col]
    input_dataframe = pd.DataFrame.from_dict({"0": obj}, orient='index')
    models = joblib.load('./models/models.pkl')
    cv_num = len(models)
    pred_proba = np.zeros((input_dataframe.shape[0], cv_num))
    for i in range(cv_num):                
        pred_proba[:,i] = models[i].predict_proba(input_dataframe)[:,1]
    pred_proba = pred_proba.mean(axis=1)
    result = int(pred_proba>0.7)
    return(result)


@app.route('/api/predict', methods = ['POST'])
def predict():
    
    if request.headers['Content-Type'] == 'application/json':
        input_data = request.json
        result = predict_probabilities(input_data)
        response = jsonify(isError= False, message= "Success", statusCode= 200, data= result)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
        return response
    return jsonify(isError= True, message= "Error", statusCode= 404)

@app.route('/', methods = ['GET'])
def hello():
    return "OK"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
