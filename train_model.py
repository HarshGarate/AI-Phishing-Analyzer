import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

print("Creating training data...")
# A small dummy dataset (0 = Safe, 1 = Phishing)
data = {
    'url_length': [22, 150, 35, 85, 20, 28, 31, 18],
    'has_ip': [0, 1, 0, 0, 0, 1, 0, 0],
    'has_at_symbol': [0, 1, 0, 1, 0, 0, 0, 0],
    'dot_count': [2, 5, 2, 4, 1, 3, 1, 1],
    'has_hyphen_domain': [0, 1, 0, 1, 0, 0, 1, 0],
    'label': [0, 1, 0, 1, 0, 1, 1, 0] 
}
df = pd.DataFrame(data)

X = df[['url_length', 'has_ip', 'has_at_symbol', 'dot_count', 'has_hyphen_domain']]
y = df['label']

print("Training Decision Tree model...")
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print("Saving model to 'models' folder...")
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/url_tree_model.pkl')

print("Success! url_tree_model.pkl is ready for Streamlit.")