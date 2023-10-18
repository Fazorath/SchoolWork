def makeAlbum(artistname,albumtitle,songs=None):
    album = {'Artist Name':artistname,
            'Album Title':albumtitle,}
    if songs:
        album['songs'] = songs
    
    return album

artist = input("Who is your Artist: ")
albumtitle = input("What is your Album Title: ")
songs = input("How many songs: ")

newalbum = makeAlbum(artist,albumtitle,songs)
print(newalbum)
