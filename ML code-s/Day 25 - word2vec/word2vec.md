```python
# importing packages
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities
```

```python
# importing dataset
df=pd.read_csv('jokes.csv');
```

```python
x=df['Question'].values.tolist()
y=df['Answer'].values.tolist()
```

```python
# Adding two futures as a corpus
# corpus(collection of text data or words)
corpus= x+y
```

```python
# creating token embedding
nltk.download("punkt") # pre-trained tokenization
tok_corp= [nltk.word_tokenize(sent.encode('utf-8').decode('utf-8')) for sent in corpus]
```

```python
# model of word2vec           
model = gensim.models.Word2Vec(tok_corp, min_count=1, size = 32)
```

```python
#model.save('testmodel')
#model = gensim.models.Word2Vec.load('test_model')
#model.most_similar('word')
#model.most_similar([vector])
```
