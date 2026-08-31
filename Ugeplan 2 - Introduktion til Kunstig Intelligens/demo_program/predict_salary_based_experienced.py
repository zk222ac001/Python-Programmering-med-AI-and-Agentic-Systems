# ============================================================
# Linear Regression Example
# Predict Salary from Years of Experience
# ============================================================

# ------------------------------------------------------------
# STEP 1: Install required libraries
# ------------------------------------------------------------
# Run this command in the terminal only if needed:
#
# pip install pandas numpy matplotlib scikit-learn
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 2: Import libraries
# ------------------------------------------------------------

# Pandas is used for working with tables and datasets
import pandas as pd

# NumPy provides mathematical operations
import numpy as np

# Matplotlib is used for graphs and visualization
import matplotlib.pyplot as plt

# LinearRegression is the Machine Learning model
from sklearn.linear_model import LinearRegression

# train_test_split separates data into training and testing sets
from sklearn.model_selection import train_test_split

# Metrics are used to evaluate model performance
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ------------------------------------------------------------
# STEP 3: Create the dataset
# ------------------------------------------------------------

data = {
    "YearsExperience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    "Salary": [
        35000,
        40000,
        45000,
        50000,
        55000,
        60000,
        65000,
        70000,
        75000,
        80000
    ]
}


# Convert dictionary into Pandas DataFrame
df = pd.DataFrame(data)


# Display the dataset
print("\n================ DATASET ================")
print(df)


# ------------------------------------------------------------
# STEP 4: Explore the dataset
# ------------------------------------------------------------

print("\n================ DATA INFORMATION ================")

print("\nFirst 5 rows:......")
print(df.head())

print("\nDataset shape:.........")
print(df.shape)

print("\nBasic statistics:..................")
print(df.describe())

print("\nMissing values:...................")
print(df.isnull().sum())


# ------------------------------------------------------------
# STEP 5: Define X and y
# ------------------------------------------------------------

# X = Input / Feature
#
# Double brackets [[ ]] are used because
# scikit-learn expects X to be two-dimensional.

X = df[["YearsExperience"]]


# y = Output / Target
#
# Single brackets are used because y is normally
# represented as a one-dimensional Series.

y = df["Salary"]


print("\n================ INPUT AND TARGET ================")

print("\nX - Years of Experience:")
print(X)

print("\ny - Salary:")
print(y)


# ------------------------------------------------------------
# STEP 6: Split the dataset
# ------------------------------------------------------------

# 80% of data will be used for training
# 20% of data will be used for testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


print("\n================ TRAIN / TEST SPLIT ================")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


print("\nTraining X:")
print(X_train)

print("\nTesting X:")
print(X_test)


# ------------------------------------------------------------
# STEP 7: Create the Linear Regression model
# ------------------------------------------------------------

model = LinearRegression()


# ------------------------------------------------------------
# STEP 8: Train the model
# ------------------------------------------------------------

model.fit(X_train, y_train)

print("\n================ MODEL TRAINING ================")

print("Model trained successfully!")


# ------------------------------------------------------------
# STEP 9: Display model parameters
# ------------------------------------------------------------

# Intercept
intercept = model.intercept_

/# Slope / coefficient
slope = model.coef_[0]


print("\n================ MODEL PARAMETERS ================")

print(f"Intercept: {intercept:.2f}")
print(f"Slope: {slope:.2f}")


# Display mathematical equation
print("\nRegression Equation:")

print(
    f"Salary = {slope:.2f} × YearsExperience "
    f"+ {intercept:.2f}"
)


# ------------------------------------------------------------
# STEP 10: Make predictions on test data
# ------------------------------------------------------------

y_pred = model.predict(X_test)


print("\n================ TEST PREDICTIONS ================")

print("Predicted salaries:")
print(y_pred)


# ------------------------------------------------------------
# STEP 11: Compare Actual vs Predicted
# ------------------------------------------------------------

results = pd.DataFrame({
    "YearsExperience": X_test["YearsExperience"],
    "Actual Salary": y_test,
    "Predicted Salary": y_pred
})


# Sort results by years of experience
results = results.sort_values("YearsExperience")


print("\n================ ACTUAL VS PREDICTED ================")

print(results)


# ------------------------------------------------------------
# STEP 12: Evaluate the model
# ------------------------------------------------------------

# Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Root Mean Squared Error
rmse = np.sqrt(mse)

# R² Score
r2 = r2_score(y_test, y_pred)


print("\n================ MODEL EVALUATION ================")

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")


# ------------------------------------------------------------
# STEP 13: Predict salary for a new employee
# ------------------------------------------------------------

new_experience = 12


# Create DataFrame using the same feature name
new_employee = pd.DataFrame({
    "YearsExperience": [new_experience]
})


predicted_salary = model.predict(new_employee)


print("\n================ NEW PREDICTION ================")

print(f"Years of Experience : {new_experience}")
print(f"Predicted Salary    : {predicted_salary[0]:,.2f}")


# ------------------------------------------------------------
# STEP 14: Visualize the original data
# ------------------------------------------------------------

plt.scatter(
    X["YearsExperience"],
    y,
    label="Actual Salary Data"
)


# ------------------------------------------------------------
# STEP 15: Draw regression line
# ------------------------------------------------------------

plt.plot(
    X["YearsExperience"],
    model.predict(X),
    label="Regression Line"
)


# ------------------------------------------------------------
# STEP 16: Add graph information
# ------------------------------------------------------------

plt.title("Salary Prediction Using Linear Regression")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid(True)

plt.legend()

plt.tight_layout()


# ------------------------------------------------------------
# STEP 17: Display graph
# ------------------------------------------------------------

plt.show()