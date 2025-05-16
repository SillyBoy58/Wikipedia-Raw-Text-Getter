import wikipediaapi
import os

dirPath = path = os.path.dirname(__file__)

wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='WikiRawTextGetter/1.0 (merlin@example.com)',
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

userInput = input("Enter an article name: ")
p_wiki = wiki_wiki.page(userInput)
txtPath = os.path.join(path, f"{userInput}RawText.txt")

print("Page - Exists: %s" % p_wiki.exists())

if p_wiki.exists():
    print(f"Found page: {p_wiki.canonicalurl}")
    while True:
        saveFile = input(f"""Do you want to save the output into a file?
The output will be saved in: {txtPath}
(y/n): """)
        if saveFile == 'y':
            with open(txtPath, 'w', encoding='utf-8') as f:
                f.write(p_wiki.text)
                print(f"\nSuccessfully saved to: {txtPath}")
            break
        elif saveFile == 'n':
            print("\nArticle Text:\n")
            print(p_wiki.text)
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

else:
    print("Page not found OwO :3 UwU QwQ TwT >w<")