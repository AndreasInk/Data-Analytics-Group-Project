# Audio Metadata Descriptions

The following are explanations of multiple metrics used in audio analysis  
More detailed descriptions can be found at [Aalto University's Speech Processing Book](https://speechprocessingbook.aalto.fi/Representations/Representations.html) or in the more research section.

## Data included

**Vocal Fundamental Frequency (VFF)** - The number of times the vocal cords, and the sound produced from them, oscillates per second, in hertz  
**Fo** - The average VFF over a period of time  
**Fhi** - The maximum VFF over a period of time  
**Flo** - The minimum VFF over a period of time  

**Jitter** - The variation in the period (the length of one oscillation) of the VFF. This corresponds to the variation in the pitch of the sound  
**Shimmer** - The variation in the amplitude (the height of one oscillation) of the VFF. This corresponds to the variation in the volume of the sound  

## Exploratory data (not included in dataset)

**Voice Onset Time** - The short delay between releasing certain consonants (like 'p' or 't') and when your vocal cords start vibrating. Can be slightly longer in PD.  
**Speech Rate** - Words spoken in a minute (or some other time period, tends to be lower in PD)  
**Noise to Harmonics Ratio** - A measure of how much noise is mixed into the voice. Higher values may reflect breathiness or hoarseness, which are more common in PD.  
**Recurrence Period Density Entropy** - Complexity of the signal (more predictable speech in PD)  

## Why these metrics?  
- Bradykinesia, a symptom of PD, affects motor control—including the fine motor skills required for speech.  
- PD can cause hypokinetic dysarthria, a motor speech disorder characterized by:  
    - Reduced loudness  
    - Monotone pitch  
	- Imprecise articulation  
	- Slowed or variable speech rate  

However, it's worth noting that people with Parkinson's have on and off times, meaning their symptoms fluctuate based on medication timing which may include changes in speech.  

## More Research on Audio Features

- **Fundamental Frequency (Fo, Fhi, Flo)**  
  - [Fundamental Frequency (F0) - Aalto University](https://speechprocessingbook.aalto.fi/Representations/Fundamental_frequency_F0.html)  
- **Jitter and Shimmer**  
  - [Jitter and Shimmer - Aalto University](https://speechprocessingbook.aalto.fi/Representations/Jitter_and_shimmer.html)  
- **Voice Onset Time (VOT)**  
  - [Voice Onset Time - ScienceDirect](https://www.sciencedirect.com/topics/medicine-and-dentistry/voice-onset-time)  
- **Speech Rate**  
  - [How Many Words Per Minute Do People Speak? - PlusAI Blog](https://plusai.com/blog/words-per-minute-for-speeches-and-presentations)  
- **Noise-to-Harmonics Ratio (NHR)**  
  - [Noise-to-harmonics ratio as an acoustic measure of voice disorders - PubMed](https://pubmed.ncbi.nlm.nih.gov/12002883/)  
- **Recurrence Period Density Entropy (RPDE)**  
  - [Biomedical Voice Analysis Using RPDE - NCBI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2583018/)  
- **Pitch Period Entropy (PPE)**  
  - [Voice disorder classification using PPE - ResearchGate](https://www.researchgate.net/publication/23406523_Exploration_of_Feature_Space_for_Disordered_Voice_Classification)  
- **Detrended Fluctuation Analysis (DFA)**  
  - [Nonlinear speech analysis algorithms - IEEE Xplore](https://ieeexplore.ieee.org/document/1415725)  