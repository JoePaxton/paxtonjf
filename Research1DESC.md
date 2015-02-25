## Plot for Pitches and Timbre

**Purpose**

Displays a bar and scatter plot for timbres and pitches for each segment throughout the track, outputting four plots (two for each - four in total).

**Resources**

http://matplotlib.org/

**Explanation**

First you need to get the Track ID from the song you want to analyze. Then you can continue making your
graph the way you want it to look using http://matplotlib.org/. After this, I used a scatter and bar plot from 
the [matplotlib.org] API and fed the data of the mean of pitches and timbre into two different plots.

```python
import echonest.remix.audio as audio

trackID = <'TRACK_ID_OF_YOUR_FAVORITE_SONG'>
segments = audio.AudioAnalysis(trackID).segments
collect = audio.AudioQuantumList()
collect_t = audio.AudioQuantumList()

for seg in segments:
    collect.append(seg.pitches)
    collect_t.append(seg.timbre)
```
