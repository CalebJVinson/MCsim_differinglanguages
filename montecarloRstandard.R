set.seed(123) 
n_simulations <- 10000
n_steps <- 252 
S0 <- 100 
mu <- 0.05 
sigma <- 0.2 
dt <- 1/n_steps
strike_prices <- c(95, 105) 
risk_free_rate <- 0.03 


simulated_paths <- matrix(0, nrow=n_steps, ncol=n_simulations)
simulated_paths[1, ] <- S0


for (i in 2:n_steps) {
  Z <- rnorm(n_simulations)
  simulated_paths[i, ] <- simulated_paths[i - 1, ] * exp((mu - 0.5 * sigma^2) * dt + sigma * sqrt(dt) * Z)
}


option_prices <- c()
payoffs <- matrix(0, nrow=n_simulations, ncol=length(strike_prices))
for (k in 1:length(strike_prices)) {
  strike_price <- strike_prices[k]
  total_payoff <- 0
  for (j in 1:n_simulations) {
    final_price <- simulated_paths[n_steps, j]
    payoff <- max(final_price - strike_price, 0)
    payoffs[j, k] <- payoff
    total_payoff <- total_payoff + payoff
  }
  average_payoff <- total_payoff / n_simulations
  option_price <- average_payoff * exp(-risk_free_rate * n_steps * dt)
  option_prices <- c(option_prices, option_price)
}


for (i in 1:length(strike_prices)) {
  cat("Estimated Call Option Price for Strike Price", strike_prices[i], ":", option_prices[i], "\n")
}


payoff_data <- data.frame(Simulation=rep(1:n_simulations, each=n_steps),
                          TimeStep=rep(1:n_steps, n_simulations),
                          Price=as.vector(simulated_paths),
                          Payoff=rep(payoffs[, 1], each=n_steps))



matplot(simulated_paths[, 1:10], type="l", col=1:10, lty=1, xlab="Time Steps", ylab="Stock Price", main="Monte Carlo Simulated Stock Price Paths for R")
