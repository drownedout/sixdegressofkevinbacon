from imdb import IMDb

ia = IMDb()

kevin_bacon = ia.get_person('0000102')

kb_movie = kevin_bacon['actor']

movie_id = []

for title in kb_movie:
	movie_id.append(title.movieID)

file = open("newfile.txt", "w")

for cast in movie_id:
	file.write(str(ia.get_person(cast)))
	file.write('\n')

file.close()