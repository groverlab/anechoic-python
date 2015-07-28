import anechoic

channel_one = anechoic.read("Anechoic_reflected_sound_file.m4a")
#anechoic.raw_plot(channel_one)
#anechoic.intensity_plot(channel_one)
anechoic.frequency_plot(channel_one)





