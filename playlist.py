from random import shuffle
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
                track = Track(fields[0], fields[1], (fields[2]))
                self.tracks.append(track)
        file.close()

    def view(self):
        print(self.title)
        trackNumber = 1
        for track in self.tracks:
            print(f"{trackNumber}. {track.title} by {track.artist} - {track.duration}")
            trackNumber += 1
    
    def shuffle_playlist(self):
        shuffle(self.tracks)

    def count_tracks(self):
        print(f"Number of tracks: {len(self.tracks)}")

    def total_duration(self):
        total = 0
        for track in self.tracks:
            duration = track.duration.split(':')
            seconds = int(duration[0])*60 + int(duration[1])
            total += seconds
            

        print(f"Total duration of playlist: {total//60}:{total%60}s")
    

    
