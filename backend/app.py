from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# load the trained model
model = joblib.load("random_forest_model.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    """API endpoint to receive data and return prediction"""

    data = request.json  # get JSON data from Streamlit

    # convert input to DataFrame (VERY IMPORTANT)
    input_df = pd.DataFrame([{
        "total_bill": data["total_bill"],
        "sex": data["sex"],
        "smoker": data["smoker"],
        "day": data["day"],
        "time": data["time"],
        "size": data["size"]
    }])

    # make prediction
    prediction = model.predict(input_df)

    # return prediction
    return jsonify({"prediction": float(prediction[0])})


if __name__ == "__main__":
    app.run(debug=True)
