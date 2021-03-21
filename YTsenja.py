from pytube import YouTube
from moviepy.editor import *
import os
def mp4():
	url = input("masukan link > ")
	v = YouTube(url)
	yt = v.streams.first()
	yt.download()
def menu():
	os.system("figlet Yt Downloader")
	print("By Senja")
	print("mailme : SenjaID@protonmail.ch")
	print("\n")
	print("1.download")
	print("2.convert mp4 ke mp3")
	print("0.exit")
def menu2():
	print("1.download mp4")
	print("0.kembali")

menu()
menu1 = input("masukan pilihan> ")
if menu1 == "1":
	menu2()
	menu2 = input("masukan pilihan> ")
	if menu2 == "1":
		mp4()
if menu1 == "0":
	exit()
if menu1 == "2":
	print("convert mp4 to mp3 ")
	print("\n")
	print("masukan judul lagu yang baru di download")
	nama = input("masukan judul lagu> ")
	nama2 = input("masukan output lagu> ")
	vd = VideoFileClip(nama)
	ad = vd.audio
	ad.write_audiofile(nama2)
	ad.close
	vd.close
else:
    os.system("python3 J.py")