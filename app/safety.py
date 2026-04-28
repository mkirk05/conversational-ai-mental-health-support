CRISIS_KEYWORDS = [
    "kill myself",
    "killing myself",
    "suicide",
    "end my life",
    "want to die",
    "no reason to live",
    "hurt myself",
    "self harm",
    "can't go on",
    "hurt someone",
    "cause harm"
]

def check_crisis(text):
    text = text.lower()
    return any(keyword in text for keyword in CRISIS_KEYWORDS)

def crisis_response():
    return(
        "I'm really sorry you're feeling this way. You don't have to go through this alone.\n"
        "If you are in immediate danger, please call emergency services (999)\n"
        "You can contact Samaritans (UK) at 116 123 or visit https://www.samaritans.org.\n"
        "They are available 24/7 and can provide support."
    )

def helpline():
    return(
        "Support & Help Information\n"
        "If you need support, you are not alone\n"
        "\nSamaritans (UK)\n"
        "Call: 116 123 (24/7)\n"
        "Website: https://www.samaritans.org\n"
        "\nEmergency\n"
        "If you are in immediate danger, call 999\n"
        "If you really need help but do not think it is an emergency call 111\n"
        "\nTalking helps\n"
        "You could speak to:\n"
        "- A trusted friend or family member\n"
        "- Your GP\n"
        "- A mental health professional\n"
        "\nThis application is not a medical service, but always available\n"
    )