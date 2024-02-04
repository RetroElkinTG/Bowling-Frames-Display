# DISCLAIMER: The entire code was created by me, with inspiration from
# Reddit user 'u/vault_dweller_707' from:
# https://www.reddit.com/r/dailyprogrammer/comments/7so37o/20180124_challenge_348_intermediate_bowling/
#
# Some exceptions are not taken into account 
# due to not being described in the challenge.
# These exceptions include; letters and empty inputs.

from ._anvil_designer import BowlingHomeTemplate
from anvil import *
import anvil.server

class BowlingHome(BowlingHomeTemplate):
  def __init__(self, **properties):
    # Sets the form properties.
    self.init_components(**properties)

  def submit_button_click(self, **event_args):
    # This method is called when the button is clicked.
    bowlinginput = self.bowling_score.text
    # Rolls, frames, and normal rounds are set.
    rolls = [int(i) for i in bowlinginput.split(" ") if i.isdigit()]
    frames = []  
    normal_rounds = 9  

    # Reddit Inspiration: START 
    # Counts normal bowling rounds.
    while normal_rounds > 0:  
        if rolls[0] == 10:  
            frames.append([10])  
            rolls = rolls[1:]  
        else:  
            frames.append([rolls[0],rolls[1]])  
            rolls = rolls[2:]  
        normal_rounds -=1  
    # Adds last frame to the frame list.
    frames.append(rolls)  
    # Loop through the frames to calculate the score.
    for i in range(len(frames)):  
        # Strikes replaced with 'X'.
        if len(frames[i]) == 1:  
            frames[i] = "X"  
        else:  
            # Spares replaced with '/'.
            if sum(frames[i][:2]) == 10:  
                frames[i][1] = "/"  
            # Misses replaced with '-'.
            if 0 in frames[i]:  
                frames[i][frames[i].index(0)] = "-"  
            for j in range(len(frames[i])):  
                # Bonus Round Strikes replaced with 'X'.
                if frames[i][j] == 10:  
                    frames[i][j] = "X"  
                # Convert scores to strings.
                else:  
                    frames[i][j] = str(frames[i][j])  
    # Reddit Inspiraton: END
                  
    # Joins all of the results and prints it for the user.       
    self.result.text = " ".join("".join(k for k in frames[l]) for l in range(len(frames)))