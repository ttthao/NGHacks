# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from voodoo_plans.models import Itinerary, Activity, Route
from django.http import HttpResponse

# sys.path.insert(0, '/Users/jsenar/projects/NGHacks/project/voodoo_plans/backend/')
# sys.path.insert(0, '/home/davidxlin/github/NGHacks/project/voodoo_plans/backend/')

import gmap_directions
import autocomplete as ac
import search_yelp
selected_activities = []

def index(request):
    return render(request, 'home.template.html', {})

def itnrsub(request):
    if request.method == 'POST':
        title = request['title']
        duration = request['duration']
        purpose = request['purpose']
        preference = request['preference']

        activities = request['activities']


        wayps = None
        origin = activities[0][display_address]
        destination = activities[-1][display_address]
        if len(activities) > 2:
            wayps = []
            for wayp in activities[1:len(activities)-1]:
                wayps.append(waypt[display_address])

        route = get_route(origin, destination, wayps)

        # distance
        distance = get_dist_duration(route)[0]

        # cost assumed to be found client-side
        cost = request['cost']

        itinerary = Itinerary(title=title,
                                purpose=purpose,
                                preference=preference,
                                cost=cost,
                                duration=duration,
                                distance=distance)
        itinerary.save()

        # activity and routes
        ordered_activities = []
        for i in range(len(activities)):
            title = activities[i]['title']
            address = activities[i]['display_address']
            rating = activities[i]['rating']
            image_url = activities[i]['image_url']
            activity = Activity(title=title, address=address, rating=rating, image_url=image_url)
            route = Route(itinerary=itinerary, activity=activity, order=i)
            ordered_activities.append(activity)
            activity.save()
            route.save()


        context = {
            'itinerary': itinerary,
            'activities': ordered_activities,
            'map': {
                'origin': origin,
                'destination': destination,
                'wayps': wayps
            }
        }

        return HttpResponse(context)

    return render(request, 'submit.template.html', {})

def complete(request):
    if request.method == 'POST':
        text = request.POST['text']
        suggestions = ac.get_autocomplete(text)
        if not suggestions:
            return
        # return render(request, 'test2.html', {})
        return HttpResponse(suggestions) #TODO

def search(request):
    print("in it")
    if request.method == 'POST':
        print("in it2")
        text = request.POST['text']
        results = search.query(text)
        if not results:
            return "No Results Found."

        print('ye', results)
        return HttpResponse(suggestions)

def current_activities(request):
    if request.method == 'POST':
        title = request['title']
        address = request['display_address']
        rating = request['rating']
        image_url = request['image_url']
        activity = Activity(title=title, address=address, rating=rating, image_url=image_url)
        activity.save()

        context = {
            'activity': activity
        }

        return render(HttpResponse(context), 'submit.template.html', {})

def algo_results(request):
    return render(request, 'results.template.html', {})

def displ_itin(request):
    return render(request, 'itinerary.template.html', {})
