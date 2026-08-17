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
# Import pandas to store and manipulate the training data in a table.
import pandas as pd

# Import pyplot to draw the scatter plot and regression line.
import matplotlib.pyplot as plt

# Import LinearRegression, the machine-learning model used in this example.
from sklearn.linear_model import LinearRegression

# -----------------------------
# Training Dataset
# -----------------------------
# Store house sizes and prices in a simple Python dictionary.
data = {
    # House sizes are measured in square feet.
    "Size": [800, 1000, 1200, 1500, 1800, 2000, 2300, 2500],
    # Prices are measured in thousands of dollars.
    "Price": [120, 150, 180, 220, 260, 300, 340, 360],
}

# Convert the dictionary into a pandas DataFrame.
df = pd.DataFrame(data)

# Print the dataset so learners can see the input data.
print(df)

# Independent Variable (X)
X = df[["Size"]]

# Dependent Variable (Y)
y = df["Price"]

# -----------------------------
# Create Model
# -----------------------------

# Create a linear regression model object.
model = LinearRegression()

# Train Model
model.fit(X, y)

# Confirm that training completed.
print("Model Trained Successfully")

# Print the intercept, which is the predicted price when size is zero.
print("Intercept:", model.intercept_)

# Print the slope, which shows how price changes as size increases.
print("Slope:", model.coef_[0])

# -----------------------------
# Predict New House
# -----------------------------
# Explain which new house size is being predicted.
print("\nPredicting Price for a New House with Size 1600 sq ft")

# Store the new house size in a DataFrame with the same column name as training data.
new_house = pd.DataFrame({"Size": [1600]})

# Ask the trained model to predict the new house price.
prediction = model.predict(new_house)

# Print the predicted price with two decimal places.
print(f"\nPredicted Price: ${prediction[0]:.2f} Thousand")

# -----------------------------
# Visualize the Regression Line
# -----------------------------

# Create a figure with a readable size.
plt.figure(figsize=(8, 5))

# Draw the original training points as blue dots.
plt.scatter(df["Size"], df["Price"], color="blue", label="Actual Houses")

# Draw the model's predicted line across the training sizes.
plt.plot(
    df["Size"], model.predict(X), color="red", linewidth=3, label="Regression Line"
)

# Label the horizontal axis.
plt.xlabel("House Size (sq ft)")

# Label the vertical axis.
plt.ylabel("Price ($1000)")

# Add a chart title.
plt.title("Linear Regression Example")

# Show the legend for dots and line.
plt.legend()

# Add grid lines to make the chart easier to read.
plt.grid(True)

# Display the chart window.
plt.show()

# -----------------------------
# Predict multiple houses
# -----------------------------

# Create a DataFrame of several house sizes to predict.
new_houses = pd.DataFrame({"Size": [800, 1000, 1200, 1500, 1800, 2000, 2300, 2500]})

# Predict prices for all of the new houses at once.
predictions = model.predict(new_houses)

# Print a heading for the prediction results.
print("\nPredictions for Multiple Houses:")

# Print each predicted price with its house number.
for i, prediction in enumerate(predictions):
    print(f"House {i + 1}: ${prediction:.2f} Thousand")
