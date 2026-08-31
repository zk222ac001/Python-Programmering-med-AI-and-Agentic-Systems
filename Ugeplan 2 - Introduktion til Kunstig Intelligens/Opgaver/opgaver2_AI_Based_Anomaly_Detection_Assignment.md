# 🚨 Assignment: Build an AI-Based Anomaly Detection System

> **Course:** Machine Learning with Python  
> **Topic:** Unsupervised Learning – Anomaly Detection  
> **Algorithm:** Isolation Forest  
> **Application Area:** Cybersecurity / Network Monitoring  
> **Level:** Beginner to Intermediate  
> **Estimated Time:** 3–4 Hours

---

# 1. 🎯 Assignment Title

## **Build an AI-Based Network Anomaly Detection System**

Your task is to design and implement a Python-based Machine Learning system that analyzes network activity and automatically identifies **unusual or suspicious behavior**.

The system will use the **Isolation Forest** algorithm from Scikit-learn.

---

# 2. 🌍 Real-World Scenario

Imagine that you are working as a junior Machine Learning Engineer in a company's **Security Operations Center (SOC)**.

The company has many devices connected to its network:

```text
                    COMPANY NETWORK
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
      Employee PCs      Servers        IoT Devices
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                   Network Activity
                          │
                          ▼
                  Thousands of Events
```

Most network activity is normal. Examples include employees browsing websites, email communication, connections to company servers, database requests, file transfers, and software updates.

However, occasionally unusual activity may appear.

```text
50 failed login attempts
        │
        ▼
Possible brute-force behavior
```

```text
One computer accesses 150 ports
        │
        ▼
Possible port scanning
```

```text
1,500 MB transferred unexpectedly
        │
        ▼
Possible unusual data transfer
```

The security team cannot manually examine every network event. Therefore, the company wants you to create an **AI-Based Anomaly Detection System**.

---

# 3. 🧠 What Problem Are You Solving?

The system should answer:

```text
             Network Event
                   │
                   ▼

       Does this event behave
       like normal activity?

                   │
           ┌───────┴───────┐
           ▼               ▼
          YES              NO
           │                │
           ▼                ▼
      ✅ NORMAL        🚨 ANOMALY
```

An **anomaly** is an observation that behaves very differently from the majority of observations.

---

# 4. Important Security Principle

Your Machine Learning system is **not** designed to say:

```text
Anomaly = Hacker
```

Instead:

```text
Anomaly Detected
       │
       ▼
Security Alert
       │
       ▼
SOC Analyst Investigates
       │
   ┌───┴──────────────┐
   ▼                  ▼
Legitimate         Possible
Activity           Security Incident
```

Unusual behavior may also come from a large backup, software update, administrator maintenance, network testing, a new application, a configuration error, or a cyberattack.

> **Anomaly detection identifies unusual behavior. It does not automatically prove malicious activity.**

---

# 5. 🎓 Learning Objectives

After completing this assignment, you should be able to:

- Explain anomaly detection.
- Explain the difference between supervised and unsupervised learning.
- Explain why anomaly detection may not require a target variable `y`.
- Create and explore network data using Pandas.
- Select useful Machine Learning features.
- Train an Isolation Forest model.
- Identify normal and anomalous observations.
- Interpret anomaly scores.
- Visualize anomalous network events.
- Test new incoming network events.
- Interpret Machine Learning output from a cybersecurity perspective.

---

# 6. 🔍 Supervised vs Unsupervised Learning

In supervised learning:

```text
                TRAINING DATA

          X                  y
          │                  │
          ▼                  ▼
    Network Data       Known Label

                        Normal
                          or
                         Attack
```

In this assignment:

```text
              NETWORK DATA

                    X
                    │
                    ▼
          Packets / Logins / Ports
                    │
                    ▼
             No known y
                    │
                    ▼
            Isolation Forest
                    │
                    ▼
        Discover unusual behavior
```

This is an example of **unsupervised anomaly detection**.

---

# 7. 🌲 Algorithm: Isolation Forest

Isolation Forest works on the idea that unusual observations are generally easier to isolate than normal observations.

```text
Normal network activity

● ● ● ● ●
 ● ● ● ●
● ● ● ● ●


                              X
```

Where:

```text
● = Normal behavior
X = Unusual behavior
```

