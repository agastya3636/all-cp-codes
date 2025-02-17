Lab 11: AI: K mean clustering to unsupervised classification

K Mean clustering-with seed, number of clusters, stopping criteria

import numpy as np
import matplotlib.pyplot as plt

def k_means_1d(data, K, max_iterations=None, tolerance_mean=0.1, tolerance_population=1):
    # Initialize the cluster centroids randomly from the data points
    centroids = np.random.choice(data, K, replace=False)
    clusters = np.zeros(len(data))
    cluster_populations = np.zeros(K)
    iteration = 0
    max_iterations = max_iterations if max_iterations else K * 10
    
    # Track the changes in centroids and populations for each iteration
    history_centroids = [centroids.copy()]
    history_populations = [cluster_populations.copy()]
    stopping_criteria_met = None
    total_population_change = 0  # Track total population change

    while iteration < max_iterations:
        iteration += 1
        # Assign clusters based on closest centroid
        for i, point in enumerate(data):
            distances = np.abs(point - centroids)
            clusters[i] = np.argmin(distances)

        # Update cluster centroids and calculate population change
        new_centroids = np.array([data[clusters == k].mean() if len(data[clusters == k]) > 0 else centroids[k] for k in range(K)])
        new_cluster_populations = np.array([np.sum(clusters == k) for k in range(K)])

        # Calculate the total population change for this iteration
        total_population_change = np.sum(np.abs(new_cluster_populations - cluster_populations))

        # Check stopping criteria
        mean_change = np.max(np.abs(new_centroids - centroids) / (np.abs(centroids) + 1e-9))

        if mean_change < tolerance_mean and total_population_change < tolerance_population:
            stopping_criteria_met = "Mean and Total Population change below tolerance"
            break
        elif mean_change < tolerance_mean:
            stopping_criteria_met = "Mean change below tolerance"
            break
        elif total_population_change < tolerance_population:
            stopping_criteria_met = "Total Population change below tolerance"
            break

        # Update centroids and populations for the next iteration
        centroids = new_centroids
        cluster_populations = new_cluster_populations
        history_centroids.append(centroids.copy())
        history_populations.append(cluster_populations.copy())

    return clusters, centroids, iteration, history_centroids, history_populations, stopping_criteria_met, total_population_change

# Sample data (one-dimensional) and user inputs
data = np.random.rand(10) * 10  # 10 random data points
K = 3  # Number of clusters

# Plot the data points in one color initially (Before Clustering)
plt.scatter(data, np.zeros_like(data), color='gray', label="Data points")
plt.title("Initial Data Scatter Plot (Before Clustering)")
plt.xlabel("Data Points")
plt.legend()
plt.show()

# Run the K-means algorithm
clusters, centroids, iterations, history_centroids, history_populations, stopping_criteria_met, total_population_change = k_means_1d(data, K)

# Display iteration-wise statistics
print("Iteration-wise Centroid and Total Population Changes:")
for i in range(len(history_centroids)):
    print(f"Iteration {i+1}:")
    print(f"  Centroids: {history_centroids[i]}")
    print(f"  Cluster Populations: {history_populations[i]}")
    if i < len(history_centroids) - 1:
        centroid_changes = np.abs(history_centroids[i+1] - history_centroids[i]) / (np.abs(history_centroids[i]) + 1e-9)
        total_population_change = np.sum(np.abs(history_populations[i+1] - history_populations[i]))
        print(f"  Mean Change: {centroid_changes.max():.2f}")
        print(f"  Total Population Change: {total_population_change}")

# Print the final iteration's population change
if len(history_centroids) > 1:
    final_population_change = np.sum(np.abs(history_populations[-1] - history_populations[-2]))
    print(f"\nFinal Total Population Change: {final_population_change}")

print(f"\nAlgorithm stopped at iteration {iterations} due to: {stopping_criteria_met}")

# Plot the centroids' evolution over iterations
for k in range(K):
    centroid_evolution = [history_centroids[i][k] for i in range(len(history_centroids))]
    plt.plot(range(1, len(centroid_evolution) + 1), centroid_evolution, marker='o', label=f"Centroid {k+1}")
plt.title("Centroid Evolution Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Centroid Value")
plt.legend()
plt.show()

# Plot the cluster population changes over iterations
for k in range(K):
    population_evolution = [history_populations[i][k] for i in range(len(history_populations))]
    plt.plot(range(1, len(population_evolution) + 1), population_evolution, marker='o', label=f"Cluster {k+1} Population")
plt.title("Cluster Population Changes Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Population Size")
plt.legend()
plt.show()

