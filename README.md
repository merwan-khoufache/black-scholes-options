# Delta Hedging and Monte Carlo Pricing

This project studies the pricing and hedging of a European call option in the Black-Scholes framework.

## Objectives

- Replicate the discrete delta hedging table from Hull (2022)
- Simulate stock price paths using Geometric Brownian Motion (GBM)
- Implement Monte Carlo pricing
- Compare:
  - Black-Scholes price
  - Monte Carlo estimate
  - Average hedging cost

## Key Concepts

- Black-Scholes model
- Delta hedging
- Discrete rebalancing error
- Monte Carlo simulation

## Results

- The average hedging cost closely matches the Black-Scholes price
- The distribution of hedging outcomes shows residual risk due to discrete hedging

## Structure

The notebook contains:
1. Black-Scholes formulas
2. GBM simulation
3. Hull table replication
4. Discrete hedging analysis
5. Monte Carlo simulation

## Requirements

- numpy
- scipy
- matplotlib
- pandas

## Author

Merwan KHOUFACHE  
MSc Data Science & AI for Finance — EDHEC

## Reference


- Hull, J. C. (2022). *Options, Futures, and Other Derivatives*. Pearson.
- Hilpisch, Y. J. (2018). *Python for Finance: Mastering Data-Driven Finance* (2nd ed.). O’Reilly Media.
