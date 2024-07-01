"""
Copyright (c) 2024 Simone Chiarella

Author: S. Chiarella
Date: 2024-06-28

This module contains different utility functions used in the pipeline.

"""
import nibabel as nib
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


def load_image(
    file: str,
) -> np.ndarray:
    """
    Load an image from a file name as a NumPy array.

    Parameters
    ----------
    file : str
        The path to the image file.

    Returns
    -------
    numpy.ndarray
        The loaded image as a NumPy array.

    """
    return nib.load(file).get_fdata()


def load_meas(
    file: str,
) -> pd.DataFrame:
    """
    Load the ground truth biometric measures from a file name.

    Parameters
    ----------
    file : str
        The path to the file containing the biometric measures.

    Returns
    -------
    pandas.DataFrame
        The loaded biometric measures as a Pandas DataFrame.

    """
    df_biometry = pd.read_csv(file, encoding='utf-8', sep='\t')
    df_biometry = df_biometry.iloc[:, 1:-2]  # remove age and pathology

    return df_biometry


def impute_missing_values(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Impute missing values in a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the missing values.

    Returns
    -------
    pandas.DataFrame
        The DataFrame with the missing values imputed.

    """
    # Check for missing values
    if df.isnull().values.any():
        print("Missing values found. Starting imputation...")

        # Initialize the IterativeImputer
        imputer = IterativeImputer(random_state=0)

        # Perform the imputation
        df_imputed = imputer.fit_transform(df)

        # Convert the result back to a DataFrame
        df = pd.DataFrame(df_imputed, columns=df.columns)

        print("Imputation completed.")
    else:
        print("No missing values found.")

    return df
