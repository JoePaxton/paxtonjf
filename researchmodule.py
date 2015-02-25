__author__ = 'JoePaxton'
import echonest.remix.audio as audio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

"""
Prints a  plot of the mean pitches over the segments during the track.
You can change the Track_ID on line 12 to a song you prefer.
Author: Joe Paxton
"""

def main():
    segments = audio.AudioAnalysis('TRVSKVZ1467FC8250D').segments
    collect = audio.AudioQuantumList()
    collect_t = audio.AudioQuantumList()
    
    for seg in segments:
        collect.append(seg.pitches)
        collect_t.append(seg.timbre)
        
    x=0
    y=0
    y_t = 0
        
    for i in range(len(collect)): 
        x = i
        y = np.mean(collect[i])
        plt.bar(x, y)
        
    for i in range(len(collect_t)): 
        x = i
        y_t = np.mean(collect_t[i])
        plt2.scatter(x, y_t)
        
    plt.title('Scatter Plot of Mean Values for Pitches by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Pitches')  
    plt.show()
    
    plt2.title('Bar Plot of Mean Values for Pitches by Segments')
    plt2.xlabel('Segments')
    plt2.ylabel('Pitches')
    pl2.show()
    return

if __name__ == '__main__':
    main()
