# Simple translation script between English and 5 Ugandan languages

translations = {
    "How are you?": {
        "Luganda": "Oli otya?",
        "Runyankole": "Oli ota?",
        "Ateso": "Ijakit?",
        "Lugbara": "Ifo ini?",
        "Acholi": "Itye nining?"
    },
    "Good morning": {
        "Luganda": "Wasuze otya nno?",
        "Runyankole": "Oraire ota?",
        "Ateso": "Ejaii itunga?",
        "Lugbara": "Ezo ni?",
        "Acholi": "Otyeno ber?"
    },
    "Thank you": {
        "Luganda": "Webale",
        "Runyankole": "Webare",
        "Ateso": "Akile",
        "Lugbara": "Afoyo",
        "Acholi": "Apwoyo"
    }
}

languages = ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"]

def main():
    print("Please choose the source language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi)")
    source = input("Source language: ").strip().title()

    if source not in languages:
        print("Invalid source language.")
        return

    print("Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi)")
    target = input("Target language: ").strip().title()

    if target not in languages:
        print("Invalid target language.")
        return

    if source == target:
        print("Source and target languages must be different.")
        return

    text = input("Enter the text to translate:\n").strip()

    # Translation logic
    found = False
    if source == "English":
        if text in translations:
            translated = translations[text].get(target, "Translation not available.")
            found = True
    elif target == "English":
        for eng_text, local_map in translations.items():
            if local_map.get(source) == text:
                translated = eng_text
                found = True
                break
    else:
        for eng_text, local_map in translations.items():
            if local_map.get(source) == text:
                translated = local_map.get(target, "Translation not available.")
                found = True
                break

    if found:
        print(f"Translation in {target}: {translated}")
    else:
        print("Sorry, translation not found or supported.")

if __name__ == "__main__":
    main()
