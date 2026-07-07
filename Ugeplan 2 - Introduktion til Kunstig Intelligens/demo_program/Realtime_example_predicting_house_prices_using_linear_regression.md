# 🏠 Real-Time Example: Predicting House Prices Using Linear Regression

## 🎯 Objective

In this exercise, you will build a **Linear Regression** model that predicts the selling price of a house based on its size (square feet).

This is one of the most common real-world applications of **Supervised Machine Learning**.

---

## 📖 Problem Statement

Imagine you work for a **real estate company**. Every day, customers ask:

> **"How much is my house worth?"**

Instead of manually estimating the price, you will build an **AI model** that learns from historical house sales and predicts the price of new houses.

---

## 🏡 Real-World Scenario

A housing company has collected the following historical sales data.

| House Size (sq ft) | Selling Price ($1000) |
|--------------------|----------------------:|
| 800 | 120 |
| 1000 | 150 |
| 1200 | 180 |
| 1500 | 220 |
| 1800 | 260 |
| 2000 | 300 |
| 2300 | 340 |
| 2500 | 360 |

This dataset will be used to train the Linear Regression model.

---

## 📊 Dataset Explanation

### Input Feature (X)

The **house size** measured in square feet.

```
House Size (sq ft)
```

### Target Variable (Y)

The **selling price** of the house.

```
House Price ($1000)
```

---

## 🤖 Machine Learning Goal

Train a model that learns the relationship

```
House Size  ─────────► House Price
```

Then use that model to predict prices for houses that have never been sold before.

---

## 📈 How Linear Regression Works

Linear Regression tries to find the **best-fit straight line** through the data.

```text
House Price
^

360 |                              ●
340 |                         ●
300 |                    ●
260 |                ●
220 |            ●
180 |        ●
150 |    ●
120 | ●
    +---------------------------------------->
      800   1200   1600   2000   2400

            Best Fit Regression Line
```

The red line represents the mathematical relationship between house size and price.

---

## 🧮 Mathematical Model

Linear Regression follows the equation

\[
Y = \beta_0 + \beta_1X
\]

Where

- **Y** = Predicted House Price
- **X** = House Size
- **β₀** = Intercept
- **β₁** = Slope (rate of change)

---

## 💡 Example Prediction

Suppose the trained model is

```text
Price = 20 + (0.14 × Size)
```

Predict the price of a **1600 sq ft** house.

```text
Price = 20 + (0.14 × 1600)

      = 20 + 224

      = 244
```

### ✅ Predicted Price

```
$244,000
```

---

## 🏢 Real-World Applications

Linear Regression is widely used in many industries.

| Industry | Example |
|-----------|---------|
| 🏠 Real Estate | House price prediction |
| 🚗 Automotive | Used car price estimation |
| 🏥 Healthcare | Predict medical expenses |
| 📈 Finance | Sales forecasting |
| ⚡ Energy | Electricity demand prediction |
| 🌾 Agriculture | Crop yield prediction |
| 🌦 Weather | Temperature forecasting |
| 🛒 Retail | Sales prediction |

---

## 🧠 Why Use Linear Regression?

- Easy to understand
- Fast to train
- Simple mathematical model
- Works well for continuous numerical values
- Excellent first algorithm for beginners

---

## 🎯 Expected Learning Outcome

After completing this exercise, students will be able to:

- Explain Linear Regression.
- Understand independent and dependent variables.
- Train a Linear Regression model.
- Predict house prices.
- Visualize the regression line.
- Evaluate model accuracy.
- Apply Linear Regression to real-world problems.