"""
Copyright (c) 2024 Simone Chiarella

Author: S. Chiarella
Date: 2024-06-28

This script runs the pipeline of FeTA-biometry-predictor.

Starting from the segmentations of 7 labels in MRI T2w fetal brain images, it
predicts 5 biometric measurements.

The seven input labels required as input are:
1. cerebrospinal fluid (CSF)
2. gray matter and developing cortical plate (GM)
3. white matter and subplate (WM)
4. lateral ventricles (LV)
5. cerebellum (CRB)
6. subcortical gray matter (SGM)
7. brainstem (BS)

The five predicted biometric measurements are:
1) brain biparietal diameter (bBIP)
2) skull biparietal diameter (sBIP)
3) transverse cerebellar diameter (TCD)
4) height of the vermis (HV)
5) length of the corpus callosum (LCC)

"""
import ax_meas_pred
import cor_meas_pred
import sag_meas_pred
import evaluate
from modules.utils import (
    load_image,
    load_meas,
)


def main():
    """Run the pipeline."""

    # Load data
    test_mask = load_image("~/sub-001_rec-mial_dseg.nii.gz")
    meas_gt = load_meas("~/biometry.tsv")

    # Predict
    bBip_pred, sBip_pred = ax_meas_pred(test_mask)
    TCD_pred = cor_meas_pred(test_mask)
    HV_pred, LCC_pred = sag_meas_pred(test_mask)

    meas_preds = [bBip_pred, sBip_pred, TCD_pred, HV_pred, LCC_pred]

    # Evaluate
    evaluate.main(meas_gt, meas_preds, "~/biometry_pred_results.txt")


if __name__ == "__main__":
    main()
