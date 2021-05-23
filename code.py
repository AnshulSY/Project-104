import statistics
import csv
import pandas as pd
df = pd.read_csv(r"/Users/anshul/Desktop/Class 104/SOCR-HeightWeight.csv")

heights = df["Weight(Pounds)"]
print(statistics.mean(heights))
print(statistics.median(heights))
print(statistics.mode(heights))