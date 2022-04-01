import numpy as np
import pandas as pd

from wordcloud import WordCloud
from wordcloud import STOPWORDS

# base data
testing_data = '../data/testing.csv'
training_data = '../data/training.csv'
validation_data = '../data/validation.csv'


train = pd.read_csv(training_data)
validation = pd.read_csv(validation_data)
test = pd.read_csv(testing_data)

data = pd.concat([train, validation])


def deal_data():
    




