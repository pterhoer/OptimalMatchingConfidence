# Optimal Matching Confidence for Biometric Systems

## PIC-Score: Probabilistic Interpretable Comparison Score for Optimal Matching Confidence in Single- and Multi-Biometric (Face) Recognition

<img src="Visualization_explained.png" width="400" align="right"> 

* [Research Paper](https://arxiv.org/abs/2003.09373) - TODO

## Table of Contents 

- [Abstract](#abstract)
- [Key Points](#key-points)
- [Results](#results)
- [Installation](#installation)
- [Citing](#citing)


## Abstract

In the context of biometrics, matching confidence refers to the confidence that a given matching decision is correct.
Since many biometric systems operate in critical decision-making processes, such as in forensics investigations, accurately and reliably stating the matching confidence becomes of high importance.
Previous works on biometric confidence estimation can well differentiate between high and low confidence, but lack interpretability.
Therefore, they do not provide accurate probabilistic estimates of the correctness of a decision.
In this work, we propose a probabilistic interpretable comparison (PIC) score that accurately reflects the probability that the score originates from samples of the same identity.
We prove that the proposed approach provides optimal matching confidence. 
Contrary to other approaches, it can also optimally combine multiple samples in a joint PIC score which further increases the recognition and confidence estimation performance.
In the experiments, the proposed PIC approach is compared against all biometric confidence estimation methods available on four publicly available databases and five state-of-the-art face recognition systems.
The results demonstrate that PIC has a significantly more accurate probabilistic interpretation than similar approaches and is highly effective for multi-biometric recognition.

## Key Points

In contrast to previous works, the proposed PIC score unifies several beneficial properties:

- **Interpretability**: The PIC score accurately reflects the probability that the comparison belongs to a genuine (same person) comparison. This allows critical decision-making processes to act upon reliable decisions or, in case of low confidence, allow to ask a more confident system or human operator for the decision.
- **Optimality**: Despite its simplicity, PIC is derived from Bayes' theorem and thus, provides optimal matching confidences given suitable training data. This might be useful, e.g. in law enforcement, when approaches with a theoretical foundation are preferred.
- **Universality**: Since PIC operates on score level, it is not limited to face and can be applied to any biometric modality and recognition model without changing its single-biometric performance. 
- **Combinability**: Contrarily to standard comparison scores, a joint PIC score can naturally be computed when multiple sample samples are given. This leads to stronger multi-biometric recognition performance without losing its interpretability and is highly beneficial when e.g. dealing with multiple video frames.
- **Integratability**: PIC is easily integrateable. It can be easily added on top of an existing biometric system without retraining that system. Moreover, it avoids the need for data- and computationally-expensive experiments to determine the wanted decision threshold due to its interpretable nature.


## Results

**Confidence Calibration Curves (CCC)** - The CCC for FaceNet on all datasets are shown. While most approaches have to deal with high under-
and over-confident predictions, the proposed PIC produces close-to-ideal (black line) probabilistic confidence estimates in most cases.

<img src="CCC.png" width="900" >

**Confidence Calibration Analysis** - The Expected Calibration Error (ECE) and Maximum Calibration Error (MCE) are shown for several dataset and FRS combinations at an FMR of 10^−3. ECE shows the average confidence calibration error, while the MCE presents the maximum calibration error. The best performance is marked in bold. Except for one case, the proposed PIC approach strongly outperforms the other confidence estimators in terms of
interpretability. This holds for the average performance, as well as for the worst-case scenario.

<img src="CCA.png" width="900" >

**Multi-Biometric PIC score recognition performance** - The recognition performance of using a joint PIC score by combining a probe sample with 1/2/5 reference samples (RS) is shown for all database and FRS combinations. Generally, the joint PIC score leads to lower recognition errors at 10^−3 FMR than in the single-biometric scenario.

**Multi-Biometric Confidence Calibration Analysis** - The expected calibration errors (ECE) are shown for a joint PIC score confidence by combining a probe sample with 1/2/5 reference samples (RS). This was done for all database and FRS combinations at an FMR of 10−3. The ECE significantly decreases when more reference samples are used. Consequently, also the probabilistic confidence interpretation of PIC becomes more accurate when multiple samples are combined.

<img src="Multi-Biometric.png" width="900" >

## Installation

TODO




## Citing

If you use this code, please cite the following papers.

TODO

```
@inproceedings{DBLP:conf/cvpr/TerhorstKDKK20,
  author    = {Philipp Terh{\"{o}}rst and
               Jan Niklas Kolf and
               Naser Damer and
               Florian Kirchbuchner and
               Arjan Kuijper},
  title     = {{SER-FIQ:} Unsupervised Estimation of Face Image Quality Based on
               Stochastic Embedding Robustness},
  booktitle = {2020 {IEEE/CVF} Conference on Computer Vision and Pattern Recognition,
               {CVPR} 2020, Seattle, WA, USA, June 13-19, 2020},
  pages     = {5650--5659},
  publisher = {{IEEE}},
  year      = {2020},
  url       = {https://doi.org/10.1109/CVPR42600.2020.00569},
  doi       = {10.1109/CVPR42600.2020.00569},
  timestamp = {Tue, 11 Aug 2020 16:59:49 +0200},
  biburl    = {https://dblp.org/rec/conf/cvpr/TerhorstKDKK20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


