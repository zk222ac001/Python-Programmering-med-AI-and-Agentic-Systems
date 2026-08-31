# ⚡🔋 Assignment: Predicting Electricity Demand in Denmark Using Linear Regression

> **Course:** Machine Learning with Python  
> **Topic:** Supervised Learning – Linear Regression  
> **Difficulty:** 🟢 Beginner to Intermediate  
> **Estimated Duration:** ⏱️ 1–2 Hours  
> **Country Context:** 🇩🇰 Denmark

---

# 🌍 Real-World Challenge

Imagine that you are working as a **Machine Learning Engineer for Energinet**, the organization responsible for operating Denmark's electricity transmission system.

Every day, electricity demand changes because of factors such as:

- 🌡️ Temperature
- 🕒 Time of day
- 📅 Day of the week
- ❄️ Season
- 🎉 Public holidays
- 🏭 Industrial activity
- 👨‍👩‍👧 Human behavior
- 🌬️ Wind conditions
- ☀️ Solar generation

Your task is to build a **Machine Learning model** that predicts Denmark's electricity demand from historical data.

---

# 🎯 Learning Objectives

After completing this assignment, students should be able to:

- ✅ Understand the idea of **supervised learning**
- ✅ Explain how **Linear Regression** works
- ✅ Create and manipulate datasets using **Pandas**
- ✅ Visualize data using **Matplotlib**
- ✅ Separate input features (**X**) and target values (**y**)
- ✅ Train a Linear Regression model using **Scikit-learn**
- ✅ Make predictions with a trained model
- ✅ Draw and interpret a regression line
- ✅ Evaluate a regression model
- ✅ Interpret MAE, MSE, RMSE and R²
- ✅ Connect Machine Learning concepts to a real-world energy problem

---

# ⚡ Why Electricity Demand Forecasting Matters

Electricity must be generated and delivered at approximately the same time that consumers use it.

If electricity production is too low:

```text
Demand > Production
        │
        ▼
⚠️ Grid instability
        │
        ▼
Possible power shortages
```

If electricity production is too high:

```text
Production > Demand
        │
        ▼
⚠️ Wasted energy / higher cost
        │
        ▼
Reduced system efficiency
```

A better forecasting system helps energy companies:

- ⚡ Produce enough electricity
- 🛡️ Avoid blackouts
- 💰 Reduce operating costs
- 🌱 Integrate renewable energy
- 🔄 Balance the national electricity grid
- 📉 Reduce unnecessary energy production

---

# 🧠 Machine Learning Concept

In this assignment, we want the computer to learn a relationship between:

### Input Feature

```text
Temperature (°C)
```

### Target Value

```text
Electricity Demand (MWh)
```

---

# 🔄 Machine Learning Workflow

```text
┌──────────────────────┐
│ Historical Energy    │
│ Data                 │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Data Preparation     │
│ Pandas               │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Data Visualization   │
│ Scatter Plot         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Separate X and y     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Train Linear         │
│ Regression Model     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Make Predictions     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Evaluate Model       │
└──────────────────────┘
```

---

# 📊 Dataset

Use the following example historical dataset.

| Day | 🌡️ Temperature (°C) | ⚡ Electricity Demand (MWh) |
|---:|---:|---:|
| 1 | 2 | 36,000 |
| 2 | 4 | 35,500 |
| 3 | 5 | 35,200 |
| 4 | 8 | 34,500 |
| 5 | 10 | 34,000 |
| 6 | 12 | 33,500 |
| 7 | 15 | 32,800 |
| 8 | 18 | 32,200 |
| 9 | 20 | 31,800 |
| 10 | 22 | 31,500 |

---

# 🔍 Understanding the Dataset

The dataset suggests the following relationship:

```text
Low Temperature
      │
      ▼
More Heating
      │
      ▼
Higher Electricity Demand
```

and:

```text
Higher Temperature
      │
      ▼
Less Heating
      │
      ▼
Lower Electricity Demand
```

This means we may expect a **negative relationship** between temperature and electricity demand.

---

# 📐 Linear Regression

Linear Regression attempts to find the best straight line through the data.

The general equation is:

```text
y = mx + b
```

Where:

| Symbol | Meaning |
|---|---|
| `y` | Predicted electricity demand |
| `x` | Temperature |
| `m` | Slope |
| `b` | Intercept |

For this project:

```text
Electricity Demand = Slope × Temperature + Intercept
```

---

# 🧩 Visual Model

