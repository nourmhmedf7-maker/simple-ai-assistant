import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"


def send_data(prompt):

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": api_key
    }

    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    data = response.json()

    try:
        response = requests.post(
            url,
            headers=headers,
            json=body
        )
        data = response.json()
        
        if response.status_code == 200:
            print(data["candidates"][0]["content"]["parts"][0]["text"])
            print("\n" + "─" * 48)

        else:
            print(f"status code : {response.status_code}")
            print(data["error"]["message"])

    except KeyError:
        print("key not founded")

    except IndexError:
        print("empty respond")

    except requests.exceptions.Timeout:
        print("The request timed out")

    except requests.exceptions.ConnectionError:
        print("Connection failed")

    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON response")






class AiModels:
    def __init__(self,name):
        self.name=name

    def talk(self):
        
        
        print()

        width = 48

        print("╔" + "═" * width + "╗")
        print("║" + " " * width + "║")
        print("║" + f"{self.name.upper()} AI ASSISTANT".center(width) + "║")
        print("║" + " " * width + "║")
        print("║" + "Your personal AI companion".center(width) + "║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        print()
        print("  [i] Type your message and press Enter.")
        print("  [i] Type 'exit' to end the conversation.")
        print()

        print("─" * 50)
        print("SYSTEM STATUS: READY".center(50))
        print("─" * 50)
        print()
        

        send_data("hi")

        print("\n" + "─" * 48)

        while True :


            prompt = input("\n  You  › ")
            

            if prompt.lower() == "exit":
                break

            send_data(prompt)




gemini = AiModels("gemini")

gemini.talk()