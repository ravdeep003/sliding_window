import sys

def sliding_window():
	try :
		# using strip() to remove any spaces,if user adds it accidentally
		file_name = raw_input("Enter a valid file name:").strip() 
		file_obj = open(file_name, "r")
	except IOError:
		# if file doesnot exist, it displays the error message and exits
		print "Error: File not found!"  
		sys.exit() 

	window_size = int(file_obj.readline().strip())
	# using strip() to remove extra space left after last digt
	stream_num = file_obj.readline().strip()
	stream_num = map(int,stream_num.split(" ")) #
	length = len(stream_num)

	# creates a list of window size and moves the window along the stream
	for start_index in range(length - window_size + 1):   
		window = stream_num[start_index:window_size + start_index] 
		print min(window),

	# Closing file	
	file_obj.close()                      

if __name__ == "__main__":
	sliding_window()