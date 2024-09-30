import numpy as np
import matplotlib.pyplot as plt

def simulate_betting(initial_capital, bet_size, num_simulations, max_rounds):
    all_capitals = []
    rounds_to_end = []        # Number of rounds played in each simulation
    max_capitals = []         # Maximum capital achieved in each simulation
    final_capitals = []       # Final capital at the end of each simulation
    bankruptcies = 0          # Number of simulations where player went bankrupt
    rounds_before_bankruptcy = []  # Rounds before bankruptcy in simulations that ended in bankruptcy

    for _ in range(num_simulations):
        capitals = [initial_capital]
        capital = initial_capital
        max_capital = initial_capital

        for round_number in range(max_rounds):
            if capital <= 0:
                bankruptcies += 1
                rounds_before_bankruptcy.append(round_number)
                break  # Player is bankrupt
            # Adjust bet size if it exceeds current capital
            current_bet = min(bet_size, capital)
            # Simulate win (+1) or loss (-1)
            outcome = np.random.choice([1, -1])
            capital += current_bet * outcome
            capitals.append(capital)
            if capital > max_capital:
                max_capital = capital
        else:
            # Completed max_rounds without bankruptcy
            round_number = max_rounds

        rounds_played = len(capitals) - 1  # Number of rounds played
        rounds_to_end.append(rounds_played)
        max_capitals.append(max_capital)
        final_capitals.append(capital)
        all_capitals.append(capitals)

    # Determine the length of the longest simulation
    max_length = max(len(c) for c in all_capitals)

    # Pad shorter simulations with their last capital value
    for capitals in all_capitals:
        if len(capitals) < max_length:
            capitals.extend([capitals[-1]] * (max_length - len(capitals)))

    # Calculate the average capital over time
    average_capital = np.mean(all_capitals, axis=0)

    # Plotting
    plt.figure(figsize=(12, 6))

    # Plot each simulation with faded lines
    for capitals in all_capitals:
        plt.plot(capitals, color='blue', alpha=0.05)

    # Plot the average capital with a bold line
    plt.plot(average_capital, color='red', linewidth=2, label='Average Capital')

    plt.title('Betting Strategy Simulation')
    plt.xlabel('Number of Rounds')
    plt.ylabel('Capital')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calculate Metrics
    avg_rounds_played = np.mean(rounds_to_end)
    avg_max_capital = np.mean(max_capitals)
    avg_final_capital = np.mean(final_capitals)
    bankruptcy_rate = (bankruptcies / num_simulations) * 100
    avg_rounds_before_bankruptcy = np.mean(rounds_before_bankruptcy) if bankruptcies > 0 else 0
    max_capital_overall = np.max(max_capitals)
    min_final_capital = np.min(final_capitals)

    # Print Metrics
    print("Simulation Metrics:")
    print(f"Average Number of Rounds Played: {avg_rounds_played:.2f}")
    print(f"Average Maximum Capital Achieved: {avg_max_capital:.2f}")
    print(f"Average Final Capital: {avg_final_capital:.2f}")
    print(f"Probability of Bankruptcy: {bankruptcy_rate:.2f}%")
    if bankruptcies > 0:
        print(f"Average Rounds Before Bankruptcy: {avg_rounds_before_bankruptcy:.2f}")
    print(f"Maximum Capital Achieved Across All Simulations: {max_capital_overall:.2f}")
    print(f"Minimum Final Capital: {min_final_capital:.2f}")

    # Plot Histogram of Final Capitals
    plt.figure(figsize=(10, 5))
    plt.hist(final_capitals, bins=50, color='green', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Final Capital')
    plt.xlabel('Final Capital')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Adjustable parameters
initial_capital = 100    # Starting capital N
bet_size = 10            # Bet size
num_simulations = 500    # Number of simulations to run
max_rounds = 10         # Maximum number of rounds per simulation

simulate_betting(initial_capital, bet_size, num_simulations, max_rounds)

