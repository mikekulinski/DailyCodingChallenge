import math

def build_cheapest_houses(price_matrix):
    best_prices = [[None for i in range(len(price_matrix[j]))] for j in range(len(price_matrix))]

    for r in range(len(price_matrix)):
        for c in range(len(price_matrix[r])):
            if (r - 1 >= 0):
                minimum = math.inf
                for i in range(len(best_prices[r-1])):
                    if abs(c - i) > 1:
                        if best_prices[r-1][i] < minimum:
                            minimum = best_prices[r-1][i]

                best_prices[r][c] = minimum + price_matrix[r][c]
            else:
                best_prices[r][c] = price_matrix[r][c]

    return min(best_prices[-1])

if __name__ == "__main__":
                # colors
    prices = [[1, 2, 3, 4], # house1
              [1, 5, 10, 5]] # house2


    print(build_cheapest_houses(prices))