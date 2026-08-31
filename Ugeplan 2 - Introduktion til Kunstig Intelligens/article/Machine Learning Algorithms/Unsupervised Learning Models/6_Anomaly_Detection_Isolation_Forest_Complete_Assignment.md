# 🚨 Unsupervised Learning: Network Anomaly Detection with Isolation Forest

> **Course:** Machine Learning with Python  
> **Topic:** Unsupervised Learning – Anomaly Detection  
> **Algorithm:** Isolation Forest  
> **Scenario:** Cybersecurity / Security Operations Center (SOC)  
> **Difficulty:** Beginner → Intermediate  
> **Estimated Duration:** 3–4 Hours

---

# 📚 Table of Contents

1. What is Anomaly Detection?
2. Why Use Unsupervised Learning?
3. Real-World SOC Scenario
4. What is Isolation Forest?
5. Why Is It Called Isolation Forest?
6. Realistic Cybersecurity Anomaly Examples
7. Dataset and Network Features
8. Complete Machine Learning Workflow
9. Complete Python Project
10. Python Code Explanation
11. Understanding `contamination`
12. Understanding `fit_predict()`
13. Understanding the Anomaly Score
14. Visual Interpretation of Normal vs Anomalous Traffic
15. SOC Investigation Workflow
16. Near-Real-Time Detection
17. Student Assignment Tasks
18. Classroom Investigation Table
19. Bonus SOC Alert Function
20. Discussion Questions
21. Suggested Grading Rubric
22. K-Means vs Anomaly Detection
23. Other Unsupervised Learning Assignment Ideas
24. Recommended Teaching Sequence
25. Key Takeaways

---

# 1. 🚨 What is Anomaly Detection?

**Anomaly Detection** is a Machine Learning technique used to identify observations that are significantly different from the majority of the data.

In cybersecurity, these unusual observations may indicate:

- Brute-force login attempts
- Port scanning
- Unusually large data transfers
- Malware communication
- Compromised devices
- Abnormal server behavior
- Network traffic spikes
- Suspicious user activity

The central question is:

```text
Is this activity behaving normally,
or is it unusually different?
```

Conceptually:

```text
Network Activity
      │
      ▼
Thousands of Events
      │
      ├── Normal
      ├── Normal
      ├── Normal
      ├── Normal
      └── ??? Unusual
               │
               ▼
        Anomaly Detection
```

---

# 2. 🧠 Why Use Unsupervised Learning?

In supervised classification, we normally have:

```text
X = Input Features

+

y = Known Correct Label
```

For example:

```text
Packets    Failed Logins    Label

120        0                Normal
900        45               Attack
```

However, in a real-world cybersecurity environment, we often do **not** know in advance which events are malicious.

We may only have:

```text
Packets
Bytes Transferred
Failed Logins
Ports Accessed
Connection Duration
```

There may be:

```text
❌ No known y
```

Therefore, anomaly detection is often approached using **unsupervised learning**.

```text
Network Measurements
         │
         ▼
       X only
         │
         ▼
Isolation Forest
         │
         ▼
Find unusual observations
```

---

# 3. 🏢 Real-World Scenario: Security Operations Center

Imagine that you work as a **Machine Learning Engineer in a Security Operations Center (SOC)**.

Your company has:

```text
Employee Computers
Servers
Routers
IoT Devices
Databases
Cloud Services
```

Every minute, these systems produce network activity.

Most of this activity is normal:

```text
Employee opens Outlook
        │
        ▼
Normal network connection

Employee opens a website
        │
        ▼
Normal network traffic

Server communicates with database
        │
        ▼
Normal network traffic
```

But occasionally something unusual happens.

Example:

```text
45 failed login attempts
        │
        ▼
Possible brute-force attack
```

Another example:

```text
One computer accesses 150 ports
        │
        ▼
Possible port scanning
```

Another:

```text
1.2 GB suddenly transferred
        │
        ▼
Possible data exfiltration
```

Another:

```text
1,400 packets/minute
        │
        ▼
Possible malicious traffic spike
```

The SOC team cannot manually inspect thousands of events every minute.

Your task is therefore to build an **AI-based anomaly detection system**.

---

# 4. 🎯 Business Problem

Your system should answer one important question:

```text
Is this network activity NORMAL
or unusually different?
```

The overall system is:

```text
                  COMPANY NETWORK

                        │
                        ▼

              Network Activity Logs

                        │
                        ▼

             ┌────────────────────┐
             │ Machine Learning   │
             │ Anomaly Detection  │
             └─────────┬──────────┘
                       │
                ┌──────┴──────┐
                │             │
                ▼             ▼

             NORMAL        ANOMALY
                              │
                              ▼
                        SOC Investigation
```

---

# 5. 🌲 What is Isolation Forest?

**Isolation Forest** is an algorithm designed specifically to identify unusual observations.

Its central idea is:

