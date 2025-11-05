# /// script
# dependencies = ["matplotlib"]
# ///

# run with: uv run assets/force-push.py

from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

frequencies = [
    "daily",
    "once every few days \n or once per PR",
    "once a week",
    "once a month or less",
    "never",
]

votes = [3, 3, 3, 21, 5]

error_votes_upper = [sqrt(n + 0.75) for n in votes]
error_votes_lower = [sqrt(n - 0.25) for n in votes]
error_votes = [error_votes_lower, error_votes_upper]

plt.barh(frequencies, votes, xerr=error_votes)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.title("How often do you force push?")
plt.xlabel("Number of regular git users in our team who voted.")
plt.savefig("assets/force-push.svg", bbox_inches="tight")
