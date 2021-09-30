from sentence_transformers import SentenceTransformer, util
from datetime import datetime
import sys , os , gzip , csv, logging

# SELECT A DIFFERENT FOR SPECIFIED MODEL LATER.
# model_name = 'paraphrase-MiniLM-L12-v2'

local_model_location  = "/home/hrs2203/Desktop/GitHub/sent_sim_django/similarity_backend/user_component/comparision_engine/sent_bert"
local_model = "comparision_custom_model"
model_name = os.path.join( local_model_location , local_model )

embedding_model = SentenceTransformer(model_name)
# embedding_model.save( os.path.join( local_model_location , local_model ) )


def MultiSentenceBertComparision(sentSet1 : list, sentSet2: list) -> list:
    embedding_set_1 = embedding_model.encode(sentSet1, convert_to_tensor=True)
    embedding_set_2 = embedding_model.encode(sentSet2, convert_to_tensor=True)

    cosine_similarity = util.pytorch_cos_sim(embedding_set_1, embedding_set_2)

    return cosine_similarity.tolist()

    
