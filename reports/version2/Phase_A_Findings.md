# Phase A: Dataset Shift Analysis Findings

## Objective

The objective of Phase A was to investigate why the Version 1 model achieved excellent performance on FD001 but showed reduced performance on FD002 and FD004 before making any modifications to the prediction pipeline.





## Dataset Validation

All four NASA C-MAPSS datasets were successfully loaded and validated.

| Dataset | Engines | Samples |
|---------|---------:|---------:|
| FD001 | 100 | 20,631 |
| FD002 | 260 | 53,759 |
| FD003 | 100 | 24,720 |
| FD004 | 249 | 61,249 |

No missing values were detected in any dataset.



## Operating Condition Analysis

  ### Introduction 
The operating settings were analyzed across all four NASA C-MAPSS datasets to determine whether the datasets represent similar or different operating conditions.


  ### Table
| Dataset | Operating Condition |
|----------|---------------------|
| FD001 | Single |
| FD002 | Multiple |
| FD003 | Single |
| FD004 | Multiple |



  ### Observations
1. FD001 and FD003 operate under a single operating condition.

2. FD002 and FD004 contain multiple operating conditions.

3. The operating setting distributions differ significantly between the two groups.


  ### Conclusion
These observations indicate that a preprocessing pipeline designed using only FD001 statistics is unlikely to generalize well to datasets containing multiple operating conditions.
















## Feature Drift Analysis

### Introduction
The mean values of all active features were compared across the four datasets to quantify distribution drift relative to FD001.


### Most Drifted Active Features

 | Rank |    Feature    | Mean Drift          |
 |------|---------------|--------------------:|
 | 1    | op_setting_1  | 47.99826339509276   |
 | 2    | op_setting_2  | 1.1434012601926722  | 
 | 3    | sensor_2      |  126.49248770680322 |
 | 4    | sensor_3      |  345.6225671652305  |
 | 5    | sensor_4      |  414.9727490082257  |
  


### Observations
1. Several active features exhibit substantial distribution drift across datasets.

2. The largest drift is observed in sensors rather than operating settings.

3. Stable feature distributions are limited to a small subset of the active features.

4. Models trained using statistics from FD001 alone may not generalize effectively to datasets with different feature distributions.


### Conclusion

The observed feature drift provides strong evidence that Version 1 preprocessing is dataset specific. A generalized preprocessing strategy is therefore required for Version 2.

















## Sensor Distribution Analysis

### Introduction
The statistical distributions of the sensor measurements were compared across all four datasets to determine whether the sensor behavior remains consistent under different operating conditions.





### Table
| Sensor | FD001 Mean | FD002 Mean | FD003 Mean | FD004 Mean |
|--------|-----------:|-----------:|-----------:|-----------:|
| sensor_1 | 518.67 | 472.91 | 518.67 | 472.88 |
| sensor_2 | 642.68 | 579.67 | 642.46 | 579.42 |
| sensor_3 | 1590.52 | 1419.97 | 1588.08 | 1417.90 |
| sensor_4 | 1408.93 | 1205.44 | 1404.47 | 1201.92 |
| sensor_5 | 14.62 | 8.03 | 14.62 | 8.03 |




### Observations
1. Sensor distributions differ substantially between the single and multiple operating condition datasets.

2. FD001 and FD003 exhibit highly similar sensor statistics.

3. FD002 and FD004 also exhibit similar sensor statistics.

4. Several sensors show large shifts in their mean values across datasets.



### Conclusion

The sensor statistics further confirm that the datasets originate from different operating conditions. This distribution shift explains why a model trained using preprocessing statistics derived only from FD001 may experience degraded performance when evaluated on FD002 and FD004.













## Correlation Analysis

### Introduction
Correlation matrices were generated for the active features in each dataset to analyze how relationships between features change under different operating conditions.

### Analysis Approach
The correlation matrix of FD001 was used as the reference. Correlation difference matrices were computed by comparing FD001 with FD002, FD003, and FD004. The feature pairs exhibiting the largest changes were identified to quantify structural differences between datasets.


### Observations
1. Correlations between several active feature pairs changed substantially across datasets.

2. FD001 and FD003 exhibited relatively similar feature relationships.

3. FD002 and FD004 showed larger deviations from the FD001 reference.

4. Distribution shift affects not only individual feature values but also the relationships between features.


### Conclusion
The observed correlation changes indicate that feature interactions vary across operating conditions. This suggests that a model trained exclusively on FD001 may learn relationships that are not fully representative of the remaining datasets.


These findings further justify the development of a generalized predictive maintenance pipeline for Version 2.






























## Feature Stability Analysis
The active features were classified into High, Medium, and Low stability categories based on their mean drift across the four NASA C-MAPSS datasets.

### Classification Method
The stability categories were determined using the 33rd and 66th percentile of the mean drift values. Features with lower drift were classified as highly stable, while those with higher drift were classified as having low stability.

### Observations
| Feature | Stability |
|---------|-----------|
| op_setting_2 | High |
| sensor_15 | High |
| sensor_11 | High |
| sensor_6 | High |
| sensor_21 | High |

1. Only a subset of the active features remain highly stable across all operating conditions.

2. Stable features are expected to generalize better across datasets.

3. Features with low stability may require adaptive preprocessing or specialized handling.

4. Treating every feature equally may reduce cross-dataset robustness.

### Conclusion

Feature stability analysis indicates that different features contribute differently to model generalization. This supports the development of feature-aware preprocessing strategies in Version 2.






























## Overall Research Conclusions
The analyses performed during Phase A consistently demonstrate that the four NASA C-MAPSS datasets do not share the same data distribution. Differences were observed in operating conditions, feature distributions, sensor statistics, and feature relationships.


The Version 1 pipeline was designed using preprocessing statistics derived from FD001. While this approach achieved excellent performance on FD001, it is not expected to generalize optimally to datasets representing different operating conditions.


The observed dataset shift is not caused by implementation errors. Instead, it reflects genuine differences between the operating environments represented by the NASA C-MAPSS datasets.


Therefore, improving generalization requires changes to the preprocessing and training strategy rather than simply increasing model complexity.


### Key Findings

- Operating conditions differ across datasets.
- Sensor distributions shift significantly.
- Multiple active features exhibit substantial drift.
- Feature relationships change across datasets.
- Only a subset of features remain consistently stable.
- Version 1 preprocessing is dataset specific.
- A generalized pipeline is justified for Version 2.






























## Motivation for Version 2
Based on the findings from Phase A, the objective of Version 2 is to improve the robustness and generalization capability of the predictive maintenance system without affecting the validated Version 1 implementation.

Version 2 will focus on the following improvements:
- Generalized preprocessing across all datasets
- Multi-dataset model training
- Out-of-Distribution (OOD) detection
- Adaptive confidence estimation
- Large-scale evaluation on all engines
- Improved deployment robustness




Phase A establishes the research foundation for the development of a generalized, explainable, and uncertainty-aware predictive maintenance decision support system in Version 2.