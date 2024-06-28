"""
Copyright (c) 2024 Simone Chiarella

Author: S. Chiarella
Date: 2024-06-28

This module contains different utility functions used in the pipeline.

"""
import nibabel as nib
import numpy as np

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
