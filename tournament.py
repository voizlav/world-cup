import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():
    usage = "Usage: python tournament.py FILENAME"

    # Check the command-line input
    if len(sys.argv) != 2:
        sys.exit(usage)
    
    # Ensure correct file extension
    if sys.argv[1][len(sys.argv[1]) - 3:] != "csv":
        sys.exit(usage)

    # Load data
    with open(sys.argv[1]) as db:
        reader = csv.reader(db)
        data = list(reader)

    teams, counts = [], {}
    # Arrange data into teams and counter
    for team in data[1:]:
        teams.append({"team": team[0], "rating": int(team[1])})
        counts[team[0]] = 0

    # Simulate N tournaments and keep track of win counts
    simulation = 0
    while simulation != N:
        winner = simulateTournament(teams)
        counts[winner] += 1
        simulation += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

    sys.exit(0)


def simulateGame(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulateRound(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulateGame(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulateTournament(teams):
    """Simulate a tournament. Return name of winning team."""

    winner = teams
    # Continue simulating rounds until there is a winner
    while len(winner) != 1:
        winner = simulateRound(winner)

    return winner[0]["team"]


if __name__ == "__main__":
    main()