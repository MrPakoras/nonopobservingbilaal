import time, re

f = open('index.html','r+')
fr = f.read()


u = input('>> Enter episode number, date:   ')

def fwrite(text):
	f.seek(0)
	f.write(text)
	f.truncate()

try:
	ul = u.split(',')

	if len(ul) == 2:
		new = re.sub(r"var start_date = new Date\('.*'\)\.getTime\(\); \/\/ Edit this", f"var start_date = new Date('{ul[1]}').getTime(); // Edit this", fr)
		fwrite()
		print(f'>> Updated - Ep: {ul[0]} | Date: {ul[1]}')
	elif len(ul) == 1:
		dt = time.strftime('%b %d %Y')
		new = re.sub(r"var start_date = new Date\('.*'\)\.getTime\(\); \/\/ Edit this", f"var start_date = new Date('{dt}').getTime(); // Edit this", fr)
		fwrite(new)		
		print(f'Updated - Ep: {ul[0]} | Date: {dt}')

	new = re.sub(r'var eps_watched = [0-9]*; \/\/ Edit this', f'var eps_watched = {ul[0]}; // Edit this', new)
	fwrite(new)
except:
	print(error)

#f.truncate()

f.close()