> **Anomalies are different from most observations and are usually easier to isolate.**

Imagine normal network events:

```text
             Normal Network Activity

        ● ● ● ●
      ● ● ● ● ●
       ● ● ● ●
         ● ●


                                      X
                                      ↑
                                  Anomaly
```

Where:

```text
● = Normal activity

X = Possible anomaly
```

The unusual point is separated from the majority of observations.

---

# 6. 🌳 Why Is It Called "Isolation Forest"?

Isolation Forest uses many trees.

Unlike a normal Decision Tree, which asks:

```text
What class does this record belong to?
```

Isolation Forest asks:

```text
How easily can this observation be isolated?
```

Consider normal data:

```text
NORMAL DATA

● ● ● ● ● ● ●
● ● ● ● ● ● ●
● ● ● ● ● ●
```

A normal observation may require many splits:

```text
Question
   │
   ▼
Question
   │
   ▼
Question
   │
   ▼
Question
   │
   ▼
Finally isolated
```

An unusual observation:

```text
                         X
```

may be separated quickly:

```text
Question
   │
   ├──────────── Normal data
   │
   └──────────── X
                 │
                 ▼
             Isolated!
```

Therefore:

```text
Few splits needed
       │
       ▼
Likely anomaly
```

while:

```text
Many splits needed
       │
       ▼
Likely normal
```

---

# 7. 🔍 Normal Activity vs Anomaly

Suppose most computers produce values in a common range:

```text
Network Activity
     ▲

High │
     │                                X
     │
     │
     │       ● ● ●
     │     ● ● ● ●
     │      ● ● ●
Low  │
     └────────────────────────────────────►
                Network Features
```

Here:

```text
● = Typical activity

X = Unusual activity
```

A classification model asks:

```text
What known class does X belong to?
```

Anomaly detection instead asks:

```text
How different is X
from the majority of observations?
```

---

# 8. 📊 Network Features

For this assignment, every network event contains:

| Feature | Meaning |
|---|---|
| `PacketsPerMinute` | Number of network packets per minute |
| `BytesTransferredMB` | Amount of data transferred |
| `FailedLogins` | Number of failed login attempts |
| `UniquePorts` | Number of different ports accessed |
| `ConnectionDurationSec` | Connection duration in seconds |

These features give the model several perspectives on network behavior.

---

# 9. ✅ Example of Normal Activity

A normal employee computer might produce:

```text
Packets/minute        = 125
Transferred data      = 42 MB
Failed logins         = 0
Ports accessed        = 4
Connection duration   = 80 sec
```

Nothing looks especially unusual.

Conceptually:

```text
NORMAL USER

Packets        125
Failed Login     0
Ports            4
Data            42 MB

        │
        ▼
Values near normal range
        │
        ▼
✅ NORMAL
```

---

# 10. 🚨 Example: Brute-Force-Like Activity

Consider:

```text
Packets/minute        = 260
Transferred data      = 18 MB
Failed logins         = 45
Ports accessed        = 2
Connection duration   = 20 sec
```

The suspicious characteristic is:

```text
45 FAILED LOGINS
```

Possible interpretation:

```text
Username / Password Attempts
          │
          ▼
Repeated Failures
          │
          ▼
Possible Brute-Force Attack
```

Visual comparison:

```text
Normal Range
     │
     ▼
0–2 failed logins


Suspicious Event
     │
     ▼
45 failed logins
```

---

# 11. 🚨 Example: Port-Scan-Like Activity

Consider:

```text
Packets/minute        = 700
Transferred data      = 12 MB
Failed logins         = 1
Ports accessed        = 150
Connection duration   = 8 sec
```

This is unusual because:

```text
Normal User
     │
     ▼
3–5 ports


Possible Scanner
     │
     ▼
150 ports
```

Conceptually:

```text
PORT-SCAN-LIKE EVENT

Packets        700
Failed Login     1
Ports          150   ◀ extremely unusual
Data            12 MB

        │
        ▼
One machine interacts
with many different ports
        │
        ▼
🚨 ANOMALY
```

---

# 12. 🚨 Example: Possible Data Exfiltration

Consider:

```text
Packets/minute        = 310
Transferred data      = 1,200 MB
Failed logins         = 0
Ports accessed        = 4
Connection duration   = 1,800 sec
```

Possible interpretation:

```text
Large Amount of Data
        │
        ▼
Unusually Long Connection
        │
        ▼
Possible Data Exfiltration
```

But the model does **not** know that this is an attack.

It only detects:

> This event looks very different from normal network behavior.

---

# 13. 🔄 Complete Machine Learning Workflow

```text
                    NETWORK LOGS
                         │
                         ▼
               ┌───────────────────┐
               │ Pandas DataFrame  │
               └─────────┬─────────┘
                         │
                         ▼
               Data Exploration
                         │
                         ▼
               Select ML Features
                         │
                         ▼
                Isolation Forest
                         │
                         ▼
               Calculate Anomaly
                    Scores
                         │
                  ┌──────┴───────┐
                  │              │
                  ▼              ▼
               Normal         Anomaly
                                  │
                                  ▼
                           SOC Investigation
```

