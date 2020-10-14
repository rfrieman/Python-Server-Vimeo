#! /usr/bin/python3

from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
#my daily timelapses are named mmdd so the script needed a date function

import vimeo

vclient = vimeo.VimeoClient(
  token='******************************',
  key='************************************',
  secret='****************************************************************************************'
)
#in the strings '  ' replace the asterisks with your own personal token, key and secret as found on the myapps Vimeo page

video_uri = vclient.replace(
    video_uri='/videos/**********',
    filename='/data/timelapses/' + yesterday.strftime('%m%d') + '.mp4'
)
#video_uri is the directory at Vimeo's end. The asterisks should be replaced with the numerical string unique to the video who's file you are replacing.
#filename includes the entire directory path. My file changes name to reflect yesterday's date.
