import math
from collections import Counter, defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.classes = set()
        self.class_word_counts = defaultdict(Counter)
        self.class_doc_counts = Counter()
        self.total_docs = 0
        self.vocabulary = set()
    
    def tokenize(self, text):
        return text.lower().split()
    
    def train(self, documents, labels):
        for doc, label in zip(documents, labels):
            self.classes.add(label)
            self.class_doc_counts[label] += 1
            self.total_docs += 1
            
            tokens = self.tokenize(doc)
            for token in tokens:
                self.class_word_counts[label][token] += 1
                self.vocabulary.add(token)
    
    def predict(self, text):
        tokens = self.tokenize(text)
        best_class = None
        best_score = float('-inf')
        
        for cls in self.classes:
            log_prob = math.log(self.class_doc_counts[cls] / self.total_docs)
            
            for token in tokens:
                word_count = self.class_word_counts[cls][token]
                total_words = sum(self.class_word_counts[cls].values())
                vocab_size = len(self.vocabulary)
                
                prob = (word_count + 1) / (total_words + vocab_size)
                log_prob += math.log(prob)
            
            if log_prob > best_score:
                best_score = log_prob
                best_class = cls
        
        return best_class
    
    def predict_proba(self, text):
        tokens = self.tokenize(text)
        scores = {}
        total_score = 0
        
        for cls in self.classes:
            log_prob = math.log(self.class_doc_counts[cls] / self.total_docs)
            
            for token in tokens:
                word_count = self.class_word_counts[cls][token]
                total_words = sum(self.class_word_counts[cls].values())
                vocab_size = len(self.vocabulary)
                
                prob = (word_count + 1) / (total_words + vocab_size)
                log_prob += math.log(prob)
            
            scores[cls] = math.exp(log_prob)
            total_score += scores[cls]
        
        return {cls: score / total_score for cls, score in scores.items()}

if __name__ == "__main__":
    train_docs = [
        "i love this movie",
        "great film excellent",
        "boring movie terrible",
        "hate this film",
        "amazing acting wonderful",
        "worst movie ever"
    ]
    
    train_labels = ["positive", "positive", "negative", "negative", "positive", "negative"]
    
    classifier = NaiveBayesClassifier()
    classifier.train(train_docs, train_labels)
    
    test_docs = ["i love this", "terrible movie", "amazing film"]
    
    for doc in test_docs:
        prediction = classifier.predict(doc)
        probabilities = classifier.predict_proba(doc)
        print(f"Text: '{doc}' -> {prediction} {probabilities}")