Another architectural view:

```text
                     🌐 NETWORK
                         │
                         ▼
                  Network Telemetry
                         │
                         ▼
                ┌─────────────────┐
                │ Pandas / Python │
                └────────┬────────┘
                         │
                         ▼
                  Select Features
                         │
                         ▼
          ┌────────────────────────────┐
          │     ISOLATION FOREST       │
          │                            │
          │ Learn common behavior      │
          │ Find easy-to-isolate data  │
          └──────────────┬─────────────┘
                         │
                ┌────────┴────────┐
                ▼                 ▼
            ✅ Normal         🚨 Anomaly
                                  │
                                  ▼
                         Calculate Priority
                         / Anomaly Score
                                  │
                                  ▼
                           SOC Investigation
                                  │
                      ┌───────────┼────────────┐
                      ▼           ▼            ▼
                   Benign     Misconfiguration   Security
                   Event                         Incident
```

---

# 14. 💻 Complete Python Project

```python
# ============================================================
# UNSUPERVISED MACHINE LEARNING
#
# Real-World Cybersecurity Project
#
# NETWORK ANOMALY DETECTION
# USING ISOLATION FOREST
# ============================================================


# ------------------------------------------------------------
# STEP 1 - Install libraries if required
# ------------------------------------------------------------
#
# Run in terminal:
#
# pip install pandas numpy matplotlib scikit-learn
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 2 - Import libraries
# ------------------------------------------------------------

# Work with tables and datasets
import pandas as pd

# Generate numerical sample data
import numpy as np

# Create graphs
import matplotlib.pyplot as plt

# Machine Learning anomaly detection algorithm
from sklearn.ensemble import IsolationForest


# ============================================================
# STEP 3 - Make Results Reproducible
# ============================================================

np.random.seed(42)


# ============================================================
# STEP 4 - Create Normal Network Activity
# ============================================================

number_of_normal_events = 120


# Create timestamps
timestamps = pd.date_range(
    start="2026-08-31 08:00:00",
    periods=number_of_normal_events,
    freq="min"
)


normal_data = pd.DataFrame({

    "Timestamp": timestamps,

    # Normally around 140 packets/minute
    "PacketsPerMinute":
        np.random.normal(
            140,
            20,
            number_of_normal_events
        ).clip(70, 220).astype(int),

    # Normally around 45 MB
    "BytesTransferredMB":
        np.random.normal(
            45,
            10,
            number_of_normal_events
        ).clip(10, 90).round(2),

    # Usually 0 or very few failed logins
    "FailedLogins":
        np.random.poisson(
            0.5,
            number_of_normal_events
        ),

    # Usually only a few different ports
    "UniquePorts":
        np.random.poisson(
            4,
            number_of_normal_events
        ) + 1,

    # Typical connection duration
    "ConnectionDurationSec":
        np.random.normal(
            75,
            20,
            number_of_normal_events
        ).clip(10, 160).round(1)
})


# ============================================================
# STEP 5 - Create Suspicious Network Events
# ============================================================

anomaly_data = pd.DataFrame({

    "Timestamp": pd.date_range(
        start="2026-08-31 10:00:00",
        periods=6,
        freq="min"
    ),

    "PacketsPerMinute": [
        260,     # Possible brute force
        700,     # Possible port scan
        310,     # Possible data exfiltration
        1400,    # Massive traffic spike
        450,     # Suspicious lateral activity
        100      # Long unusual connection
    ],

    "BytesTransferredMB": [
        18,
        12,
        1200,
        600,
        220,
        900
    ],

    "FailedLogins": [
        45,
        1,
        0,
        0,
        12,
        0
    ],

    "UniquePorts": [
        2,
        150,
        4,
        20,
        60,
        3
    ],

    "ConnectionDurationSec": [
        20,
        8,
        1800,
        15,
        300,
        3600
    ]
})


# ============================================================
# STEP 6 - Combine Normal and Suspicious Events
# ============================================================

df = pd.concat(
    [
        normal_data,
        anomaly_data
    ],
    ignore_index=True
)


print("\n========================================")
print("            NETWORK DATA")
print("========================================")

print(df)


# ============================================================
# STEP 7 - Explore Dataset
# ============================================================

print("\n========================================")
print("            DATA EXPLORATION")
print("========================================")


print("\nFirst 5 rows:")

print(
    df.head()
)


print("\nLast 10 rows:")

print(
    df.tail(10)
)


print("\nDataset Shape:")

print(
    df.shape
)


print("\nStatistical Information:")

print(
    df.describe()
)


print("\nMissing Values:")

print(
    df.isnull().sum()
)


# ============================================================
# STEP 8 - Select Machine Learning Features
# ============================================================

features = [

    "PacketsPerMinute",

    "BytesTransferredMB",

    "FailedLogins",

    "UniquePorts",

    "ConnectionDurationSec"
]


X = df[features]


print("\n========================================")
print("            ML FEATURES")
print("========================================")

print(
    X.head()
)


# ============================================================
# STEP 9 - Create Isolation Forest
# ============================================================

model = IsolationForest(

    # Number of Isolation Trees
    n_estimators=200,

    # We expect approximately 5% unusual activity
    contamination=0.05,

    # Make results reproducible
    random_state=42
)


# ============================================================
# STEP 10 - Train Model and Detect Anomalies
# ============================================================

df["Prediction"] = model.fit_predict(
    X
)


# ============================================================
# STEP 11 - Convert Prediction to Human-Friendly Labels
# ============================================================

# Isolation Forest returns:
#
#  1  = Normal
# -1  = Anomaly

df["Status"] = df["Prediction"].map({

    1: "Normal",

    -1: "Anomaly"
})


# ============================================================
# STEP 12 - Calculate Anomaly Score
# ============================================================

df["AnomalyScore"] = model.decision_function(
    X
)


# Lower scores generally indicate
# more unusual observations.


# ============================================================
# STEP 13 - Display Complete Results
# ============================================================

print("\n========================================")
print("        ANOMALY DETECTION RESULTS")
print("========================================")

print(
    df[
        [
            "Timestamp",
            "PacketsPerMinute",
            "BytesTransferredMB",
            "FailedLogins",
            "UniquePorts",
            "ConnectionDurationSec",
            "Status",
            "AnomalyScore"
        ]
    ]
)


# ============================================================
# STEP 14 - Display Only Detected Anomalies
# ============================================================

anomalies = df[
    df["Status"] == "Anomaly"
]


print("\n========================================")
print("          DETECTED ANOMALIES")
print("========================================")

print(
    anomalies
)


# ============================================================
# STEP 15 - Sort by Most Suspicious
# ============================================================

most_suspicious = df.sort_values(
    by="AnomalyScore"
)


print("\n========================================")
print("       MOST SUSPICIOUS EVENTS")
print("========================================")

print(
    most_suspicious[
        [
            "Timestamp",
            "PacketsPerMinute",
            "BytesTransferredMB",
            "FailedLogins",
            "UniquePorts",
            "ConnectionDurationSec",
            "AnomalyScore",
            "Status"
        ]
    ].head(10)
)


# ============================================================
# STEP 16 - Visualize Failed Logins vs Ports
# ============================================================

normal_events = df[
    df["Status"] == "Normal"
]


anomaly_events = df[
    df["Status"] == "Anomaly"
]


plt.figure(
    figsize=(10, 6)
)


plt.scatter(

    normal_events["FailedLogins"],

    normal_events["UniquePorts"],

    label="Normal"
)


plt.scatter(

    anomaly_events["FailedLogins"],

    anomaly_events["UniquePorts"],

    marker="X",

    s=180,

    label="Anomaly"
)


plt.title(
    "Network Anomaly Detection"
)


plt.xlabel(
    "Failed Login Attempts"
)


plt.ylabel(
    "Unique Ports Accessed"
)


plt.grid(True)


plt.legend()


plt.tight_layout()


plt.show()


# ============================================================
# STEP 17 - Visualize Traffic Over Time
# ============================================================

plt.figure(
    figsize=(12, 6)
)


plt.plot(

    df["Timestamp"],

    df["PacketsPerMinute"],

    label="Packets Per Minute"
)


plt.scatter(

    anomaly_events["Timestamp"],

    anomaly_events["PacketsPerMinute"],

    marker="X",

    s=150,

    label="Detected Anomaly"
)


plt.title(
    "Network Traffic Over Time"
)


plt.xlabel(
    "Time"
)


plt.ylabel(
    "Packets Per Minute"
)


plt.xticks(
    rotation=45
)


plt.grid(True)


plt.legend()


plt.tight_layout()


plt.show()


# ============================================================
# STEP 18 - Test a New Incoming Network Event
# ============================================================

new_event = pd.DataFrame({

    "PacketsPerMinute": [850],

    "BytesTransferredMB": [500],

    "FailedLogins": [35],

    "UniquePorts": [100],

    "ConnectionDurationSec": [25]
})


# ============================================================
# STEP 19 - Predict New Event
# ============================================================

new_prediction = model.predict(
    new_event
)[0]


new_score = model.decision_function(
    new_event
)[0]


print("\n========================================")
print("           NEW NETWORK EVENT")
print("========================================")


print(
    new_event
)


if new_prediction == -1:

    print(
        "\n🚨 ALERT: ANOMALOUS NETWORK ACTIVITY"
    )

else:

    print(
        "\n✅ Network activity appears NORMAL"
    )


print(
    f"Anomaly Score: {new_score:.4f}"
)
```

