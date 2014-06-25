"""
       Fitting naive bayes model, is fairly simple.  We want to estimate
       the probability of a document being one label or another

       We want the label that maximizes -> P (label | document)

       By Bayes rule, P(label | document) = P(document | label) * P(label)
       P(document | label) is the likelihood function
       P(label) is the prior

       We can find the label that maximizes P(label | document) by maximizing
       P(document | label) * P(label) so we need to compute
       P(document | label) and P(label)

       Under the NAIVE assumption, we assume all the words in the document are
       independent, so we can MULTIPLY their probabilities.
       So P(document | label) = P ( word_1 in doc | label) *
                                P ( word_2 in doc | label) * ... *
                                P ( word_n in doc | label)

       So we now just need to compute P ( word_i in doc | label) and P(label).

       P ( word_i in doc | label) is easy to compute, its just
       COUNT(word_i in doc) / COUNT(word_i with label L)

       So we iterate through our dataset. We count how often any word appears
       in a document with a certain label.

       If we have 3 email subject: "buy gold now", "send gold nigeria",
                                   "nigeria presidential election"
       and they are labeled for spam as follows:
          "buy gold now" : SPAM, "send gold nigeria": SPAM,
          "nigeria presidential election": NOT SPAM
       Then, for example, we saw 2/3 total spam documents, the word nigera
       3 times, twice in spam documents once not in a spam document.

       So P(nigeria | SPAM) =
          COUNT(nigeria in spam documents) / COUNT(spam documents) = 2/2
       P(gold | SPAM) =
          COUNT(gold in spam documents) / COUNT(spam documents) = 2/2
       P(buy | SPAM) =
          COUNT(gold in spam document) / COUNT(spam documents)

       So for every word we need to keep a counter of how many
       spam documents and non-spam documents it appeared in


       ------ Computing Priors ------

       Priors are also computed from the data.  We saw 2/3 spam documents,
       so the prior probability of a document being spam,
       without looking at the text is 2/3.  This is the uninformed prior
       as we are just setting it from the data, but if we had predisposed
       ideas on the spam distribution we could adjust it
       """

import numpy as np
import math
import pandas as pd
import string

class NaiveBayes():


  def __init__(self):

    """ Setup useful datastructures
        Feel free to change this
    """

    self._word_counts = {}  ## Table indexed on word + class, holds count(word + class)
    self._class_counts = {} ## Array of counts per class [ 143, 234 ]
    self._priors = {}


  def fit(self, X, Y):
    """Fit a Multinomial NaiveBayes model from the training set (X, y)



        Parameters
        ----------
        X : array-like of shape = [n_samples]
            The training input samples.

        Y : array-like, shape = [n_samples]

        Returns
        -------
        self : object
            Returns self.
    """
    for (x, y) in zip(X, Y):
      self._fit_instance(x, y)

    self._fit_priors()

  def _fit_priors(self):
    """Set priors based on data"""
    ##TODO##

  def _fit_instance(self, instance, y):
    """Train based on single samples       

     Parameters
        ----------
        instance : string = a line of text or single document
                   instance =  "This is not an insult"
                   instance = "You are a big moron"
        y : int = class of instance
                = 0 , 1 , class1, class2

    """
    ## Update counts on y
    ## Want to increment by word (in case same word in sentence > 1)
    
    ## Update counts on word + label y
    ## Use pair (word, y) as key and increment counts
    trans = string.maketrans("","")
    cleanInstance = instance.translate(trans, string.punctuation).split()

    for word in cleanInstance:
      try:
        self._word_counts[(y, word)] += 1
      except KeyError:
        self._word_counts[(y, word)] = 1
      try:
        self._class_counts[y] += 1
      except KeyError:
        self._class_counts[y] = 1


  def predict(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[int] = class per sample
    """

    return [self._predict_instance(x) for x in X]


  def predict_proba(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[array[ float, float ... ], ...] =  class probabilities 
                                                     per sample 
    """

    return [ self._predict_instance(instance) for instance in X ]

  def _predict_instance(self, instance):
    """ Return array of class predictions for samples
      Parameters
      ----------
        instance : string = a line of text or single document

        Returns
        -------
          : array[ float, float ... ] =  class probabilities 
    """
    ##TODO##
    classes = '???'
    return [self._compute_class_probability(instance, c) for
            c in classes]

  def _prior_prob(self, c):
    return self._priors[c]

  def _compute_class_probability(self, instance, c):
    """ Compute probability of instance under class c
        Parameters
        ----------
        instance : string = a line of text or single document

        Returns
        -------
          p : float =  class probability

      HINT : Often times, multiplying many small probabilities leads to 
      underflow, a common numerical trick is to compute the log probability.

      Remember, the log(p1 * p2 * p3) = log p1 + log p2 + log p3
    """
    ##TODO##
    return 0


if __name__ == '__main__':
  data = pd.read_csv(
    '/Users/aditya/Github/Data-Science-Class/sentiment-model/training.txt',
    sep='\t')
  model = NaiveBayes()
  model.fit(data.Phrase, data.Sentiment)

  print np.exp(model.predict_proba(["This is not an insult", 
                                    "You are a big moron moron moron"]))