The unusual observation can often be separated quickly:

```text
All Network Events
        │
        ▼
     Split Data
        │
    ┌───┴──────────────┐
    ▼                  ▼
Many Similar        Unusual
Events              Event
                       │
                       ▼
                Isolated Quickly
                       │
                       ▼
                  🚨 Anomaly
```

---

# 8. 📊 Dataset Requirements

Create a network activity dataset containing at least:

| Feature | Description |
|---|---|
| `PacketsPerMinute` | Number of network packets in one minute |
| `BytesTransferredMB` | Amount of data transferred |
| `FailedLogins` | Number of failed login attempts |
| `UniquePorts` | Number of different ports contacted |
| `ConnectionDurationSec` | Duration of the network connection |

Create at least **30–50 normal observations** and **3–5 unusual observations**. For an advanced version, create **100+ observations**.

---

# 9. ✅ Example Normal Activity

| Feature | Value |
|---|---:|
| Packets/minute | 130 |
| Data transferred | 42 MB |
| Failed logins | 0 |
| Ports | 4 |
| Connection duration | 75 sec |

```text
Packets              130
Failed Logins          0
Ports                  4
Transferred Data      42 MB
Duration              75 sec
        │
        ▼
Values close to normal behavior
        │
        ▼
✅ NORMAL
```

---

# 10. 🚨 Example Anomaly 1 — Login Activity

| Feature | Value |
|---|---:|
| Packets/minute | 280 |
| Data transferred | 20 MB |
| Failed logins | 55 |
| Ports | 3 |
| Duration | 25 sec |

```text
Failed Logins

Normal
0–2
 │
 ▼
Suspicious Event
55
```

Possible interpretation:

```text
Repeated Login Attempts
         │
         ▼
Many Authentication Failures
         │
         ▼
Possible Brute-Force-Like Activity
```

---

# 11. 🚨 Example Anomaly 2 — Port Scanning

| Feature | Value |
|---|---:|
| Packets/minute | 700 |
| Data transferred | 12 MB |
| Failed logins | 1 |
| Ports | 150 |
| Duration | 8 sec |

```text
Normal Computer
3–5 Ports
    │
    ▼
Normal

Possible Scanner
150 Ports
    │
    ▼
Unusual
```

---

# 12. 🚨 Example Anomaly 3 — Large Data Transfer

| Feature | Value |
|---|---:|
| Packets/minute | 310 |
| Data transferred | 1,500 MB |
| Failed logins | 0 |
| Ports | 4 |
| Duration | 1,800 sec |

```text
Normal Transfer
      │
      ▼
40–60 MB

New Event
      │
      ▼
1,500 MB
      │
      ▼
Much Larger Than Normal
      │
      ▼
🚨 Investigate
```

---

# 13. 🔄 Complete Assignment Workflow

```text
                    START
                      │
                      ▼
              Create Network Data
                      │
                      ▼
              Pandas DataFrame
                      │
                      ▼
                Explore Data
                      │
                      ▼
               Select Features
                      │
                      ▼
             Isolation Forest
                      │
                      ▼
                Train Model
                      │
                      ▼
               Detect Anomalies
                      │
                      ▼
              Calculate Scores
                      │
                      ▼
             Visualize Results
                      │
                      ▼
             Test New Event
                      │
                      ▼
            Security Interpretation
                      │
                      ▼
                     END
```

---

# 14. 📝 Task 1 — Create the Dataset

Create a Pandas DataFrame containing network activity with both normal and unusual observations.

Do not create a target such as:

```text
Attack = Yes/No
```

for model training.

Remember:

```text
Unsupervised Learning
        │
        ▼
No target y required
```

---

# 15. 📝 Task 2 — Explore the Dataset

Use Pandas to display:

- First five rows
- Dataset shape
- Statistical information
- Missing values

Answer:

> What appears to be the normal range for each network feature?

---

# 16. 📝 Task 3 — Select Machine Learning Features

Create `X` using:

```text
PacketsPerMinute
BytesTransferredMB
FailedLogins
UniquePorts
ConnectionDurationSec
```

```text
                X
        ┌───────┼─────────┐
        ▼       ▼         ▼
     Packets  Logins    Ports
        │       │         │
        └───────┼─────────┘
                ▼
        Data + Duration
                │
                ▼
        Isolation Forest
```

