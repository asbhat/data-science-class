import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model():
    train = pd.read_csv('training.txt', sep='\t')
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(train.Phrase)

    model = MultinomialNB().fit(X_train, list(train.Sentiment))
    return model, vectorizer


model, vec = train_model()
def is_positive(text):
    test = vec.transform([text])
    return model.predict_proba(test)[0][1]


if __name__ == '__main__':
    print is_positive("So good!")
    print is_positive("So terrible!")
