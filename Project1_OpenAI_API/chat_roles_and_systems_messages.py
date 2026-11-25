#!/usr/bin/env python3
# The examples mentioned in this code are inspired from DataCamp's track for Forward Deployed Engineers

import os
from openai import OpenAI  # https://developers.openai.com/api/reference/python

# Use case 1: Create a chat bot that teaches French in a few words
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system",
               "content": "You are a French language tutor. Your answer do not exceed 5 sentences."},

              {"role": "user",
               "content": "What are a few different ways to say Good morning in French and how do you use them?"}
              ],
    max_completion_tokens=100
)

# Extract the assistant's text response
print(response.choices[0].message.content)


# Use case 2: A chatbot that teaches Dutch and create a study plan
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=150,
    messages=[
        {"role": "system",
         "content": "You are a study planning assistant that creates plans for learning new skills."},
        {"role": "user",
         "content": "I want to learn to speak Dutch."}
    ]
)

print(response.choices[0].message.content)


# Use case 3: A study plan assistant with guardrails
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint - Case where the model answer with a detailed plan
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": sys_msg},
        {"role": "user", "content": "Help me learn to speak spanish."}
    ]
)

print(response.choices[0].message.content)


# Create a request to the Chat Completions endpoint - The system spot a non-language related skill
# and answers this is not their niche

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": sys_msg},
        {"role": "user", "content": "Help me learn to dance salsa."}
    ]
)

print(response.choices[0].message.content)

# Output
# Apologies, to focus on languages, we no longer create learning plans on other topics.


# Use case 4: Data Science tutor.
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a data science tutor"},
        {"role": "user", "content": "What is the difference between mutable and immutable objects? "}
    ]
)


# Use Case 5: Creating a chat for conversations with more guardrails
# Example conversation can be provided using the assistant role.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)

# Output:
# Greece is a southeastern European country known for its rich history and significant contributions to Western civilization, particularly in philosophy, politics, and the arts. It consists of the mainland and numerous islands, with Athens as the capital. Greece has a Mediterranean climate, famous archaeological sites like the Acropolis, and is renowned for its cuisine and beautiful landscapes. The official language is Greek, and the country is a member of the European Union.


# Use Case 6: Adding more guardrails
# Providing examples helps mitigate undesirable or inaccurate model responses, so they're a good practice in many use cases. However, adding more examples didn't really improve the response length. In this case, an example in the system message and a few user-assistant pairs would likely provide more optimal responses.

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add in the extra examples and responses
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        {"role": "user", "content": "Give me a quick summary of Benin."},
        {"role": "assistant", "content": "Benin is a country of the size of Belgium located on the West coast of Africa. Its beautiful capital is Cotonou."},
        {"role": "user", "content": "Give me a quick summary of Spain."},
        {"role": "assistant", "content": "Spain is a country that borders the South of France. Its capital is Madrid."},
        {"role": "user", "content": "Give me a quick summary of Mexico."},
        {"role": "assistant", "content": "Mexico is a country that borders the US. It is known for its cultural history and its capital is Mexico."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)

# Greece is a southeastern European country known for its rich ancient history and contributions to art and philosophy. The capital city is Athens, which is home to iconic landmarks like the Acropolis. Greece is also famous for its beautiful islands, Mediterranean cuisine, and vibrant culture.
