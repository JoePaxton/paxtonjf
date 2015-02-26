#Problem

We want to shift the tempo (the pace of a musical composition) of a track in order to transition into another track
with a smooth transition. 

# Questions
1. Does [EchoNest] provide us with the tools/attributes to change the tempo of one track
   to match another track's tempo?
2. Does shifting the tempo of a track sound "smooth"?
3. Can we shift other attributes of a track in order to make a smooth transition?

# Resources
1. [EchoNest]
2. [stretch.py]

### 1. [EchoNest] tempo attribute:

The [EchoNest] provides us with infromation about the track's attributes. You can find the tempo and the
time signature of a track. When we print out 't', the only thing that comes up on the console is "Lateralus".
This is simply the song name from the "Tool Lateralus" album. I am not sure how to get the actual tempo
and time_signature as an actual value, but I will look at this more carefully in the [EchoNest] API. 

```python
import pyechonest.track as track

track = track.track_from_filename('C:\users\joe\desktop\lateralus.mp3')
track.tempo
print track
track.time_signature
print track

```
Running this code only prints "Lateralus" as stated above the code.

### 2. The relevance of [stretch.py]:

This example can be found on the [EchoNest Remix] API and it comes in a compressed zip folder of 
echo-nest-remix-examples. This expands the entire track, beat by beat. You can alter the timeScale
function to change the time of a beat and you can create a new track from these modified beats. 
When you import dirac, it only works on raw data for the first parameter and a floating-point ratio.

```python
import math
import os
import sys
import dirac
from echonest.remix import audio

audiofile = audio.LocalAudioFile(input_filename)
beats = audiofile.analysis.beats
collect = []

for beat in beats:
  beat_audio = beat.render()
  scaled_beat = dirac.timeScale(beat_audio.data, ratio)
  ts = audio.AudioData(ndarray=scaled_beat, shape=scaled_beat.shape,
      sampleRate=audiofile.sampleRate, numChannels=scaled_beat.shape[1])
  collect.append(ts)
  
out = audio.assemble(collect, numChannels=2)
out.encode(output_filename)
``` 
The render function gets the raw audio data from the beat and then is scaled by calling the
dirac.timeScale() function. After this we create a new AudioData object and append it to
an output list and write the output data.

[EchoNest]: http://developer.echonest.com/docs/v4/
[EchoNest Remix]: http://echonest.github.io/remix/apidocs/  
[stretch.py]:https://github.com/echonest/remix/blob/master/examples/stretch/simple_stretch.py