---

# 15. 🔍 Python Code Explanation

## `import pandas as pd`

```python
import pandas as pd
```

Pandas is used to:

- Create DataFrames
- Store network logs
- Select features
- Add prediction columns
- Filter anomalies
- Sort events

Conceptually:

```text
Raw Network Measurements
        │
        ▼
    Pandas DataFrame
        │
        ▼
Structured Table
```

---

# 16. Why Use NumPy?

```python
import numpy as np
```

NumPy helps generate realistic synthetic network traffic.

For example:

```python
np.random.normal(
    140,
    20,
    120
)
```

means approximately:

```text
Generate 120 values

Average ≈ 140

Variation ≈ 20
```

This produces data such as:

```text
132
145
121
160
138
149
...
```

instead of:

```text
140
140
140
140
140
```

Real systems naturally vary.

---

# 17. Why Use `np.random.seed(42)`?

```python
np.random.seed(42)
```

makes the generated data reproducible.

Without a fixed seed:

```text
Run 1 → Different data

Run 2 → Different data

Run 3 → Different data
```

With:

```python
np.random.seed(42)
```

students get the same random sequence each time.

This makes classroom demonstrations easier to reproduce.

---

# 18. Creating Normal Network Activity

Example:

```python
"PacketsPerMinute":
    np.random.normal(
        140,
        20,
        number_of_normal_events
    )
```

