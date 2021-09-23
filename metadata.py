import os

dirname = os.path.dirname(__file__)

x=1

while x <= 100:

	fin = open(dirname + '/data/metadata/origonal_data'+str(x)+'.json', 'rt')
	#output file to write the result to
	fout = open(dirname + '/data/metadata/edited_metadata/'+str(x)+'.json', "wt")
	#for each line in the input file
	for line in fin:
		#read replace the string and write to output file
		fout.write(line.replace('""', '"https://gateway.pinata.cloud/ipfs/Qma1rfddbns6hfqwf2GTxQwfYtREM6LXTHgDKatAEabsHC/PsychPunk_'+str(x)+'.png"'))
	#close input and output files
	fin.close()
	fout.close()
	x+=1
	
print('metadata edited')
print('---------------')
