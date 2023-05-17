# Abstract Reasoning

*keywords: abstract reasoning, Raven's Progressive Matrices (RPM), abstrct visual reasoning*

Table of Content

- [Datasets](#datasets)
- [Learning Methods](#learning-methods)
- [Models](#models)
- [Representative works](#representative-works)

## Datasets

* Sandia matrices: a set of rules
* Synthetic RPMs: first-order logic
* D-Set and G-Set
* PGM: relation, object, attribute
* RAVEN: hierarchical structure (relation, attributes):

  > entity: type/shape, size, color
  > layout: number, position
  > component structure: L-R, U-D, O-IC, O-IG
  > relations: Constant, Progression, Arithmetic, Distribute Three
  >

  * I-RAVEN: -shortcut
  * RAVEN-FAIR: -bias

## Learning Methods

* supervised training
* auxiliary training
* contrastive training
* learning with an optimal trajectory
* data augmentation
* Disentangled representations, autoencoder
* unsupervised learning: pseudo label, pair-wise discriminator

## Models

* baselines: CNN, ResNet, LSTM
* relational reasoning：Relation Network
* hierarchical networks: pan