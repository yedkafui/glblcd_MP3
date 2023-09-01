
from playlist import Track, Playlist

myPlaylist = Playlist("Pop Music","pop_music.csv")
myPlaylist.load()

myPlaylist.view()

myPlaylist.shuffle_playlist()
print()
myPlaylist.count_tracks()
myPlaylist.total_duration()