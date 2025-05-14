import os
import sys
from openai import OpenAI

xml_path = sys.argv[1]
kt_path = sys.argv[2]

# Initialize OpenAI client with API key from environment variable.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read the XML layout file
with open(xml_path, "r", encoding="utf-8") as xml_file:
    xml_content = xml_file.read()

# Read the Kotlin activity file
with open(kt_path, "r", encoding="utf-8") as kt_file:
    activity_content = kt_file.read()

# Construct the prompt
prompt = f"""
Below is an Android activity implementation in Kotlin and its corresponding XML layout file. Using these files, generate test cases for regression testing.

Requirements:
- Test cases should be ready to execute
- They should cover all the possible cases
- Include meaningful comments as well

Activity file content:
{activity_content}

XML Layout file content:
{xml_content}
"""

# Send the prompt to OpenAI
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
