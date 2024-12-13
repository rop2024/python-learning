class Quote:
    def __init__(self, quote, author = "Internet"):
        self.__quote = quote
        self.__author = author

    def set_quote(self, quote):
        self.__quote = quote

    def set_authour(self, author):
        self.__author = author

    def get_quote(self):
        return self.__quote
    
    def get_author(self):
        return self.__author
