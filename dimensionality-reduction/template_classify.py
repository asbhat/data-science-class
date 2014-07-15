from sklearn.cross_validation import cross_val_score
from sklearn.decomposition import RandomizedPCA
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

import os, sys
import random
#setup a standard image size; this will distort some images but will get everything into the same shape
STANDARD_SIZE = (300, 167)
def img_to_matrix(filename, verbose=False):
    """
    takes a filename and turns it into a numpy array of RGB pixels
    """
    img = Image.open(filename)
    if verbose==True:
        print "changing size from %s to %s" % (str(img.size), str(STANDARD_SIZE))
    img = img.resize(STANDARD_SIZE)
    img = list(img.getdata())
    img = map(list, img)
    img = np.array(img)
    return img

def flatten_image(img):
    """
    takes in an (m, n) numpy array and flattens it 
    into an array of shape (1, m * n)
    """
    s = img.shape[0] * img.shape[1]
    img_wide = img.reshape(1, s)
    return img_wide[0]

if __name__ == '__main__':

    img_dir = "images/"
    images = [img_dir+ f for f in os.listdir(img_dir)]
    random.shuffle(images)
    ### Right now this says the targe is true if the file has 'kittens' in the name.
    ### This means we are building a binary classifier of kitten or not.  Change this is so you can pass an argument 
    ### to build a classifier for any set of images.  Use sys.argv ('import sys' first)
    labels = np.array([1 if "kittens" in f.split('/')[-1] else 0 for f in images])
 
    data = []

    ### Apply transformation for each matrix
    for image in images:
      img = img_to_matrix(image)
      img = flatten_image(img)
      data.append(img)
 
    data = np.array(data)


    ### This creates a simpler representation of the images other than the raw pixels
    ### Change the number of components to see how this effects classification accuracy
    pca = RandomizedPCA(n_components=50)

    print "Original size of X", data.shape
    ### Transform your dataset `data` into a feature setX 
    X = pca.fit_transform(data)
    print "Reduced size of X", X.shape

    ### Setup a classifier (or multiple, play around with different models) 
    ### How much data do you have?  Do you think the relationships are linear?
    model = LogisticRegression(C = 5)

    ### Do some cross validation
    print "Components:", 50, np.mean(cross_val_score(model, X, labels, scoring='roc_auc'))



