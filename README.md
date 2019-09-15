
# HackTheNorth2019
Hack the north 2019 hack! Grabs articles from Reddit post that the user clicks on and plot's bias based on article category in a chrome extension. 

news_sources.json values derived from http://libguides.gustavus.edu/FakeNews
uses a scale of -5 to 5 to rank the general bias of a news news_sources. -5 being the most left, and 5 being the most right
** Note that having a rating scale is inherently biased in itself

### How to start the extension on a local server
1. in the project repo, run `node server.js`
2. in chrome, visit `chrome://extensions` and turn on Developer Mode in the top right
3. Click Load unpacked and select the `quickstart` folder in this project's repo
4. Enjoy!

Devpost link: https://devpost.com/software/speczo-n1zhpf
