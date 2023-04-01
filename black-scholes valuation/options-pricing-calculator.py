import math

def binomial_tree(S, K, r, T, sigma, n, option_type):
    """
    Calculates the price of an American-style option using the binomial tree method.
    
    Parameters:
    S (float): current price of the underlying asset
    K (float): strike price of the option
    r (float): risk-free interest rate
    T (float): time to expiration (in years)
    sigma (float): volatility of the underlying asset
    n (int): number of time steps in the binomial tree
    option_type (str): 'call' or 'put'
    
    Returns:
    float: the estimated price of the option
    """
    dt = T / n
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)
    
    # Initialize the stock prices at each node of the tree
    stock_price = [[S * u ** j * d ** (i - j) for j in range(i + 1)] for i in range(n + 1)]
    
    # Initialize the option values at expiration
    option_value = [[max(0, stock_price[i][j] - K) if option_type == 'call' else max(0, K - stock_price[i][j]) for j in range(i + 1)] for i in range(n + 1)]
    
    # Work backwards through the tree to calculate the option value at each node
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            early_exercise = max(0, stock_price[i][j] - K) if option_type == 'call' else max(0, K - stock_price[i][j])
            option_value[i][j] = max(early_exercise, math.exp(-r * dt) * (p * option_value[i + 1][j + 1] + (1 - p) * option_value[i + 1][j]))
            
    return option_value[0][0]

# Example usage:
S = 100 # Current stock price
K = 105 # Strike price
r = 0.05 # Risk-free interest rate
T = 1 # Time to expiration (in years)
sigma = 0.2 # Volatility
n = 50 # Number of time steps in the binomial tree
option_type = 'call' # Type of option ('call' or 'put')

option_price = binomial_tree(S, K, r, T, sigma, n, option_type)
print(f"The estimated price of the {option_type} option is ${option_price:.2f}")
