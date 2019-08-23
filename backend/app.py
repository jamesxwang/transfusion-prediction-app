from flask import Flask
import pickle
import joblib

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

models = joblib.load('./models/models.pkl')
for i in range(len(models)):                
    y_val_prdt[:,i] = model[i].predict_proba(test[predictors])[:,1]
    test_preds = y_val_prdt.mean(axis=1)
    y_val_pred = (test_preds >0.63).astype(np.int32)
    # print(y_val_prdt, test_preds, y_val_pred)

if __name__ == '__main__':
    app.run(debug=True)
