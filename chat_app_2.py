from app.classifier import predict_emotion
from app.response_generator_2 import generate_response, continue_conversation
from app.safety import check_crisis, crisis_response
import operator as op

print("Mental Health AI Chat (type 'quit' or 'q' to exit)\n")

conversation_history=[]
more_info = "I'm here to support you and listen. Would you be able to tell me more about how you are feeling?"
not_relevant = "I'm sorry I am unable to help with that. I'm here to support you and listen. If you'd like to share how you're feeling, I'm here for that."

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit" or user_input.lower() == "q":
        print("Chat ended. If you need support, please consider reaching out to a professional or a helpline.")
        exit()

    if check_crisis(user_input):
        print("\nAI:", crisis_response(), "\n")
        exit()

    emotion = predict_emotion(user_input)
    reply = generate_response(user_input, emotion)

    if reply == "ALERT":
        print("\nAI:", crisis_response(), "\n")
        exit()
    
    if op.contains(reply, more_info) or op.contains(reply, not_relevant):
        print(f"AI: {reply}\n")
            
        conversation_history.append({
            "user": user_input,
            "ai": reply
        })
        
    else:
        print(f"\n Detected emotion: {emotion}")
        print(f"AI: {reply}\n")

        conversation_history.append({
            "user": user_input,
            "ai": reply
        })
        break

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit" or user_input.lower() == "q":
        print("Chat ended. If you need support, please consider reaching out to a professional or a helpline.")
        exit()

    if check_crisis(user_input):
        print("\nAI:", crisis_response(), "\n")
        exit()

    reply = continue_conversation(user_input, emotion, conversation_history)

    if reply == "ALERT":
        print("\nAI:", crisis_response(), "\n")
        exit()
    
    print(f"AI: {reply}\n")

    conversation_history.append({
        "user": user_input,
        "ai": reply
    })
