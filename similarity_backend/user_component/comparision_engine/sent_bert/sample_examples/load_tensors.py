"""
# Tensor to list:
> a_list  = embeddings.tolist()
# list to Tensor:
> a_tensor = torch.Tensor(a_list).cuda()
"""

import json, torch
from sentence_transformers import util
from torch.functional import Tensor

sentences = [
    'The cat sits outside',
    'A man is playing guitar',
    'The new movie is awesome',
    'The dog plays in the garden',
    'A woman watches TV',
    'The new movie is so great'
]

tensors = []
fileObj : dict = dict()
with open("saveSample.json", 'r') as tensorFile:
    fileObj = json.load(tensorFile)

for sent in sentences:
    tensors.append( torch.Tensor(fileObj.get(sent, [])) )

for i in range(3):
    val = util.pytorch_cos_sim( tensors[i] ,  tensors[i+3] )
    val.squeeze_(dim=-1)
    print("{:30} : {:30} :: Score: {:.4f}".format(
        sentences[i], sentences[i+3],  val[0]
    ))


