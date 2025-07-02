import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",             # change if needed
    password="",             # add your password here if set
    database="resume_matcher"
)
cursor = db.cursor()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    return ' '.join([word for word in text.split() if word not in stop_words])