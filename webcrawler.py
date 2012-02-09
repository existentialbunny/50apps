
'''
Crawl function will start from a seed link looking for queries

Seed - starts with a one term dictionary where the key is the 0th depth
    and the value is the starting site

depth - is the max depth to crawl, which also serves to rank per level

query - is a search string of words separated by space characters
'''
def Crawl(linklist={}, depth=2, query="python"):
    import urllib
    import re
    query = re.sub('\s+', '|',query)
    
    visitedlist = set()
    for i in linklist:
        visitedlist = visitedlist.union(set(linklist[i]))

    for i in range(depth):
        if i in linklist.keys():
            sitesperdepth=set(linklist[i])
        else:
            break
        for thissite in sitesperdepth:
            if thissite not in visitedlist or i == 0:
                try:
                    site = urllib.urlopen(thissite)
                    visitedlist.add(site)
                    contents = site.read()
                    rank = re.findall(query, contents,re.IGNORECASE)
                    if len(rank) > 0:
                        print("{0}, Search Rank: {1}, Seed Rank: {2}".format(thissite, len(rank), i))

                        links = re.findall(r"\<a href=[\'\"](http://[^\"\']+)[\"\']\>", contents)
                        
                        if (i + 1) in linklist.keys():
                            linklist[i + 1].extend(links)
                        else:
                            linklist[i + 1] = links
                        
                    site.close()
                except Exception:
                    print("BLACKLISTING: ", thissite)
                    visitedlist.add(thissite)
        
if __name__ == '__main__':
    Seed = {0:["http://news.ycombinator.com/"]} 
    Crawl(Seed, 5, "python hacker")
