from pytube import YouTube


#obtain user input
def user_input():
	link = input("Enter content link: ")
	yt = YouTube(link)
	return yt

#content metadata
def content_info(yt):
	print("Title: ", yt.title)
	print("Number of views: " + str(yt.views))
	print("Length of video: " + str(yt.length) + " seconds")
	print("Description: " + yt.description)
	print("Ratings: " + str(yt.rating))

#get highest resolution available
def locate_highest_res(yt):
	ys = yt.streams.get_highest_resolution()
	return ys

#starting download
def start_download(ys, path):
	print("Downloading..")
	ys.download(path)
	print("Donwload completed!!")



