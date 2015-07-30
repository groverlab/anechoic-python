import numpy
import pylab
from matplotlib.ticker import FormatStrFormatter


def raw_plot(channel_one):
    pylab.plot(numpy.linspace(0, len(channel_one)/44100.0, len(channel_one)), channel_one)
    pylab.xlabel("Time (s)  (equivalent to distance)")
    pylab.ylabel("Reflected sound measurements")
    ax=pylab.gca()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.4f'))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
    pylab.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)

def intensity_plot(channel_one):
    pylab.plot(numpy.linspace(0, len(channel_one)/44100.0, len(channel_one)), numpy.power(channel_one,2))
    pylab.xlabel("Time (s)  (equivalent to distance)")
    pylab.ylabel("Reflected sound intensity")
    ax=pylab.gca()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.4f'))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
    pylab.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)

def frequency_plot(channel_one):
    pylab.specgram(channel_one, Fs=44100)
    pylab.xlabel("Time (s)  (equivalent to distance)")
    pylab.ylabel("Frequency")
    ax=pylab.gca()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.4f'))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
    pylab.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)

def show():
    pylab.show()


