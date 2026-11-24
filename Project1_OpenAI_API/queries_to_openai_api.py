#!/usr/bin/env python3

## Example 1: Ask Chatgpt to write a polite reply accepting an AI engineer job offer.

# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", 
     "content": "Write a polite reply accepting an AI Engineer job offer."}]
)

print(response.choices[0].message.content)



## Example 2: Announce my new AI Engineer role on LinkedIn.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  # Specify the model
  model="gpt-4o-mini",
  messages=[
    # Assign the correct role
    {"role": "user", 
     "content": "Announce my new AI Engineer role on LinkedIn."}]
)

print(response.choices[0].message.content)



## Example 3: Ask chatgpt for a quick productivity tip

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "Quick productivity tip."}]
)

# Extract the content from the response
print(response.choices[0].message.content)



## Example 4: 

prompt = """
Update name to Carlos, pronouns to he/him, and job title to Senior Content Developer
in the following text

Joanne is a Content Developer at Greenhouse. Her favorite programming language is R, 
which she uses for her statistical analysis.
"""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}]
)

# Extract the content from the response
print(response.choices[0].message.content)

# Response looks like:
# Carlos is a Senior Content Developer at Greenhouse. His favorite programing language
# is R which he uses for his statistical analysis. 




## Example 5: Text summarization

test= "Long text provided by the user"
prompt = f""" Summarize the customer support data into three key points {test} """

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}]
)

# Extract the content from the response
print(response.choices[0].message.content)

