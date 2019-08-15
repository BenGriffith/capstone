# Load libraries
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def onehot_encoding(feature):
    values = np.array(feature)
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)

    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    
    return onehot_encoded

def convert_age_to_days(age):
    '''
    Converting value from AgeuponOutcome to age in number of days
    '''

    days_in_week = 7
    days_in_month = 30
    days_in_year = 365
    age_list = age.split()

    if age_list[1][0] == 'w':
        age_in_days = int(age_list[0]) * 7
    elif age_list[1][0] == 'm':
        age_in_days = int(age_list[0]) * 30
    elif age_list[1][0] == 'y':
        age_in_days = int(age_list[0]) * 365
    else:
        age_in_days = int(age_list[0])

    return age_in_days