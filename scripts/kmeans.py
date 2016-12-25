from sklearn.cluster import KMeans
import numpy as np
import csv


dataset = []
dataset_full = []

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

	print "Clustered " + str(len(estimator.labels_)) + " datapoints"

	found_labels_with_bots = []

	for i in range(0, 5):
		if estimator.labels_[15 + i] not in found_labels_with_bots:
			
			bid = estimator.labels_[15 + i]

			found_labels_with_bots.append(bid)

			print "Bot" + str(i) + " belongs to cluster id: " + str(bid)
			print "Also belonging to cluster_id " + str(bid)

			for i in range(len(estimator.labels_)):
				if estimator.labels_[i] == bid:
					print dataset_full[i][0]

if __name__ == "__main__":

	dataset_file = "../dataset/dataset.csv"
	
	data = load_dataset(dataset_file)

	dataset = data[0]
	dataset_full = data[1]

	dataset = np.array(dataset)

	cluster_kmeans(dataset)

