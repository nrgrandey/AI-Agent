import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types




def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Generate content using Google Gemini API")
    parser.add_argument("prompt", type=str, help="The prompt to generate content for")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    if len(args.prompt) < 1:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]


    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print(response.text)
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
