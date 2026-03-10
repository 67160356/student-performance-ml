df["total_score"] = (
    df["math_score"] +
    df["reading_score"] +
    df["writing_score"]
)

df["pass"] = df["total_score"].apply(lambda x: 1 if x >= 150 else 0)
