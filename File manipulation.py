#create a file
#Steps->
#open a file,give name+extension,#clickenter(write in it)
fo=open("C:\\Users\\01.txt",'w')
fo.write("Done first one writing\n")
#write multiple lines 
list_lines=["1stone\n","2ndone for multiple writing\n"]
fo.writelines(list_lines)
fo.close()
#update a file
 #steps->same but open the file in append mode
fo=open("C:\\Users\\01.txt",'a')
fo.write("appending area")
#update with multiple lines
 #steps->same by creating the list of items
list_lines=["append multiple 1","append multiple 2"]
fo.writelines(list_lines)
fo.close()
#use case1
#one file has half data and the next file has half data, so make it into one
fp1=open("C:\\Users\\02.txt",'a')
fp2=open("C:\\Users\\03.txt",'r')
info=fp2.read()
fp1.write(info)
fp1.close()
fp2.close()
#moving a file
# steps0->import os and shutil and create new directory if need or else use shutil.move
import os,shutil
#os.mkdir("C:\\Users\\VISERION\\Documents\\sublime progs\\folder") already done once
##copying a file
##same 
#copy multiple files
list_lines=["C:\\Users\\01.txt","C:\\Users\\02.txt"]
#make a list of files to be copied and use a loop
for i in list_lines:
	shutil.copy(i,"C:\\Users\\folder")
#rename files
os.rename("C:\\Users\\y","C:\\Users\\001")
#same but .rename
