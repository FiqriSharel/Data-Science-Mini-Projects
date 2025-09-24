# Height, Weight, and Shoe Size Gender Prediction
This is a simple machine learning project that uses scikit-learn to classify gender (`male` or `female`) based on three features:
- Height (cm)  
- Weight (kg)  
- Shoe size (EU)  


# Dataset
The dataset is a small, manually created list of 30 samples with the following format:

python
X = [
    [170, 65, 42],  # height, weight, shoe size
    [160, 55, 38],
    ...
]

y = [
    'male',
    'female',
    ...
]

# Model
Uses scikit-learn's DecisionTreeClassifier.

Trains the model on the dataset.

Predicts gender based on new inputs.


# Requirement
- Python 3.8+
- scikit-learn

Install dependencies:
pip install scikit-learn

