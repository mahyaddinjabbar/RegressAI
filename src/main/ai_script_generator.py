import os
import sys
from openai import OpenAI

xml_path = sys.argv[1]
kt_path = sys.argv[2]

# OpenAI client with API key from environment variable.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# read XML layout file
with open(xml_path, "r", encoding="utf-8") as xml_file:
    xml_content = xml_file.read()

# read Kotlin activity file
with open(kt_path, "r", encoding="utf-8") as kt_file:
    activity_content = kt_file.read()

# the prompt
prompt = f"""
You are an expert Android QA automation engineer.

Using the following Android Activity and its XML layout file, generate comprehensive **Kotlin test cases** for regression testing using the **Espresso framework**.

### Requirements:
- The test cases must be executable Kotlin code using Espresso
- Use AndroidX imports
- Cover all critical UI interactions and edge cases
- Include tests for UI visibility, click actions, navigation, input validation, and dynamic content
- Include meaningful and concise comments
- Output should contain only the Kotlin code

### Activity file content:
{activity_content}

### XML Layout file content:
{xml_content}
"""

# Sending the prompt to OpenAI
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates test cases for Android applications."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
)

# Extract the response text
generated_test_cases = response.choices[0].message.content

# Save the generated test cases to a file
output_path = "generated_tests.robot"
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(generated_test_cases)

print(f"✅ Generated test cases saved to {output_path}")
