def print_chat_box(message, sender="User"):
    border = "╭───╮"
    line = "│ {} │".format(message)
    end_line = "╰───╯"
    
    if sender == "User":
        print(f"{border}\n{line}\n{end_line}")
    elif sender == "Bot":
        print(f"{border}\n{line}\n{end_line}")

print_chat_box("Hello! Let's start by setting up your URL!", sender="Bot")

url = input("You: Paste the URL here: ")

socialType = input("You: FB or TW? ")

if socialType == "fb":
    url += "?utm_source=facebook"

elif socialType == "tw":
    url += "?utm_source=twitter-mo"

medium = input("You: Course or series? ")

if medium == "course":
    url += "&utm_medium=social-media&utm_campaign=course-"

elif medium == "series":
    url += "&utm_medium=social-media&utm_campaign=series-"

urlSlug = url.split('/')
content_between_last_two_slashes = urlSlug[-2]
url = url + content_between_last_two_slashes + "/"

if medium == "course":
    url += "&utm_content=course-"

elif medium == "series":
    url += "&utm_content=series-"

print_chat_box(f"Bot: Final URL with content: {url}{content_between_last_two_slashes}/", sender="Bot")

