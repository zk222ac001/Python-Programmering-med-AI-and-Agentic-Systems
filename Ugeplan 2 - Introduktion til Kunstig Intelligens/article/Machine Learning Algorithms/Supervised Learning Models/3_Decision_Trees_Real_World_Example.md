# 🌳 Decision Trees in Machine Learning

> **Course:** Machine Learning with Python  
> **Topic:** Supervised Learning – Decision Trees  
> **Level:** Beginner to Intermediate  
> **Real-World Example:** 🏦 Bank Loan Approval

---

# 1. What is a Decision Tree?

A **Decision Tree** is a supervised Machine Learning algorithm that makes predictions by asking a sequence of questions.

It works similarly to how a human makes decisions.

For example:

```text
Should a bank approve a loan?

                Credit Score?
                     │
             ┌───────┴───────┐
             │               │
           < 650            >= 650
             │               │
             ▼               ▼
         ❌ Reject        Income?
                            │
                    ┌───────┴───────┐
                    │               │
                 < 40,000        >= 40,000
                    │               │
                    ▼               ▼
                ❌ Reject        Debt?
                                   │
                            ┌───────┴───────┐
                            │               │
                          High             Low
                            │               │
                            ▼               ▼
                        ❌ Reject       ✅ Approve
```

The model learns these decision rules automatically from historical data.

---

# 2. Decision Tree is Supervised Learning

A Decision Tree normally learns from examples where the correct answer is already known.

For example:

| Income | Credit Score | Debt | Loan Approved |
|---:|---:|---:|---|
| 30,000 | 580 | 20,000 | No |
| 45,000 | 670 | 10,000 | Yes |
| 60,000 | 720 | 5,000 | Yes |
| 25,000 | 610 | 18,000 | No |

The model sees:

```text
INPUT FEATURES
      │
      ├── Income
      ├── Credit Score
      ├── Debt
      └── Employment Years
             │
             ▼
      Decision Tree
             │
             ▼
       Loan Approved?
             │
        ┌────┴────┐
        ▼         ▼
       YES        NO
```

Because the correct answer is provided during training, it is called **supervised learning**.

---

# 3. Classification vs Regression

Decision Trees can solve **two different types of problems**.

## Classification

Classification predicts a category.

Examples:

```text
Loan Approved → Yes / No

Email → Spam / Not Spam

Patient → High Risk / Low Risk

Student → Pass / Fail
```

In Scikit-learn, we use:

```python
DecisionTreeClassifier
```

## Regression

Regression predicts a numerical value.

Examples:

```text
House Price → 2,500,000 DKK

Electricity Demand → 35,000 MWh

Salary → 55,000

Temperature → 18.5°C
```

In Scikit-learn, we use:

```python
DecisionTreeRegressor
```

For this example, we will use **classification**.

---

# 🏦 4. Real-World Example: Bank Loan Approval

Imagine you work as a **Machine Learning Engineer for a bank**.

The bank wants an AI model that helps determine whether a customer's loan application should be approved.

The historical dataset contains:

```text
Income
Credit Score
Debt
Employment Years
        │
        ▼
   Machine Learning
        │
        ▼
 Loan Approved
     Yes / No
```

---

# 5. Features and Target

We have four input features.

```text
X
│
├── Income
├── CreditScore
├── Debt
└── EmploymentYears
```

The target is:

```text
y
│
└── LoanApproved
```

Where:

```text
0 = Loan rejected
1 = Loan approved
```

---

# 6. Complete Python Code

