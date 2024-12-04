#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <fstream>

int main() {

    int n_simulations = 10000;
    int n_steps = 252; 
    double S0 = 100.0; 
    double mu = 0.05; 
    double sigma = 0.2; 
    double dt = 1.0 / n_steps;
    double strike_price = 105.0; 
    double risk_free_rate = 0.03; 

    
    std::mt19937 generator(123); 
    std::normal_distribution<double> distribution(0.0, 1.0);

    
    std::vector<std::vector<double>> simulated_paths(n_steps, std::vector<double>(n_simulations, S0));

    
    for (int i = 1; i < n_steps; ++i) {
        for (int j = 0; j < n_simulations; ++j) {
            double Z = distribution(generator);
            simulated_paths[i][j] = simulated_paths[i - 1][j] * std::exp((mu - 0.5 * sigma * sigma) * dt + sigma * std::sqrt(dt) * Z);
        }
    }

    
    double total_payoff = 0.0;
    std::vector<double> payoffs(n_simulations);
    for (int j = 0; j < n_simulations; ++j) {
        double final_price = simulated_paths[n_steps - 1][j];
        double payoff = std::max(final_price - strike_price, 0.0);
        payoffs[j] = payoff;
        total_payoff += payoff;
    }

    
    double average_payoff = total_payoff / n_simulations;
    double option_price = average_payoff * std::exp(-risk_free_rate * n_steps * dt);

    
    std::cout << "Estimated Call Option Price: " << option_price << std::endl;

    
    std::ofstream file("payoff_data.csv");
    if (file.is_open()) {
        file << "Simulation,TimeStep,Price,Payoff\n";
        for (int j = 0; j < n_simulations; ++j) {
            for (int i = 0; i < n_steps; ++i) {
                file << j << "," << i << "," << simulated_paths[i][j] << "," << (i == n_steps - 1 ? payoffs[j] : 0.0) << "\n";
            }
        }
        file.close();
    } else {
        std::cerr << "Unable to open file for writing payoff data." << std::endl;
    }

    return 0;
}
