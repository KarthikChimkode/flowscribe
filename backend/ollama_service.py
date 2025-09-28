import requests
import json

class OllamaService:
    def __init__(self, host='http://localhost:11434'):
        self.url = f"{host}/api/generate"

    def generate(self, model: str, prompt: str, temperature: float = 0.7, max_tokens: int = 512) -> str:
        
        payload = {
            "model": model,
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True
        }
   
        

        combined_response = ""
        with requests.post(self.url, json=payload, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    try:
                        # Ollama streams lines prefixed with "data: ", remove it
                        line_str = line.decode('utf-8').strip()
                        if line_str.startswith("data: "):
                            line_str = line_str[len("data: "):]
                        # Ignore empty events
                        if line_str in ["[DONE]", ""]:
                            continue
                        json_obj = json.loads(line_str)
                        # 'response' field contains the text
                        if "response" in json_obj:
                            combined_response += json_obj["response"]
                    except json.JSONDecodeError:
                        continue  # skip invalid lines
        print("Prompt sent to Ollama:", prompt)
        print("Combined response from Ollama:", combined_response)
        return combined_response

if __name__ == "__main__":
    client = OllamaService()
    prompt = "Write a Python function to calculate factorial of a number."
    output = client.generate(model="codellama:7b", prompt=prompt)
    print("Final Generated Output:\n", output)
