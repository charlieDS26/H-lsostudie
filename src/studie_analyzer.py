import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

class HealthAnalyzer:
    def __init__(self, data):
        self.data = data
    """
    Skapar en HealthAnalyzer med ett dataset.
    """

    def descriptive_statistics(self): # Beräknar beskrivande statistik.
    
        columns = [
            "age",
            "weight",
            "height",
            "systolic_bp",
            "cholesterol"
        ]

        return self.data[columns].agg(
        ["mean", "median", "min", "max"]
    )

    def plot_bp(self):

        """
        Skapar ett histogram över systoliskt blodtryck.
        """
        plt.figure(figsize=(6,4))
        plt.hist(
            self.data["systolic_bp"],
            bins=20
        )
        plt.xlabel("Systolisk blodtryck (i mmHg)")
        plt.ylabel("Antal människor")
        plt.title("Blodtrycks fördelning")
        plt.show()

    def linear_regression(self):
        """
        Utför linjär regression för att förutsäga
        systoliskt blodtryck utifrån ålder.
        """
        x = self.data[["age"]]

        y = self.data["systolic_bp"]

        model = LinearRegression()
        model.fit(x, y)

        return model

    def plot_regression(self):
        """
        Visar sambandet mellan ålder och blodtryck
        tillsammans med regressionslinjen.
        """
        import matplotlib.pyplot as plt

        x = self.data[["age"]]
        y = self.data["systolic_bp"]

        model = self.linear_regression()

        predictions = model.predict(x)

        plt.figure(figsize=(8, 5))

        plt.scatter(x, y, alpha=0.5,
                    label="Observerat blodtryck")

        plt.plot(x, predictions,
                 color="red",
                 label="Regressionslinje")

        plt.xlabel("Ålder (år)")
        plt.ylabel("Systoliskt blodtryck (mmHg)")
        plt.title("Linjär regression: Ålder och blodtryck")

        plt.legend()
        plt.show()

    def regression_results(self):
        """
        Beräknar modellens lutning, intercept, och R2 värde.
        """
        x = self.data[["age"]]
        y = self.data["systolic_bp"]

        model = self.linear_regression()
        predictions = model.predict(x)

        return {
            "Lutning": model.coef_[0],
            "Intercept": model.intercept_,
            "R2": r2_score(y, predictions),
        }