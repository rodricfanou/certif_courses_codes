#!/usr/bin/env python3
# The examples mentioned in this code are inspired from DataCamp's track for Forward Deployed Engineers

# Use case 1: Ask Chatgpt to write a polite reply accepting an AI engineer job offer.

# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Write a polite reply accepting an AI Engineer job offer.",
        }
    ],
)

print(response.choices[0].message.content)


# Use case 2: Announce my new AI Engineer role on LinkedIn.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    # Specify the model
    model="gpt-4o-mini",
    messages=[
        # Assign the correct role
        {"role": "user", "content": "Announce my new AI Engineer role on LinkedIn."}
    ],
)

print(response.choices[0].message.content)


# Use case 3: Ask chatgpt for a quick productivity tip

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Quick productivity tip."}],
)

# Extract the content from the response
print(response.choices[0].message.content)


# Use case 4: Text manipulation

prompt = """
Update name to Carlos, pronouns to he/him, and job title to Senior Content Developer
in the following text

Joanne is a Content Developer at Greenhouse. Her favorite programming language is R, 
which she uses for her statistical analysis.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
)

# Extract the content from the response
print(response.choices[0].message.content)

# Response looks like:
# Carlos is a Senior Content Developer at Greenhouse. His favorite programing language
# is R which he uses for his statistical analysis.


# Use case 5: Text summarization

test = "Long text provided by the user"  # the text can be really long or not
prompt = f""" Summarize the customer support data into three key points {test} """

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Limit on the number of tokens the model will output/length of the response
    max_completion_tokens=30,
)

# Extract the content from the response
print(response.choices[0].message.content)


# Use case 6: Discuss planes rather than cars in the text below; enforce max token to 100

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt = """Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100,
)

# Extract and print the response text
print(response.choices[0].message.content)

# Output:
# A plane is a vehicle that is typically powered by jet engines or propellers. It has wings and is designed to carry passengers and/or cargo through the air. Planes have become a ubiquitous part of modern society and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Planes are often associated with freedom, independence, and mobility.


# Use case 7: Summarize a long text into 2 bullets

finance_text = "Long finance text"

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=400
)

print(response.choices[0].message.content)


# Use case 8: Compose the cost of the execution of a prompt

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")

# Output:
# Estimated cost: $0.0003492


# Use case 9: Text Generation

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """
Generate a product description for SonicPro headphones, including:
Active noise cancellation (ANC)
40-hour battery life
Foldable design
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=100,
    # Temperature varies from 0 to 2 - When closer to 0 it varies a little
    # when closer to 2, it varies a lot.
    temperature=0.75
)

print(response.choices[0].message.content)
