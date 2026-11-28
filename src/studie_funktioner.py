import numpy as np
import pandas as pd

def calculate_disease_rate(data):
    return data["disease"].mean()
    """
    Beräknar andelen personer med sjukdomen.
    """

def simulate_disease_rate(data, n=1000, seed=42):
    """
    Simulerar sjukdomsförekomst för slumpade människor.
    """
    probability = calculate_disease_rate(data)

    rng = np.random.default_rng(seed)

    simulated = rng.binomial(
        1,
        probability,
        size=n
    )

    return simulated.mean()