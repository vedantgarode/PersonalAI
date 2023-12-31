from fastapi import FastAPI
import openai
import os 
app = FastAPI()

openai.api_key = "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"
@app.get("/")
async def root():
   return {"message": "Hello World"}


@app.get("/convo")
async def convo():
   
   response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
         {"role": "system", "content": "You are a helpful assistant."},
         {"role": "user", "content": "Who won the world series in 2020?"},
         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
         {"role": "user", "content": "Where was it played?"}
      ]
   )

   return(response['choices'][0]['message']['content'])