---

# 17. 📝 Task 4 — Create the Isolation Forest

Your model should include:

```text
n_estimators
contamination
random_state
```

Explain what each parameter means.

---

# 18. 🧠 Understanding `n_estimators`

`n_estimators` controls how many Isolation Trees are created.

```text
Network Dataset
      │
      ├────► Tree 1
      ├────► Tree 2
      ├────► Tree 3
      ├────► ...
      └────► Tree 200
                │
                ▼
          Combined Result
```

---

# 19. 🧠 Understanding `contamination`

For example:

```text
contamination = 0.05
```

means approximately:

```text
100 Network Events

95 → Expected Normal
5  → Expected Anomalies
```

It does **not** mean that 5% of the company's traffic is definitely malicious.

---

# 20. 📝 Task 5 — Train the Model

Train the Isolation Forest using the feature dataset.

Isolation Forest typically returns:

```text
 1 = Normal
-1 = Anomaly
```

---

# 21. 📝 Task 6 — Convert Predictions to Readable Labels

Your final DataFrame should look similar to:

| Packets | Failed Logins | Ports | Prediction | Status |
|---:|---:|---:|---:|---|
| 125 | 0 | 3 | 1 | Normal |
| 135 | 1 | 4 | 1 | Normal |
| 900 | 50 | 150 | -1 | Anomaly |

Convert `1` to `Normal` and `-1` to `Anomaly`.

---

# 22. 📝 Task 7 — Calculate Anomaly Scores

Calculate an anomaly score for each event.

```text
Most Unusual                         More Normal

      ◀──────────────────────────────────▶

Very low score                    Higher score
```

Use the scores to rank the most unusual events.

---

# 23. 📝 Task 8 — Display Only Anomalies

Create a filtered table containing only detected anomalies.

| Packets | Data MB | Failed Logins | Ports | Status |
|---:|---:|---:|---:|---|
| 900 | 500 | 50 | 150 | Anomaly |
| 700 | 12 | 1 | 120 | Anomaly |

Write a short explanation for each anomaly.

---

# 24. 📈 Task 9 — Visualize the Results

Recommended graph:

```text
X-axis → Failed Logins
Y-axis → Unique Ports
```

```text
Unique Ports
     ▲

150  │                           X
     │
120  │                      X
     │
  5  │ ● ● ● ●
  4  │ ● ● ●
  3  │ ● ●
     └──────────────────────────────►
               Failed Logins

● = Normal
X = Anomaly
```

Include a title, axis labels, legend, grid, and different markers for anomalies.

---

# 25. ⚡ Task 10 — Test a New Network Event

Use this example:

| Feature | Value |
|---|---:|
| Packets/minute | 850 |
| Data transferred | 500 MB |
| Failed logins | 35 |
| Ports | 100 |
| Duration | 25 sec |

```text
New Network Event
        │
        ▼
Create DataFrame
        │
        ▼
Isolation Forest
        │
        ▼
Prediction
        │
   ┌────┴─────┐
   ▼          ▼
Normal      Anomaly
```

Display either:

```text
✅ NORMAL NETWORK ACTIVITY
```

or:

```text
🚨 SECURITY ALERT:
ANOMALOUS NETWORK ACTIVITY
```

---

# 26. 🔍 Task 11 — Security Investigation

For every anomaly, provide a possible interpretation.

| Event | Main Unusual Feature | Possible Explanation | Model Result |
|---|---|---|---|
| A | 55 failed logins | Possible brute-force activity | Anomaly |
| B | 150 ports | Possible port scanning | Anomaly |
| C | 1,500 MB transfer | Backup or possible unusual transfer | Anomaly |

Use cautious language such as **Possible**, **Potential**, **May indicate**, and **Requires investigation**.

---

# 27. 🧪 Experiment: Change `contamination`

Train the model using:

```text
0.01
0.05
0.10
0.20
```

Complete:

| Contamination | Number of Anomalies | Observation |
|---:|---:|---|
| 0.01 | | |
| 0.05 | | |
| 0.10 | | |
| 0.20 | | |

Answer:

> What happens when contamination increases?

---

# 28. ⭐ Bonus Task — Create Your Own Security Events

Create three events:

