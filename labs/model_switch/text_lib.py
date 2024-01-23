import os
from langchain.llms.bedrock import Bedrock
def get_text_response(input_content): #text-to-text client function
    llm = Bedrock( #create a Bedrock llm client
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="anthropic.claude-v2:1", #set the foundation model
        model_kwargs={ #anthropic
            "max_tokens_to_sample": 512,
            "temperature": 0, 
            "top_k": 250, 
            "top_p": 1, 
            "stop_sequences": ["\n\nHuman:"] 
        }
    )
    return llm.predict(f"\n\nHuman:{input_content}\n\nAssistant:") #return a response to the prompt