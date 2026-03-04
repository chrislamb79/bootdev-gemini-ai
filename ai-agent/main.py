def main():
    print("Hello from ai-agent!")
    import os
    from dotenv import load_dotenv
    import argparse

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise ValueError('API Key is not present')
    
    from google import genai

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Gemini AI")
    parser.add_argument("user_prompt", type=str, help="Ask a question...")
    args = parser.parse_args()

    from google.genai import types
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages
    )
    if (response.usage_metadata) == None:
        raise ValueError('No response, potential failed API request')
    else:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)
        

if __name__ == "__main__":
    main()
