# 1 Open showcase_lib.py
# 2 import statements
import os
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate

# 3 Add function to create a bedrock LangChain client

def get_llm():
    
    model_kwargs = { #AI21
        "maxTokens": 1024, 
        "temperature": 0, 
        "topP": 0.5, 
        "stopSequences": [], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    
    llm = Bedrock(
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="ai21.j2-ultra-v1", #set the foundation model
        model_kwargs=model_kwargs) #configure the properties for Claude
    
    return llm
    
# 4 Add function to create custom prompt
    
def get_prompt(user_input, template):
    
    prompt_template = PromptTemplate.from_template(template) #this will automatically identify the input variables for the template

    prompt = prompt_template.format(user_input=user_input)
    
    return prompt

# 5 Add function to call Bedrock

def get_text_response(user_input, template): #text-to-text client function
    llm = get_llm()
    
    prompt = get_prompt(user_input, template)
    
    return llm.predict(prompt) #return a response to the prompt

# 6 Save the file
