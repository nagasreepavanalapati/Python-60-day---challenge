import random
import math
import numpy as np
import pandas as pd


def generate_data(n):
    return [
        (
            f"STU_{i + 1}",
            random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 50)
        )
        for i in range(n)
    ]


def classify_students(df):
    categories = {"At Risk": set(), "Average": set(), "Good": set(), "Top Performer": set()}

    for _, row in df.iterrows():
        sid, m, a = row["student_id"], row["marks"], row["attendance"]

        if m < 40 or a < 50:
            categories["At Risk"].add(sid)
        elif 40 <= m <= 70:
            categories["Average"].add(sid)
        elif 71 <= m <= 90:
            categories["Good"].add(sid)
        elif m > 90 and a > 80:
            categories["Top Performer"].add(sid)

    return {k: list(v) for k, v in categories.items()}


def analyze_data(df):
    marks = df["marks"].values

    mean_val = sum(marks) / len(marks)
    median_val = np.median(marks)
    std_dev = np.std(marks)

    corr = np.corrcoef(df["marks"], df["attendance"])[0][1]

    min_m, max_m = np.min(marks), np.max(marks)
    df["normalized_marks"] = [(x - min_m) / (max_m - min_m) if max_m != min_m else 0 for x in marks]

    consistency = std_dev < 15
    attendance_risk = len([a for a in df["attendance"] if a < 50]) > 3
    top_count = len(df[(df["marks"] > 90) & (df["attendance"] > 80)])
    high_achievement = top_count >= 2

    summary_tuple = (mean_val, std_dev, max_m)

    if consistency and not attendance_risk and high_achievement:
        insight = "Stable Academic System"
    elif attendance_risk or not high_achievement:
        insight = "Critical Attention Required"
    else:
        insight = "Moderate Performance"

    return mean_val, median_val, std_dev, corr, summary_tuple, insight


n = int(input())

data = generate_data(n)

df = pd.DataFrame(data, columns=["student_id", "marks", "attendance", "assignment"])

df["performance_index"] = [
    (0.7 * m + 0.3 * a) * math.log(att + 1)
    for m, a, att in zip(df["marks"], df["assignment"], df["attendance"])
]

categories = classify_students(df)

mean_v, median_v, std_v, corr_v, summary, insight = analyze_data(df)

print(df)
print(categories)
print("Mean:", mean_v)
print("Median:", median_v)
print("Std Dev:", std_v)
print("Correlation:", corr_v)
print("Tuple:", summary)
print("Final Insight:", insight)