import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story" , "The story of a boy and his toys which come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print( toy_story.storyline)

avatar = media.Movie("Avatar" , "A marine on an alien planet" ,"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print( avatar.storyline)

#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock" , "Using rock music to learn"
                             ,"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille","A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris","Going back in time to meet Authors"
                                ,"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games","A Really real reality show","https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg","https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toy_story ,avatar , school_of_rock , ratatouille , midnight_in_paris
          , hunger_games]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)

