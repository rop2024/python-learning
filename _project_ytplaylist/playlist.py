import datetime

class Playlist:
    def __init__(self, title,video_number, playlist_duration,target_date ,current_date = datetime.date.today):
        # any playlist should have a title and number of videos, current date or date started, target date
        # then add things like days left and watched till videos
        # also total duration of playlist which would help compute how much average time more to give on project
        self.title = title
        self.__video_number = video_number
        self.__playlist_duration = playlist_duration
        self.__target_date = target_date
        self.__current_date = current_date
        self.__days_left = self.__target_date - self.__current_date
        self.__watched_till = 0
        self.__url = ""
        
    def set_video_number(self, number):
        # settting total number of videos in playlist
        self.__video_number = number


    def set_playlist_duration(self, duration):
        # this should get calculated in minutes, then if asked then only conversion to other units
        self.__playlist_duration = duration


    def set_target_date(self, target):
        # setting a date object
        self.__target_date = target
    

    def set_wt(self,watched_till):
        self.__watched_till = watched_till
    

    def set_url(self, url):
        self.__url = url

        