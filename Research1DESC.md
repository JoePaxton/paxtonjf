## Plot for Pitches and Timbre

**Purpose**

Displays one plot that shows the average Pitches during each segment throughout the song and displays
another plot that shows the average Timbre during each segment throughout the song.

**Explanation**

First you need to get the Track ID from the song you want to analyze. Then you can continue making your
graph the way you want it to look using matplotlib. After this, I used a scatter and bar plot from 
the [matplotlib.org] API and fed the data of the mean of pitches and timbre into two different plot.

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

**Resources**

[matplotlib.org]: http://matplotlib.org/  
