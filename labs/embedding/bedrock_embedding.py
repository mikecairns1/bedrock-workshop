# 1 Open bedrock_embedding.py
# 2 import statements
from langchain.embeddings import BedrockEmbeddings
from numpy import dot
from numpy.linalg import norm

# 3 Initialize the Bedrock Embeddings LangChain client
#create an Amazon Titan Embeddings client
belc = BedrockEmbeddings()

# 4 Define the classes to store embeddings and the comparison results
class EmbedItem:
    def __init__(self, text):
        self.text = text
        self.embedding = belc.embed_query(text)

class ComparisonResult:
    def __init__(self, text, similarity):
        self.text = text
        self.similarity = similarity

# 5 Define the function to compare the similarity of two vectors
def calculate_similarity(a, b): #See Cosine Similarity: https://en.wikipedia.org/wiki/Cosine_similarity
    return dot(a, b) / (norm(a) * norm(b))
    
# 6 Build a list of embeddings from the items.txt file

#Build the list of embeddings to compare
items = []

with open("items.txt", "r") as f:
    text_items = f.read().splitlines()

for text in text_items:
    items.append(EmbedItem(text))

# 7 Compare embeddings and display lists to show how similar or different the various texts are

for e1 in items:
    print(f"Closest matches for '{e1.text}'")
    print ("----------------")
    cosine_comparisons = []
    
    for e2 in items:
        similarity_score = calculate_similarity(e1.embedding, e2.embedding)
        
        cosine_comparisons.append(ComparisonResult(e2.text, similarity_score)) #save the comparisons to a list
        
    cosine_comparisons.sort(key=lambda x: x.similarity, reverse=True) # list the closest matches first
    
    for c in cosine_comparisons:
        print("%.6f" % c.similarity, "\t", c.text)
    
    print()

# 8 Save the file

