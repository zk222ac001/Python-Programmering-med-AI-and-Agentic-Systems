# 🌲 Random Forest in Machine Learning

> **Course:** Machine Learning with Python  
> **Topic:** Supervised Learning – Random Forest  
> **Level:** Beginner to Intermediate  
> **Real-World Example:** 🏦 Bank Loan Approval  
> **Previous Model:** 🌳 Decision Tree

---

# 1. What is Random Forest?

A **Random Forest** is a Machine Learning algorithm that combines **many Decision Trees** instead of relying on only one tree.

The basic idea is:

```text
                    Customer Data
                         │
                         ▼
                ┌─────────────────┐
                │  Random Forest  │
                └────────┬────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     Decision Tree   Decision Tree   Decision Tree
          1              2              3
          │              │              │
          ▼              ▼              ▼
       Approve         Reject         Approve
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                     Majority Vote
                         │
                         ▼
                   ✅ APPROVED
```

Instead of trusting one Decision Tree, Random Forest asks **many trees** and combines their answers.

---

# 2. Why is it Called a "Forest"?

A single model is:

```text
🌳 Decision Tree
```

Many Decision Trees together become:

```text
🌳  🌳  🌳  🌳  🌳
     RANDOM FOREST
```

Therefore:

```text
One Tree
   │
   ▼
Decision Tree


Many Trees
   │
   ▼
Random Forest
```

---

# 3. Random Forest is Supervised Learning

Like Linear Regression and Decision Trees, Random Forest normally learns from data where the correct answers are already known.

For example:

| Income | Credit Score | Debt | Employment Years | Loan Approved |
|---:|---:|---:|---:|---|
| 30,000 | 580 | 20,000 | 1 | No |
| 45,000 | 670 | 10,000 | 4 | Yes |
| 60,000 | 720 | 5,000 | 8 | Yes |
| 25,000 | 610 | 18,000 | 2 | No |
| 70,000 | 750 | 4,000 | 10 | Yes |

The model receives:

```text
            INPUT FEATURES

Income
Credit Score
Debt
Employment Years
        │
        ▼
┌───────────────────────┐
│     Random Forest     │
└───────────┬───────────┘
            │
            ▼
      Loan Approved
        YES / NO
```

---

# 4. Classification and Regression

Random Forest can solve both problems.

## Classification

Predict a category:

```text
Loan → Approve / Reject

Email → Spam / Not Spam

Student → Pass / Fail

Traffic → Attack / Normal
```

Use:

```python
RandomForestClassifier
```

## Regression

Predict a numerical value:

```text
Salary → 65,000

House Price → 3,200,000 DKK

Electricity Demand → 34,500 MWh
```

Use:

```python
RandomForestRegressor
```

For this example we will use:

```python
RandomForestClassifier
```

---

# 🏦 5. Real-World Example: Loan Approval

Imagine that a bank wants to predict whether an applicant should receive a loan.

Input:

```text
Income
   │
Credit Score
   │
Debt
   │
Employment Years
   │
   ▼
Random Forest
   │
   ▼
Loan Approved?
   │
┌──┴──┐
▼     ▼
YES   NO
```

---

# 6. Decision Tree vs Random Forest

A Decision Tree uses one set of learned rules:

```text
Customer
   │
   ▼
Credit Score?
   │
   ▼
Income?
   │
   ▼
Debt?
   │
   ▼
Approved
```

Random Forest uses many trees:

```text
                    Customer

                       │
                       ▼

        ┌──────────────┼──────────────┐
        ▼              ▼              ▼

      Tree 1         Tree 2         Tree 3
        │              │              │
        ▼              ▼              ▼
     Approve         Approve         Reject

        └──────────────┼──────────────┘
                       ▼

                  Majority Vote

                       ▼

                    APPROVE
```

---

# 7. Complete Python Example

