# capstone
Machine Learning Nanodegree Capstone Project

Every year, approximately 7.6 million companion animals end up in US shelters. Many animals are given up as unwanted by their owners, while others are picked up after getting lost or taken out of cruelty situations. Many of these animals find forever families to take them home, but just as many are not so lucky.

Approximately 2.7 million shelter animals are euthanized in the US every year.

In this multi-class classification problem, a dataset of intake information (breed, color, sex, age, etc.) provided by the Austin Animal Center will be used to train a supervised learning algorithm. The trained model will then be utilized to help predict the outcome (adoption, died, euthanasia, return to owner or transfer) of future shelter animals.

Knowing the predicted outcomes can help shelters identify and understand trends in animal outcomes. Such insights could help shelters focus their resources on specific animals who might need extra help finding a new home. For example, if the predicted outcome for a certain animal or breed in a shelter is euthanasia, the shelter could align their efforts to help see these euthanasia candidates find a new home.

I intend to follow the workflow outline below as closely as possible:
- Step 1: Problem Preparation
  - Load libraries
  - Load dataset
- Step 2: Data Summarization
  - Descriptive statistics such as .info(), .describe(), .head() and .shape
  - Data visualization such as histograms, density plots, box plots, scatter matrix and correlation matrix
- Step 3: Data Preparation
  - Data cleaning such as handling missing values
  - Feature preparation and data transforms such as one-hot encoding
- Step 4: Evaluate Algorithm(s)
  - Split-out validation dataset
  - Test options and evaluation metric
  - Spot check and compare algorithms
- Step 5: Improve Algorithm(s)
  - Algorithm tuning
  - Compare selected algorithm against Ensembles
- Step 6: Model Finalization
  - Predictions on validation / test dataset