```text
                 Electricity Demand
                        ▲
                        │
       High Demand      │  ●
                        │    ●
                        │      ●
                        │        ●
                        │          ●
                        │             ●
       Low Demand       │                ●
                        └──────────────────────►
                          Low        High
                           Temperature
```

The regression model will attempt to draw the **best-fit line** through these observations.

---

# 📝 Assignment Tasks

---

## 🟦 Task 1 — Create the Dataset

Create a **Pandas DataFrame** using the dataset provided above.

Your DataFrame should contain three columns:

- `Day`
- `Temperature`
- `Electricity_Demand`

### ✅ Expected Result

A table similar to:

```text
Day   Temperature   Electricity_Demand
1     2             36000
2     4             35500
...
```

### 💡 Reflection

Why is Pandas useful for Machine Learning projects?

---

## 🟩 Task 2 — Explore the Dataset

Before building the model, inspect the data.

Display:

- First five rows
- Column names
- Number of rows and columns
- Basic statistical information

### Questions

1. What is the minimum temperature?
2. What is the maximum temperature?
3. What is the average electricity demand?
4. Are there any missing values?

---

## 🟨 Task 3 — Visualize the Data

Create a **scatter plot** showing:

```text
X-axis → Temperature
Y-axis → Electricity Demand
```

Your graph must include:

- 📌 Title
- 📌 X-axis label
- 📌 Y-axis label
- 📌 Grid

### Example

```text
Electricity Demand
       ▲
36000  │ ●
35000  │   ● ●
34000  │       ● ●
33000  │            ●
32000  │                ● ●
31000  │                    ●
       └────────────────────────►
         2   5   10   15   20
              Temperature
```

### 💡 Question

What relationship can you observe between temperature and electricity demand?

---

## 🟥 Task 4 — Define X and y

Separate the dataset into:

### Input

```text
X = Temperature
```

### Target

```text
y = Electricity Demand
```

### Diagram

```text
             TRAINING DATA

Temperature               Electricity Demand

    2°C   ───────────────► 36,000 MWh
    4°C   ───────────────► 35,500 MWh
    5°C   ───────────────► 35,200 MWh
    8°C   ───────────────► 34,500 MWh
   10°C   ───────────────► 34,000 MWh
```

---

## 🟪 Task 5 — Train the Linear Regression Model

Create and train a **Linear Regression** model.

Conceptually:

```text
Training Data
     │
     ▼
┌───────────────────────┐
│ Linear Regression     │
│ Learning Algorithm    │
└──────────┬────────────┘
           │
           ▼
    Trained Model
```

The model should learn the mathematical relationship between:

```text
Temperature → Electricity Demand
```

---

## 🟧 Task 6 — Display Intercept and Slope

Display:

- **Intercept**
- **Slope / coefficient**

### Example

```text
Model Trained Successfully

Intercept:
37,850

Slope:
-285
```

### Explain the Values

#### Intercept

The intercept represents the model's predicted electricity demand when:

```text
Temperature = 0°C
```

#### Slope

The slope represents how much predicted electricity demand changes when temperature increases by **1°C**.

For example:

```text
Slope = -285
```

means approximately:

```text
Temperature increases by 1°C
           │
           ▼
Electricity Demand decreases
by approximately 285 MWh
```

---

# 🔮 Task 7 — Predict Future Electricity Demand

Use your trained model to predict electricity demand at:

| Temperature | Prediction Required |
|---:|---|
| 6°C | ✅ |
| 14°C | ✅ |
| 25°C | ✅ |

### Prediction Workflow

```text
New Temperature
      │
      ▼
┌──────────────────────┐
│ Trained Linear       │
│ Regression Model     │
└──────────┬───────────┘
           │
           ▼
Predicted Electricity
Demand
```

### Expected Output Format

```text
Temperature: 6°C
Predicted Demand: XXXXX MWh

Temperature: 14°C
Predicted Demand: XXXXX MWh

Temperature: 25°C
Predicted Demand: XXXXX MWh
```

### 💡 Question

Does the predicted demand increase or decrease as temperature increases?

Explain why.

---

# 📈 Task 8 — Draw the Regression Line

Create a graph containing:

- 🔵 Original data points
- 📉 Regression line
- 🏷️ Graph title
- ↔️ X-axis label
- ↕️ Y-axis label
- 🧮 Grid
- 🗂️ Legend

### Conceptual Diagram

