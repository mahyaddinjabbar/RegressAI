import os
from openai import OpenAI

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("secrets.OPENAI_API_KEY"))

# Read the XML layout file
with open("app_code/activity_login.xml", "r", encoding="utf-8") as xml_file:
    xml_content = xml_file.read()

# Read the Android activity Java file
with open("app_code/LoginActivity.java", "r", encoding="utf-8") as java_file:
    activity_content = java_file.read()

# Construct the prompt
prompt = f"""

Below is an Android activity implementation in kotlin and its corresponding XML layout file. Using these files, generate testcases for regression testing.

Requirements: 
-Testcases should be ready to execute, 
-They should cover all the possible cases
-Include meaningful comments

Activity file content:
{activity_content}


XML Layout file content: 
{xml_content}

"""