This means:

> Normal network activity is centered around approximately 140 packets per minute, with natural variation.

Conceptually:

```text
Normal Activity

128
145
151
119
139
163
...
```

---

# 19. Creating Suspicious Events

The example deliberately introduces unusual observations.

For example:

```python
"FailedLogins": [
    45,
    1,
    0,
    0,
    12,
    0
]
```

One event has:

```text
45 failed logins
```

while normal systems may have:

```text
0
1
occasionally 2
```

This makes that observation easier for Isolation Forest to isolate.

---

# 20. Why Use Several Features?

Imagine looking only at:

```text
FailedLogins
```

A data-exfiltration event might have:

```text
FailedLogins = 0
```

and would appear normal.

But if we also examine:

```text
BytesTransferred = 1200 MB

Connection Duration = 1800 sec
```

the event becomes unusual.

Therefore:

```python
features = [
    "PacketsPerMinute",
    "BytesTransferredMB",
    "FailedLogins",
    "UniquePorts",
    "ConnectionDurationSec"
]
```

allows the model to consider several dimensions of behavior at the same time.

---

# 21. Understanding One Network Event as a Feature Vector

A single network event can be represented as:

```text
                    ONE NETWORK EVENT

                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
      Packets            Data             Logins
         │                 │                 │
         ├─────────────────┼─────────────────┤
                           │
                    Ports + Duration
                           │
                           ▼
                 Numerical Feature Vector
                           │
                           ▼
                    Isolation Forest
```

For example:

```python
new_event = pd.DataFrame({
    "PacketsPerMinute": [850],
    "BytesTransferredMB": [500],
    "FailedLogins": [35],
    "UniquePorts": [100],
    "ConnectionDurationSec": [25]
})
```

can be interpreted as:

```text
New Event
   │
   ├── Packets ............... 850
   ├── Data .................. 500 MB
   ├── Failed Logins ......... 35
   ├── Ports ................. 100
   └── Duration .............. 25 sec
                │
                ▼
         Isolation Forest
                │
                ▼
        Unusual compared
        with normal data
                │
                ▼
           🚨 ANOMALY
```

---

# 22. Why Don't We Use `Timestamp` as a Feature?

`Timestamp` provides context:

```text
When did the event happen?
```

For this beginner model, it is not directly used as an anomaly-detection feature.

It is useful later for investigation:

```text
08:12 → Normal

09:35 → Normal

10:03 → Anomaly
```

In an advanced project, students could derive:

```text
Hour of Day
Day of Week
Weekend
Night-Time Activity
Business Hours / Non-Business Hours
```

---

# 23. Creating the Isolation Forest

```python
model = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)
```

This is the central Machine Learning object.

---

# 24. 🌲 Understanding `n_estimators=200`

```python
n_estimators=200
```

means:

```text
Create 200 Isolation Trees
```

Conceptually:

```text
Network Data
     │
     ├────────► Tree 1
     ├────────► Tree 2
     ├────────► Tree 3
     ├────────► ...
     └────────► Tree 200
                   │
                   ▼
             Combined Result
```

Using many trees produces a more stable anomaly estimate than relying on one tree.

---

# 25. 🚨 Understanding `contamination`

```python
contamination=0.05
```

roughly means:

> The model is configured to expect approximately 5% of observations to be anomalous.

For:

```text
100 events
```

the assumption is approximately:

```text
95 normal
5 unusual
```

Visual:

```text
100 Network Events
        │
        ├────────────────────── 95 expected normal
        │
        └──── 5 expected unusual
```

