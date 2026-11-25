import pandas as pd
import matplotlib.pyplot as plt

class HealthAnalyzer:
    def __init__(self, data):
        self.data = data

    def descriptive_statistics(self):
        columns = [
            "age",
            "weight",
            "height",
            "systolic_bp",
            "cholesterol"
        ]

        return self.data[columns].agg(
            ["mean", "median," "min," "max"]
        )

    def plot_bp(self):
        plt.figure(figsize=(6,4))
        plt.hist(
            self.data["systolic_bp"],
            bins=20
        )
        plt.xlabel("Systolisk blodtryck (i mmHg)")
        plt.ylabel("Antal människor")
        plt.title("Blodtrycks fördelning")
        plt.show()