```python
# ============================================================
# MACHINE LEARNING WITH PYTHON
# Random Forest Classification
#
# Real-World Example:
# Predict Bank Loan Approval
# ============================================================


# ------------------------------------------------------------
# STEP 1 - Install libraries
# ------------------------------------------------------------
#
# pip install pandas matplotlib scikit-learn
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 2 - Import libraries
# ------------------------------------------------------------

# Data handling
import pandas as pd

# Graph visualization
import matplotlib.pyplot as plt

# Random Forest model
from sklearn.ensemble import RandomForestClassifier

# Train/test split
from sklearn.model_selection import train_test_split

# Evaluation
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# ============================================================
# STEP 3 - Create dataset
# ============================================================

data = {

    "Income": [
        30000, 45000, 60000, 25000, 70000,
        55000, 32000, 80000, 40000, 65000,
        28000, 90000, 50000, 35000, 75000,
        42000, 68000, 38000, 85000, 48000,
        58000, 33000, 72000, 52000, 95000,
        36000, 62000, 44000, 78000, 47000
    ],

    "CreditScore": [
        580, 670, 720, 610, 750,
        690, 600, 780, 640, 710,
        590, 800, 660, 620, 760,
        650, 730, 630, 790, 680,
        700, 605, 745, 675, 810,
        615, 715, 655, 770, 665
    ],

    "Debt": [
        20000, 10000, 5000, 18000, 4000,
        8000, 16000, 3000, 14000, 6000,
        19000, 2000, 11000, 15000, 3500,
        12000, 5000, 13000, 2500, 9000,
        7000, 17000, 4500, 9500, 1500,
        15500, 5500, 10500, 3000, 8500
    ],

    "EmploymentYears": [
        1, 4, 8, 2, 10,
        6, 2, 12, 3, 7,
        1, 15, 5, 2, 11,
        4, 9, 3, 14, 5,
        7, 2, 10, 5, 16,
        2, 8, 4, 12, 5
    ],

    "LoanApproved": [
        0, 1, 1, 0, 1,
        1, 0, 1, 0, 1,
        0, 1, 1, 0, 1,
        0, 1, 0, 1, 1,
        1, 0, 1, 1, 1,
        0, 1, 0, 1, 1
    ]
}


# ============================================================
# STEP 4 - Create Pandas DataFrame
# ============================================================

df = pd.DataFrame(data)


print("\n========================================")
print("          LOAN APPLICATION DATA")
print("========================================")

print(df)


# ============================================================
# STEP 5 - Explore dataset
# ============================================================

print("\n========================================")
print("            DATA EXPLORATION")
print("========================================")


print("\nFirst 5 rows:")
print(df.head())


print("\nDataset Shape:")
print(df.shape)


print("\nStatistical Information:")
print(df.describe())


print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# STEP 6 - Define X and y
# ============================================================

# X = Input features

X = df[[
    "Income",
    "CreditScore",
    "Debt",
    "EmploymentYears"
]]


# y = Target

y = df["LoanApproved"]


print("\n========================================")
print("             INPUT FEATURES")
print("========================================")

print(X.head())


print("\n========================================")
print("                 TARGET")
print("========================================")

print(y.head())


# ============================================================
# STEP 7 - Train/Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


print("\n========================================")
print("            TRAIN / TEST SPLIT")
print("========================================")


print("Total Records:", len(df))

print("Training Records:", len(X_train))

print("Testing Records:", len(X_test))


# ============================================================
# STEP 8 - Create Random Forest Model
# ============================================================

model = RandomForestClassifier(

    # Number of Decision Trees
    n_estimators=100,

    # Maximum depth of each tree
    max_depth=5,

    # Make results reproducible
    random_state=42
)


# ============================================================
# STEP 9 - Train Random Forest
# ============================================================

model.fit(
    X_train,
    y_train
)


print("\n========================================")
print("              MODEL TRAINING")
print("========================================")


print("Random Forest trained successfully!")


# ============================================================
# STEP 10 - Make Predictions
# ============================================================

y_pred = model.predict(
    X_test
)


print("\n========================================")
print("                PREDICTIONS")
print("========================================")


print(y_pred)


# ============================================================
# STEP 11 - Actual vs Predicted
# ============================================================

results = X_test.copy()


results["Actual"] = y_test

results["Predicted"] = y_pred


print("\n========================================")
print("          ACTUAL VS PREDICTED")
print("========================================")


print(results)


# ============================================================
# STEP 12 - Accuracy
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\n========================================")
print("             MODEL EVALUATION")
print("========================================")


print(
    f"Accuracy: {accuracy * 100:.2f}%"
)


# ============================================================
# STEP 13 - Confusion Matrix
# ============================================================

cm = confusion_matrix(
    y_test,
    y_pred
)


print("\nConfusion Matrix:")

print(cm)


# ============================================================
# STEP 14 - Classification Report
# ============================================================

print("\nClassification Report:")


print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# ============================================================
# STEP 15 - Predict New Customer
# ============================================================

new_customer = pd.DataFrame({

    "Income": [60000],

    "CreditScore": [720],

    "Debt": [5000],

    "EmploymentYears": [7]
})


prediction = model.predict(
    new_customer
)


print("\n========================================")
print("            NEW CUSTOMER")
print("========================================")


print(new_customer)


if prediction[0] == 1:

    print("\nPrediction: LOAN APPROVED")

else:

    print("\nPrediction: LOAN REJECTED")


# ============================================================
# STEP 16 - Prediction Probability
# ============================================================

probability = model.predict_proba(
    new_customer
)


print("\nPrediction Probability:")


print(
    f"Rejected: {probability[0][0] * 100:.2f}%"
)


print(
    f"Approved: {probability[0][1] * 100:.2f}%"
)


# ============================================================
# STEP 17 - Feature Importance
# ============================================================

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_
})


importance = importance.sort_values(

    by="Importance",

    ascending=False
)


print("\n========================================")
print("            FEATURE IMPORTANCE")
print("========================================")


print(importance)


# ============================================================
# STEP 18 - Plot Feature Importance
# ============================================================

plt.figure(
    figsize=(8, 5)
)


plt.bar(

    importance["Feature"],

    importance["Importance"]
)


plt.title(
    "Random Forest Feature Importance"
)


plt.xlabel(
    "Features"
)


plt.ylabel(
    "Importance"
)


plt.xticks(
    rotation=20
)


plt.grid(
    axis="y"
)


plt.tight_layout()


plt.show()
```

