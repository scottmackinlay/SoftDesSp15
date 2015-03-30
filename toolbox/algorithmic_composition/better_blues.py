""" Synthesizes a blues solo algorithmically """

from Nsound import *
import numpy as np
from random import choice
import random

sampling_rate = 44100.0
Wavefile.setDefaults(sampling_rate, 16)

bass = GuitarBass(sampling_rate)    # use a guitar bass as the instrument
solo = AudioStream(sampling_rate, 1)
blues_scale = [0, 25, 28, 30, 31, 32, 35, 37, 40, 42, 43, 44, 47, 49, 52, 54]
beats_per_minute = 45               # Let's make a slow blues solo

def add_note(out, instr, key_num, duration, bpm, volume):
    """ Adds a note from the given instrument to the specified stream

        out: the stream to add the note to
        instr: the instrument that should play the note
        key_num: the piano key number (A 440Hzz is 49)
        duration: the duration of the note in beats
        bpm: the tempo of the music
        volume: the volume of the note
	"""
    freq = (2.0**(1/12.0))**(key_num-49)*440.0
    stream = instr.play(duration*(60.0/bpm),freq)
    stream *= volume
    out << stream


def make_lick(bars,speediness):
    total=0 #amount of time spent in this lick
    curr_note=7
    score=[]
    while 1:
        note_change=random.randint(-3,3)
        duration=random.randint(1,4)/float(speediness)
        if total+duration<bars:
            total+=duration
            score+=[[curr_note+note_change,duration]]
        else:
            score+=[[0,bars-total]]
            return score
    
def make_score(bars):
    lick=make_lick(2)
  

score=(make_lick(4,4)*3+make_lick(4,4))*2
for note in score:
    curr_note=note[0]
    add_note(solo, bass, blues_scale[curr_note], note[1], beats_per_minute, 1.0)

# solo >> "blues_solo.wav"


backing_track = AudioStream(sampling_rate, 1)
Wavefile.read('backing.wav', backing_track)
m = Mixer()
solo *= 0.7             # adjust relative volumes to taste
backing_track *= 2.0
m.add(2.25, 0, solo)    # delay the solo to match up with backing track    
m.add(0, 0, backing_track)
m.getStream(500.0) >> "slow_blues.wav"