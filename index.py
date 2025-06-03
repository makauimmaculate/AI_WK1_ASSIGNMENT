# 👋 Welcome Message
print("👋 Hey, I’m CryptoBuddy — your AI-powered financial sidekick!")
print("Ask me about profitable or sustainable cryptocurrencies! 💸🌱")
print("Type 'exit' to end the conversation.\n")

# 📊 Predefined Crypto Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# 🤖 Get User Input
def get_user_input():
    return input("You: ").lower()

# 🧠 Chatbot Logic
def chatbot_response(query):
    if "sustainable" in query or "eco" in query or "green" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "trending" in query or "profit" in query or "profitable" in query:
        candidates = [coin for coin in crypto_db
                      if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
        if candidates:
            print(f"CryptoBuddy: {candidates[0]} is looking strong for profits! 🚀")
        else:
            print("CryptoBuddy: Hmm, nothing seems super profitable at the moment. 🤔")

    elif "long-term" in query or "growth" in query:
        recommend = "Cardano"
        print(f"CryptoBuddy: {recommend} is trending up and has a top-tier sustainability score! 🚀")

    elif "help" in query:
        print("CryptoBuddy: You can ask things like:\n"
              "- 'Which crypto is trending?'\n"
              "- 'What's the most sustainable coin?'\n"
              "- 'What should I invest in for growth?'")

    elif "disclaimer" in query:
        print("CryptoBuddy: ⚠️ Crypto is risky—always do your own research!")

    else:
        print("CryptoBuddy: Sorry, I didn’t understand that. Try asking about trends, sustainability, or growth. 💡")

# 🔁 Start Chat Loop
while True:
    user_query = get_user_input()
    if "exit" in user_query:
        print("CryptoBuddy: Bye! Stay smart and crypto-safe! 🫡")
        break
    chatbot_response(user_query)