---

# 8. Understanding the Machine Learning Workflow

```text
Historical Data
       │
       ▼
┌──────────────────────┐
│ Pandas DataFrame     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Define X and y       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Train/Test Split     │
│                      │
│ 80% / 20%            │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Random Forest        │
│ Training             │
│                      │
│ model.fit()          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Prediction           │
│                      │
│ model.predict()      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Model Evaluation     │
│                      │
│ Accuracy             │
│ Precision            │
│ Recall               │
│ F1 Score             │
└──────────────────────┘
```

---

# 9. Creating the Random Forest

This line creates the model:

```python
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
```

There are three important parameters here.

---

# 10. What is `n_estimators`?

```python
n_estimators=100
```

means:

> Create **100 Decision Trees**.

Conceptually:

```text
Random Forest

Tree 1
Tree 2
Tree 3
Tree 4
Tree 5
...
Tree 100
```

Every tree makes its own prediction.

---

# 11. Majority Voting

Imagine only five trees:

```text
Tree 1 → APPROVE

Tree 2 → APPROVE

Tree 3 → REJECT

Tree 4 → APPROVE

Tree 5 → REJECT
```

Count the votes:

```text
APPROVE = 3

REJECT = 2
```

Therefore:

```text
Final Prediction
      │
      ▼
✅ APPROVE
```

For classification, this idea is commonly called **majority voting**.

---

# 12. Why Don't All Trees Learn Exactly the Same Thing?

If all 100 trees were identical:

```text
Tree 1 → same
Tree 2 → same
Tree 3 → same
...
```

there would be little advantage.

Random Forest introduces randomness.

Each tree is trained using different sampled observations and considers random subsets of features when choosing splits.

