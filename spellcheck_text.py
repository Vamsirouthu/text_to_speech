import pandas as pd
from textblob import TextBlob

# Load the original dataset
df = pd.read_csv("tts_dataset.csv")

# Apply spelling correction to each line
def correct_spelling(text):
    try:
        return str(TextBlob(text).correct())
    except Exception:
        return text  # fallback in case correction fails

print("Starting spelling correction...")
df["corrected_text"] = df["text"].apply(correct_spelling)

# Save corrected version
df.to_csv("tts_dataset_corrected.csv", index=False)
print("Spelling-corrected dataset saved as 'tts_dataset_corrected.csv'")
