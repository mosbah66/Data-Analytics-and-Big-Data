import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Preprocess guest reviews
reviews = pd.read_csv("reviews.csv")
texts = reviews['comments'].dropna().astype(str).apply(lambda x: [word for word in word_tokenize(x.lower()) if word.isalpha()])
texts = texts.apply(lambda x: [word for word in x if word not in stopwords.words('english')])

# Build LDA model
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda_model = gensim.models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

# Print discovered topics
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx + 1}: {topic}")
