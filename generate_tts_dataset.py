from datasets import load_dataset
from gtts import gTTS
from pathlib import Path
import pandas as pd

# Step 1: Create audio folder
audio_dir = Path("audio")
audio_dir.mkdir(parents=True, exist_ok=True)

# Step 2: Load dataset from Hugging Face
print("Downloading dataset...")
dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train[:100]")

# Step 3: Filter valid text samples
texts = [item["text"].strip() for item in dataset if item["text"].strip()]

# Step 4: Generate audio
rows = []
for i, text in enumerate(texts):
    audio_path = audio_dir / f"sample_{i}.mp3"
    try:
        print(f"{i}] Generating: {text[:50]}...")
        tts = gTTS(text)
        tts.save(audio_path)
        print(f"Saved: {audio_path}")
        rows.append({"id": i, "text": text, "audio_path": str(audio_path)})
    except Exception as e:
        print(f"Failed on {i}: {e}")

# Step 5: Save metadata
df = pd.DataFrame(rows)
df.to_csv("tts_dataset.csv", index=False)
print("\n Done! CSV saved as 'tts_dataset.csv' and audio in '/audio'")