It does **not** mean:

```text
5% of traffic is definitely malicious
```

Students should experiment with:

```python
contamination=0.01
```

```python
contamination=0.03
```

```python
contamination=0.05
```

```python
contamination=0.10
```

```python
contamination=0.20
```

and observe how the number of flagged observations changes.

---

# 26. Understanding `random_state=42`

```python
random_state=42
```

helps make the model reproducible.

It means students running the same code are more likely to receive the same result.

The value `42` is not special.

It could also be:

```python
random_state=1
```

or:

```python
random_state=100
```

The important point is that a fixed value makes the random parts reproducible.

---

# 27. Understanding `fit_predict()`

This line:

```python
df["Prediction"] = model.fit_predict(X)
```

performs two steps:

```text
                  fit_predict()

             ┌─────────┴─────────┐
             ▼                   ▼
            FIT               PREDICT

       Learn structure      Decide which
       of the dataset       observations
                            look unusual
             │                   │
             └─────────┬─────────┘
                       ▼
                 Final Result
```

Isolation Forest returns:

```text
 1 = Normal

-1 = Anomaly
```

---

# 28. Making Predictions Human-Friendly

We convert:

```text
1
-1
```

to:

```text
Normal
Anomaly
```

using:

```python
df["Status"] = df["Prediction"].map({
    1: "Normal",
    -1: "Anomaly"
})
```

Now:

```text
Prediction     Status

    1          Normal

    1          Normal

   -1          Anomaly
```

This is easier for a SOC analyst to read.

---

# 29. 📉 Understanding the Anomaly Score

We calculate:

```python
df["AnomalyScore"] = model.decision_function(X)
```

This gives more information than a simple:

```text
Normal / Anomaly
```

A simplified interpretation is:

```text
More suspicious                       More normal

-0.40      -0.20       0       +0.10       +0.30
  │           │        │          │            │
  ▼           ▼        ▼          ▼            ▼
Very       Unusual   Boundary    Normal      More
Unusual                                      Normal
```

Within a fitted model:

```text
Lower decision-function score
        │
        ▼
Generally more unusual
```

while:

```text
Higher / more positive score
        │
        ▼
Generally more normal
```

This allows analysts to rank alerts.

---

# 30. Sorting the Most Suspicious Events

```python
most_suspicious = df.sort_values(
    by="AnomalyScore"
)
```

Conceptually:

```text
Priority 1 → Most unusual

Priority 2 → Next most unusual

Priority 3 → Next

...
```

This is closer to a real SOC workflow because analysts often need to prioritize alerts.

---

# 31. 📈 Visualizing Failed Logins vs Ports

One useful graph compares:

```text
X-axis → Failed Login Attempts

Y-axis → Unique Ports Accessed
```

Conceptually:

```text
Unique Ports
    ▲

160 │                              X
140 │
120 │
100 │
 80 │
 60 │
 40 │
 20 │
  5 │  ● ● ● ● ●
    └────────────────────────────────►
           Failed Logins
```

Where:

```text
● = Normal

X = Anomaly
```

This can make port-scanning or authentication anomalies visually obvious.

---

# 32. 📈 Visualizing Traffic Over Time

Another useful graph is:

```text
Time
  │
  ▼
Packets Per Minute
```

Conceptually:

```text
Packets
   ▲

1400│                           X
1200│
1000│
 800│
 600│                 X
 400│
 200│ ● ● ● ● ● ● ●
    └────────────────────────────► Time
```

This helps students see traffic spikes.

---

# 33. 🛡️ Important Security Principle

The Machine Learning system should **not** automatically say:

```text
ANOMALY = HACKER
```

Instead:

```text
Machine Learning
      │
      ▼
Anomaly Detected
      │
      ▼
Generate Alert
      │
      ▼
SOC Analyst Investigates
      │
      ├── Legitimate unusual activity?
      │
      └── Possible security incident?
```

An anomaly may be caused by:

```text
Software Update

Large Backup

Administrator Maintenance

Network Testing

New Application

Misconfiguration

Security Scan

Actual Cyberattack
```

Therefore:

> **Anomaly ≠ confirmed attack**

Instead:

> **Anomaly = unusual behavior that deserves investigation.**

---

# 34. ⚡ Near-Real-Time Detection

The project can also test a newly arriving event:

```python
new_event = pd.DataFrame({
    "PacketsPerMinute": [850],
    "BytesTransferredMB": [500],
    "FailedLogins": [35],
    "UniquePorts": [100],
    "ConnectionDurationSec": [25]
})
```

Conceptually:

```text
New Network Event
        │
        ▼
850 packets/minute
500 MB transferred
35 failed logins
100 ports
        │
        ▼
Isolation Forest
        │
        ▼
🚨 ANOMALY
```

A production-style architecture might be:

