from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("house_price_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        square_footage = float(request.form["square_footage"])
        num_bedrooms = int(request.form["num_bedrooms"])
        num_bathrooms = int(request.form["num_bathrooms"])
        year_built = int(request.form["year_built"])
        lot_size = float(request.form["lot_size"])
        garage_size = int(request.form["garage_size"])
        neighborhood_quality = int(request.form["neighborhood_quality"])

        input_data = pd.DataFrame([[
            square_footage,
            num_bedrooms,
            num_bathrooms,
            year_built,
            lot_size,
            garage_size,
            neighborhood_quality
        ]], columns=[
            "Square_Footage",
            "Num_Bedrooms",
            "Num_Bathrooms",
            "Year_Built",
            "Lot_Size",
            "Garage_Size",
            "Neighborhood_Quality"
        ])

        prediction = round(model.predict(input_data)[0], 2)
        
    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)