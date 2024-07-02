"""
Copyright (c) 2024 Simone Chiarella

Author: S. Chiarella
Date: 2024-07-02

Store the functions to extract the biometric measurements from the segmented
labels.

"""
import numpy as np


dict_views = {
    'sag': 0,
    'cor': 1,
    'ax': 2,
}


def get_voxels_in_between(
    mask: np.ndarray,
    view: str,
    direction: str,
) -> list | int:
    """
    Get the number of voxels in between the two most distant points in each
    slice, along a selected view (sagittal, coronal, or axial) and direction
    (horizontal or vertical).

    Parameters
    ----------
    mask : numpy.ndarray
        The segmented label array.
    view : str
        The view of the image (axial, coronal, or sagittal).
    direction : str
        The direction of the measurement (horizontal or vertical).

    Returns
    -------
    list | int
        The number of voxels in between the two most distant points. It is a
        list if mask is 3D, and an integer if mask is 2D.

    """
    if mask.ndim != 3 and mask.ndim != 2:
        raise ValueError("The mask should be a 3D or 2D array.")
    if view not in dict_views:
        raise ValueError("The view should be 'sag', 'cor', or 'ax'.")
    if direction is not "h" and direction is not "v":
        raise ValueError("The direction should be 'h' or 'v'.")

    view = dict_views[view]

    voxels_in_between = []

    if mask.ndim == 3:
        for slice_idx in range(mask.shape[view]):
            slice_label = mask[:, :, slice_idx]
            # Find indices where the label is present
            rows, cols = np.where(slice_label > 0)
            if direction == "h":
                if len(cols) > 0:  # If there are labeled points in the slice
                    # Max horizontal distance in voxels
                    max_dist_voxels = max(cols) - min(cols)
                    voxels_in_between.append(max_dist_voxels)
                else:
                    voxels_in_between.append(0)  # No label in this slice
            elif direction == "v":
                if len(rows) > 0:
                    # Max vertical distance in voxels
                    max_dist_voxels = max(rows) - min(rows)
                    voxels_in_between.append(max_dist_voxels)
                else:
                    voxels_in_between.append(0)

    if mask.ndim == 2:
        rows, cols = np.where(mask > 0)
        if direction == "h":
            if len(cols) > 0:
                max_dist_voxels = max(cols) - min(cols)
                voxels_in_between = max_dist_voxels
            else:
                voxels_in_between = 0
        elif direction == "v":
            if len(rows) > 0:
                max_dist_voxels = max(rows) - min(rows)
                voxels_in_between = max_dist_voxels
            else:
                voxels_in_between = 0

    return voxels_in_between
