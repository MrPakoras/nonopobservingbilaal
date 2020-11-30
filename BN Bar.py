from PIL import Image as i
import math, os
from git import Repo

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

# filepath = 'C:/Users/Anas/AppData/Local/GitHubDesktop/GitHubDesktop.exe'
# os.startfile(filepath)

## https://stackoverflow.com/questions/41836988/git-push-via-gitpython

PATH_OF_GIT_REPO = "H:/Anas' Stuff/HTML-CSS-JS/HTML/nonopobservingbilaal/.git"  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'Updated Progress Bar'

print('Pushing to Github...')

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print('Done.')
    except:
        print('Some error occured while pushing the code')    

git_push()