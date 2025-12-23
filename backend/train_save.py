"""the purpose of this file is to load the data from load_data.py
and load the trained model from train_model.py
and save the trained model to afile  using joblib"""
import joblib
from data.load_data import load_data
from model.train_model import train_model
def train_and_save_model():
    """load data,train the model and save the trained model to a file"""

    #load the data
    df=load_data()

    #train model
    model=train_model(df)

    # save the trained model to afile
    joblib.dump(model,'random_forest_model.pkl')
    print("Model trained and saved to random_forest_model.pkl")

if __name__ == "__main__":
    train_and_save_model()