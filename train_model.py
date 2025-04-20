import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("data/enhanced_hr_email_validation_dataset.csv")

# Ensure the dataset is loaded correctly
print("Columns in the dataset:", df.columns)

# Define the feature and target variables
X = df["email_description"]  # Email descriptions
y = df["is_valid"]  # The target variable (is_valid)

# Convert text data into numeric features using TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the trained model and vectorizer
joblib.dump(model, "model/email_category_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")
