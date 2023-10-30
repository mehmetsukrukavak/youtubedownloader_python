from pytube import YouTube

url = input("enter video url: ")

path = ""

YouTube(url).streams.get_highest_resolution().download(path)