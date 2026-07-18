# Version 1 Preprocessing Audit

## Objective

The objective of this audit is to inspect every preprocessing stage used in Version 1 and determine whether it is dataset independent or dataset specific before designing the Version 2 preprocessing pipeline.


## Version 1 Pipeline
Raw NASA Dataset
        ↓
Load Dataset
        ↓
Generate RUL
        ↓
Clip RUL
        ↓
Feature Engineering
        ↓
Feature Selection
        ↓
Feature Scaling
        ↓
Sequence Generation
        ↓
Save Processed Files



## Audit Status
| Stage | Status |
|--------|--------|
| Dataset Loading | Pending |
| RUL Generation | Pending |
| RUL Clipping | Pending |
| Feature Engineering | Pending |
| Feature Selection | Pending |
| Feature Scaling | Pending |
| Sequence Generation | Pending |
| Processed Data Saving | Pending |




### Audit Notes

Dataset loading is fully reusable for Version 2. The implementation accepts a dataset path as input, performs only file parsing and column assignment, and does not contain any FD001-specific assumptions. No modifications are required.



### RUL Generation

The RUL generation logic correctly computes the Remaining Useful Life for each engine using the standard NASA C-MAPSS formulation:

RUL = Maximum Engine Cycle − Current Cycle

The implementation operates only on the provided dataframe and does not contain dataset-specific assumptions. Although the demonstration code loads the FD001 dataset, the reusable `generate_rul()` function is fully compatible with all NASA C-MAPSS datasets. No modifications are required for Version 2.


### Build Dataset Pipeline

The dataset construction pipeline correctly combines dataset loading, RUL generation, engine-level splitting, and dataset saving into a structured workflow.

However, two improvements are required for Version 2:

1. The raw dataset path is hardcoded to `train_FD001.txt`, limiting the pipeline to a single operating condition.

2. The RUL clipping threshold is hardcoded to 125. Although this value is appropriate for Version 1, it should become a configurable preprocessing parameter in Version 2.

The remaining stages, including engine-level splitting and dataset saving, are reusable without modification.





### Constant Feature Detection

Version 1 automatically identifies constant features using the training dataset. The detection algorithm is correct and fully automated.

However, the analysis is performed only on the FD001 training data. Since Phase A demonstrated that feature distributions differ across datasets, constant feature detection should be performed using all training datasets in Version 2. This ensures that only globally constant features are removed.

### Feature Selection

Feature selection simply removes the features listed in `constant_features.txt`. The implementation is dataset independent and can be reused without modification. Only the source of the constant feature list changes in Version 2.



### Feature Scaling

Version 1 uses a StandardScaler fitted exclusively on the FD001 training dataset. The implementation correctly fits the scaler on the training data and applies the same transformation to the validation and test datasets, preventing data leakage.

However, the scaler statistics represent only one operating condition. Phase A demonstrated significant distribution differences across the NASA C-MAPSS datasets, indicating that a scaler trained only on FD001 may not normalize the remaining datasets appropriately.

Version 2 should fit the StandardScaler using the combined training data from all datasets while preserving the same transformation workflow.




### Sequence Generation

The sequence generation pipeline is fully dataset independent. Sequences are created separately for each engine, preventing data leakage across engine boundaries.

The implementation correctly excludes identifier and target columns, uses the clipped RUL target, and generates fixed-length sliding windows for GRU training.

The only optional improvement for Version 2 is replacing the hardcoded sequence length with a configurable parameter. No algorithmic changes are required.