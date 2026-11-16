"""
AI Meme Caption Generator
Lightweight keyword + template based funny caption generator.
Works offline. Easy to extend.
"""

import random
import re


# Templates (you can keep adding more)
TEMPLATES = [
    "When {desc}... me: {reaction}",
    "Nobody:\nAbsolutely nobody:\nMe after {desc}: {reaction}",
    "{desc}? Mere dimaag mein sirf {reaction}",
    "Expectation: {desc}\nReality: {reaction}",
    "Boss: {desc}\nMe: {reaction}",
    "That moment when {desc} and you just {reaction}",
    "POV: {desc}\nMy brain: {reaction}",
    "Me trying to {desc}: {reaction}",
    "Life after {desc}: {reaction}",
    "Everyone else: normal\nMe after {desc}: {reaction}",
]

REACTIONS = [
    "main toh gayab",
    "scene on hai",
    "kya bakchodi hai ye",
    "bhai ye kya ho raha hai",
    "full confusion",
    "brain 404 not found",
    "main kya karun ab",
    "silent treatment",
    "internal screaming",
    "just vibing in chaos",
    "this is fine",
    "send help",
    "why is life like this",
    "main nahi de raha exam",
    "system failure",
    "error 500",
    "bhai mat puch",
    "bas ho gaya aaj ka",
    "main so raha hu",
    "full drama mode",
]

HINGLISH_EXTRA = [
    "Arre bhai {desc} dekh ke mood off",
    "Ye {desc} dekh ke lagta hai zindagi cheat code use kar rahi hai",
    "Jab {desc} ho toh samajh lo universe tera mazak udha raha hai",
    "{desc} = instant depression button",
    "Bhai {desc} ke baad toh therapy chahiye",
]


def clean_desc(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


def generate_captions(description: str, n: int = 5):
    desc = clean_desc(description)
    if not desc:
        return ["Bhai kuch toh likh de situation ka"]

    captions = []

    # Template based
    for _ in range(n - 1):
        template = random.choice(TEMPLATES)
        reaction = random.choice(REACTIONS)
        caption = template.format(desc=desc, reaction=reaction)
        captions.append(caption)

    # One hinglish extra
    captions.append(random.choice(HINGLISH_EXTRA).format(desc=desc))

    random.shuffle(captions)
    return captions


def main():
    print("=" * 55)
    print("   AI Meme Caption Generator")
    print("=" * 55)
    print("Describe the meme situation / image in short.")
    print("Example: 'exam result aaya' or 'salary day pe bank balance'")
    print()

    while True:
        desc = input("Describe situation (or 'quit'): ").strip()
        if desc.lower() in ['quit', 'exit', 'q']:
            break
        if not desc:
            continue

        print("\nGenerated Captions:\n")
        captions = generate_captions(desc, n=5)
        for i, cap in enumerate(captions, 1):
            print(f"{i}. {cap}")
            print()
        print("-" * 40)


if __name__ == "__main__":
    main()
