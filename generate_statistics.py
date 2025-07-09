import pandas as pd

# Load the dataset
df = pd.read_csv("tts_dataset.csv")

# Add a word count column
df["num_words"] = df["text"].apply(lambda x: len(str(x).split()))

# Print basic statistics
print("Total sentences:", len(df))
print("Total words:", df["num_words"].sum())
print("Average words per sentence:", round(df["num_words"].mean(), 2))
print("Maximum words in a sentence:", df["num_words"].max())
print("Minimum words in a sentence:", df["num_words"].min())

# Save the updated dataset
df.to_csv("tts_dataset_with_stats.csv", index=False)
print("Updated dataset saved as 'tts_dataset_with_stats.csv'")
