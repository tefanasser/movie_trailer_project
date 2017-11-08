# importing the file that contains class Movie , and fresh_tomatoes to create the
# HTML page
import media
import fresh_tomatoes

# create movie objects 
frozen=media.Movie("Frozen","When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her "
                   "home in infinite winter,her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman "
                   "to change the weather condition.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                   "https://www.youtube.com/watch?v=TbQm5doF_Uc")

titanic=media.Movie("Titanic","A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious,"
                    "ill-fated R.M.S. Titanic.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg"
                    ,"https://www.youtube.com/watch?v=ZQ6klONCq4s")

seven=media.Movie("Seven","Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives."
                  ,"https://images-na.ssl-images-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                  "https://www.youtube.com/watch?v=4M7M-juFLTU")

fight_club=media.Movie("Fight Club","An insomniac office worker, looking for a way to change his life, "
                       "crosses paths with a devil-may-care soap maker, forming an underground fight club that"
                       "evolves into something much, much more.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=SUXWAEX2jlg")

forrest_gump=media.Movie("Forrest Gump","JFK, LBJ, Vietnam, Watergate, and other history unfold through the perspective"
                         " of an Alabama man with an IQ of 75."
                         ,"https://images-na.ssl-images-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg"
                         ,"https://www.youtube.com/watch?v=bLvqoHBptjg")

# create a list of favorite movies
movies=[frozen,titanic,seven,fight_club,forrest_gump]

# create html page
fresh_tomatoes.open_movies_page(movies)
