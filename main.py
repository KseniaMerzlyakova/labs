import pydub as pydub
#import os
#print(os.getcwd())
from pydub import AudioSegment
s = AudioSegment.from_file("12.wav")
sf = s.speedup(2.0)
sf.export('new.wav', format= "wav")