Conceptually:

```text
Original Dataset
       │
       ├───────────────┐
       │               │
       ▼               ▼

Sample A            Sample B
   │                    │
   ▼                    ▼

Tree 1               Tree 2
```

Another sample:

```text
Original Dataset
       │
       ▼

Sample C
       │
       ▼

Tree 3
```

Therefore the trees become different from one another.

---

# 13. Bootstrap Sampling

Random Forest commonly uses something called **bootstrap sampling**.

Suppose our original records are:

```text
A
B
C
D
E
```

One tree might receive:

```text
A
A
B
D
E
```

Another tree:

```text
B
C
C
D
E
```

Another:

```text
A
B
D
D
E
```

Notice that some records may appear more than once, and some may not appear in a tree's sample.

This creates diversity between trees.

---

# 14. Random Feature Selection

Random Forest also introduces randomness when choosing features.

Suppose we have:

```text
Income
Credit Score
Debt
Employment Years
```

Tree 1 might consider:

```text
Income
Debt
```

Tree 2 might consider:

```text
Credit Score
Employment Years
```

Tree 3 might consider:

```text
Income
Credit Score
```

This prevents all trees from relying on exactly the same feature at every split.

---

# 15. `model.fit()`

```python
model.fit(
    X_train,
    y_train
)
```

means:

> Train all the Decision Trees inside the Random Forest.

Conceptually:

```text
Training Dataset
      │
      ▼
Random Sampling
      │
      ├────────────┐
      ▼            ▼

   Dataset A    Dataset B
      │            │
      ▼            ▼

    Tree 1       Tree 2

      │
      ├─────────────── ...
      │
      ▼

    Tree 100
```

---

# 16. `model.predict()`

```python
model.predict(X_test)
```

asks every relevant tree to make a prediction.

Conceptually:

```text
New Customer
     │
     ▼

┌─────────┐
│ Tree 1  │ → YES
└─────────┘

┌─────────┐
│ Tree 2  │ → YES
└─────────┘

┌─────────┐
│ Tree 3  │ → NO
└─────────┘

       ...
        │
        ▼

     Voting
        │
        ▼

   Final Answer
```

---

# 17. Prediction Probability

We can use:

```python
model.predict_proba(new_customer)
```

Suppose the model produces:

```text
Rejected = 15%

Approved = 85%
```

Then:

```text
                  Random Forest

                        │
              ┌─────────┴──────────┐
              ▼                    ▼

         Rejected               Approved

            15%                    85%

                                    │
                                    ▼

                               ✅ APPROVED
```

For a classroom demonstration, this is useful for understanding model confidence-like outputs, although such probabilities should not automatically be interpreted as perfectly calibrated real-world probabilities.

---

# ⭐ 18. Feature Importance

One particularly useful feature of Random Forest is:

```python
model.feature_importances_
```

It can provide an estimate of which input features were most useful to the forest.

For example:

```text
CreditScore         0.43
Income              0.27
Debt                0.21
EmploymentYears     0.09
```

Conceptually:

```text
Feature Importance

Credit Score       ████████████████ 43%

Income             ██████████       27%

Debt               ████████         21%

Employment Years   ███               9%
```

The model may therefore be relying most strongly on:

```text
Credit Score
```

for this particular dataset.

---

# 19. What Does Feature Importance Mean?

Suppose:

```text
CreditScore = 0.43
```

This does **not** mean:

```text
CreditScore gives 43% accuracy
```

Instead, it indicates that CreditScore contributed relatively strongly to the tree splits across the forest according to the model's built-in importance measure.

---

# 20. Accuracy

We calculate:

```python
accuracy_score(
    y_test,
    y_pred
)
```

Imagine:

```text
100 customers
       │
       ▼

92 correctly predicted
8 incorrectly predicted
```

Then:

```text
Accuracy = 92%
```

---

# 21. Confusion Matrix

Example:

```text
                     PREDICTED

                 Reject     Approve

ACTUAL Reject      40          5

ACTUAL Approve      3         52
```

