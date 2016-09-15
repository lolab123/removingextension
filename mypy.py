import os
import sys



for i in range (0,1000):
	var = raw_input('enter the extension:  ')
	var2 = 'dir /b/s *.'+ (var)
	var3 = 'del /s *.'+ (var)
	print (var3)
	print ('following file will be deleted.')
	i = os.system(var2)
	os.system(var3)
	break

Hello world
