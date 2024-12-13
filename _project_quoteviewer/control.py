import json

from quote import Quote

class QuoteControl():
    def __init__(self):
        self.quotes = []
        self.total = len(self.quotes)

    def create(self):
        quote = input("Quote : ").lower()
        author = input("By: ").lower()

        quo = Quote(quote, author)
        self.quotes.append(quo)
        return

    def delete(self):
        author = input("Input the name of authour : ").lower()

        print(f"Quotes by -{author.capitalize} are - ")

        dict = {}
        i = 0

        for quote in self.quotes:
            if quote.get_author() == author:
                dict[i+1] = quote.get_quote()
            
        print("Select the number you want to delete : ")
        for key, value in dict:
            print(f"{key}. {value}")

        choice = int(input("Choose what you want to delete: "))

        for quote in self.quotes:
            if quote[choice] == quote.quote:
                self.quotes.remove(quote)
                print("Quote was removed !")
                return
            print("No such quote found")
            return

    def list(self):
        i = 0
        for quote in self.quotes:
            print(f"[{i+1}]. {quote.get_quote()} by {quote.get_author}")

        
    def backup(self):
        quote_dict = [quote.__dict__ for quote in self.quotes]
        file = open("quotes.json", "w")
        json.dump(quote_dict, file,default= str, indent = 4 )
        file.close()

        print("Backup successful !")

    def load(self):
        file = open("quotes.json", "r")
        content = file.read()
        cleandata = json.loads(content)
        self.quotes = []

        for quote in cleandata:
            quo = Quote(quote= quote["quote"], author= quote["author="])

            self.quotes.append(quote)
        

    def append(self):
        pass

    