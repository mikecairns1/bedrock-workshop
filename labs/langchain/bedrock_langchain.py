# 1 Open bedrock_langchain.py

#2 Import statements
import os
from langchain.llms.bedrock import Bedrock

# 3 Initialize the LangChain Bedrock client
llm = Bedrock( #create a Bedrock llm client
    credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
    region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
    model_id="ai21.j2-ultra-v1" #set the foundation model
)

# 4 Set the prompt for the call to Bedrock
prompt = "What is the largest city in Vermont?"

# 5 Call the Bedrock API
response_text = llm.predict(prompt) #return a response to the prompt

#6 Display the response
print(response_text)

#7 Save the file