```python
# ============================================================
# MACHINE LEARNING WITH PYTHON
# Decision Tree Classification
#
# Real-World Example:
# Predict Bank Loan Approval
# ============================================================

# STEP 1 - Install libraries if necessary
# pip install pandas matplotlib scikit-learn

# STEP 2 - Import libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# STEP 3 - Create dataset
data = {
    "Income": [
        30000, 45000, 60000, 25000, 70000,
        55000, 32000, 80000, 40000, 65000,
        28000, 90000, 50000, 35000, 75000,
        42000, 68000, 38000, 85000, 48000
    ],
    "CreditScore": [
        580, 670, 720, 610, 750,
        690, 600, 780, 640, 710,
        590, 800, 660, 620, 760,
        650, 730, 630, 790, 680
    ],
    "Debt": [
        20000, 10000, 5000, 18000, 4000,
        8000, 16000, 3000, 14000, 6000,
        19000, 2000, 11000, 15000, 3500,
        12000, 5000, 13000, 2500, 9000
    ],
    "EmploymentYears": [
        1, 4, 8, 2, 10,
        6, 2, 12, 3, 7,
        1, 15, 5, 2, 11,
        4, 9, 3, 14, 5
    ],
    "LoanApproved": [
        0, 1, 1, 0, 1,
        1, 0, 1, 0, 1,
        0, 1, 1, 0, 1,
        0, 1, 0, 1, 1
    ]
}

# STEP 4 - Convert to DataFrame
df = pd.DataFrame(data)

print("\n====================================")
print("        LOAN APPLICATION DATA")
print("====================================")
print(df)

# STEP 5 - Explore dataset
print("\nFirst five rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nStatistical Information:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# STEP 6 - Define X and y
X = df[[
    "Income",
    "CreditScore",
    "Debt",
    "EmploymentYears"
]]

y = df["LoanApproved"]

# STEP 7 - Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTotal records:", len(df))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# STEP 8 - Create Decision Tree
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

# STEP 9 - Train the model
model.fit(X_train, y_train)

print("\nDecision Tree trained successfully!")

# STEP 10 - Make predictions
y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

# STEP 11 - Actual vs Predicted
results = X_test.copy()
results["Actual"] = y_test
results["Predicted"] = y_pred

print("\nActual vs Predicted:")
print(results)

# STEP 12 - Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

# STEP 13 - Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# STEP 14 - Classification Report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)

# STEP 15 - Predict a new customer
new_customer = pd.DataFrame({
    "Income": [60000],
    "CreditScore": [720],
    "Debt": [5000],
    "EmploymentYears": [7]
})

prediction = model.predict(new_customer)

print("\nNew Customer:")
print(new_customer)

if prediction[0] == 1:
    print("\nPrediction: LOAN APPROVED")
else:
    print("\nPrediction: LOAN REJECTED")

# STEP 16 - Prediction probability
probability = model.predict_proba(new_customer)

print("\nPrediction Probabilities:")
print("Rejected:", probability[0][0])
print("Approved:", probability[0][1])

# STEP 17 - Visualize Decision Tree
plt.figure(figsize=(18, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Rejected", "Approved"],
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Decision Tree - Bank Loan Approval")
plt.tight_layout()
plt.show()
```

---

# 7. Understanding the Program

The complete Machine Learning process is:

```text
Historical Loan Data
        │
        ▼
┌─────────────────────────┐
│     Pandas DataFrame    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Define X and y          │
│                         │
│ X = Customer Data       │
│ y = Loan Approval       │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Train/Test Split        │
│                         │
│ 80% Train / 20% Test    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Decision Tree Training  │
│                         │
│ model.fit()             │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Make Predictions        │
│                         │
│ model.predict()         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Evaluate Model          │
│                         │
│ Accuracy                │
│ Confusion Matrix        │
│ Precision               │
│ Recall                  │
│ F1 Score                │
└─────────────────────────┘
```

---

# 8. What Does `DecisionTreeClassifier()` Do?

We create the model with:

```python
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
```

`DecisionTreeClassifier` tells Scikit-learn that we want to predict a **category**, not a continuous numerical value.

Our categories are:

```text
0 → Rejected
1 → Approved
```

---

# 9. What is `max_depth`?

```python
max_depth=3
```

limits how deep the tree is allowed to grow.

Without a limit, the tree can become very complicated:

```text
                        Question
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
          Question                   Question
          /      \                   /      \
       Question Question          Question Question
       /    \      /   \          /   \      /   \
      ...   ...   ...  ...       ...  ...   ...  ...
```

A very large tree can memorize the training data. This is called **overfitting**.

```text
Training Data
     │
     ▼
Very Complex Tree
     │
     ▼
Memorizes Training Data
     │
     ├── Excellent training accuracy
     │
     └── Poor new-data performance
```

Using `max_depth=3` helps control model complexity.

---

# 10. How Does the Tree Choose Questions?

Suppose the dataset contains:

```text
Income
Credit Score
Debt
Employment Years
```

The tree might ask:

```text
CreditScore <= 645?
```

The algorithm searches for a feature and threshold that best separate the classes.

