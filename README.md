# Django Backend for BTP Project : Semantic Similarity Comparision Engine.

# About Project

> for docs on approaches utilized please refer to this [link](./similarity_backend/user_component/comparision_engine/s7m1.md)

<details>

<summary> Progress </summary>

- Front End
    - [ ]  Home Page
    - [ ]  Authentication
        - [ ]  Single User
        - [ ]  Organization
    - [ ]  Comparison page ( For both Org and Individuals )
        - [ ]  Multiple sentence A and Multiple Sentence B ( Comparison )
            - [ ]  Inserting One by One
            - [ ]  Inserting with file upload in specific format
    - [ ]  Company registration page
        - [ ]  Upload file
    - [ ]  API Help Page


- Back End
    - [x]  DB
        - [x]  DB Models
        - [x]  DB Layer
    - [ ]  REST API layer
        - [ ]  For Interaction with front-end
        - [x]  For Interaction with other world
    - [x]  Comparison Engine Integration
----
- Comparison Engine
    - [x]  Corpus Based Algorithm - Embedding generator
    - [x]  Sent-Sim Algorithm - Embedding generator
    - [x]  Comparison Methods
        - [x]  One to One
        - [x]  One to Many
        - [x]  Many to Many
----
- Jupyter Notebook
    - [x] Make Notebook showing tests and results
    - [x] Download customer support sample files
    - [x] Try using Quora trained Sent-BERT, better question comparision

</details>

<br /> 

# References

1. Y. Li, D. McLean, Z. A. Bandar, J. D. O'Shea and K. Crockett, "Sentence similarity based on semantic nets and corpus statistics," in IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 8, pp. 1138-1150, Aug. 2006, doi: 10.1109/TKDE.2006.130.

2. Miller, G.A., 1995. WordNet: a lexical database for English. Communications of the ACM, 38(11), pp.39-41.

3. Reimers, N. and Gurevych, I., 2019. Sentence-bert: Sentence embeddings using siamese bert-networks. arXiv preprint arXiv:1908.10084.

4. Devlin, J., Chang, M.W., Lee, K. and Toutanova, K., 2018. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805.








