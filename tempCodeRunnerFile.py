import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=2):
    stop_words = set(stopwords.words("english"))
    word_frequencies = {}
    
    words = word_tokenize(text)
    for word in words:
        if word.lower() not in stop_words and word not in string.punctuation:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    max_freq = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_freq
    
    sentence_scores = {}
    sentences = sent_tokenize(text)
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]
    
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return " ".join(summarized_sentences)

text = input("enter your text : ")
summary = summarize_text(text)
print("Summary:")
print(summary)
