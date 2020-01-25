cd_la_compania = "Ivan Villazon", "Franco Arguelles", "La Compania", ((1, "Almas Felices"), (2, "Loquita por mi"),
                                                                      (3, "Cuando Muera esta ilusion"), (4, "Sera que te molesta"),
                                                                      (5, "Bellos Amores"), (6, "El Masticandi"),
                                                                      (7, "Asi me paso contigo"),(8, "El amor se impone"),
                                                                      (9, "El detallista"), (10, "La pelionera")<
                                                                      (10, "Moliendo cafe"))
print(cd_la_compania)

author, acordeonist, cd_title, discografy = cd_la_compania
print(author)
print(acordeonist)
print(cd_title)
# print(discografy)

for song in discografy:
    track, title = song
    print(f"\tTrack number: {track}, Title: {title}")


