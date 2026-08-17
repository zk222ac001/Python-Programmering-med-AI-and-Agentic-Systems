# Step 1: Install Libraries
# pip install pandas
# pip install matplotlib
# pip install scikit-learn

"""
pandas → Data handling
Matplotlib → Data visualization
Scikit-Learn → Machine Learning
------------------------------------------------------------
What is pandas?
Pandas is one of the most popular Python libraries
for working with structured data.

It allows us to:
- Read CSV and Excel files
- Organize data into tables
- Filter rows and columns
- Handle missing values
- Perform statistical analysis
- Prepare datasets for Machine Learning

Think of Pandas as an Excel spreadsheet inside Python.
-------------------------------------------------------------
What is Matplotlib?

Matplotlib is a Python library used for creating graphs and charts.
Machine Learning models become much easier to understand when data is visualized.
It helps us create:

- Line graphs
- Scatter plots
- Bar charts
- Pie charts
- Histograms
- Regression lines
---------------------------------------------------------------
## What is Scikit-Learn?

Scikit-Learn is the most widely used Machine Learning library in Python.
Instead of writing complex mathematical algorithms yourself, Scikit-Learn provides ready-made implementations.

It supports:

- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines
- K-Means Clustering
- Naive Bayes
- Neural Networks (basic)
- Model Evaluation
"""

# ............................................................
# Step 2: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -----------------------------
# Training Dataset
# -----------------------------
data = {
    "Size": [800, 1000, 1200, 1500, 1800, 2000, 2300, 2500],
    "Price": [120, 150, 180, 220, 260, 300, 340, 360],
}
df = pd.DataFrame(data)
print(df)
# Independent Variable (X)
X = df[["Size"]]
# Dependent Variable (Y)
y = df["Price"]

# -----------------------------
# Create Model
# -----------------------------

model = LinearRegression()
# Train Model
model.fit(X, y)
print("Model Trained Successfully")
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

# -----------------------------
# Predict New House
# -----------------------------
print("\nPredicting Price for a New House with Size 1600 sq ft")
new_house = pd.DataFrame({"Size": [1600]})
prediction = model.predict(new_house)
print(f"\nPredicted Price: ${prediction[0]:.2f} Thousand")

# -----------------------------
# Visualize the Regression Line
# -----------------------------

plt.figure(figsize=(8, 5))
plt.scatter(df["Size"], df["Price"], color="blue", label="Actual Houses")
plt.plot(
    df["Size"], model.predict(X), color="red", linewidth=3, label="Regression Line"
)
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price ($1000)")
plt.title("Linear Regression Example")

plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# Predict multiple houses
# -----------------------------

new_houses = pd.DataFrame({"Size": [800, 1000, 1200, 1500, 1800, 2000, 2300, 2500]})
predictions = model.predict(new_houses)
print("\nPredictions for Multiple Houses:")
for i, prediction in enumerate(predictions):
    print(f"House {i + 1}: ${prediction:.2f} Thousand")
