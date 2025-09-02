import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    ## capture inputs ##
    user_prompt = sys.argv[1]
    verbose = True if "--verbose" in sys.argv else False
    ## store inputs
    messages =  [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    print("=== Hello from womblex! ===")
    print("===========================")

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    if verbose : print(f"User prompt: {user_prompt}")
    print(response.text)
    if verbose : print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    if verbose : print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