Interpretation:

```text
40 → correctly rejected

52 → correctly approved

5 → incorrectly approved

3 → incorrectly rejected
```

---

# 22. Precision

Precision asks:

> Of everyone predicted as approved, how many actually belonged to the approved class?

```text
                Correct Positive Predictions
Precision = ───────────────────────────────────
                 All Positive Predictions
```

---

# 23. Recall

Recall asks:

> Of all truly approved applications, how many did the model successfully identify?

```text
                 Correctly Identified Positives
Recall = ─────────────────────────────────────────
                    All Actual Positives
```

---

# 24. F1 Score

F1 balances:

```text
Precision
    │
    ├───────┐
    │       │
    ▼       ▼
          F1 Score
    ▲       ▲
    │       │
Recall ─────┘
```

It is particularly useful when relying on accuracy alone would be misleading.

---

# 25. What is `max_depth`?

```python
max_depth=5
```

controls the maximum depth of each Decision Tree.

Without limits:

```text
Tree
 │
 ├── Question
 │    ├── Question
 │    │    ├── Question
 │    │    │    ├── Question
 │    │    │    │    └── ...
```

A very deep tree can overfit.

Limiting tree depth helps control complexity.

---

# 26. Why Random Forest Usually Performs Better Than One Decision Tree

A single tree can make a poor decision.

For example:

```text
One Decision Tree

Applicant
    │
    ▼
Bad Split
    │
    ▼
Wrong Prediction
```

Random Forest reduces dependence on one tree:

```text
Tree 1 → Wrong

Tree 2 → Correct

Tree 3 → Correct

Tree 4 → Correct

Tree 5 → Wrong
          │
          ▼

Correct wins 3 vs 2
          │
          ▼
Final prediction = Correct
```

This averaging/voting behavior often makes Random Forest more robust.

---

# 27. Overfitting Comparison

## Decision Tree

```text
Training Data
     │
     ▼
Very Deep Tree
     │
     ▼
Memorization
     │
     ▼
Overfitting
```

## Random Forest

```text
Tree 1
Tree 2
Tree 3
...
Tree 100
    │
    ▼
Combine Predictions
    │
    ▼
More Stable Model
```

Random Forest can still overfit, but it is generally less prone to the instability of a single unrestricted tree.

---

# 28. Decision Tree vs Random Forest

| Feature | Decision Tree | Random Forest |
|---|---|---|
| Number of trees | 1 | Many |
| Easy to visualize | ✅ Very easy | ❌ Entire forest is difficult |
| Easy to explain | ✅ High | 🟡 Moderate |
| Accuracy | Often good | Often better |
| Overfitting risk | Higher | Usually lower |
| Training speed | Faster | Slower |
| Prediction speed | Faster | Slower |
| Feature importance | ✅ | ✅ |
| Ensemble model | ❌ | ✅ |

---

# 29. Linear Regression vs Decision Tree vs Random Forest

| Model | Main Purpose | Learning Style |
|---|---|---|
| Linear Regression | Predict number | Equation |
| Decision Tree | Classification / Regression | Decision rules |
| Random Forest | Classification / Regression | Many Decision Trees |

Conceptually:

```text
LINEAR REGRESSION

X
│
▼
Equation
│
▼
Number
```

```text
DECISION TREE

X
│
▼
Questions
│
▼
Prediction
```

```text
RANDOM FOREST

X
│
├────► Tree 1
├────► Tree 2
├────► Tree 3
├────► ...
└────► Tree 100
          │
          ▼
     Combined Result
```

---

# 30. Advantages of Random Forest

Random Forest provides several benefits:

- ✅ Often gives strong performance
- ✅ Works for classification
- ✅ Works for regression
- ✅ Handles nonlinear relationships
- ✅ Less sensitive than a single Decision Tree
- ✅ Can estimate feature importance
- ✅ Usually does not require feature scaling
- ✅ Handles multiple input features well
- ✅ Can model complicated relationships

---

# 31. Disadvantages

There are also disadvantages:

