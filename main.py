def main():
    with open("/Users/arsh/workspace/github.com/Arshh-Mansuri/Bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    words = len(file_contents.split(" "))+1
    #print(words)
    file_contents=file_contents.lower()
    char_count = {}
    for char in  file_contents:
        if char.isalpha():
            if char in char_count:
                char_count[char]+=1
            else:
                char_count[char]=1
    #print(char_count)
    report(char_count,words)
def report(char_count,words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for key in char_count:
        print(f"The {key} character was found {char_count[key]} times")
    print("--- End report ---")

main()