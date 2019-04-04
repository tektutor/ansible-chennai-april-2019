#!/usr/bin/python

class MediaPlayer:
   
   def __init__(self):
       print('MediaPlayer constructor')

   def play(self):
       print('MediaPlayer is playing')

class VideoPlayer(MediaPlayer): 

   def __init__(self):
      MediaPlayer.__init__(self)
      print('VideoPlayer constructor')

   def play(self):
       MediaPlayer.play(self)
       print('VideoPlayer is playing')

class MP3Player(MediaPlayer): 

   def __init__(self):
      MediaPlayer.__init__(self)
      print('MP3Player constructor')

   def play(self):
       MediaPlayer.play(self)
       print('Mp3 Player is playing')

videoPlayer = VideoPlayer()
videoPlayer.play()

mp3Player = MP3Player()
mp3Player.play()

videoPlayer = mp3Player
videoPlayer.play()









