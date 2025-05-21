import os
import sys
from openai import OpenAI

# Read file paths from command-line arguments
xml_path = sys.argv[1]
kt_path = sys.argv[2]

# Validate file paths
if not os.path.isfile(xml_path):
    print(f"❌ ERROR: The XML path provided is not a file or does not exist: {xml_path}")
    sys.exit(1)

if not os.path.isfile(kt_path):
    print(f"❌ ERROR: The Kotlin file path provided is not a file or does not exist: {kt_path}")
    sys.exit(1)

# Extract test file name from Kotlin activity filename
activity_file_name = os.path.basename(kt_path).replace(".kt", "")  # e.g., HomeActivity
test_file_name = f"{activity_file_name}Test.kt"

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read XML content
with open(xml_path, "r", encoding="utf-8") as xml_file:
    xml_content = xml_file.read()

# Read Activity (Kotlin) content
with open(kt_path, "r", encoding="utf-8") as kt_file:
    activity_content = kt_file.read()

# Prompt for GPT
prompt = f"""

Below is an Android activity implementation in kotlin and its corresponding XML layout file. Using these files, generate testcases for regression testing.

Requirements: 
-Testcases should be ready to execute, 
-They should cover all the possible cases
-Include meaningful comments as well

Activity file content:
{activity_content}


XML Layout file content: 
{xml_content}

"""

# Request GPT to generate test cases
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates test cases for Android applications."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
)

generated_test_cases = response.choices[0].message.content

# Save test cases to file
with open("generated_tests.kt", "w", encoding="utf-8") as output_file:
    output_file.write(generated_test_cases)

print(f"✅ Test cases saved to: {test_file_name}")
