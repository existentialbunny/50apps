
def Crawl(linklist={}, depth=2, query="python"):
	import urllib
	import re

	visitedlist = set()
	for i in linklist:
		visitedlist = visitedlist.union(set(linklist[i]))

	for i in range(depth):
		if i in linklist.keys():
			sitesperdepth=linklist[i]
		else:
			break
		for thissite in sitesperdepth:
			if thissite not in visitedlist or i == 0:
				try:
					site = urllib.urlopen(thissite)
					visitedlist.add(site)
					contents = site.read()
					if re.findall(query, contents,re.IGNORECASE):
						print(thissite)

						links = re.findall(r"\<a href=[\'\"](http[s]*://[^\"\']+)[\"\']\>", contents)
						
						if (i + 1) in linklist.keys():
							linklist[i + 1].extend(links)
						else:
							linklist[i + 1] = links
						
					site.close()
				except Exception:
					print("FAILED OPENING: ", thissite)
		
if __name__ == '__main__':
	Seed = {0:["http://news.ycombinator.com/"]} 
	Seed[-1] = ["http://fish.sekure.us"]
	Crawl(Seed, 5, "python")