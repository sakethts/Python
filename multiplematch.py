filenames = ["1.txt", "2.txt", "3.txt" , "4.txt"] #file names to be matched
files = [open(name) for name in filenames]
sets = [set(line for line in file) 		#Line by line matching
            for file in files]
#with open('1.txt', 'r') as file1:
#    with open('2.txt', 'r') as file2:
#	with open('3.txt', 'r') as file3:
same = set.intersection(*sets)

same.discard('\n')

with open('output.txt', 'w') as file_out:	#output file
    for line in same:
        file_out.write(line)





