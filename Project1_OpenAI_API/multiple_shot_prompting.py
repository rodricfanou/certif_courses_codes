#!/usr/bin/env python3
# The examples mentioned in this code are inspired from DataCamp's track for Forward Deployed Engineers

import os
from openai import OpenAI

# Use case 1: Zero shot prompting
# Apart from answering questions, transforming text, and generating new text,
# OpenAI's models can also be used for classification tasks, such as
# categorization and sentiment analysis.

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Define a multi-line prompt to classify sentiment
prompt = """Classify the sentiment given by each of those cases using the numbers 1 - 5 (positive to negative):
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100
)

print(response.choices[0].message.content)

# output:
# 1. Unbelievably good! - 5
# 2. Shoes fell apart on the second use. - 1
# 3. The shoes look nice, but they aren't very comfortable. - 3
# 4. Can't wait to show them off! - 5


# Use case 2: One shot prompting

# We create the client for each case to make sure it is a new one.
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Add the example to the prompt
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5 (positive)
2. Unbelievably good! =
3. Shoes fell apart on the second use. =
4. The shoes look nice, but they aren't very comfortable. =
5. Can't wait to show them off! = """

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)

print(response.choices[0].message.content)

# Output
# Here are the sentiment classifications:

# 1. Love these! = 5 (positive)
# 2. Unbelievably good! = 5 (positive)
# 3. Shoes fell apart on the second use. = 1 (negative)
# 4. The shoes look nice, but they aren't very comfortable. = 3 (neutral)
# 5. Can't wait to show them off! = 5 (positive)


# Use case 3: Few-shot prompting: all the examples!
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Add the final example
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 
6. Can't wait to show them off! = """

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)