```text
Electricity Demand
       ▲
36000  │ ●
       │  ╲
35000  │   ●╲
       │      ╲
34000  │       ●╲
       │          ╲
33000  │           ●╲
       │              ╲
32000  │               ●╲
       │                  ╲●
31000  │
       └────────────────────────►
           Temperature (°C)

       ● Historical Data
       ╲ Regression Line
```

---

# 🧪 Task 9 — Evaluate the Model

Evaluate the model using:

- **MAE**
- **MSE**
- **RMSE**
- **R² Score**

---

## 1️⃣ Mean Absolute Error — MAE

MAE measures the average absolute difference between actual and predicted values.

```text
Actual Value
      │
      │ Difference
      ▼
Predicted Value
```

### Interpretation

Lower MAE = Better predictions.

---

## 2️⃣ Mean Squared Error — MSE

MSE squares prediction errors before averaging them.

```text
Error
  │
  ▼
Error²
  │
  ▼
Average
```

Large errors receive a stronger penalty.

### Interpretation

Lower MSE = Better model.

---

## 3️⃣ Root Mean Squared Error — RMSE

RMSE is the square root of MSE.

```text
MSE
 │
 ▼
Square Root
 │
 ▼
RMSE
```

An advantage of RMSE is that it uses the **same unit as the target variable**.

For this assignment:

```text
RMSE unit = MWh
```

---

## 4️⃣ R² Score

R² indicates how well the model explains variation in the data.

Typical interpretation:

| R² | Interpretation |
|---:|---|
| 1.00 | Perfect fit |
| 0.90+ | Very strong |
| 0.70–0.90 | Good |
| 0.50–0.70 | Moderate |
| Below 0.50 | Weak |

> ⚠️ A high R² does not automatically mean that the model is suitable for real-world deployment.

---

# 🧠 Task 10 — Discussion Questions

Answer each question in your own words.

---

### ❓ Question 1

Why does electricity demand often increase during winter in Denmark?

Think about:

- Heating
- Lighting
- Shorter daylight hours
- Indoor activity

---

### ❓ Question 2

Why is Linear Regression considered a **supervised learning algorithm**?

Use the following idea:

```text
Input + Known Correct Output
          │
          ▼
   Machine Learning
          │
          ▼
       Model
```

---

### ❓ Question 3

Is electricity-demand prediction a:

- Classification problem
- Regression problem

Explain your answer.

---

### ❓ Question 4

Suggest at least **three additional features** that could improve the model.

Possible examples:

- 🌬️ Wind speed
- 📆 Day of week
- 🎉 Public holiday
- 💧 Humidity
- 🕒 Hour of day
- ☀️ Solar production
- ⚡ Electricity price
- 🏭 Industrial activity
- ❄️ Season

Explain **why each feature could influence electricity demand**.

---

# ⭐ Bonus Task — Multiple Linear Regression

The simple model uses only:

```text
Temperature
```

A more advanced model could use several features.

For example:

```text
                 ┌─────────────┐
Temperature ────►│             │
                 │             │
Wind Speed ─────►│ Multiple    │
                 │ Linear      │────► Electricity Demand
Humidity ───────►│ Regression  │
                 │             │
Day of Week ────►│             │
                 └─────────────┘
```

Build a **Multiple Linear Regression** model using:

- Temperature
- Wind Speed
- Humidity

Then compare it with the simple Linear Regression model.

---

# 📊 Model Comparison Table

Students should create a comparison table.

| Model | Features | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Simple Linear Regression | Temperature | | | |
| Multiple Linear Regression | Temperature, Wind Speed, Humidity | | | |

### Discussion

Which model performs better?

Why do you think this happens?

---

# 🚀 Challenge Task — Build a Smarter Energy Model

Try adding more real-world features:

```text
                    ┌──────────────────┐
Temperature ───────►│                  │
Hour ──────────────►│                  │
Day of Week ───────►│                  │
Wind Speed ────────►│ Machine Learning │
Solar Generation ──►│ Model            │────► Demand Forecast
Holiday ───────────►│                  │
Energy Price ──────►│                  │
                    └──────────────────┘
```

Compare the results with your original model.

---

# 🌱 Real-World Energy AI Pipeline

