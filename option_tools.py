import numpy as np
from scipy.stats import norm

def d1(S, K, T, r, sigma, q=0.0):
    S = np.asarray(S, dtype=float)
    T = np.asarray(T, dtype=float)
    sigma = np.asarray(sigma, dtype=float)

    K = float(K)
    r = float(r)
    q = float(q)

    if np.any(S <= 0):
        raise ValueError("S must be > 0")
    if K <= 0:
        raise ValueError("K must be > 0")
    if np.any(T <= 0):
        raise ValueError("T must be > 0 to compute d1")
    if np.any(sigma <= 0):
        raise ValueError("sigma must be > 0 to compute d1")

    return (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))


def d2(S, K, T, r, sigma, q=0.0):
    T = np.asarray(T, dtype=float)
    sigma = np.asarray(sigma, dtype=float)
    return d1(S, K, T, r, sigma, q=q) - sigma * np.sqrt(T)

def bs_price(S, K, T, r, sigma, q=0.0, option="call"):
    """
    Calculate the Black-Scholes call / put option price.

    Parameters:
    S (float): Current stock price
    X (float): Strike price
    T (float): Time to maturity (in years)
    r (float): Risk-free interest rate
    sigma (float): Volatility of the stock's returns
    """
    D1 = d1(S, K, T, r, sigma, q=q)
    D2 = d2(S, K, T, r, sigma, q=q)

    opt = option.lower()

    if opt == "call":
        return S*np.exp(-q*T)*norm.cdf(D1) - K*np.exp(-r*T)*norm.cdf(D2)

    elif opt == "put":
        return K*np.exp(-r*T)*norm.cdf(-D2) - S*np.exp(-q*T)*norm.cdf(-D1)

    else:
        raise ValueError("option must be 'call' or 'put'")

def payoff(S, K, option="call"):
    opt = option.lower()
    if opt == "call":
        return np.maximum(S - K, 0.0)
    elif opt == "put":
        return np.maximum(K - S, 0.0)
    else:
        raise ValueError("option must be 'call' or 'put'")

def parity_rhs(S, K, T, r, q=0.0):
    return S*np.exp(-q*T) - K*np.exp(-r*T)

def delta(S,K,T,r,sigma, q=0.0, option="call"):
    D1 = d1(S, K, T, r, sigma, q=q)
    opt = option.lower()
    if opt == "call":
        return np.exp(-q*T) * norm.cdf(D1)
    elif opt == "put":
        return np.exp(-q*T) * (norm.cdf(D1) - 1)
    else:
        raise ValueError("option must be 'call' or 'put'")

def gamma(S, K, T, r, sigma, q=0.0):
    D1 = d1(S, K, T, r, sigma, q=q)
    return np.exp(-q*T) * norm.pdf(D1) / (S * sigma * np.sqrt(T))

def vega (S, K, T, r, sigma, q=0.0):
    D1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    return S * np.exp(-q * T) * norm.pdf(D1) * np.sqrt(T)

def theta(S, K, T, r, sigma, q=0.0, option="call"):
    D1 = d1(S, K, T, r, sigma, q=q)
    D2 = d2(S, K, T, r, sigma, q=q)

    opt = option.lower()

    if opt == "call":
        return (
            - S * np.exp(-q*T) * norm.pdf(D1) * sigma / (2 * np.sqrt(T))
            - r * K * np.exp(-r*T) * norm.cdf(D2)
            + q * S * np.exp(-q*T) * norm.cdf(D1)
        )

    elif opt == "put":
        return (
            - S * np.exp(-q*T) * norm.pdf(D1) * sigma / (2 * np.sqrt(T))
            + r * K * np.exp(-r*T) * norm.cdf(-D2)
            - q * S * np.exp(-q*T) * norm.cdf(-D1)
        )

    else:
        raise ValueError("option must be 'call' or 'put'")

def rho(S, K, T, r, sigma, q=0.0, option="call"):
    D2 = d2(S, K, T, r, sigma, q=q)

    opt = option.lower()

    if opt == "call":
        return K * T * np.exp(-r*T) * norm.cdf(D2)

    elif opt == "put":
        return -K * T * np.exp(-r*T) * norm.cdf(-D2)

    else:
        raise ValueError("option must be 'call' or 'put'")




