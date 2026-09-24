import joblib
import pandas as pd

# Load trained model
model = joblib.load("house_price_model.pkl")

# Take input from user
square_footage = float(input("Enter Square Footage: "))
num_bedrooms = int(input("Enter Number of Bedrooms: "))
num_bathrooms = int(input("Enter Number of Bathrooms: "))
year_built = int(input("Enter Year Built: "))
lot_size = float(input("Enter Lot Size: "))
garage_size = int(input("Enter Garage Size: "))
neighborhood_quality = int(input("Enter Neighborhood Quality (1-10): "))

# Create input DataFrame
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

# Predict house price
prediction = model.predict(input_data)

print("\nPredicted House Price:", prediction[0])