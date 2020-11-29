from PIL import Image as i
import math

eps = int(input('>> Episodes watched:   ')) # Episdes watched

file = open('ep.txt','r') # Text file with current episode number
ce = int(file.read()) # Currnt episode
file.close()

print(eps, ce)
perc = eps/ce # Fraction completed
print(f'{perc*100}%')

mode = 'RGB'
twid, thei = 2000, 100

bkg = i.new(mode, (twid, thei)) # Background
bar = i.new(mode, (math.floor((twid-20)*perc), thei-20), (0, 255, 145))# Progress bar

bkg.paste(bar, (10,10))

bkg.save('progress_bar.png')
bkg.show()