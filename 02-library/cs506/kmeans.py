from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    # GOAL : Returns a new point which is the center of all the points.
    #assuming there is an array of points, and each point is an array of x values, x being the dimensionality of all points
    #assuming all points have the same dimenionality.
    pointDimensions = []
    dims = len(points[0]) #dimensionality
    for i in range(dims):
        totalValueDimension = 0;
        for point_index in range(len(points)):
            totalValueDimension += points[point_index][i]
        pointDimensions.append(totalValueDimension/len(points))
    return pointDimensions
        


def update_centers(dataset, assignments):
    #Compute the center for each of the assigned groups, return `k` centers in a list
    # Find number of clusters, k
    k = max(assignments) + 1
    centers = []
    for clust in range(k):
        # Find all samples in cluster i
        cluster_samples = []
        for sample in range(len(dataset)):
            if assignments[sample] == clust:
                cluster_samples.append(dataset[sample])
        centers.append(point_avg(cluster_samples))
    return centers

def assign_points(data_points, centers):
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    res = 0
    if (b == 0):
        b = [0] * len(a)
    if (type(a) == int):
        x = []
        x.append(a)
    else:
        x = a
    for i in range(len(x)):
        res += (x[i] - b[i])**2
    return res**(1/2)

def distance_squared(a, b):
    return (distance(a, b)**2)

def generate_k(dataset, k):
    points = []
    for i in range(k):
        rand_min = i*(int(len(dataset)/k))
        rand_max = (i + 1)*(int(len(dataset)/k))
        point = random.randint(rand_min, rand_max) #random point in the specified range
        points.append(dataset[point])
    return points

def cost_function(clustering):
    #calculate sum of distances squared
    res = 0
    origin = [0 for i in range(len(clustering))]
    for point in clustering:
        res += distance_squared(point, origin)
    return res


def generate_k_pp(dataset, k):
    #return a random set of k points from the data_set where points are picked with a probability 
    #proportional to their distance as per kmeans pp
    ws = [distance(point ,0) for point in dataset]
    centroids = []
    chosen_index = []
    for j in range(k):
        i = random.choices(range(len(dataset)), weights = ws, k = 1)[0]
        while i in chosen_index:
            i = random.choices(range(len(dataset)), weights = ws, k = 1)[0]
        centroids.append(dataset[i])
        chosen_index.append(i)
    return centroids


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
