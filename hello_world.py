def make_album(singer,name):
	"""唱片的歌手和名字"""
	full_blbum=singer+' '+name
	return full_blbum.title()
while True:
	print("\nPlease tell me the name and singer of this album: ")
	print("(enter 'q' at any time to quit)")
	singer=input("singer: ")
	if singer=='q':
		break
	name=input("name: ")
	if name=='q':
		break
	album=make_album(singer,name)
	print("\ni very like "+album+" !")
	

			
	
