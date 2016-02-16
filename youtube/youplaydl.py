#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2016 Anshul Joshi anshuljoshi.cse@gmail.com
# license: GNU GENERAL PUBLIC LICENSE <http://www.gnu.org/licenses/gpl-3.0.html>
#
# Anshul Joshi anshuljoshi.github.io

import re, urllib2, sys, time, os

def checkplaylist(playlisturl):
    if 'list=' in playlisturl:
        aftereq = playlisturl.rfind('=') + 1
        actualPlaylistURL = playlisturl[aftereq:]
        return actualPlaylistURL
    else:
        print "Booo..!! Could'nt find the playlist."
        exit(1)

def readPageSource(playlisturl):
    try:
        reqtoyoutube = urllib2.Request(playlisturl)
        readpagesource = urllib2.urlopen(reqtoyoutube).read()
        pagesource = str(readpagesource)
        return pagesource
    except urllib2.URLError as e:
        print e.reason
        exit(1)

def createURLsPlaylist(url_match):
    watchstring_amp = 0
    youtubeURL = []
    if url_match:
        for watch in url_match:
            watchstring = str(watch)
            if '&' in watchstring:
                watchstring_amp = watchstring.index('&')
            youtubeURL.append('http://www.youtube.com/' + watchstring[:watchstring_amp])
        allyoutubeURL = list(set(youtubeURL))
        return allyoutubeURL
    else:
        print "Oooops! Can't find videos in the playlist."
        exit(1)

def getURLofVideos(playlisturl, flag=0):
    pagesource = ''
    actualPlaylistURL = ''

    if flag==0:
        actualPlaylistURL = checkplaylist(playlisturl)
        pagesource = readPageSource(playlisturl)
    else:
        pagesource=open(playlisturl, "r").read()

    watchstring = re.compile(r'watch\?v=\S+?list=' + actualPlaylistURL)
    url_match = re.findall(watchstring, pagesource)
    allyoutubeURL = createURLsPlaylist(url_match)
    return allyoutubeURL

def dlvideo(url_arr):
    try:
        for i in url_arr:
            os.system('youtube-dl --output "%%(uploader)s%%(title)s.%%(ext)s" %s' %i)
    except:
        print "Boo!!!! You did something wrong..."

def dlaudio(url_arr):
    try:
        for i in url_arr:
            os.system('youtube-dl --extract-audio --audio-format mp3 --output "%%(uploader)s%%(title)s.mp3" %s' %i)
    except:
        print "Boo!!!! You did something wrong..."

def calldownloader(playlisturl,flag=0):
    if flag==0 or flag==1:
        listofURLs = getURLofVideos(playlisturl)
        if flag==1:
            dlaudio(listofURLs)
        else:
            dlvideo(listofURLs)
    elif flag==2:
        seturlfetch = 1
        listofURLs = getURLofVideos(playlisturl, seturlfetch)
        dlvideo(listofURLs)
    else:
        print "Wrong flag."
        exit(1)

def main():
    flag=0
    if len(sys.argv) < 2:
        print "USAGE: python youplaylistdl.py <URLofPlaylist>/<PageSource> Option(default=0(videos), 1(audio), 2(provide pagesource))"
        exit(1)
    else:
        source = sys.argv[1]
        try:
            if sys.argv[2]:
                flag = int(sys.argv[2])
        except:
            pass
        if flag!=2 and 'http' not in source:
            source = 'http://' + source
            calldownloader(source, flag)
        else:
            calldownloader(source, flag)

if __name__ == '__main__':
    main()
