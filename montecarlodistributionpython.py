import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(123) 
n_simulations = 10000
n_steps = 252  
S0 = 100  
mu = 0.05  
sigma = 0.2  
dt = 1 / n_steps


simulated_paths = np.zeros((n_steps, n_simulations))
simulated_paths[0, :] = S0


for i in range(1, n_steps):
    Z = np.random.normal(size=n_simulations)
    simulated_paths[i, :] = simulated_paths[i - 1, :] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

final_prices = simulated_paths[-1, :]


plt.figure(figsize=(10, 6))
plt.plot(simulated_paths[:, :10])
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.title("Monte Carlo Simulated Stock Price Paths")
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(final_prices, bins=50, kde=True)
plt.xlabel("Final Stock Price")
plt.ylabel("Frequency")
plt.title("Distribution of Final Stock Prices from Monte Carlo Simulations")
plt.show()
