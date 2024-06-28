"""
Copyright (c) 2024 Simone Chiarella

Author: S. Chiarella
Date: 2024-06-28

This script runs the pipeline of FeTA-biometry-predictor.

Starting from the segmentations of 7 labels in MRI T2w fetal brain images, it
predicts 5 biometric measures.

The seven input labels required as input are:
1. cerebrospinal fluid (CSF)
2. gray matter and developing cortical plate (GM)
3. white matter and subplate (WM)
4. lateral ventricles (LV)
5. cerebellum (CRB)
6. subcortical gray matter (SGM)
7. brainstem (BS)

The five predicted biometric measures are:
1) brain biparietal diameter (bBIP_ax)
2) skull biparietal diameter (sBIP_ax)
3) transverse cerebellar diameter (TCD_cor)
4) height of the vermis (HV)
5) length of the corpus callosum (LCC)

"""
