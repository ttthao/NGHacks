import googlemaps

KEY = 'AIzaSyA3U5PWSSk2RHpwxT8XRtzib6AsgurB168'
CLIENT = googlemaps.Client(KEY)
waypoints = ''

#Returns route from origin to destination w/ waypoints in between
def get_route(origin, destination, wayps=None):
	if wayps:
		route = CLIENT.directions(origin, destination, waypoints=wayps)
	else:
		route = CLIENT.directions(origin, destination)
	return route[0]

#Returns pair of total distance, total duration
#Distance is in meters, duration is in seconds
def get_dist_duration(route):
	totalDistance = 0
	totalDuration = 0
	#Step through each leg of the route to get distance and duration
	legs = route['legs']
	for i in xrange(len(legs)):
		totalDistance += legs[i]['distance']['value']
		totalDuration += legs[i]['duration']['value']
	return totalDistance, totalDuration
