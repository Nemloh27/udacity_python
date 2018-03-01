import media
import fresh_tomatoes

toy_story = media.Movie("toy story","A story about toys coming to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://youtu.be/KYz2wyBy3kc")
avatar = media.Movie("avatar","A crappy ripoff movie","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://youtu.be/5PSNL1qE6VY")
school_of_rock = media.Movie("school of rock","A deadbeat teaches music class","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://youtu.be/XCwy6lW5Ixc")


#print toy_story.storyline
#print avatar.storyline
#print school_of_rock.storyline
#avatar.show_trailer()

movies = [toy_story, avatar, school_of_rock]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
