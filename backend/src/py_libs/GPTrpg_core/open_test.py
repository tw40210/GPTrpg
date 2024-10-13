import openai
from src.py_libs.GPTrpg_core.env import api_key

openai.api_key = api_key

def getChatGPTResponse(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages = messages,
        temperature=1)
    return response['choices'][0]['message']['content'] # type: ignore


if __name__ == '__main__':
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you tell me a joke?"}
    ]
    print(getChatGPTResponse(messages))
