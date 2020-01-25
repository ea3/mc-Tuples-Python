t = "a", "b", "C"   # This is a tuple
print(t)

print("a", "b", "c")   # Not a tuple
print(("a", "b", "c"))    # This is also a tuple

welcome = "Welcome to my nightmare", "Alice Copper", 1975

bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imelda Day", 2011, ((1,"Pulling the rug"), (2, "Phsyco"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
metallica = ["Ride the lightning", "Metallica", 1984]

print(imelda)

title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)
print(tracks)

for song in tracks:
    track, title = song
    print(f"\tTrack number {track}, Title: {title}")
