import streamlit as st
from app.classifier import predict_emotion
from app.response_generator_2 import generate_response, continue_conversation
from app.safety import check_crisis, crisis_response, helpline
import operator as op

st.set_page_config(page_title="Mental Health AI chat")

#Session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

if "emotion" not in st.session_state:
    st.session_state.emotion = None

if "stage" not in st.session_state:
    st.session_state.stage = "initial"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_help" not in st.session_state:
    st.session_state.show_help = False

if "chat_active" not in st.session_state:
    st.session_state.chat_active = True

if "crisis_triggered" not in st.session_state:
    st.session_state.crisis_triggered = False

#Header
st.title("Mental Health AI Assistant")

col1, col2 = st.columns([8,1])

with st.sidebar:
    st.header("Help & Support")

    button_label = "Hide Help" if st.session_state.show_help else "Show Help"

    if st.button(button_label):
        st.session_state.show_help = not st.session_state.show_help
        st.rerun()
    
    if st.session_state.show_help:
        st.info(helpline())

#Introduction message

if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "Hi, I'm here to listen. You can talk to me about how you're feeling.\n\n"
            "Anything said within this chat is not a medical diagnosis, but I'll try to support you.\n\n"
            "For help information, open the sidebar"
        )
    })

# Display chat

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

#Input
user_input = None
if st.session_state.chat_active:
    user_input = st.chat_input("Type your message...")

if user_input:

    #show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("User"):
        st.write(user_input)

    #safety check
    if check_crisis(user_input):
        response = crisis_response()

        st.session_state.messages.append({
            "role": "assistant", 
            "content": response})
        
        st.session_state.chat_active = False
        st.session_state.crisis_triggered = True

        st.rerun()
    
    more_info = "I'm here to support you and listen. Would you be able to tell me more about how you are feeling?"
    not_relevant = "I'm sorry I am unable to help with that. I'm here to support you and listen. If you'd like to share how you're feeling, I'm here for that."

    #Initial stage
    if st.session_state.stage == "initial":

        emotion = predict_emotion(user_input)
        reply = generate_response(user_input, emotion)

        if reply == "ALERT":
            response = crisis_response()
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response
            })
            
            st.session_state.chat_active = False
            st.session_state.crisis_triggered = True

            st.rerun()
        
        st.session_state.conversation_history.append({
            "user": user_input,
            "ai": reply
        })

        st.session_state.emotion = emotion

        #Check if to continue with initial stage
        if op.contains(reply, more_info) or op.contains(reply, not_relevant):
            st.session_state.stage = "initial"
        else:
            st.session_state.stage = "conversation"
        
        response = reply

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
    
    else:
        reply = continue_conversation(
            user_input,
            st.session_state.emotion,
            st.session_state.conversation_history
        )

        if reply == "ALERT":
            response = crisis_response()

            st.session_state.messages.append({
                "role": "assistant", 
                "content": response
            })
            
            st.session_state.chat_active = False
            st.session_state.crisis_triggered = True

            st.rerun()

        st.session_state.conversation_history.append({
            "user": user_input,
            "ai": reply
        })

        response = reply

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    #Display AI response
    with st.chat_message("assistant"):
        st.write(response)

#chat ended message 
if not st.session_state.chat_active:
    if st.session_state.crisis_triggered:
        st.error("This chat has ended. If you feel you need immediate help call 999")
    else:
        st.warning("Chat has ended. Start a new chat if you would like to talk about another problem.")

#Controls

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("New chat"):
        st.session_state.conversation_history = []
        st.session_state.messages = []
        st.session_state.emotion = None
        st.session_state.stage = "initial"
        st.session_state.chat_active = True
        st.session_state.crisis_triggered = False
        st.rerun()

with col2:
    if st.session_state.chat_active and not st.session_state.crisis_triggered:
        if st.button("End Chat"):

            st.session_state.chat_active = False

            st.session_state.messages.append({
                "role": "assistant",
                "content":(
                    "This chat has ended\n\n"
                    "If you feel you need support, consider speaking to a professional.\n\n"
                    "You can contact Samaritans at 116 123."
                )
            })

            st.rerun()

#Footer
st.markdown("---")
st.markdown(
    "If you need support, contact **Samaritans (UK) - 116 123** or visit https://www.samaritans.org"
)
