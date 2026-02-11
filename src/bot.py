from datasets import load_dataset
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load data from openbmb/UltraChat 2.5GB https://huggingface.co/datasets/openbmb/UltraChat

# ds = load_dataset("openbmb/UltraChat", split="train", streaming=True)
#
# out_path = "pairs.jsonl"
# max_pairs = 2_000_000  # choose how big you want
#
# count = 0
# with open(out_path, "w", encoding="utf-8") as f:
#     for row in ds:
#         # Each row is a list of utterances alternating user/assistant
#         convo = row.get("data") or row.get("conversation") or row.get("dialogue") or row.get("messages")
#         if not convo or len(convo) < 2:
#             continue
#
#         # Make (user -> assistant) pairs: (0->1), (2->3), ...
#         for i in range(0, len(convo) - 1, 2):
#             user = str(convo[i]).strip()
#             bot  = str(convo[i + 1]).strip()
#             if user and bot:
#                 f.write(json.dumps({"input": user, "output": bot}, ensure_ascii=False) + "\n")
#                 count += 1
#                 if count >= max_pairs:
#                     break
#         if count >= max_pairs:
#             break


# Load pairs
BASE_DIR = os.path.dirname(__file__)
data_path = os.path.join(BASE_DIR, "pairs.jsonl")
inputs, outputs = [], []
with open(data_path, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        inputs.append(obj["input"])
        outputs.append(obj["output"])

# Build search index
vectorizer = TfidfVectorizer(stop_words="english", max_features=200000)
X = vectorizer.fit_transform(inputs)

def chat(message: str) -> str:
    q = vectorizer.transform([message])
    sims = cosine_similarity(q, X).ravel()
    best = sims.argmax()

    if sims[best] < 0.25:
        return "I’m not sure how to answer that yet."

    return outputs[best]


