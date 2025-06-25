import re
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# ✅ Simple keyword overlap
def simple_match_score(resume_text, jd_text):
    resume_words = set(clean_text(resume_text).split())
    jd_words = set(clean_text(jd_text).split())
    common = resume_words.intersection(jd_words)

    if not jd_words:
        return 0

    score = (len(common) / len(jd_words)) * 100
    return round(score, 2)

# 🤖 NLP-based Cosine Similarity
def nlp_match_score(resume_text, jd_text):
    vectorizer = CountVectorizer().fit_transform([resume_text, jd_text])
    vectors = vectorizer.toarray()
    cosine = cosine_similarity(vectors)
    score = cosine[0][1] * 100
    return round(score, 2)

# 🔁 Combined function
def get_matching_scores(resume_text, jd_text):
    simple_score = simple_match_score(resume_text, jd_text)
    nlp_score = nlp_match_score(resume_text, jd_text)

    return {
        "simple_match_score": f"{simple_score}%",
        "nlp_cosine_similarity": f"{nlp_score}%"
    }
