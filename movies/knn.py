from euclidean import dist
from math import sqrt

def knn(movie_ratings, predict_movie, prev_rated,num_neighbors):

	#prev_rated is a dictionary of previously rated movies (movie_id: rating)
	eucl_dist = {}
	for k,v in prev_rated:
		print prev_rated
		eucl_dist[str(dist(movie_ratings,predict_movie,v))] = (k, v)
	# sort keys of eucl_dict
	eucl_keys = [int(x) for x in eucl_dist.keys()]
	sorted_keys = sorted(eucl_keys)

	neighbors = sorted_keys[0:num_neighbors]
	user_rating_total = 0
	for neighbor in neighbors:
		user_rating_total += eucl_dist[neighbor][1]
	knn_est = user_rating_total/num_neighbors

	return knn_est

#movie_ratings, film1, film2):
# a is movie to be predicted
# b, c, d are movies already rated by user

	# d = sqrt(total)
	# max_d = sqrt(25*num_critics)
	# ratio = 1 - d/max_d

	# return ratio



# get eucl distance between a and b, a and c, a and d

# insert eucl into a list

# sort the list 

# get first k eucl from list

# match user's ratings for first k movies

# take average of those ratings to get predicted rating of a
