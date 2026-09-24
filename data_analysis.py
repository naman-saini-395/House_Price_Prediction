import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("house_price_regression_dataset.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Duplicate values
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

print(df.duplicated().sum())


# 1. House Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["House_Price"], kde=True)
plt.title("House Price Distribution")
plt.xlabel("House Price")
plt.ylabel("Number of Houses")
plt.show()


# 2. Square Footage vs House Price
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Square_Footage", y="House_Price", data=df)
plt.title("Square Footage vs House Price")
plt.xlabel("Square Footage")
plt.ylabel("House Price")
plt.show()


# 3. Bedrooms vs House Price
plt.figure(figsize=(8, 5))
sns.boxplot(x="Num_Bedrooms", y="House_Price", data=df)
plt.title("Bedrooms vs House Price")
plt.xlabel("Number of Bedrooms")
plt.ylabel("House Price")
plt.savefig("graph.png")
plt.close()
plt.savefig("house_price_distribution.png")
plt.close()
plt.savefig("square_footage_vs_price.png")
plt.close()
plt.savefig("bedrooms_vs_price.png")
plt.close()

# 4. Correlation Heatmap

plt.figure(figsize=(10, 7))

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("correlation_heatmap.png")
plt.close()


# Machine Learning Data Preparation

X = df.drop("House_Price", axis=1)
y = df["House_Price"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

print("\nX Shape:")
print(X.shape)

print("\ny Shape:")
print(y.shape)

from sklearn.model_selection import train_test_split

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("\nTesting Data:")
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)

from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel Training Completed!")

# Make predictions on test data
y_pred = model.predict(X_test)

print("\nPredicted Prices:")
print(y_pred[:5])

print("\nActual Prices:")
print(y_test.head().values)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Model Evaluation

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Actual vs Predicted Prices

plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")

# Perfect prediction line
min_price = min(y_test.min(), y_pred.min())
max_price = max(y_test.max(), y_pred.max())

plt.plot(
    [min_price, max_price],
    [min_price, max_price],
    linestyle="--"
)

plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.close()

print("\nActual vs Predicted graph saved!")

import joblib

# Save trained model
joblib.dump(model, "house_price_model.pkl")

print("\nModel saved successfully!")