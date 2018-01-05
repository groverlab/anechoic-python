import subprocess
import scipy.io.wavfile
import numpy
import tempfile
import os.path

def read(filename):
    subprocess.call(["ffmpeg", "-y", "-v", "24", "-i", filename, filename[:-3]+"wav"])
    w=scipy.io.wavfile.read(filename[:-3]+"wav")
    channel_one = numpy.float64(w[1][:,0])
    numpy.savetxt("out.csv", channel_one, delimiter=",")
    return channel_one

