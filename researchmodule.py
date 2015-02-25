__author__ = 'JoePaxton'
import echonest.remix.audio as audio
import numpy as np
import matplotlib.pyplot as plt

"""
Prints a plot of the mean pitches and timbre over the segments during the track.
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
        
    for i in range(len(collect)): 
        x = i
        y = np.mean(collect[i])
        y_t = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.scatter(x, y)

    plt.title('Scatter Plot of Mean Values for Pitches by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Pitches')  
    plt.show()      
        
    for i in range(len(collect)): 
        x = i        
        y = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.scatter(x, y)

    plt.title('Scatter Plot of Mean Values for Pitches by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Pitches')  
    plt.show()

    for i in range(len(collect)): 
        x = i
        y = np.mean(collect[i])
        y_t = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.bar(x, y)

    plt.title('Bar Plot of Mean Values for Timbre by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Timbre')  
    plt.show()      
        
    for i in range(len(collect)): 
        x = i        
        y = np.mean(collect_t[i])
        print '\rIterating through segments...',i,
        plt.bar(x, y)

    plt.title('Bar Plot of Mean Values for Timbre by Segments')
    plt.xlabel('Segments')
    plt.ylabel('Timbre')  
    plt.show()
        
    return

if __name__ == '__main__':
    main()
