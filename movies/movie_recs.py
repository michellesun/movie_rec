import correlation # how to import module from another folder? 
import euclidean

def genre(chosen_line):
	genre_binary = chosen_line[5:]
	# create a dictionary of index in list and genre
	genre_dict = { 	0: "unknown", 
					1: "Action",
					2: "Adventure",
					3: "Animation",
					4: "Children's",
					5: "Comedy",
					6: "Crime",
					7: "Documentary",
					8: "Drama",
					9: "Fantasy",
					10: "Film-Noir",
					11: "Horror",
					12: "Musical",
					13: "Mystery",
					14: "Romance",
					15: "Sci-Fi",
					16: "Thriller",
					17: "War",
					18: "Western" }
	genres = []
	for index, num in enumerate(genre_binary):
		if num == '1':
			genres.append(genre_dict[index])
	return genres


def movie_details(movie_id):
	movie_id = str(movie_id)
	movie_name = movie_dict[movie_id]['title']
	genres = ""
	for genre in movie_dict[movie_id]['Genres']:
		if not genres:
			genres = genre
		else:
			genres += ", " + genre
	print "Movie %s: %s \n%s" %(movie_id,movie_name,genres)
	return movie_name, genres

def get_user(user_id):
	user_id = str(user_id)
	print "%s %s, age %s" %(user_dict[user_id]['gender'],user_dict[user_id]['occupation'],user_dict[user_id]['age'])

def user_rating(item_id,user_id):
	# go through all lines in db:
	title = movie_dict[str(item_id)]['title']
	rating = user_ratings[title][str(user_id)]
	print "User " + str(user_id) + " rated movie " + title + " at " + str(rating) + " stars"
		
def rate(movie_id, rating):
	movie_name = movie_dict[str(movie_id)]['title']
	# if user_rating.get(movie_name):
	# 	user_rating[movie_name][user_id] = float(rating)
	USER_RATING[str(movie_id)] = rating
	print "You have rated movie " + str(movie_id) + ": " + movie_name + " at " + str(float(rating)) + " stars"

# create a list of rating by this user
USER_RATING = {}

def predict(movie_id):
	movie_name1 = movie_dict[str(movie_id)]['title']
	pearson = []
	for k,v in USER_RATING.iteritems():
		movie_name2 = movie_dict[k]['title']
		pearson.append((correlation.pearson_similarity(user_ratings, movie_name1, movie_name2), v))
	# get the max pearson score and assign the associated rating to prediction
	sorted_list = sorted(pearson)
	sorted_list.reverse()
	print sorted_list
	score = sorted_list[0][0]
	most_similar_rating = sorted_list[0][1]
	if score <= 0:
		print "Cannot predict score. Please rate more movies"
		return
	prediction = ("%.1f" %round(score * most_similar_rating))
	print "Best Pearson guess for movie %s: %s is %s stars" %(movie_id, movie_name1, prediction)

def new_predict(movie_id):
	movie_name1 = movie_dict[str(movie_id)]['title']
	eucl = []
	for k, v in USER_RATING.iteritems():
		movie_name2 = movie_dict[k]['title']
		eucl.append((euclidean.dist(user_ratings,movie_name1,movie_name2),v,k))
	sorted_list = sorted(eucl)
	score = sorted_list[0][0]
	sorted_list.reverse()
	highest_ratio = sorted_list[0][1]
	movie_id2 = sorted_list[0][2]
	prediction = ("%.1f" %round(score * highest_ratio))
	print sorted_list
	print "Best Euclidean guess for movie %s: %s is %s stars" %(movie_id, movie_name1, prediction)	

def average_movie_rating(movie_id):
	movie_name = movie_dict[str(movie_id)]['title']
	if user_ratings.get(movie_name):
		# average = sum getvalues / count getvalues??
		total = 0
		count = 0
		for key in user_ratings[movie_name]:
			total += user_ratings[movie_name][key]
			count += 1
		print ("%.2f" %round(total/count,2))
	else:
		print "No user ratings for this movie"

def main():
	global USER_RATING
	while True:
		commands = raw_input("> ").split()
		if commands[0] not in ["movie_details", "average_movie_rating", "get_user", "user_rating", "rate", "predict","new_predict"]:
			print "I didn't understand that command!"
		elif commands[0] == "movie_details":
			movie_details(commands[1])
		elif commands[0] == "average_movie_rating":
			average_movie_rating(commands[1])
		elif commands[0] == "get_user":
			get_user(commands[1])
		elif commands[0] == "user_rating":
			user_rating(int(commands[1]), int(commands[2]))
		elif commands[0] == "rate":
			rate(int(commands[1]), int(commands[2]))
		elif commands[0] == "predict":
			predict(int(commands[1]))
		elif commands[0] == "new_predict":
			new_predict(int(commands[1]))

movie_dict = {}
f = open('/Users/student/src/movies/ml-100k/u.item')
lines = f.readlines()
for line in lines:
	split_line = line.split('|')
	movie_dict[split_line[0]] = {
		'title': split_line[1],
		'release date': split_line[2],
		'video release date': split_line[3],
		'IMDB URL': split_line[4],
		'Genres': genre(split_line)
	}
f.close()

user_dict = {}
f = open('/Users/student/src/movies/ml-100k/u.user')
ulines = f.readlines()
for uline in ulines:
	split_uline = uline.split('|')
	# Change from "M"/"F" to Male/Female
	if split_uline[2] == "M":
		split_uline[2] = "Male"
	else: 
		split_uline[2] = "Female"

	user_dict[split_uline[0]] = {
		'age': split_uline[1],
		'gender': split_uline[2],
		'occupation': split_uline[3]
	}
f.close()

user_ratings = {}
f = open('/Users/student/src/movies/ml-100k/u.data')
ulines = f.readlines() 
for uline in ulines:
	split_uline = uline.split()
	movie_name = movie_dict[split_uline[1]]['title']
	if user_ratings.get(movie_name):
		user_ratings[movie_name][split_uline[0]] = float(split_uline[2])
	else:	
		user_ratings[movie_name] = {
			split_uline[0]: float(split_uline[2])
		}
f.close()

if __name__ == '__main__':
	main()