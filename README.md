## Hustlr: The Web App that Names Your Startup

A Flask webapp with a Mongo backend that will generate a name of a startup based on Hacker News.

![](https://raw.githubusercontent.com/veekaybee/hustlr/master/static/startup2.png)

To see it in action, [go here.](http://hackurname.com/) 

## About

This webapp serves the code needed to generate your own Hacker News startup name.

## Underlying Business Logic

```{python}

# Import Python HN API and Pyphen
from hackernews import HackerNews
import pyphen
import random
from itertools import chain

# Generate dictionary
dic = pyphen.Pyphen(lang='en')

# Generate HN
hn = HackerNews()

# Get top 50 Stories
top_stories = hn.top_stories(limit=50)

# Get individual words in titles
words = [title for story in top_stories for title in story.title.strip("'").strip(",").split(' ')]

# Get syllables per word
syllables = [syllable for word in words if not word.islower() and not word.isupper() for syllable in dic.inserted(word).split("-") ]

# Generate mixed list of syllables
mixed_bag = [syllable for syllable in syllables if len(syllables) > 1]

print("***Congrats on your new startup:***")
print(f"{random.choice(mixed_bag).upper()}{random.choice(mixed_bag).upper()}")

```

## To Build Locally:

1. Clone repo
2. Install `Mongo`, `Python3`, `Docker`, and `Docker-Compose`.
3. CD into the repo. 
4. Run `docker-compose build`
5. Run `docker-compose up`
6. Navigate to `localhost` on your browser. 
