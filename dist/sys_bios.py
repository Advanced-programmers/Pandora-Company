#coding=utf-8

'''
The format of this code is advocated!

vFile = [directory:str, fileName:str, [Content..:str]]
vFolder = [directory:str, folderName:str, [vFolder..], [vFile..]]

Version:1.0
'''

import os

class BIOS:

	'''
	new(path):
		New a file.
	delete(path):
		Delete a file.
	load(path):
		Load a file.
	save(file):
		Save a file.
	getEveryFileByDir(withPath = False):
		Get a list of every file with data.
	getEveryFolderByDir(withPath = False):
		Get a list of every folder.
	'''

	# Public function
	def new(self, vFile):
		self.setVFile(vFile)

	def delete(self, vFile):
		pass

	def getVFile(self, vFile):
		if os.path.exists(vFile[0] + '\\' + vFile[1]):
			file = open(vFile[0] + '\\' + vFile[1])
			raw_content = file.readlines()
			file.close()
			content = []
			for line in raw_content:
				if line[-1] == '\n':
					content.append(line[0:-1])
				else:
					content.append(line)
			return [vFile[0], vFile[1], content]
		else:
			print('[WARN][BIOS-getVFile]There is no file named: \'' + vFile[0] + '\\' + vFile[1] + '\'')

	def setVFile(self, vFile):
		path = vFile[0] + '\\' + vFile[1]
		file = open(path, 'w')
		# print(self.content,self.path)
		for line in vFile[2]:
			file.writelines(line + '\n')
		file.close()

	def getVFolder(self, vFolder):
			path = ''
			if vFolder[0] == '':
				path = vFolder[1]
			else:
				path = vFolder[0] + '\\' + vFolder[1]
			list = os.listdir(path)
			# Generate subVFolder.
			subVFolder = []
			subVFile = []
			for each in list:
				if os.path.isdir(path + '\\' + each):
					subVFolder.append(self.getVFolder([path, each]))
			# Generate subVFile.
				elif os.path.isfile(path + '\\' + each):
					subVFile.append(self.getVFile([path, each]))
			return [vFolder[0], vFolder[1], subVFolder, subVFile]

	def isExist(self, vFile):
		if os.path.exists(vFile[0] + '\\' + vFile[1]):
			return True
		else:
			return False

if __name__ == '__main__':
	I = BIOS()

# TEST function-new(self, vFile):void
	# Test 1: New a empty file in "test\".
	print('Test 1: New a empty file in "test\\".')
	print('Forecast result: "".')
	newTestFile = ['test', 'newEmptyFile.txt', []]
	I.new(newTestFile)
	print('Result: "' + '' + '".\n')

	# Test 2: New a file with content in "test\".
	print('Test 2: New a file with content in "test\\".')
	print('Forecast result: "".')
	newFile = ['test', 'newFile.txt', ['Line 1', 'Line 2']]
	I.new(newFile)
	print('Result: "' + '' + '".\n')

# TEST function-getVFile(path):[Directory, [vFolder..], [vFile..]]
	# Test 3: Get "test\newFile.txt" & print.
	print('Test 3: Get "test\\newFile.txt" & print.')
	print('Forecast result: "[\'Line 1\', \'Line 2\']".')
	file = I.getVFile(['test', 'newFile.txt'])
	print('Result: "' + str(file[2]) + '".\n')

	# Test 4: Add a line in "test\newFile.txt" & save & print.
	print('Test 4: Add a line in "test\\newFile.txt" & save & print.')
	print('Forecast result: "[\'Line 1\', \'Line 2\', \'Line 3\']".')
	file[2].append('Line 3')
	I.setVFile(file)
	file = I.getVFile(['test', 'newFile.txt'])
	print('Result: "' + str(file[2]) + '".\n')

# TEST function-getVFolder(dir):[fileList..]
	# Test 5: Print every file in "test\".
	print('Test 5: Print every file in "test\\".')
	print('Forecast result: "[[\'test\', \'newEmptyFile.txt\', []], [\'test\', \'newFile.txt\', [\'Line 1\', \'Line 2\', \'Line 3\']]]".')
	print('Result: "' + str(I.getVFolder(['', 'test'])[3]) + '".\n')

	# Test 6: Print every folder name in "test\".
	print('Test 6: Print every thing in "test\\".')
	print('Forecast result: "[[\'test\', \'Folder 1\', [], []], [\'test\', \'Folder 2\', [], []]]".')
	print('Result: "' + str(I.getVFolder(['', 'test'])[2]) + '".\n')
