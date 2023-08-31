import random
class Track:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration =duration

class Playlist:
    def __init__(self,title,filename):
        self.title = title
        self.filename = filename
        self.tracks = []

    def load(self):
        self.tracks = []
        print("Loading tracks from CSV file...")
        file = open(self.filename, "r")
        for line in file:
            fields = line.split(";")
            if len(fields) > 2:  # Needed to ignore empty lines of the csv files
                track = Track(fields[0], fields[1], int(fields[2]))
                self.tracks.append(track)
        file.close()

    def view(self):
        print(self.title)
        trackNumber = 1
        for track in self.tracks:
            print(str(trackNumber) + ") " + track.title + " by " + track.artist + " - " + str(track.duration) + "s")
            trackNumber += 1

    ##### Compelte this code by adding all the required method of the Playlist class #######
