from sentence_transformers import SentenceTransformer, util


# SELECT A DIFFERENT FOR SPECIFIED MODEL LATER.
model = SentenceTransformer('paraphrase-MiniLM-L12-v2')


def MultiSentenceBertComparision(sentSet1 : list, sentSet2: list):
    embedding_set_1 = model.encode(sentSet1, convert_to_tensor=True)
    embedding_set_2 = model.encode(sentSet2, convert_to_tensor=True)

    cosine_similarity = util.pytorch_cos_sim(embedding_set_1, embedding_set_2)

    return cosine_similarity

    
