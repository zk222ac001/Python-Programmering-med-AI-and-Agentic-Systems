# ⚡ Assignment: Predicting Electricity Demand in Denmark Using Linear Regression

## Course

Machine Learning with Python

**Topic:** Supervised Learning – Linear Regression

**Difficulty:** Beginner to Intermediate

**Estimated Duration:** 3–4 Hours

---

# Learning Objectives

After completing this assignment, students will be able to:

- Understand supervised learning.
- Apply Linear Regression to real-world data.
- Load and preprocess datasets using Pandas.
- Visualize electricity consumption.
- Train a Linear Regression model.
- Predict future electricity demand.
- Evaluate model performance.
- Interpret prediction results.

---

# Background

Electricity demand changes every day due to many factors such as:

- Time of day
- Temperature
- Season
- Holidays
- Industrial activity
- Human behavior

Energy companies use Machine Learning to predict electricity demand so they can:

- Produce enough electricity
- Avoid blackouts
- Reduce operating costs
- Integrate renewable energy
- Balance the national power grid

As a Machine Learning Engineer working for **Energinet**, your task is to build an AI model that predicts Denmark's daily electricity demand.

---

# Real-World Scenario

Energinet has collected historical electricity consumption data.

Your job is to develop a Machine Learning model that predicts the electricity demand for future days.

---

# Dataset

Example dataset

| Day | Temperature (°C) | Electricity Demand (MWh) |
|----:|-----------------:|-------------------------:|
|1|2|36000|
|2|4|35500|
|3|5|35200|
|4|8|34500|
|5|10|34000|
|6|12|33500|
|7|15|32800|
|8|18|32200|
|9|20|31800|
|10|22|31500|

---

# Machine Learning Problem

Input (X)

```
Temperature
```

Output (Y)

```
Electricity Demand
```

Goal

```
Temperature
        │
        ▼

Machine Learning Model

        │
        ▼

Electricity Demand
```

---

# Assignment Tasks

## Task 1

Create a Pandas DataFrame using the dataset.

---

## Task 2

Visualize the dataset using a scatter plot.

Label both axes.

---

## Task 3

Separate the dataset into

- X (Temperature)
- y (Electricity Demand)

---

## Task 4

Train a Linear Regression model.

---

## Task 5

Display

- Intercept
- Slope

Explain what each value means.

---

## Task 6

Predict electricity demand when

- Temperature = 6°C
- Temperature = 14°C
- Temperature = 25°C

---

## Task 7

Draw the regression line.

Your graph must include

- Scatter plot
- Regression line
- Title
- X-axis label
- Y-axis label
- Grid
- Legend

---

## Task 8

Evaluate the model using

- MAE
- MSE
- RMSE
- R² Score

Explain each metric.

---

## Task 9

Answer the following questions.

### Question 1

Why does electricity demand usually increase during winter?

---

### Question 2

Why is Linear Regression considered a supervised learning algorithm?

---

### Question 3

Is electricity demand a

- Classification problem
- Regression problem

Explain your answer.

---

### Question 4

Suggest three additional features that could improve the prediction model.

Examples

- Wind speed
- Day of week
- Public holidays
- Humidity
- Hour of day
- Solar production

---

## Bonus Task

Build a **Multiple Linear Regression** model using

- Temperature
- Wind Speed
- Humidity

Compare the prediction accuracy with the simple Linear Regression model.

---

# Deliverables

Students must submit

- Python source code
- Graph showing regression line
- Screenshot of predictions
- Short report (2–3 pages)
- Answers to discussion questions

---

# Expected Output

Example

```
Model Trained Successfully

Intercept:
37850

Slope:
-285
```

Prediction

```
Temperature: 6°C

Predicted Demand:
34,800 MWh
```

---

# Grading Rubric

| Criteria | Marks |
|-----------|------:|
| Data Loading | 10 |
| Data Visualization | 10 |
| Model Training | 20 |
| Predictions | 15 |
| Regression Plot | 15 |
| Model Evaluation | 15 |
| Code Quality | 10 |
| Discussion Questions | 5 |

**Total:** 100 Marks

---

# Real-World Applications

The same techniques are used by

- 🇩🇰 Energinet (Denmark)
- 🇬🇧 National Grid (United Kingdom)
- 🇩🇪 TenneT Germany
- 🇺🇸 PJM Interconnection (USA)
- 🇪🇺 European Network of Transmission System Operators (ENTSO-E)

Machine Learning helps these organizations

- Forecast electricity demand
- Optimize renewable energy usage
- Reduce carbon emissions
- Prevent power shortages
- Improve smart grid operations

---

# Recommended Dataset

Students are encouraged to use real-world data from the following sources.

### Energinet Open Data

https://www.energidataservice.dk/

---

### Open Power System Data

https://open-power-system-data.org/

---

### ENTSO-E Transparency Platform

https://transparency.entsoe.eu/

---

# Challenge

Can you improve the prediction accuracy by adding

- Hour of the day
- Day of the week
- Wind speed
- Solar generation
- Public holidays
- Electricity price

Compare the results with the simple Linear Regression model.