# make a program to open a file and read the contents, while reading the content update the dictionary where key is the word
# and value is the frequency and display the words with top 5 frequency

def main():
    freq = {}
    top_keys  = []

    file = open("text.txt", "r")
    content = file.read()
    content = content.lower().split()
    for x in content:
        if x in freq:
            freq[x] +=1
        else:
            freq[x] = 1

    print(freq)

    # freq has the freq now print the top 5
    word = ""
    max = 0

    for key, value in freq.items():
        if value > max:
            max = value
            word = key

    print(word)

    file.close()

if __name__ == "__main__":
    main()
