import time

f = open('index - copy.html','a+')
fr = f.read()


u = input('>> Enter episode number, date:   ')

try:
	ul = u.split(',')

	if len(ul) == 2:
		new = fr.replace("var start_date = new Date('Nov 24 2020').getTime(); // Edit this", f"var start_date = new Date('{ul[1]}').getTime(); // Edit this")
		print(f'>> Updated - Ep: {ul[0]} | Date: {ul[1]}')
	elif len(ul) == 1:
		dt = time.strftime('%b %d %Y')
		new = fr.replace("var start_date = new Date('Nov 24 2020').getTime(); // Edit this", f"var start_date = new Date('{dt}').getTime(); // Edit this")
		print(f'Updated - Ep: {ul[0]} | Date: {dt}')

	new = new.replace('var eps_watched = 18; // Edit this', f'var eps_watched = {ul[0]}; // Edit this')
except:
	print(error)


f.write(new)

f.close()