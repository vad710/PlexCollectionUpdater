from plexapi.server import PlexServer
import os
import sys

baseurl: str = 'http://diskstation:32400'
token: str = sys.argv[1]
plex = PlexServer(baseurl, token)

LIBRARY_NAME: str = "Courses"

videos = plex.library.section(LIBRARY_NAME).all()

print("Processing {} Videos".format(len(videos)))

counter: int = 0

for video in videos:
    counter += 1
    for part in video.iterParts():

        base_folder: str = os.path.basename(os.path.dirname(os.path.dirname(part.file)))

        print("{} - Assigning video '{}' to collection '{}'".format(counter, part.file, base_folder))

        #if part.file[0:len(PATH_FOLDER)] == PATH_FOLDER:
        hasCollection = False
        for tag in video.collections:
            if tag.tag == base_folder:
                hasCollection = True
        if hasCollection:
            continue
        video.addCollection(base_folder)

print("Finished processing all files")