### Event A — Normal

```text
Packets           = 130
Data              = 45 MB
Failed Logins     = 0
Ports             = 4
Duration          = 75 sec
```

### Event B — Authentication Anomaly

```text
Packets           = 300
Data              = 15 MB
Failed Logins     = 80
Ports             = 3
Duration          = 30 sec
```

### Event C — Port Scanning Anomaly

```text
Packets           = 750
Data              = 10 MB
Failed Logins     = 0
Ports             = 180
Duration          = 10 sec
```

Before running the model:

```text
Student Prediction
        │
        ▼
Normal or Anomaly?
        │
        ▼
Run ML Model
        │
        ▼
Compare
        │
        ▼
Explain
```

---

# 29. 🚀 Advanced Challenge — Near-Real-Time Monitoring

Extend the project so that network events can be checked one after another.

```text
           Incoming Network Event
                    │
                    ▼
             Python Program
                    │
                    ▼
            Isolation Forest
                    │
                    ▼
              Anomaly Score
                    │
             ┌──────┴──────┐
             ▼             ▼
          Normal        Suspicious
                            │
                            ▼
                       Generate Alert
```

A simulated stream is sufficient.

---

# 30. 🏢 Real-World System Architecture

```text
                   COMPANY NETWORK

        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
     Firewall         Servers        Endpoints
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                Network Telemetry
                        │
                        ▼
                  Log Collector
                        │
                        ▼
                Feature Extraction
                        │
                        ▼
              ┌──────────────────┐
              │ Isolation Forest │
              └─────────┬────────┘
                        │
                ┌───────┴───────┐
                ▼               ▼
             Normal          Anomaly
                                │
                                ▼
                            SOC Alert
                                │
                                ▼
                         Security Analyst
```

---

# 31. 💬 Discussion Questions

1. What is anomaly detection?
2. Why can anomaly detection be considered unsupervised learning?
3. Why is there no target variable `y` in this project?
4. What does Isolation Forest do?
5. Why are anomalies easier to isolate?
6. What does `contamination` mean?
7. What does `random_state` do?
8. What do prediction values `1` and `-1` mean?
9. What does an anomaly score tell us?
10. Why should several network features be analyzed together?
11. Why could a backup be detected as anomalous?
12. Why does anomaly detection not automatically prove an attack?
13. What might happen if contamination is set too high?
14. What might happen if contamination is set too low?
15. How could this system be improved for a real SOC?

---

# 32. 📦 Deliverables

Submit:

1. `anomaly_detection.py`
2. Dataset or Python-generated data
3. Normal/anomaly predictions
4. Filtered anomaly table
5. Anomaly scores
6. Visualization
7. At least three new-event tests
8. Short 2–3 page report
9. Discussion-question answers
10. Short security interpretation

---

# 33. 📄 Suggested Report Structure

```text
1. Introduction
2. What is Anomaly Detection?
3. Why Unsupervised Learning?
4. Dataset
5. Selected Features
6. Isolation Forest
7. Results
8. Visualization
9. Security Interpretation
10. New Event Testing
11. Limitations
12. Conclusion
```

---

# 34. 🏆 Assessment Rubric

| Area | Marks |
|---|---:|
| Explanation of anomaly detection | 10 |
| Dataset creation and exploration | 10 |
| Feature selection | 10 |
| Isolation Forest implementation | 15 |
| Anomaly detection results | 15 |
| Anomaly-score interpretation | 10 |
| Visualization | 10 |
| New-event testing | 5 |
| Cybersecurity interpretation | 10 |
| Code quality and documentation | 5 |
| **Total** | **100** |

---

# 35. ✅ Expected Learning Outcome

```text
              NETWORK DATA
                    │
                    ▼
             Select Features
                    │
                    ▼
             Isolation Forest
                    │
                    ▼
             Learn Patterns
                    │
                    ▼
              Detect Unusual
                 Behavior
                    │
            ┌───────┴───────┐
            ▼               ▼
        ✅ Normal        🚨 Anomaly
                            │
                            ▼
                    SOC Investigation
```

## Final Assignment Goal

> **Demonstrate how Python and unsupervised Machine Learning can automatically analyze network activity, identify unusual behavior, prioritize suspicious events, and support a human security analyst in deciding which events require further investigation.**
