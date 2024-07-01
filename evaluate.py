"""
Copyright (c) 2024 Simone Chiarella

Author: S. Chiarella
Date: 2024-07-01

This script evaluates the predictions of the biometric measurements.

"""
import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from modules.utils import impute_missing_values

def main(
    meas_gt: pd.DataFrame,
    meas_preds: np.ndarray,
    store_path: str,
) -> None:
    """
    Run and store the evaluation of the biometric measurement predictions.

    Parameters
    ----------
    meas_gt : pd.DataFrame
        The ground truth biometric measurements.
    meas_preds : np.ndarray
        The predicted biometric measurements.
    store_path : str
        The path to the .txt file to store the evaluation results.

    """
    meas_gt = impute_missing_values(meas_gt)
    meas_gt = meas_gt.to_numpy()

    # Calculate mean absolute error, mean squared error, and R2 score
    mae = mean_absolute_error(meas_gt, meas_preds)
    mse = mean_squared_error(meas_gt, meas_preds)
    r2 = r2_score(meas_gt, meas_preds)

    print(
        f"Mean Absolute Error: {mae}\n"
        f"Mean Squared Error: {mse}\n"
        f"R2 Score: {r2}\n"
    )

    # Save the results to a text file
    with open(store_path, 'w') as file:
        file.write(f"Mean Absolute Error: {mae}\n")
        file.write(f"Mean Squared Error: {mse}\n")
        file.write(f"R2 Score: {r2}\n")

    print(f"Results saved to {store_path}")