Example:

```text
Credit Score

580 → Reject
590 → Reject
600 → Reject
610 → Reject
620 → Reject

670 → Approve
690 → Approve
720 → Approve
750 → Approve
780 → Approve
```

A split near `CreditScore = 645` may separate many rejected and approved applications.

---

# 11. Understanding a Decision Tree Node

A tree node may look like:

```text
CreditScore <= 645
gini = 0.49
samples = 16
value = [7, 9]
class = Approved
```

## `CreditScore <= 645`

This is the question:

```text
          CreditScore <= 645?
                │
        ┌───────┴───────┐
       YES              NO
        │                │
        ▼                ▼
  Left branch       Right branch
```

---

# 12. What Does `samples` Mean?

```text
samples = 16
```

means that **16 training observations reached this node**.

---

# 13. What Does `value` Mean?

```text
value = [7, 9]
```

means approximately:

```text
7 rejected applications
9 approved applications
```

Therefore:

```text
value = [Rejected, Approved]
```

---

# 14. What is Gini?

Gini measures how mixed the classes are.

Example:

```text
gini = 0.48
```

## Pure Node

```text
🟢 🟢 🟢 🟢 🟢
```

All observations belong to the same class.

```text
Gini = 0
```

## Mixed Node

```text
🟢 🔴 🟢 🔴 🔴 🟢
```

The classes are mixed, so the Gini value is higher.

The Decision Tree tries to create nodes that are as **pure as possible**.

---

# 15. Decision Process for a New Customer

Example new customer:

```text
Income            = 60,000
Credit Score      = 720
Debt              = 5,000
Employment Years  = 7
```

The tree may follow rules like:

```text
                     Credit Score > 645?
                              │
                             YES
                              │
                              ▼
                      Income > 45,000?
                              │
                             YES
                              │
                              ▼
                       Debt < 10,000?
                              │
                             YES
                              │
                              ▼
                       ✅ LOAN APPROVED
```

This is one reason Decision Trees are popular: their predictions can often be explained as a sequence of rules.

---

# 16. Understanding `model.fit()`

```python
model.fit(X_train, y_train)
```

means:

> **Learn from the training examples.**

Linear Regression learns something like:

```text
y = mx + b
```

A Decision Tree instead learns rules resembling:

```text
IF something
    THEN something
ELSE
    something else
```

---

# 17. Understanding `model.predict()`

```python
model.predict(X_test)
```

asks the trained model to classify new examples.

```text
New Applicant
      │
      ▼
Decision Tree
      │
      ▼
Questions
      │
      ▼
Leaf Node
      │
      ▼
Approved / Rejected
```

---

# 18. Prediction Probability

```python
model.predict_proba(new_customer)
```

may produce something like:

```text
Rejected: 0.10
Approved: 0.90
```

Conceptually:

```text
                       Probability

Rejected  ─────────────── 10%

Approved  ─────────────── 90%
```

The predicted class would therefore be:

```text
APPROVED
```

> ⚠️ With a tiny training dataset, these probabilities should not be treated as reliable real-world banking risk probabilities.

---

# 19. Accuracy

```python
accuracy = accuracy_score(
    y_test,
    y_pred
)
```

Suppose:

```text
10 applications tested

9 predictions correct
1 prediction incorrect
```

Then:

```text
Accuracy = 9 / 10 = 90%
```

---

# 20. Confusion Matrix

A confusion matrix is useful for classification problems.

Example:

```text
                PREDICTED

              Reject   Approve

ACTUAL Reject     8        2

       Approve    1        9
```

This means:

```text
8 rejected customers correctly identified

9 approved customers correctly identified

2 rejected customers incorrectly approved

1 approved customer incorrectly rejected
```

Different types of errors may have very different consequences in real applications.

---

# 21. Classification Metrics

The classification report includes:

```text
Precision
Recall
F1-score
```

## Precision

Precision asks:

> Of all applications predicted as approved, how many were actually approved?

```text
                    Correct Approvals
Precision = ──────────────────────────────
              All Predicted Approvals
```

## Recall

Recall asks:

> Of all applicants who should have been approved, how many did the model correctly identify?

```text
                 Correct Approvals
Recall = ─────────────────────────────
             All Actual Approvals
```

## F1 Score

F1 combines precision and recall.

