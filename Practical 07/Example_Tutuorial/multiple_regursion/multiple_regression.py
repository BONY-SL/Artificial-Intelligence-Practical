import pandas as pd
from sklearn import linear_model

# Read the dataset
df = pd.read_csv("data.csv")

# Select features (independent variables)
X = df[['Weight', 'Volume']]
y = df['CO2']  # Target variable (dependent variable)

# Create and train the model
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Predict with correct feature names
input_data = pd.DataFrame([[2300, 1300]], columns=['Weight', 'Volume'])
predictedCO2 = regr.predict(input_data)

print(predictedCO2)
