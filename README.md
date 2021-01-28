# musical_env_bike
This is the project "Musical Environmental Bike" which was created as part of the course Data Sonification at the HPI.

## The Data
![Disjoint PM Raincloud Plots](https://raw.githubusercontent.com/malte-b/musical_env_bike/readme_images/readme_images/disjoint_pm_raincloud.png)

## Generate Rhythm
The rhythm can consist of eighth notes (E), quarter notes (Q) and half notes (H). If the PM values are high we want the music to be faster.  
Imagine we have 120 bpm. That is 2 beats per second. Since our sequencer steps 1 time every second we have for every data point 2 beats (= one half note) to compose.  
For each data point we generate two thresholds determining the probabilities for a slow, medium or fast rhythm. In the picture below these thresholds are 0.2, and 0.7. This means a 20% probability for a half note, 50% probability for a medium fast rhythm with quater notes and 30% probability for a fast rhythm with eighth notes.  
As shown in the picture below we generate a random number for each data point. By comparing that to the data-based thresholds we get the rhythm.
![Probability Based Rhythm Generation](https://raw.githubusercontent.com/malte-b/musical_env_bike/readme_images/readme_images/generate_rhythm.png)
