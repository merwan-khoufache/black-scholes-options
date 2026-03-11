# Black-Scholes Options 

**Author:** KHOUFACHE Merwan  
**Program:** M1 Data Science & AI for Finance — EDHEC Business School  
**Date:** March 2026

---

## Overview

This repository contains two projects built around the **Black-Scholes model** for European option pricing.  
Both projects rely on a shared pricing library (`option_tools.py`) implemented from scratch.

| Project | Notebook | Description |
|---------|----------|-------------|
| BS Pricing & Greeks | `bs_pricing.ipynb` | Pricing, payoff, time value, put-call parity, Greeks |
| Delta Hedging Simulation | `delta_hedging.ipynb` | Monte Carlo simulation of a delta hedging strategy |

---

## Repository Structure

```
black-scholes-options/
│
├── option_tools.py          # Core Black-Scholes library
│
├── bs_pricing.ipynb         # Project 1 — Option pricing & Greeks
├── delta_hedging.ipynb      # Project 2 — Delta hedging simulation
│
└── README.md
```

---

## Project 1 — BS Pricing & Greeks &nbsp;(`bs_pricing.ipynb`)

Implements and visualizes the Black-Scholes model for European call and put options.

**Contents:**
- Black-Scholes pricing formula for calls and puts
- Price vs payoff — shaded area represents time value
- Time value analysis — maximum at ATM
- Put-call parity verification
- Full Greeks: Delta, Gamma, Vega, Theta, Rho

**Parameters:**

| Symbol | Value | Description |
|--------|-------|-------------|
| $K$ | 100 | Strike price |
| $T$ | 1 year | Time to maturity |
| $r$ | 2% | Risk-free rate |
| $\sigma$ | 20% | Volatility |
| $q$ | 0% | Dividend yield |

---

## Project 2 — Delta Hedging Simulation &nbsp;(`delta_hedging.ipynb`)

Simulates a delta hedging strategy for a short position in 100,000 European call options,  
following Hull (2022), *Options, Futures, and Other Derivatives*, Chapter 19.

**Contents:**
- Stock price simulation via Euler-Maruyama discretization of GBM
- Week-by-week delta hedging loop with financing costs
- Replication of Hull Table 19.2 (ITM scenario, final price $57.25)
- Path dependency analysis — cumulative cost across 3 trajectories
- Monte Carlo analysis on 1,000 independent paths

**Key result:** The average net hedging cost converges to the Black-Scholes price  
with a relative error of ~0.56% under weekly rebalancing.

**Parameters:**

| Symbol | Value | Description |
|--------|-------|-------------|
| $S_0$ | 49 | Initial stock price |
| $K$ | 50 | Strike price (slightly OTM) |
| $T$ | 20 weeks | Time to maturity |
| $r$ | 5% | Risk-free rate |
| $\sigma$ | 20% | Volatility |
| $N$ | 100,000 | Number of options sold |

---

## `option_tools.py` — Core Library

All pricing and Greeks functions are centralized in `option_tools.py` and imported by both notebooks.  
Every function supports **vectorized NumPy inputs**.

### Pricing

| Function | Signature | Description |
|----------|-----------|-------------|
| `d1` | `(S, K, T, r, sigma, q=0)` | Computes $d_1$ from the BS formula |
| `d2` | `(S, K, T, r, sigma, q=0)` | Computes $d_2 = d_1 - \sigma\sqrt{T}$ |
| `bs_price` | `(S, K, T, r, sigma, q=0, option="call")` | Black-Scholes price — call or put |
| `payoff` | `(S, K, option="call")` | Intrinsic value at maturity |
| `parity_rhs` | `(S, K, T, r, q=0)` | RHS of put-call parity: $Se^{-qT} - Ke^{-rT}$ |

### Greeks

| Function | Signature | Description |
|----------|-----------|-------------|
| `delta` | `(S, K, T, r, sigma, q=0, option="call")` | $\partial C / \partial S$ |
| `gamma` | `(S, K, T, r, sigma, q=0)` | $\partial^2 C / \partial S^2$ |
| `vega` | `(S, K, T, r, sigma, q=0)` | $\partial C / \partial \sigma$ |
| `theta` | `(S, K, T, r, sigma, q=0, option="call")` | $\partial C / \partial T$ |
| `rho` | `(S, K, T, r, sigma, q=0, option="call")` | $\partial C / \partial r$ |

All functions raise a `ValueError` for invalid inputs (negative $S$, $K$, $T$, or $\sigma$).

---

## Installation

```bash
git clone https://github.com/yourusername/black-scholes-options.git
cd black-scholes-options
pip install numpy scipy matplotlib pandas
```

Both notebooks import directly from `option_tools.py` — no additional setup required.

---

## Reference

> Hull, J.C. (2022). *Options, Futures, and Other Derivatives* (11th ed.). Pearson.  
> Chapter 19 — The Greek Letters & Delta Hedging.
