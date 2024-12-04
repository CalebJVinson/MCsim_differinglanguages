import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
np.random.seed(123)  # for reproducibility
n_simulations = 10000
n_steps = 252  # days in a year
S0 = 100  # initial stock price
mu = 0.05  # expected return
sigma = 0.2  # volatility
dt = 1 / n_steps

# Initialize matrix to store the simulated paths
simulated_paths = np.zeros((n_steps, n_simulations))
simulated_paths[0, :] = S0

# Simulate paths
for i in range(1, n_steps):
    Z = np.random.normal(size=n_simulations)
    simulated_paths[i, :] = simulated_paths[i - 1, :] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

# Run 10,000 i.i.d. simulations for the final price distribution
final_prices = simulated_paths[-1, :]

# Plot some paths
plt.figure(figsize=(10, 6))
plt.plot(simulated_paths[:, :10])
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.title("Monte Carlo Simulated Stock Price Paths")
plt.show()

# Plot the distribution of final prices
plt.figure(figsize=(10, 6))
sns.histplot(final_prices, bins=50, kde=True)
plt.xlabel("Final Stock Price")
plt.ylabel("Frequency")
plt.title("Distribution of Final Stock Prices from Monte Carlo Simulations")
plt.show()
