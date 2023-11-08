"""
Try to help Harry Potter calculate the final points for a Quidditch
game. In the game, players score points by successfully scoring goals and catching the
Golden Snitch. You'll need to write a Python program that calculates the total points for a
Quidditch match based on the provided data.
You are provided with a list called quidditch_events, which contains strings representing the
events that occurred during the Quidditch match. Each event can be one of the following:
➢ "goal": Represents a successful goal scored by a team. This event is worth 10 points.
➢ "snitch": Represents the capture of the Golden Snitch, which is worth 150 points.
➢ "foul": Represents a foul committed during the game. A foul deducts 30 points from
the team's score.
Example: quidditch_events = ["goal", "goal", "snitch", "goal", "foul", "goal"]
Create two variables, gryffindor_score and slytherin_score, initialized to 0, to keep track
of the points scored by each team.
Loop through the quidditch_events list and use conditional statements to update the scores
accordingly. After processing all the events, compare the scores of the two teams. The team
with the higher score wins the match. If the scores are tied, the match is declared a tie.
Print the final scores for Gryffindor and Slytherin, and declare the winner or announce a tie
"""

quidditch_events = ["goal", "goal", "snitch", "goal", "foul", "goal"]

gryffindor_score = 0
slytherin_score = 0
ravenclaw_score = 0
hufflepuff_score = 0

for event in quidditch_events:
  if event == "goal": 
    gryffindor_score += 10
    slytherin_score += 10
    ravenclaw_score += 10
    hufflepuff_score += 10
  elif event == "snitch":
    gryffindor_score += 150
    slytherin_score += 150
    ravenclaw_score += 150
    hufflepuff_score += 150
  elif event == "foul": 
    gryffindor_score -= 30
    slytherin_score -= 30
    ravenclaw_score -= 30
    hufflepuff_score -= 30

if gryffindor_score > slytherin_score:
  print("Gryffindor wins the match!")
elif slytherin_score > gryffindor_score:
  print("Slytherin wins the match!")
else:
  print("The match is a tie!")

print(f"Gryffindor: {gryffindor_score} points")
print(f"Slytherin: {slytherin_score} points")
