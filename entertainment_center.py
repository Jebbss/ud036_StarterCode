import media
import fresh_tomatoes
#move_title, movie_summary, movie_trailer, movie_poster)
resvoir_dogs = media.Movie('Resvoir Dogs','A heist does not go to plan','https://www.youtube.com/watch?v=vayksn4Y93A','https://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg')
pulp_fiction = media.Movie('Pulp Fiction', 'Four alinear wacky stories', 'https://www.youtube.com/watch?v=Mnb_3ibUp38','https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg')
jackie_brown = media.Movie('Jack Brown','A relationship evolves','https://www.youtube.com/watch?v=G7HkBDNZV7s','https://upload.wikimedia.org/wikipedia/en/8/80/Jackie_Brown70%27s.jpg')
kill_bill_one = media.Movie('Kill Bill Vol.1','A bride hunts her groom','https://www.youtube.com/watch?v=7kSuas6mRpk','https://upload.wikimedia.org/wikipedia/en/2/2c/Kill_Bill_Volume_1.png')
kill_bill_two = media.Movie('Kill Bill Vol.2','A bride finds her groom','https://www.youtube.com/watch?v=WTt8cCIvGYI','https://upload.wikimedia.org/wikipedia/en/c/c4/Kill_Bill_Volume_2.png')
inglourious = media.Movie('Inglourious','A mission does not go to plan','https://www.youtube.com/watch?v=KnrRy6kSFF0','https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg')

movies = [resvoir_dogs, pulp_fiction, jackie_brown, kill_bill_one, kill_bill_two, inglourious]
fresh_tomatoes.open_movies_page(movies)
