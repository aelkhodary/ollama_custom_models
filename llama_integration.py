import requests

def submit_prompt(prompt):
    response_raw = requests.post('http://localhost:11434/api/generate', json={
        "model": "email-rewriter",
        "stream": False,
        "prompt": prompt,
    })

    response = response_raw.json()

    return response["response"]

rewritten_email = submit_prompt("This is the stupidest idea I've ever heard!")

print("Here is the reworded email:")
print(rewritten_email)