```text
Weather Data
     │
     ├─────────────┐
     │             │
     ▼             ▼
Temperature     Wind Speed

Calendar Data
     │
     ▼
Day / Holiday

Energy Data
     │
     ▼
Historical Demand
     │
     └───────────────┐
                     ▼
             ┌─────────────────┐
             │ Machine Learning│
             │ Forecasting     │
             └────────┬────────┘
                      │
                      ▼
             Electricity Demand
                 Prediction
                      │
                      ▼
             ┌─────────────────┐
             │ Grid Planning   │
             │ & Optimization  │
             └─────────────────┘
```

---

# 📦 Deliverables

Students must submit:

- ✅ Python source code
- ✅ Screenshot of the original dataset
- ✅ Scatter plot
- ✅ Regression-line graph
- ✅ Screenshot of predictions
- ✅ Model evaluation results
- ✅ Answers to discussion questions
- ✅ Short report of approximately **2–3 pages**

---

# 📝 Suggested Report Structure

## 1. Introduction

Explain:

- What electricity demand forecasting is
- Why it is important
- What your model is trying to predict

## 2. Dataset

Describe:

- Number of observations
- Input feature
- Target variable

## 3. Machine Learning Method

Explain:

- Supervised learning
- Linear Regression
- X and y

## 4. Results

Include:

- Intercept
- Slope
- Predictions
- Regression graph
- Evaluation metrics

## 5. Discussion

Discuss:

- Model strengths
- Model limitations
- Possible improvements

## 6. Conclusion

Summarize what you learned from the project.

---

# 📋 Grading Rubric

| Criteria | Marks |
|---|---:|
| 📥 Data Loading | 10 |
| 📊 Data Exploration & Visualization | 10 |
| 🧠 Model Training | 20 |
| 🔮 Predictions | 15 |
| 📈 Regression Plot | 15 |
| 🧪 Model Evaluation | 15 |
| 💻 Code Quality | 10 |
| 💬 Discussion Questions | 5 |
| **Total** | **100** |

---

# 🏆 Success Criteria

A successful submission should demonstrate that the student can move through the entire Machine Learning workflow:

```text
Problem
   │
   ▼
Dataset
   │
   ▼
Visualization
   │
   ▼
Model Training
   │
   ▼
Prediction
   │
   ▼
Evaluation
   │
   ▼
Interpretation
```

---

# 🌍 Real-World Applications

Similar forecasting techniques are used by organizations such as:

- 🇩🇰 **Energinet**
- 🇬🇧 **National Grid**
- 🇩🇪 **TenneT**
- 🇺🇸 **PJM Interconnection**
- 🇪🇺 **ENTSO-E**

Machine Learning can help power-grid operators:

- ⚡ Forecast electricity demand
- 🌬️ Integrate wind energy
- ☀️ Integrate solar energy
- 💰 Reduce operating costs
- 🌱 Reduce carbon emissions
- 🔋 Improve energy storage planning
- 🛡️ Reduce the risk of electricity shortages

---

# 📚 Recommended Real-World Data Sources

## 🇩🇰 Energinet — Energy Data Service

**Website:**  
https://www.energidataservice.dk/

Useful for:

- Electricity consumption
- Electricity production
- Electricity prices
- Wind generation
- Solar generation

---

## 🌍 Open Power System Data

**Website:**  
https://open-power-system-data.org/

Useful for:

- European electricity consumption
- Renewable energy generation
- Time-series energy data

---

## 🇪🇺 ENTSO-E Transparency Platform

**Website:**  
https://transparency.entsoe.eu/

Useful for:

- European electricity demand
- Electricity generation
- Cross-border electricity flows

---

# 🧭 Final Challenge

Can you create a more realistic electricity-demand forecasting model by adding:

- 🕒 Hour of the day
- 📅 Day of the week
- 🌡️ Temperature
- 🌬️ Wind speed
- ☀️ Solar generation
- 🎉 Public holidays
- 💶 Electricity price

Then answer:

> **Does adding more useful features improve prediction accuracy?**

Compare your results using:

```text
MAE
MSE
RMSE
R²
```

---

# 🎓 Final Reflection

Write a short reflection answering:

1. What did you learn from this assignment?
2. What was the most difficult part?
3. Why is data visualization useful before model training?
4. What does the slope tell you about electricity demand?
5. What additional data would you collect if you worked for Energinet?
6. Would you trust this simple model for Denmark's real electricity grid? Why or why not?

---

> ## 💡 Key Takeaway
>
> Machine Learning is not only about training a model.
>
> A complete Machine Learning project involves:
>
> **Understanding the problem → preparing data → visualizing patterns → training → predicting → evaluating → improving.**
