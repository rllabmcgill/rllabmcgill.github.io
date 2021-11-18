# OG Author: Pierre Luc Bacon
# Updated by: Koustuv Sinha

import feedparser
from operator import itemgetter
from collections import defaultdict
from bs4 import BeautifulSoup
import yaml

# Profs with their DBLP RSS feeds and the start dates
# Include `dblp` and `startyear` tags in _data/professors.yml file
# to search DBLP for their papers

professors = yaml.load(open("_data/professors.yml"))
profs_with_dblp = [p for p in professors if ("dblp" in p) and ("startyear" in p)]
print(f"Fetching paper details for {len(profs_with_dblp)} professors and affiliates")

# File where the papers will be written. This file is included by `_pages/publications.md`
output_file = "_includes/dblp_pubs.html"

publications = defaultdict(dict)

# Maintain a list of unique papers
seen_entries = []
total = 0

print("Fetching papers from DBLP...")
for prof in profs_with_dblp:
    prof_name = prof["name"]
    print(f"Fetching papers for author : {prof_name}")
    dblp = prof["dblp"]
    start_year = prof["startyear"]
    d = feedparser.parse(dblp)
    print(f"Got {len(d['entries'])} papers")
    ct = 0

    for entry in d["entries"]:
        # Prune papers beyond profs start date at McGill
        if int(entry["published"]) < int(start_year):
            continue
        # DBLP returns all arxiv papers as well. Assuming the conference paper is the latest one,
        # we choose the first entry of the title.
        # This also assumes no two paper has the same title.
        if entry["title"] not in seen_entries:
            # Parse the summary, which is a formatted html.
            soup = BeautifulSoup(entry["summary"], "html.parser")
            authors = soup.find_all(itemprop="author")
            author_string = ",".join([str(auth.contents[0]) for auth in authors])
            # Not all papers have correct venues, ignore them
            isPartOf = soup.find_all(itemprop="isPartOf")
            if len(isPartOf) == 0:
                venue = ""
            else:
                isPartOfContents = isPartOf[0].contents
                if len(isPartOfContents) == 0:
                    venue = ""
                else:
                    venue = isPartOfContents[0].get_text() + f" ({entry['published']})"
            title_with_link = f"<i><a href='{entry['link']}'>{entry['title']}</a></i>"
            formatted_cite = author_string + "; " + title_with_link + " " + venue
            publications[int(entry["published"])][entry["id"]] = formatted_cite
            seen_entries.append(entry["title"])
            ct += 1

    print(f"Collected {ct} papers")
    total += ct

print(f"Writing total of {total} papers in {output_file}")

# Write in the output file
with open(output_file, "w") as f:
    # add an index for quick search
    years = publications.keys()
    header = "Years active:" + ",".join([f" [{y}](#{y})" for y in years]) + "\n\n"
    f.write(header)
    for year, pubs in sorted(publications.items(), key=itemgetter(0), reverse=True):
        if year > 1997:
            pubsyear = ["<li>" + pub + "</li>\n\n" for pub in pubs.values()]
            f.write("## {0}\n\n <ul>{1}</ul>\n\n".format(year, "".join(pubsyear)))

print("Done")