```text
                    Routers
                      │
                    Firewall
                      │
                    Servers
                      │
                  Endpoints
                      │
                      ▼
             Network Telemetry
                      │
                      ▼
             Log Collection System
                      │
                      ▼
             Feature Extraction
                      │
                      ▼
            ┌────────────────────┐
            │ Isolation Forest   │
            └─────────┬──────────┘
                      │
               ┌──────┴──────┐
               ▼             ▼
            Normal        Suspicious
                              │
                              ▼
                         SOC Alert
                              │
                              ▼
                       Human Analyst
```

---

# 35. 🧪 Classroom Investigation Task

After running the program, students should investigate each detected anomaly as junior SOC analysts.

A useful report table is:

| Time | Packets | Failed Logins | Ports | Data MB | Model Result | Possible Explanation |
|---|---:|---:|---:|---:|---|---|
| 10:00 | 260 | 45 | 2 | 18 | Anomaly | Possible brute force |
| 10:01 | 700 | 1 | 150 | 12 | Anomaly | Possible port scan |
| 10:02 | 310 | 0 | 4 | 1200 | Anomaly | Possible data exfiltration |
| 10:03 | 1400 | 0 | 20 | 600 | Anomaly | Traffic spike |
| 10:04 | 450 | 12 | 60 | 220 | Anomaly | Possible lateral activity |
| 10:05 | 100 | 0 | 3 | 900 | Anomaly | Long unusual connection |

Students should explain their reasoning instead of only copying the model output.

---

# 36. 🧠 Student Hypothesis Before Running the Model

Give students events like these:

| Event | Packets | Data MB | Failed Logins | Ports | Student Decision |
|---|---:|---:|---:|---:|---|
| A | 125 | 38 | 0 | 3 | ? |
| B | 280 | 15 | 55 | 2 | ? |
| C | 650 | 12 | 1 | 145 | ? |
| D | 300 | 1,400 | 0 | 4 | ? |
| E | 145 | 42 | 1 | 5 | ? |

Before running Python, students should predict:

```text
Normal?
or
Anomaly?
```

Then:

```text
Student Hypothesis
       │
       ▼
Run Python Model
       │
       ▼
Compare Result
       │
       ▼
Explain Differences
```

This turns the assignment into analytical work instead of simply running code.

---

# 37. 🎯 Student Assignment Tasks

Students should complete the following work:

1. Create or load the network dataset.
2. Explore the dataset using Pandas.
3. Explain each security-related feature.
4. Select the Machine Learning features.
5. Create an Isolation Forest model.
6. Train the model using `fit_predict()`.
7. Convert `1` and `-1` predictions into readable labels.
8. Calculate anomaly scores.
9. Rank the most unusual events.
10. Visualize anomalies.
11. Investigate each flagged observation.
12. Create at least three new network events.
13. Predict whether each new event is normal or anomalous.
14. Explain why anomaly detection does not automatically prove a cyberattack.

---

# 38. Example Student Test Events

## Scenario A — Likely Normal

```text
Packets = 130
Failed Logins = 0
Ports = 4
Data = 40 MB

Expected:
Probably Normal
```

---

## Scenario B — Possible Authentication Anomaly

```text
Packets = 500
Failed Logins = 80
Ports = 3
Data = 20 MB

Expected:
Potential Anomaly
```

---

## Scenario C — Possible Large Transfer Anomaly

```text
Packets = 200
Failed Logins = 0
Ports = 5
Data = 2000 MB

Expected:
Potential Data Transfer Anomaly
```

---

# 39. ⭐ Bonus Challenge: SOC Alert Function

Students can create:

```python
def check_network_event(
    packets,
    bytes_mb,
    failed_logins,
    unique_ports,
    duration
):

    event = pd.DataFrame({

        "PacketsPerMinute": [packets],

        "BytesTransferredMB": [bytes_mb],

        "FailedLogins": [failed_logins],

        "UniquePorts": [unique_ports],

        "ConnectionDurationSec": [duration]
    })


    prediction = model.predict(
        event
    )[0]


    score = model.decision_function(
        event
    )[0]


    if prediction == -1:

        print("🚨 SECURITY ALERT")

    else:

        print("✅ Normal network activity")


    print(
        f"Anomaly Score: {score:.4f}"
    )
```

Then call:

```python
check_network_event(
    packets=900,
    bytes_mb=400,
    failed_logins=50,
    unique_ports=120,
    duration=15
)
```

Workflow:

```text
New Network Event
       │
       ▼
check_network_event()
       │
       ▼
Isolation Forest
       │
       ▼
Anomaly Score
       │
   ┌───┴────┐
   ▼        ▼
Normal    Alert
```

---

# 40. 💬 Discussion Questions

Students should answer:

