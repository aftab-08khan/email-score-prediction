import pandas as pd

# Define the dataset
data = {
    "email_description": [
        "Hi John, we have a new tech role at our company...",
        "Dear Jane, I hope this email finds you well...",
        "Hey Alice, just wanted to give you a quick update...",
        "Win a free iPhone! Click here...",
        "Your account has been compromised. Reset now...",
        "Thank you for your recent purchase!",
        "Join our webinar on AI and machine learning...",
        "Congratulations! You've won a $1000 gift card...",
        "Reminder: Your appointment is tomorrow at 10 AM...",
        "Exclusive offer: 50% off on all products...",
    ],
    "score": [8, 9, 7, 2, 1, 6, 8, 3, 7, 4],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("email_score_dataset.csv", index=False)

print("Dataset created successfully!")