```text
Precision
    +
Recall
    │
    ▼
 F1 Score
```

It is useful when both precision and recall matter.

---

# 22. Decision Tree vs Linear Regression

| Linear Regression | Decision Tree |
|---|---|
| Usually predicts numbers | Can classify or predict numbers |
| Learns an equation | Learns decision rules |
| Uses `y = mx + b` | Uses `if / else` style logic |
| Models a linear relationship | Can model nonlinear relationships |
| Uses slope and intercept | Uses branches and nodes |
| Example: Salary prediction | Example: Loan approval |

Conceptually:

```text
LINEAR REGRESSION

Experience
    │
    ▼
 y = mx + b
    │
    ▼
Salary
```

versus:

```text
DECISION TREE

Customer
   │
   ▼
Question 1
   │
   ▼
Question 2
   │
   ▼
Question 3
   │
   ▼
Approve / Reject
```

---

# 23. Real-World Applications

## 🏦 Banking

```text
Customer Data
      ↓
Credit Risk
      ↓
Loan Decision
```

## 🏥 Healthcare

```text
Symptoms
   ↓
Test Results
   ↓
Risk Category
```

## 🔐 Cybersecurity

```text
Network Traffic
      ↓
Suspicious Behavior?
      ↓
Attack / Normal
```

## 🛒 E-commerce

```text
Customer Behavior
       ↓
Purchase History
       ↓
Will Buy / Won't Buy
```

## 🎓 Education

```text
Attendance
Study Hours
Assignments
     │
     ▼
Decision Tree
     │
     ▼
Pass / Fail
```

---

# 24. Advantages of Decision Trees

- ✅ Easy to understand
- ✅ Easy to visualize
- ✅ Useful for classification
- ✅ Useful for regression
- ✅ Able to model nonlinear relationships
- ✅ Able to discover rules automatically
- ✅ Often interpretable
- ✅ Usually do not require feature scaling

---

# 25. Disadvantages of Decision Trees

- ❌ Can overfit
- ❌ Small changes in data may create a different tree
- ❌ Deep trees can become difficult to interpret
- ❌ A single tree may perform worse than ensemble models
- ❌ Small datasets can produce unreliable rules

This naturally leads to more advanced models:

```text
Decision Tree
      │
      ▼
Many Decision Trees
      │
      ▼
Random Forest
```

---

# 26. Simple Classroom Explanation

> A Decision Tree is a Machine Learning model that learns **if/else questions from historical data** and uses those questions to make predictions for new data.

Example:

```text
IF CreditScore > 650

    IF Income > 45,000

        IF Debt < 10,000

            APPROVE

        ELSE

            REJECT

    ELSE

        REJECT

ELSE

    REJECT
```

---

# 27. Traditional Programming vs Machine Learning

## Traditional Programming

```text
Rules + Data
      │
      ▼
    Answer
```

## Machine Learning

```text
Data + Historical Answers
          │
          ▼
    Learn the Rules
          │
          ▼
      New Prediction
```

---

# 🎓 28. Recommended Learning Sequence

```text
1. Linear Regression
       ↓
Predict a Number
       ↓
2. Decision Tree Classification
       ↓
Predict a Category
       ↓
3. Decision Tree Regression
       ↓
Predict a Number using Tree Rules
       ↓
4. Random Forest
       ↓
Combine Many Decision Trees
       ↓
5. Classification Metrics
       ↓
Accuracy / Precision / Recall / F1
```

---

# 💡 Suggested Classroom Exercise

A beginner-friendly exercise is **Student Pass/Fail Prediction**.

Possible input features:

- Study Hours
- Attendance
- Assignments Completed
- Previous Grade

Target:

```text
Pass / Fail
```

Conceptually:

```text
Study Hours
Attendance
Assignments
Previous Grade
      │
      ▼
Decision Tree
      │
      ▼
Pass / Fail
```

This example is easy for students to understand because they can immediately see how each branch of the tree affects the final prediction.

---

# ✅ Key Takeaway

```text
Historical Data
      │
      ▼
Learn Decision Rules
      │
      ▼
Decision Tree
      │
      ▼
New Input
      │
      ▼
Classification / Prediction
```

A Decision Tree differs from Linear Regression because it learns **decision rules and branches** rather than a single mathematical straight-line equation.
