
def Crawl(linklist={}, depth=2, query="python"):
	import urllib
	import re

	flatlist = set()
	for i in linklist:
		flatlist = flatlist.union(set(linklist[i]))
	

	for i in range(depth):
		sitesperdepth=linklist[i]
		
		for thissite in sitesperdepth:
			print("OPENING: ", thissite)
			if thissite not in flatlist or i == 0:
				site = urllib.urlopen(thissite)
				contents = site.read()
				if re.findall(query, contents,re.IGNORECASE):
					print(thissite)

					links = re.findall(r"\<a href=[\'\"](http[s]*://[^\"\']+)[\"\']\>", contents)
					
					if (i + 1) in linklist.keys():
						linklist[i + 1].extend(links)
					else:
						linklist[i + 1] = links
					flatlist = flatlist.union(set(linklist))
		
if __name__ == '__main__':
	Seed = {0:["http://news.ycombinator.com/"]} 
	Seed[-1] = ["http://fish.sekure.us"]
	Crawl(Seed, 5, "python")