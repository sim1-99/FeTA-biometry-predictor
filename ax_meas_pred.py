"""
Copyright (c) 2024 Simone Chiarella

Author: S. Chiarella
Date: 2024-07-02

Extract the axial biometric measurements (bBip, sBip) from the segmented
labels.

"""
import numpy as np

from modules.biometric import (
    get_voxels_in_between,
)

def main(
    mask: np.ndarray,
) -> tuple[
    float,
    float,
]:
    """
    Extract the axial biometric measurements (bBip, sBip) from the segmented
    labels.

    Parameters
    ----------
    mask : numpy.ndarray
        The segmented labels of the fetal brain.

    Returns
    -------
    tuple[float, float]
        The extracted axial biometric measurements.

    """
    CSF_label = mask == 1
    GM_label = mask == 2
    
    sBip = get_voxels_in_between(CSF_label, view="ax", direction="h")
    bBip = get_voxels_in_between(GM_label, view="ax", direction="h")
    
    return (
        bBip,
        sBip,
    )
