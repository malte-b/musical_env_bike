# Project Documentation
## Data Sonification and Opportunities of Sound, WS 2020/21
Course offered by: Dr. Julia von Thienen, Dr. Marisol Jimenez, Dr. Henrik von Coler, Dr. Nico Steckhan & Dr. Knut Kaulke

### Project title
Musical Environmental Bike

### Team members, affiliations, contact details
**Malte Barth**  
malte.barth@student.hpi.de  
Data Engineering

**Carla Terboven**  
carla.terboven@student.hpi.de  
IT-Systems Engineering

### The project aim and why this is important
The *Sonic Bike* project already exists since 2008. The goal is to hear sonified air pollution data while riding a bike.

We joined the project after meeting *Kaffe Matthews*.
- unsere Ziele  (Gather environmental data

Attract attention of other pedestrians

Raise awareness of air pollution
?)

We believe that our computer science background can help us to (Projekt anders angehen und neue Möglichkeiten geben), allerdings keine ahnung von pd
<!-- 2) Introduction to the topic: basically ☺, please ensure a good consistency between your communicated project aims and the chosen sound design / sonification approach
2a) The aim of your project, and why it is important/interesting: Generally ☺, please re-adjust or amend based on your preferred methodology and solutions -->

### Theoretical embedding, related works
<!-- 2b) Theoretical embedding - related works: Please provide more literature references. For instance, what other approaches are there for the sonification of air pollution or similar data (where the Geiger counter can be one example)? What other approaches are there for the use of ordinary objects – like bikes – as artistic pieces to bring awareness to some issue?... -->

### Methods
The original sonic bike project gathers live data on the bike with an air pollution sensor with 12 channels. The data is then processed at the back of the bike, using Raspberry Pi and PD vanilla.
Due to the COVID-19 pandemic we decided to use CSV data instead of live data. Moreover we play our strength in programming skills and use a Python script to step through the data and preprocess it. Finally we use osc to send the processed information to PD. Here we read messages as notes and play the notes with a synthesizer to hear the sonified data.

// einleitung warum wir die nächsten 5 abschnitte gewählt haben
<!-- 3) Methods used: Generally ☺. Please ensure the communication of a suitable portfolio of project aims. E.g., why is it necessary to mimick chords, why do you create a rhythm etc.? Simpler approaches might be more suited to help listeners understand levels of air pollution in diagnostically straightforward ways. Maybe you have artistic aims? That’s good, just explain them. -->

#### Data Preparation
PM = “Particulate Matter“
PM 2.5 = amount of µg/m³ of particles	smaller than 2.5 µm

Average Limits per Year:

|          | PM 1     | PM 2.5   | PM 10    |
| -------- | -------- | -------- | -------- |
| EU       | -        | 25 µg/m³ | 40 µg/m³ |
| WHO      | -        | 10 µg/m³ | 20 µg/m³ |

// erklären wie und warum man zu disjoint kommt

![Disjoint PM Raincloud Plots](https://raw.githubusercontent.com/malte-b/musical_env_bike/readme_images/readme_images/disjoint_pm_raincloud.png)


#### Generate Pitch
Based on disjoint PM1 values

If pollution is high the pitch gets higher

// ADD DESCRIPTION

#### Generate Volume
Based on disjoint PM2.5 values

If pollution is high it gets louder

// ADD DESCRIPTION

#### Generate Rhythm
The rhythm can consist of eighth notes (E), quarter notes (Q) and half notes (H). If the PM values are high we want the music to be faster.  
Imagine we have 120 bpm. That is 2 beats per second. Since our sequencer steps 1 time every second we have for every data point 2 beats (= one half note) to compose.  
For each data point we generate two thresholds determining the probabilities for a slow, medium or fast rhythm. In the picture below these thresholds are 0.2, and 0.7. This means a 20% probability for a half note, 50% probability for a medium fast rhythm with quater notes and 30% probability for a fast rhythm with eighth notes.  
As shown in the picture below we generate a random number for each data point. By comparing that to the data-based thresholds we get the rhythm.

![Probability Based Rhythm Generation](https://raw.githubusercontent.com/malte-b/musical_env_bike/readme_images/readme_images/generate_rhythm.png)

#### PD Patch


### Work results
<!-- 4) Work results: creative outcome, e.g. demo, installation, code: Great that you had a well-functioning prototype and were able to share this in class! -->

### Where to find the code and demo/prototypical application
Code: https://github.com/malte-b/musical_env_bike  
In-Class Demo: https://1drv.ms/b/s!AnD1AVr_uHBJkHPlirrGs40Kx7ko?e=8xV6Z3  
Final Demo:

### Conclusion, discussion, limitations and avenues for future work
<!-- 5) Conclusion and discussion, including limitations of your work and potential avenues for future work: Please work this out in detail. There should be a headline “conclusions” re-stating your overarching aims/vision and reviewing how far you have come with this; there should be a headline “limitations” followed by a couple of bullet points with the limitations you currently acknowledge, suggesting next likely steps to follow. Compare your slide 11 to slide 4. Your next step is to use more than one channel. Why? Which of your three goals on slide 11 is not fully met as of yet? Why would creating more channels be a helpful means to better achieving this particular goal? -->
Next steps:
Add more than one channel to make multiple notes at the same time possible 
Maybe use a different synth


### Acknowledgements
We would like to thank Kaffe Matthews and Henrik von Coler for their help and expertise they shared with us.  
Kaffe Matthews inspired and leaded us to the sonic bike topic. She provided data and new ideas in several meetings.  
Henrik von Coler was our technical mentor and helped us in multiple meetings to set up the technical framework.

Thank you, Julia von Thienen for the inspiring lecture and the confidence that we will find a working, exciting project when we ourselves had no ideas yet.

### Reference List
<!-- Literature references: Please add this.
-->
Sonic Bikes  
https://sonicbikes.net/environmental-bike-2020/
https://www.kaffematthews.net/project/environmental-bike-2020
https://www.kaffematthews.net/category/Lisbon/
PD examples  
https://hvc.berlin/puredata/
https://archive.flossmanuals.net/pure-data/network-data/osc.html
