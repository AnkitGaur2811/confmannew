import re # for normalzing the text 
import nltk # For all the NLP work
from nltk.corpus import stopwords as st # for having stop words
from nltk.stem import WordNetLemmatizer # Wordlemmatizer
from keybert import KeyBERT # Key Bert



nltk.download('stopwords')
lmtzr = WordNetLemmatizer()


def createstoplist():
    stop_words = set(nltk.corpus.stopwords.words('english'))
    new_words = ["fig","figure","image","sample","using","show", "result", "large","also", "one", "two", "three","four", "five", "seven","eight","nine"]
    stop_words = list(stop_words.union(new_words))
    return stop_words

# Preprocess the text for keyword extraction
def pre_process(text,stop_words):
    # lowercase
    text=text.lower()
    #remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    # remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)
    ##Convert to list from string
    text = text.split()
    # remove stopwords
    text = [word for word in text if word not in stop_words]
    # remove words less than three letters
    text = [word for word in text if len(word) >= 3]
    # lemmatize
    text = [lmtzr.lemmatize(word) for word in text]
    return ' '.join(text)

def KeyBertExtractor(text):
    kw_model = KeyBERT()
    keywords = []
    x = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words="english")
    for i in x:
        keywords.append(i[0])
    y = kw_model.extract_keywords(text, keyphrase_ngram_range=(2, 2), stop_words="english")
    for i in y:
        keywords.append(i[0])
    return keywords


def keyword_extractor(papab):
    stop_words=createstoplist()
    abstract = pre_process(papab,stop_words)
    key1 = KeyBertExtractor(abstract)
    finalkeys = key1
    return finalkeys
