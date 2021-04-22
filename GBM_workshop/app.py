from flask import Flask, render_template

import xgboost as xgb

app = Flask(__name__)

# Load model on app start
model = xgb.XGBClassifier()
model.load_model("datasets/gbm_demo.model")

@app.route('/')
def index():
    # TODO: Optional -- call roc_auc_score() with hardcoded input to show a model prediction
    score = None

    params = model.get_params()
    return render_template('index.html', score=score, params=params)


if __name__ == "__main__":
    app.debug = True
    app.run(port=8080)