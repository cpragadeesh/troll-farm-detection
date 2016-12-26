from sklearn.cluster import KMeans, DBSCAN, Birch
import numpy as np
import csv
import skfuzzy as fuzz
from math import sqrt

dataset = []
dataset_full = []

def infer_results(labels, algo):
	"""Infer results related to bot from estimator labels"""

	found_labels_with_bots = []

	print algo + " Clustering results: "
	print "Clustered " + str(len(labels)) + " datapoints"

	for i in range(0, 5):
		if labels[15 + i] not in found_labels_with_bots:
			
			bid = labels[15 + i]

			found_labels_with_bots.append(bid)

			print "Bot" + str(i + 1) + " belongs to cluster id: " + str(bid)
			print "Also belonging to cluster_id " + str(bid)

			for i in range(len(labels)):
				if labels[i] == bid:
					print dataset_full[i][0]

def load_dataset(dataset_file):

	dataset = []
	dataset_full = []

	with open(dataset_file, "r") as f:

		reader = csv.reader(f)

		for line in reader:
			dataset.append(line[1: ])
			dataset_full.append(line)

	return [dataset, dataset_full]

def cluster_kmeans(dataset):
	
	estimator = KMeans(n_clusters=8, init="k-means++").fit(dataset)

	infer_results(estimator.labels_, "KMeans")
	

def cluster_dbscan(dataset):

	estimator = DBSCAN(eps=3500, min_samples=2).fit(dataset)

	infer_results(estimator.labels_, "DBSCAN")


def cluster_birch(dataset):

	estimator = Birch(branching_factor=5, threshold=0.5, n_clusters=10, compute_labels=True).fit(dataset)

	infer_results(estimator.predict(dataset), "BIRCH")


def cluster_fcm(dataset):
	
	dataset = np.transpose(dataset)

	cntr, u, u0, d, jm, p, fpc = fuzz.cmeans(dataset, c=12, m=2, error=0.0001, maxiter=10000, init=None)

	labels = np.argmax(u, axis=0)

	infer_results(labels, "Fuzzy C-Means")


def compute_dist_between_bots():
	
	d = [["bot1",69240.0,35700.0,10.0,0.0,-33540.0,0.0],
		["bot2",69000.0,35100.0,10.0,0.0,-33900.0,0.0],
		["bot3",69600.0,35580.0,10.0,0.0,-34020.0,0.0],
		["bot4",71160.0,35580.0,10.0,0.0,-35580.0,0.0],
		["bot5",68880.0,33240.0,9.0,0.0,-35640.0,0.0]]

	dist = 0.0
	min_dist = float("inf")
	max_dist = -float("inf")

	for i in range(5):
		for j in range(i + 1, 5):
			dist = 0.0
			for k in range(1, len(d[i])):
				dist = dist + (d[i][k] - d[j][k]) * (d[i][k] - d[j][k])
			dist = sqrt(dist)
			min_dist = min(min_dist, dist)
			max_dist = max(max_dist, dist)

	print "Minimum distance = " + str(min_dist)
	print "Maximum distance = " + str(max_dist)


if __name__ == "__main__":

	dataset_file = "../dataset/dataset.csv"
	
	data = load_dataset(dataset_file)

	dataset = data[0]
	dataset_full = data[1]

	dataset = np.array(dataset, dtype=float)

	#compute_dist_between_bots()

	cluster_kmeans(dataset)

	print 

	cluster_dbscan(dataset)

	print 

	cluster_birch(dataset)

	print 

	cluster_fcm(dataset)

