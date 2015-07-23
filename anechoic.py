import subprocess
import scipy.io.wavfile
import pylab
import numpy

subprocess.call(["ffmpeg", "-y", "-v", "24", "-i", "Anechoic_reflected_sound_file.m4a", "out.wav"])
w=scipy.io.wavfile.read("out.wav")
channel_one = numpy.float64(w[1][:,0])
#pylab.specgram(channel_one, Fs=44100)
#pylab.psd(channel_one)
#pylab.plot(channel_one)
pylab.plot(numpy.linspace(0, len(channel_one)/44100.0, len(channel_one)), numpy.power(channel_one,2))
pylab.xlabel("Time (s)  (equivalent to distance)")
pylab.ylabel("Reflected sound intensity")
pylab.show()

