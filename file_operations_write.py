with open ("story.txt", "a") as f:
    while True:
        text = input("What do you want to write (press q to exit)")
        if text == "q":
            break
        f.write(text+"\n")

