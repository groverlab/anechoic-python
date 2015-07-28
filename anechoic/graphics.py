import numpy
import pylab

def raw_plot(channel_one):
    pylab.plot(numpy.linspace(0, len(channel_one)/44100.0, len(channel_one)), channel_one)
    pylab.xlabel("Time (s)  (equivalent to distance)")
    pylab.ylabel("Reflected sound measurements")
    pylab.show()

def intensity_plot(channel_one):
    pylab.plot(numpy.linspace(0, len(channel_one)/44100.0, len(channel_one)), numpy.power(channel_one,2))
    pylab.xlabel("Time (s)  (equivalent to distance)")
    pylab.ylabel("Reflected sound intensity")
    pylab.show()

def frequency_plot(channel_one):
    pylab.specgram(channel_one, Fs=44100)
    pylab.xlabel("Time (s)  (equivalent to distance)")
    pylab.ylabel("Frequency")
    pylab.show()

