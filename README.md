# Design and implementation of a task-based Q&A system based on TCM knowledge graph

## Group information
- **Group members**: Yuxin Chen & Ying Xu

## Introduction
The question answering system uses natural language as the interaction method, providing concise and effective answers to user's questions. The use of question answering systems for information retrieval meets the modern society's demand for efficient and accurate information retrieval, and the development of knowledge graph technology provides abundant data support for the advancement of question answering systems. The knowledge-based question answering system is based on the structured knowledge stored in the knowledge graph, which processes and understands natural language questions asked by users, searches for answers and returns them to the user. Traditional Chinese medicine (TCM) has accumulated profound and effective medical practice theories as China's traditional medicine. The research on task-based question answering system based on TCM knowledge graph mainly includes the following contents:

Firstly, this paper uses "Compendium of Materia Medica" as the full-text data basis, with herbs as the center, extracting effective knowledge information from TCM websites using web crawling technology, and structuring it to construct a TCM knowledge graph including six entity types and multiple relationship types.

Secondly, the extraction of TCM entities and the classification of their types from the user's natural language queries. In entity recognition, the training question is converted into a feature vector using an embedding layer, which is used as input to BiLSTM. Finally, the CRF layer constrains the result label and outputs the named entity recognition result. The model recognition accuracy is 98.73%. Naive Bayes classification is used to classify the other parts of the query after extracting the entities, resulting in a classification accuracy of 93.98%.

Finally, the key TCM entities and corresponding query types of the question are obtained, and after the entities are segmented and processed for similarity, the question is converted into a query language on the TCM knowledge graph, and information retrieval is performed on the TCM knowledge graph. Answers are generated according to the template and returned to the user.

Experimental results show that the task-based question answering system based on the TCM knowledge graph fully implements the process from data collection to question answering retrieval applications for TCM-related knowledge and can provide relatively accurate answers to users' natural language queries.               

## How to Contribute
Please note that this project is released with a [Contributor Code of Conduct](https://github.com/KingOfOrikid/Design-and-implementation-of-a-task-based-Q-A-system-based-on-TCM-knowledge-graph/blob/main/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.              
         
If you think you can help in any of these areas or in many areas we haven't thought of yet, then please take a look at our [Contributors' guidelines](https://github.com/KingOfOrikid/Design-and-implementation-of-a-task-based-Q-A-system-based-on-TCM-knowledge-graph/blob/main/CONTRIBUTING.md).          
           
## Contact us
If you want to report a problem or suggest an enhancement we'd love for you to [open an issue](../../issues) at this github repository because then we can get right on it. But you can also contact [Yuki(Yuxin)](https://github.com/KingOfOrikid) by email yuxin.yuki.chen@gmail.com.
