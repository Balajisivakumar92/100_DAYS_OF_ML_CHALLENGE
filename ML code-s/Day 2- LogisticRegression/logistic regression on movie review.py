# importing the packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# data preprocessing
df = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
df.dropna(inplace=True)
df["Postive rated"]=np.where(df['sentiment']>0,1,0)
#df.loc[df["Postive rated"] == 1,"Postive rated"]='good feedback'
#df.loc[df["Postive rated"] == 0,"Postive rated"]='bad feedback'
X_train, X_test, y_train, y_test = train_test_split(df['review'],df['Postive rated'],random_state=0)

# converting text into number's using CountVectorizer
vect=CountVectorizer(min_df=5,ngram_range=(1,2)).fit(X_train)
X_train_vetorised=vect.transform(X_train)

# model fitting
model=LogisticRegression()
model.fit(X_train_vetorised,y_train)

# model prediction
predictions=model.predict(vect.transform(X_test))

# Accuracy of the model
print ("AUC:",roc_auc_score(y_test,predictions))

# coefficient or weight
feature_name=np.array(vect.get_feature_names())
sort_coeff=model.coef_[0].argsort()
print ("small coeff : {}",format(feature_name[sort_coeff[:10]]))
print ("large coeff : {}",format(feature_name[sort_coeff[:-12:-1]]))

# user manual testing
testing=raw_input("Enter the sentence for testing: ")
y_hat = (model.predict(vect.transform([testing])))
if y_hat == [1]:
    print "Feedback Positive: GOOD MOVIE 😍😍😍😍 👏👌 "
else:
    print "Feedback Negative: BAD MOVIE 😟😏😠😤 👎👎👎"
