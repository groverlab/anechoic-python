import anechoic

data = anechoic.read("face.m4a") 

#anechoic.raw_plot(data)
anechoic.intensity_plot(data)
#anechoic.frequency_plot(data)

anechoic.show()

