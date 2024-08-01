#  Data collection, preprocessing,  feautures extraction and evaluatiom model
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# create a sample dataset

data = [
    ("I love NLP", "Positive"),
    ("I hate the technology", "Negative"),
    ("it's okey , nothing special", "neutral")
]

# separate all the sentence and labels
sentences, labels = zip (*data)
# download the kits from the library which we have been imported
nltk.download('punkt')
nltk.download('stopwords')
# initialize the stopwords with passing the language
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    # remove the stop words and punctuation
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)
# preprocess for the sentence which we pass as data
preprocessed_sentences = [preprocess(sentence) for sentence in sentences]
# feature extraction
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(preprocessed_sentences)
# split the data into traings as well as test data for model training and evaluation
x_train, x_test, y_train, y_test = train_test_split(x,labels, test_size=0.2, random_state=42)
# train nave bayes classifier
classifier = MultinomialNB()
classifier.fit(x_train, y_train)
# we can write the code of prediction y from x
y_pred = classifier.predict(x_test)
# evaluating the model 
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division='warn')
print(f"Accuracy: {accuracy}")
print("Classification Report")
print(report)
