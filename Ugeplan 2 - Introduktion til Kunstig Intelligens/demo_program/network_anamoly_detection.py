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