#!/usr/bin/env python

import time


print("  __   __  __   _____   ____   __   __     _       ____   __ ")
print(" | _| |  \/  | | ____| |  _ \  \ \ / /    / \     / ___| |_ |")
print(" | |  | |\/| | |  _|   | | | |  \ V /    / _ \   | |      | |")
print(" | |  | |  | | | |___  | |_| |   | |    / ___ \  | |___   | |")
print(" | |  |_|  |_| |_____| |____/    |_|   /_/   \_\  \____|  | |")
print(" |__|====================================================|__|")
print("                     M   E   D   Y   A   C                   ")



title = raw_input ("Enter your index title: ")

txt = raw_input ("Enter your text her: ")

color = raw_input ("Enter your text color: ")

background = raw_input ("Enter your index background Color: ")

img = raw_input ("Enter link image for your index if you want: ")

song = raw_input ("Enter link song for your index if you want: ")

file=open('index.html', 'w')


a = '''
<html><head><title>%s</title></head><br><br>

<body bgcolor="%s" style="background-image: url('http://i50.tinypic.com/154x5s1.gif')">>

<center><h1><font color="%s"> %s </font></h1><br>

<img src="%s" alt="" ></center>


<embed name="song" src="%s" loop="false" hidden="true" autostart="true" alt="" >

               <center> <font face="Tahoma" size="3"> ============================================<br><br>

           <br>
<font size="+4" color="Red">
Sorry Admin This is just a Test :'(
<br>
		<font face="Tahoma" size="3"> =====================================================<br><br>


		[#] <font color="#FF0000">I'm Sorry Admin </font> ! <br>


<p><font face="Tahoma" size="2"></font></p>

		<br>

<p><font face="Tahoma" size="2">[#] Where is the Security ?</font></p>

<p><font face="Tahoma" size="2">[#] Server boXed | LOL ! <br> </font></p>

		<font color="#FF0000">[#] Contact:</font> https://www.facebook.com/????????</font></div>
<p></center>
''' %(title , background , color , txt , img , song)

file.write(a)

print("Please Wait ...")
time.sleep(3)
print("File successfully Created")
time.sleep(1)
print("[DONE]")