- ❌ More computationally expensive than one tree
- ❌ Requires more memory
- ❌ Harder to visualize
- ❌ Harder to explain than a single Decision Tree
- ❌ Feature importance can sometimes be misleading
- ❌ Many trees can make the model slower

---

# 32. Real-World Applications

## 🔐 Cybersecurity

```text
Network Traffic
       │
       ▼
Random Forest
       │
       ▼
Attack / Normal
```

## 🏦 Banking

```text
Customer Information
       │
       ▼
Random Forest
       │
       ▼
Credit Risk
```

## 🎓 Education

```text
Study Hours
Attendance
Grades
Assignments
      │
      ▼
Random Forest
      │
      ▼
Pass / Fail
```

## 🏭 Predictive Maintenance

```text
Temperature
Vibration
Pressure
Motor Speed
      │
      ▼
Random Forest
      │
      ▼
Machine Failure?
```

## ⚡ Energy

```text
Temperature
Wind Speed
Hour
Day
Historical Demand
       │
       ▼
Random Forest Regressor
       │
       ▼
Electricity Demand
```

This would also be an excellent extension of a Denmark electricity-demand assignment.

---

# 33. Simple Classroom Explanation

A simple way to explain Random Forest is:

> **One Decision Tree asks one expert. Random Forest asks many experts and uses their combined opinion.**

For example:

```text
Question:
Should we approve this loan?

Expert 1 → YES

Expert 2 → YES

Expert 3 → NO

Expert 4 → YES

Expert 5 → NO

          │
          ▼

      Majority Vote

          │
          ▼

      ✅ APPROVE
```

---

# 34. Traditional Decision Tree vs Random Forest

```text
Decision Tree

Customer
   │
   ▼
One Tree
   │
   ▼
Prediction
```

versus:

```text
Random Forest

Customer
   │
   ▼
Many Trees
   │
   ▼
Many Predictions
   │
   ▼
Voting / Averaging
   │
   ▼
Final Prediction
```

---

# 🎓 35. Recommended Teaching Sequence

```text
1️⃣ Linear Regression
        │
        ▼
Predict numerical values

        │
        ▼

2️⃣ Decision Tree
        │
        ▼
Learn IF / ELSE rules

        │
        ▼

3️⃣ Random Forest
        │
        ▼
Combine many Decision Trees

        │
        ▼

4️⃣ Classification Metrics
        │
        ▼
Accuracy
Precision
Recall
F1

        │
        ▼

5️⃣ Compare Models
```

---

# 💡 36. Suggested Student Assignment

## 🌲 Student Performance Prediction Using Random Forest

### Scenario

A university wants to identify whether students are likely to:

```text
PASS
```

or:

```text
FAIL
```

Use these features:

```text
Study Hours
Attendance
Assignments Completed
Previous Grade
Sleep Hours
```

Target:

```text
Pass / Fail
```

Machine Learning workflow:

```text
Student Data
      │
      ▼
Data Preparation
      │
      ▼
Train/Test Split
      │
      ▼
Random Forest
      │
      ▼
Prediction
      │
      ▼
Pass / Fail
      │
      ▼
Evaluate
```

Students could compare:

```text
Decision Tree
      VS
Random Forest
```

using:

```text
Accuracy
Precision
Recall
F1 Score
```

---

# ✅ Key Takeaway

```text
              RANDOM FOREST

                  Dataset
                     │
                     ▼
              Random Samples
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼

      Tree 1       Tree 2       Tree 3
        │            │            │
        ▼            ▼            ▼

   Prediction    Prediction    Prediction

        └────────────┼────────────┘
                     │
                     ▼

             Voting / Averaging

                     │
                     ▼

               Final Prediction
```

The most important difference to remember is:

```text
Decision Tree
      =
One Tree


Random Forest
      =
Many Decision Trees
      +
Random Sampling
      +
Combined Predictions
```

For a Machine Learning course, a strong progression is:

**Linear Regression → Decision Tree → Random Forest → Model Evaluation → Compare Algorithms.**
