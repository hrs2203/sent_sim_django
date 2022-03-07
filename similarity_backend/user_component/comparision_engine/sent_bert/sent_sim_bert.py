from typing import Dict
from sentence_transformers import SentenceTransformer, util
from datetime import datetime
import os
import json

import torch
from torch._C import dtype

# SELECT A DIFFERENT FOR SPECIFIED MODEL LATER.
model_name = 'paraphrase-MiniLM-L12-v2'

# local_model_location = "/home/hrs2203/Desktop/GitHub/sent_sim_django/similarity_backend/user_component/comparision_engine/sent_bert"
# local_model = "comparision_custom_model"
# model_name = os.path.join(local_model_location, local_model)

embedding_model = SentenceTransformer(model_name)
# embedding_model.save( os.path.join( local_model_location , local_model ) )


def GetSaveFileName(user_id: int) -> str:
    """Data file name

    Args:
        user_id (int): user id

    Returns:
        str: save file location
    """
    file: str = os.path.join(
        local_model_location,
        "static_file",
        f"user_data_{user_id}.json"
    )
    return file


def SaveData(user_id: int, sentencs_pairs: list) -> str:
    """Save/update file for each users data

    Args:
        user_id (int): user id
        sentencs_pairs (list): sentence pair of sentence and reponse

    Returns:
        str: location of the stored file
    """

    # Generate embedding data
    new_body = dict()
    sentence_embeddings = embedding_model.encode(
        [i[0] for i in sentencs_pairs], convert_to_numpy=True
    ).tolist()
    # mold the data in desired format
    for [key, value], emb in zip(sentencs_pairs, sentence_embeddings):
        new_body[key] = [emb, value]

    file_path = os.path.join(
        local_model_location,
        "static_file",
        f"user_data_{user_id}.json"
    )

    # checking file existance, if not creating one
    if not os.path.exists(os.path.join(local_model_location, "static_file")):
        os.makedirs(os.path.join(local_model_location, "static_file"))

    if not os.path.exists(file_path):
        with open(file_path, "w") as file_obj:
            json.dump({"user_id": user_id, "body": {}}, file_obj, indent=2)

    # loading file and saving data to it
    file_content = {}
    with open(file_path, "r") as file_obj:
        file_content = json.load(file_obj)

     # Merging old and new data
    file_content["user_id"] = file_content.get("user_id", user_id)
    file_content["body"] = {**file_content.get("body", {}), **new_body}

    # saving data
    with open(file_path, "w") as file_obj:
        json.dump(file_content, file_obj, indent=2)

    return file_path


def LoadData(user_id: int) -> dict:
    """Load data saved for certain user

    Args:
        user_id (int): user id

    Returns:
        dict: saved data
    """

    file_path = os.path.join(
        local_model_location,
        "static_file",
        f"user_data_{user_id}.json"
    )

    # checking file existance, if not creating one
    if not os.path.exists(os.path.join(local_model_location, "static_file")):
        os.makedirs(os.path.join(local_model_location, "static_file"))

    if not os.path.exists(file_path):
        with open(file_path, "w") as file_obj:
            json.dump({"user_id": user_id, "body": {}}, file_obj, indent=2)

    # loading file and saving data to it
    file_content = {"user_id": user_id, "body": {}}
    with open(file_path, "r") as file_obj:
        file_content = json.load(file_obj)

    return file_content

def FormatSaveData(data: dict) -> list:
    data["body"] = [ [item, data["body"][item][1] ] for item in data["body"].keys() ]
    return data


def CompareAndOrder(new_sentences: list, db_sentences: dict) -> list:
    """Compare sentences and sort each col by the relevance

    Args:
        new_sentences (list): new sentences to compare
        db_sentences (dict): saved data in db, json["body"]

    Returns:
        list: sorted list with solutions
    """
    new_embeddings = embedding_model.encode(
        new_sentences, convert_to_tensor=True)
    saved_embeddings = torch.Tensor(
        [item[0] for item in db_sentences.values()]
    )
    for item in db_sentences.keys():
        db_sentences[item] = [item, db_sentences[item][1]]
    saved_list = list(db_sentences.values())

    comparisions = util.pytorch_cos_sim(new_embeddings, saved_embeddings)

    new_length = len(new_embeddings)
    saved_length = len(saved_embeddings)

    sim_dict = dict()

    for i in range(new_length):
        key = new_sentences[i]
        value = sorted([
            saved_list[j]+[float(comparisions[i][j])]
            for j in range(saved_length)
        ], key=lambda a: a[2])[::-1]
        sim_dict[key] = value

    return sim_dict


def MultiSentenceBertComparision(sentSet1: list, sentSet2: list) -> list:
    embedding_set_1 = embedding_model.encode(sentSet1, convert_to_tensor=True)
    embedding_set_2 = embedding_model.encode(sentSet2, convert_to_tensor=True)

    cosine_similarity = util.pytorch_cos_sim(embedding_set_1, embedding_set_2)

    return cosine_similarity.tolist()

# custom test
# MultiSentenceBertComparision(['nice day'],["good weather"])
# sent_pair = [
#     ["nice day", "nice weather"],
#     ["bad food", "poison"],
#     ["nice lecture","g"]
# ]
# # SaveData(1, sent_pair)
# l = LoadData(1)
# t = [i[0] for i in sent_pair]
# resp = CompareAndOrder(t, l['body'])
# for i in resp:
#     print(i, resp[i])
