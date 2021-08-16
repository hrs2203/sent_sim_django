import json
from sentence_transformers import SentenceTransformer, util

print("Loading Model")
model = SentenceTransformer('paraphrase-MiniLM-L12-v2')

# Two lists of sentences
sentences = [
    'The cat sits outside',
    'A man is playing guitar',
    'The new movie is awesome',
    'The dog plays in the garden',
    'A woman watches TV',
    'The new movie is so great'
]
print("Generating Embeddings")
embeddings = model.encode(sentences, convert_to_tensor=True)
print("Converting Embeddings")
embeddings_dict = dict()
for sent, emb in zip(sentences, embeddings):
    embeddings_dict[sent] = emb.tolist()
print("Saving Embeddings")
with open("saveSample.json", 'w') as saveTensor:
    json.dump( embeddings_dict, saveTensor , indent=2)




