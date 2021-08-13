from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-MiniLM-L12-v2')

# Two lists of sentences
sentences1 = ['The cat sits outside',
             'A man is playing guitar',
             'The new movie is awesome']

sentences2 = ['The dog plays in the garden',
              'A woman watches TV',
              'The new movie is so great']

#Compute embedding for both lists
# print("Generating embeddings for sentences")
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
# print("Sent1 done")
embeddings2 = model.encode(sentences2, convert_to_tensor=True)
# print("Sent2 done")

#Compute cosine-similarits
# print("Computing cosine similarity")
cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

#Output the pairs with their score
# print("Results")
for i in range(len(sentences1)):
    print("{:30} : {:30} :: Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))
