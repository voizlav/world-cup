# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():
    usage = "Usage: python tournament.py FILENAME"

    # Ensure correct usage
    if len(sys.argv) != 2:
        print(usage)
        sys.exit(1)

    if sys.argv[1][len(sys.argv[1]) - 3:] != "csv":
        print(usage)
        sys.exit(1)

    # Load data
    with open(sys.argv[1]) as db:
        reader = csv.reader(db)
        data = list(reader)

    teams, counts = [], {}
    # Arrange data into teams and counter
    for team in data[1:]:
        teams.append({'team': team[0], 'rating': int(team[1])})
        counts[team[0]] = 0

    # Simulate N tournaments and keep track of win counts
    simulation = 0
    while simulation != N:
        winner = simulate_tournament(teams)
        counts[winner] += 1
        simulation += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

    sys.exit(0)


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""

    winner = teams
    # Continue simulating rounds until there is a winner
    while len(winner) != 1:
        winner = simulate_round(winner)

    return winner[0]['team']


if __name__ == "__main__":
    main()