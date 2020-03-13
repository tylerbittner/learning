from flask import Flask, render_template

import xgboost as xgb

app = Flask(__name__)

# Load model on app start
model = xgb.XGBClassifier()
model.load_model("datasets/gbm_demo.model")

@app.route('/')
def index():
    # TODO call roc_auc_score() with hardcoded input
    score = None
    params = model.get_params()
    return render_template('index.html', score=score, params=params)