# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on different property features.

## 📌 Project Overview

This project uses a House Price Regression dataset to train a Linear Regression model.

The model takes the following features as input:

- Square Footage
- Number of Bedrooms
- Number of Bathrooms
- Year Built
- Lot Size
- Garage Size
- Neighborhood Quality

It then predicts the estimated House Price.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Flask
- HTML
- CSS

## 📊 Dataset

The project uses the House Price Regression Dataset containing:

- 1000 records
- 8 columns
- 7 input features
- 1 target variable: `House_Price`

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Analysis
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Correlation Analysis
   ↓
Train-Test Split
   ↓
Linear Regression
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Flask Web Application
   ↓
House Price Prediction
🤖 Machine Learning Model

Linear Regression was used for house price prediction.

Dataset Split
Training data: 80%
Testing data: 20%
📈 Model Performance

The model was evaluated using:

MAE
MSE
RMSE
R² Score

Results on the test set:

MAE: 8174.58
RMSE: 10071.48
R² Score: 0.99843
🌐 Web Application

A Flask-based web interface allows users to enter house details and receive an estimated house price.

Input Features
Square Footage
Number of Bedrooms
Number of Bathrooms
Year Built
Lot Size
Garage Size
Neighborhood Quality
▶️ How to Run
1. Clone the repository
git clone <your-github-repository-url>
2. Open the project
cd House_Price_Prediction
3. Create and activate virtual environment
python -m venv venv

Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run Flask application
python app.py
6. Open in browser
http://127.0.0.1:5000
📁 Project Structure
House_Price_Prediction/
│
├── app.py
├── data_analysis.py
├── prediction.py
├── house_price_model.pkl
├── house_price_regression_dataset.csv
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── visualizations/
⚠️ Note

The model performance reported above is based on the provided dataset and its test split. It should not be interpreted as guaranteed accuracy for real-world house prices.

👨‍💻 Project

House Price Prediction using Machine Learning and Flask.