from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

app = FastAPI()

from openai import AzureOpenAI

from transformers import BertTokenizerFast, AutoModelForCausalLM, pipeline

# Machine leaning model
# Initialize the NER pipeline
ner = pipeline('ner', grouped_entities=True)
#test sentence
sentence = 'Scott is using his iPhone in the office. The office is in Glasgow.'

def get_entities(sentence):
    ner_results = ner(sentence)
    for i in ner_results:
        sentence = sentence.replace(i['word'], i['entity_group'])
    return sentence

# Azure openAI request
# Parameters
client = AzureOpenAI(
  azure_endpoint = "https://hkust.azure-api.net",
  api_version = "2023-05-15",
  api_key = "f0f00b34e41f4bb4b68ad79231843c9e" #put your api key here
)

# Function
def get_response(message, instruction):
    response = client.chat.completions.create(
		model = 'gpt-35-turbo',
        temperature = 1,
        messages = [
            {"role": "system", "content": instruction},
            {"role": "user", "content": message}
        ]
    )
    return response

#Backend
#Rounting
origins = [
    "http://localhost:3000",  # React app
    "http://localhost:8000",  # FastAPI server (change if needed)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#get input in <CustomInput> and return the result in <CustomOutput>
class Sentence(BaseModel):
    sentence: str

@app.post("/sentence")
async def read_sentence(sentence: Sentence):
    result = get_entities(sentence.sentence)
    ans = get_response(result, "You are a data analysis programmer.")
    return {"sentence": result, "ans": ans.choices[0].message.content}

   

if __name__ == "__main__":
    ans = get_response("give me an example of pandas import", "You are a data analysis programmer.")
    print(ans)
    ans = ans.choices[0].message.content
    print(ans)