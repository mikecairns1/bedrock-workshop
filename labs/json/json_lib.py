# 1 OPen json_lib.py
# 2 import statements
import os
import json
from json import JSONDecodeError
from langchain.llms.bedrock import Bedrock

# 3 Add function to create bedrock LangChain client
def get_llm():

    llm = Bedrock( #create a Bedrock llm client
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="ai21.j2-ultra-v1", #use the AI21 Jurassic-2 Ultra model
        model_kwargs = {"maxTokens": 1024, "temperature": 0.0 } #for data extraction, minimum temperature is best
    )

    return llm

# 4 Add the function to attempt converting the text results to a JSON object

def validate_and_return_json(response_text):
    try:
        response_json = json.loads(response_text) #attempt to load text into JSON
        return False, response_json, None #returns has_error, response_content, err 
    
    except JSONDecodeError as err:
        return True, response_text, err #returns has_error, response_content, err 

# 5 Add function to call Bedrock

def get_json_response(input_content): #text-to-text client function
    
    llm = get_llm()

    response = llm.predict(input_content) #the text response for the prompt
    
    return validate_and_return_json(response)

# 6 Save the file