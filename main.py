import requests, string, random, threading


print('How many memes do you want to scrape? [Max 50]')
amount = int(input('> '))

print('Which subreddit do you want to scrape from?')
subreddit = input('> ')

def downloadMeme(meme):
    ra = requests.get(meme['url']).content
    open(f'Memes/{"".join(random.choices(string.ascii_uppercase + string.digits, k=15))}.png', 'wb').write(ra)
    print(meme['url'])

currentScrape = ''
while amount > 50:
    r = requests.get(f'https://meme-api.herokuapp.com/gimme/{subreddit}/50')
    for meme in r.json()['memes']:
        threading.Thread(target=downloadMeme, args=(meme,)).start()
    amount -= 50
    currentScrape = r.text

r = requests.get(f'https://meme-api.herokuapp.com/gimme/{subreddit}/{amount}')
if currentScrape != r.text:
    for meme in r.json()['memes']:
        threading.Thread(target=downloadMeme, args=(meme,)).start()
