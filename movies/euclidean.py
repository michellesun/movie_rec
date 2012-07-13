from math import sqrt


def dist(movie_ratings, film1, film2):
	common_critics = []
	film1_critics = movie_ratings[film1]
	film2_critics = movie_ratings[film2]

	for critic in film1_critics:
		if critic in film2_critics:
			common_critics.append(critic)

	if len(common_critics) == 0:
		return 0


# check how many common critics to determine dimension
	num_critics = len(common_critics)
	total = 0

	for critic in common_critics:
		p = movie_ratings[film1][critic]
		q = movie_ratings[film2][critic]
		square = (p-q)**2
		total += square
	d = sqrt(total)
	max_d = sqrt(25*num_critics)
	ratio = 1 - d/max_d

	return ratio


# 	> rate 71 5
# You have rated movie 71: Lion King, The (1994) at 5.0 stars
# > rate 588 5
# You have rated movie 588: Beauty and the Beast (1991) at 5.0 stars
# > rate 12 4
# You have rated movie 12: Usual Suspects, The (1995) at 4.0 stars
# > rate 890 1
# You have rated movie 890: Mortal Kombat: Annihilation (1997) at 1.0 stars
# > predict 1
# Traceback (mo