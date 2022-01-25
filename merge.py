import csv

with open("movies.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]
    headers = data[0]

headers.append("poster_link")
with open("final.csv","a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)

with open("movie_links.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovielinks = data[1:]

for i in allmovies:
    posterfound = any(i[0] in j for j in allmovielinks)
    if posterfound:
        for movielinkitem in allmovielinks:
            if i[0] == movielinkitem[0]:
                i.append(movielinkitem[1])
                if len(i) == 20:
                    with open("final.csv","a+",encoding="utf8") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(i) 
