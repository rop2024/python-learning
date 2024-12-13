from playlist import Playlist as pl

class Manager:
    def __init__(self):
        # making a list of Playlist object's addresses
        self.__pls = []
        self.__total = len(self.__pls)
    
    def create(self):
        # take all through terminal and add them to objects
        # add confirmation message when the work is done
        # also catch the error when for some reason data was not added
        pass
    
    def delete(self):
        # convert the objects into dictionary
        # dict[i] = name of the playlist
        # select the number u want to delete
        # search this object in self.__pls and delete
        # ask for update backup, and update it if asked 
        pass
    
    def list(self):
        # set up getter methods and get the respected values that you want to print
        # just print them with important parameters
        pass
    
    def backup(self):
        # convert the objects in dictionary format
        # push or bump them into json file called backup
        # return any error possible
        pass
    
    def load(self):
        # check into .json file
        # if empty return empty message
        # else load the data into memory
        pass
    

