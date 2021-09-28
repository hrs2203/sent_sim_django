# Django Backend for BTP Project : Semantic Similarity Comparision Engine.

## About

for docs on approaches utilized please refer to this [link](./similarity_backend/user_component/comparision_engine/s7m1.md)

## Model Description

## Components

- Front End
    - [x]  Home Page
    - [x]  Authentication
        - [x]  Single User
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
    - [ ]  Comparison Engine Integration
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
    - [ ] Make Notebook showing tests and results
    - [ ] Download customer support sample files
    - [ ] Try using Quora trained Sent-BERT, better question comparision