1. Why is this considered unsupervised learning?
2. Why is there no target `y`?
3. What is the difference between an anomaly and an attack?
4. Why might a legitimate backup be classified as anomalous?
5. What does `contamination=0.05` mean?
6. What happens if contamination changes to `0.20`?
7. Why are several network features better than only using failed logins?
8. What does the anomaly score represent?
9. Why should a human analyst investigate alerts?
10. Why can a port scan look different from brute-force activity?
11. Why might a large data transfer be legitimate?
12. What other network features could improve the model?
13. How could time of day become a useful feature?
14. What are the risks of too many false alarms?
15. What are the risks of missing real anomalies?

---

# 41. 🏆 Suggested Grading Rubric

| Area | Marks |
|---|---:|
| Dataset Understanding | 10 |
| Security Feature Explanation | 10 |
| Isolation Forest Implementation | 20 |
| Anomaly Identification | 15 |
| Anomaly Score Interpretation | 10 |
| Visualization | 10 |
| New Event Detection | 10 |
| Security Investigation | 10 |
| Code Quality | 5 |
| **Total** | **100** |

---

# 42. 🎯 K-Means vs Anomaly Detection

Both can be used in unsupervised learning, but they answer different questions.

| Concept | K-Means | Anomaly Detection |
|---|---|---|
| Learning | Unsupervised | Often unsupervised / semi-supervised |
| Main question | Which group? | Is this unusual? |
| Output | Cluster 0, 1, 2 | Normal / Anomaly |
| Example | Customer segmentation | Network anomaly detection |
| Typical algorithm | K-Means | Isolation Forest |
| Known `y` required? | No | Usually no |
| Main goal | Discover groups | Discover unusual observations |

Conceptually:

```text
K-MEANS

Customers
   │
   ▼
Find Similarities
   │
   ├── Cluster A
   ├── Cluster B
   └── Cluster C
```

versus:

```text
ANOMALY DETECTION

Network Events
      │
      ▼
Learn Common Pattern
      │
      ▼
Find Unusual Events
      │
   ┌──┴───┐
   ▼      ▼
Normal  Anomaly
```

---

# 43. Other Real-World Unsupervised Learning Assignments

## 🚨 Cybersecurity Anomaly Detection

Detect unusual network or login activity using Isolation Forest.

---

## 🏭 Machine Failure Detection

Use:

```text
Temperature
Vibration
Pressure
Motor Current
RPM
```

to identify abnormal machine behavior.

---

## 💳 Financial Transaction Anomaly Detection

Analyze:

```text
Transaction Amount
Transaction Frequency
Country
Time
Merchant Type
```

to identify unusual transactions.

---

## 🤖 Robot Sensor Anomaly Detection

Use:

```text
LiDAR
Ultrasonic Distance
Motor Current
IMU
Wheel Encoder
Battery Voltage
```

to detect unusual robot behavior.

---

## ⚡ Electricity Consumption Anomaly Detection

Identify unusual household or building energy consumption.

---

## 🗄️ Server Health Anomaly Detection

Use:

```text
CPU
RAM
Disk
Network Traffic
Request Rate
Response Time
```

to identify unusual server behavior.

---

## 🧩 DBSCAN

Use clustering to find:

```text
Clusters
+
Noise / Outliers
```

DBSCAN is especially interesting because it can automatically identify points that do not belong to any dense cluster.

---

## 📉 PCA

Use Principal Component Analysis to reduce datasets with many features into:

```text
2 dimensions
or
3 dimensions
```

for visualization and exploration.

---

# 44. Recommended Unsupervised Learning Teaching Sequence

A useful progression is:

```text
K-Means
   │
   ▼
Understand Clustering
   │
   ▼
Elbow Method
   │
   ▼
Silhouette Score
   │
   ▼
Isolation Forest
   │
   ▼
Anomaly Detection
   │
   ▼
DBSCAN
   │
   ▼
Clusters + Noise Detection
   │
   ▼
PCA
   │
   ▼
Dimensionality Reduction
```

---

# 45. 🎓 Main Learning Outcome

Students should understand:

```text
CLASSIFICATION

Known Historical Labels
       │
       ▼
Normal / Attack
       │
       ▼
Learn From Labels
```

versus:

```text
ANOMALY DETECTION

Mostly Unlabeled Data
       │
       ▼
Learn Common Patterns
       │
       ▼
Find Unusual Behavior
       │
       ▼
Investigation
```

---

# 46. ✅ Final Key Takeaway

The most important real-world principle is:

> **Anomaly detection does not automatically detect hackers. It detects behavior that is unusual enough to deserve further investigation.**

The complete security workflow is:

```text
Network Telemetry
      │
      ▼
Feature Extraction
      │
      ▼
Isolation Forest
      │
      ▼
Anomaly Score
      │
      ▼
Normal / Anomaly
      │
      ▼
SOC Alert
      │
      ▼
Human Investigation
      │
      ├── Benign Event
      ├── Misconfiguration
      └── Security Incident
```

This makes anomaly detection a strong real-world Machine Learning exercise because students learn not only how to run an algorithm, but also how Machine Learning fits into a realistic **cybersecurity investigation workflow**.
