import google.generativeai as ai

API_KEY = 'AIzaSyApuwquT3nEv23TJtDEOg6MVllNc9A8pQs'
ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

while True:
    msg = input("You : ")
    if msg.lower() == "exit" or msg.lower()=="goodbye":
        print("BeyondAi : GoodBye!")
        break
    reponse = chat.send_message(msg)
    print("BeyondAi : ",reponse.text)