# Plot the final clustered data points in different colors (After Clustering)
for k in range(K):
    plt.scatter(data[clusters == k], np.zeros_like(data[clusters == k]), label=f"Cluster {k+1}")
plt.scatter(centroids, np.zeros_like(centroids), color='black', marker='x', s=100, label="Centroids")
plt.title("Final Clustering Result (After K-means)")
plt.xlabel("Data Points")
plt.legend()
plt.show()

# Final stopping criterion
print(f"\nFinal Stopping Criterion: {stopping_criteria_met}")






Number of Clusters-K?

import numpy as np
import matplotlib.pyplot as plt

def k_means_1d(data, K, max_iterations=None, tolerance_mean=0.1, tolerance_population=1):
    # Initialize the cluster centroids randomly from the data points
    centroids = np.random.choice(data, K, replace=False)
    clusters = np.zeros(len(data))
    cluster_populations = np.zeros(K)
    iteration = 0
    max_iterations = max_iterations if max_iterations else K * 10
    
    # Track the changes in centroids and populations for each iteration
    history_centroids = [centroids.copy()]
    history_populations = [cluster_populations.copy()]
    stopping_criteria_met = None
    total_population_change = 0  # Track total population change

    while iteration < max_iterations:
        iteration += 1
        # Assign clusters based on closest centroid
        for i, point in enumerate(data):
            distances = np.abs(point - centroids)
            clusters[i] = np.argmin(distances)

        # Update cluster centroids and calculate population change
        new_centroids = np.array([data[clusters == k].mean() if len(data[clusters == k]) > 0 else centroids[k] for k in range(K)])
        new_cluster_populations = np.array([np.sum(clusters == k) for k in range(K)])

        # Calculate the total population change for this iteration
        total_population_change = np.sum(np.abs(new_cluster_populations - cluster_populations))

        # Check stopping criteria
        mean_change = np.max(np.abs(new_centroids - centroids) / (np.abs(centroids) + 1e-9))

        if mean_change < tolerance_mean and total_population_change < tolerance_population:
            stopping_criteria_met = "Mean and Total Population change below tolerance"
            break
        elif mean_change < tolerance_mean:
            stopping_criteria_met = "Mean change below tolerance"
            break
        elif total_population_change < tolerance_population:
            stopping_criteria_met = "Total Population change below tolerance"
            break

        # Update centroids and populations for the next iteration
        centroids = new_centroids
        cluster_populations = new_cluster_populations
        history_centroids.append(centroids.copy())
        history_populations.append(cluster_populations.copy())

    # Calculate the total within-cluster variance
    total_variance = sum([np.sum((data[clusters == k] - centroids[k])**2) for k in range(K)])

    return clusters, centroids, iteration, history_centroids, history_populations, stopping_criteria_met, total_variance

# Sample data (larger one-dimensional data set)
data = np.random.rand(100) * 100  # 100 random data points

# List to store total within-cluster variance for different K values
total_within_cluster_variances = []

# Run K-means for K values from 1 to 10
for K in range(1, 11):
    _, _, _, _, _, _, total_variance = k_means_1d(data, K)
    total_within_cluster_variances.append(total_variance)
    print(f"K = {K}, Total Within-Cluster Variance = {total_variance:.2f}")

# Plot K vs Total Within-Cluster Variance
plt.plot(range(1, 11), total_within_cluster_variances, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Total Within-Cluster Variance")
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()


Image segmentation with K mean
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate a simple 1D grayscale image (as a linear array)
image = np.array([50, 60, 70, 80, 90, 100, 150, 200, 210, 220, 230, 240, 250])
image = image.reshape(-1, 1)  # Reshape for KMeans compatibility (as a column vector)

# Number of classes (K)
K = 3

# Apply K-means clustering
kmeans = KMeans(n_clusters=K, random_state=0)
kmeans.fit(image)
segmented_image = kmeans.cluster_centers_[kmeans.labels_]

# Convert clustered image back to 1D for visualization
segmented_image = segmented_image.flatten()

# Plot the original and segmented images
plt.figure(figsize=(12, 6))

# Original image plot
plt.subplot(1, 2, 1)
plt.plot(image.flatten(), color='black', marker='o', linestyle='-', linewidth=1)
plt.title("Original 1D Grayscale Image")
plt.xlabel("Pixel Index")
plt.ylabel("Intensity")

# Segmented image plot
plt.subplot(1, 2, 2)
plt.plot(segmented_image, color='red', marker='o', linestyle='-', linewidth=1)
plt.title(f"Segmented Image with K={K}")
plt.xlabel("Pixel Index")
plt.ylabel("Intensity")

plt.tight_layout()
plt.show()
