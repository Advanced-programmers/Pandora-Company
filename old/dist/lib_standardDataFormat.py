#coding=utf-8

'''
The format of this code is advocated!

Version:1.0
'''

import sys_bios

class infoLoader:

	'''
	This class is used to be a container of a infoFile.

	load(path):
		Load infoFile.
	save():
		Save infoFile.
	setValueByEntry(entry, value, section = ''):
		Set value.
	getValueByEntry(entry, section = ''):
		Get value.
	addValueByEntry(entry, section = '', addend = 1):
		Add the value by a number.
	TODO delEntry(entry, section = '')
	'''

	bios = sys_bios.BIOS()

	# Public function
	def load(self, vFile):
		self.content = self.bios.getVFile(vFile)

	def save(self):
		self.bios.save(self.content)

	def setValueByEntry(self, entry, value, section = ''):
		value = str(value)
		currentSection = ''
		newData = []
		section_found = False
		entry_found = False
		for line in self.content[2]:
			if line[0] == '[':
				flag1, flag2 = 0, line.find(']')
				if flag2 != -1:
					while line[flag1 + 1] == ' ':
						flag1 += 1#'_|_s'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'n|_'
					currentSection = line[flag1 + 1:flag2]
					newData.append('[ ' + currentSection + ' ]')
				else:
					print('[WARN]Broken data in:' + self.content[0] + '\\' + self.content[1] + '\'')
			elif currentSection == section:
				section_found = True
				if line.find('=') != -1:
					flag1, flag2, flag3, flag4 = 0, line.find('='), line.find('='), len(line)
					while line[flag1] == ' ':
						flag1 += 1#'_|e'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'y|_'
					while line[flag3 + 1] == ' ':
						flag3 += 1#'_|_v'
					while line[flag4 - 1] == ' ':
						flag4 -= 1#'e|_'
					if line[flag1:flag2] == entry:
						entry_found = True
						newData.append(line[flag1:flag2] + ' = ' + value)
					else:
						newData.append(line[flag1:flag2] + ' = ' + line[flag3 + 1:flag4])
		if not section_found:
			newData.append('[ ' + section + ' ]')
		self.content = [self.content[0], self.content[1], newData]
		if not entry_found:
			currentSection = ''
			newData = []
			for line in self.content[2]:
				if line[0] == '[':
					flag1, flag2 = 0, line.find(']')
					if flag2 != -1:
						while line[flag1 + 1] == ' ':
							flag1 += 1#'_|_s'
						while line[flag2 - 1] == ' ':
							flag2 -= 1#'n|_'
						currentSection = line[flag1 + 1:flag2]
						newData.append('[ ' + currentSection + ' ]')
						if currentSection == section:
							newData.append(entry + ' = ' + value)
					else:
						print('[WARN]Broken data in: \'' + self.content[0] + '\\' + self.content[1] + '\'')
				else:
					newData.append(line)
			self.content = [self.content[0], self.content[1], newData]

	def getValueByEntry(self, entry, section = ''):
		section_found = False
		entry_found = False
		currentSection = ''
		for line in self.content[2]:
			if line[0] == '[':
				flag1, flag2 = 0, line.find(']')
				if flag2 != -1:
					while line[flag1 + 1] == ' ':
						flag1 += 1#'_|_s'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'n|_'
					currentSection = line[flag1 + 1:flag2]
				else:
					print('[WARN]Broken data in: \'' + self.content[0] + '\\' + self.content[1] + '\'')
			elif currentSection == section:
				section_found = True
				if line.find('=') != -1:
					flag1, flag2, flag3, flag4 = 0, line.find('='), line.find('='), len(line)
					while line[flag1] == ' ':
						flag1 += 1#'_|e'
					while line[flag2 - 1] == ' ':
						flag2 -= 1#'y|_'
					while line[flag3 + 1] == ' ':
						flag3 += 1#'_|_v'
					while line[flag4 - 1] == ' ':
						flag4 -= 1#'e|_'
					if line[flag1:flag2] == entry:
						entry_found = True
						return line[flag3 + 1:flag4]
		if not section_found:
			print('[WARN]There is no section: \'' + section + '\' in file: \'' + self.content[0] + '\\' + self.content[1] + '\'')
		elif not entry_found:
			print('[WARN]There is no entry: \'' + entry + '\' in section: \''+ section + '\' in file: \'' + self.content[0] + '\\' + self.content[1] + '\'')

	def addValueByEntry(self, entry, section = '', addend = 1):
		value = self.getValueByEntry(entry, section)
		if value.isdigit():
			newValue = int(value) + addend
			self.setValueByEntry(entry, newValue, section)
		else:
			print('[WARN]The custom variables:\'' + entry + '\' in section: \'' + section + '\' in file: \'' + self.content[0] + '\\' + self.content[1] + '\' is not numbers!')

class cmdLoader:

	bios = sys_bios.BIOS()

	def load(self, vFile):
		self.content = self.bios.getVFile(vFile)

	def save(self):
		self.bios.save(self.content)

	def isExist(self, vFile):
		if self.bios.isExist(vFile):
			return True
		else:
			return False

if __name__ == '__main__':
	I = infoLoader()
	I.load('save\sys.save')
	I.setValueByEntry('name', 'YYY', 'value')
	print(I.getValueByEntry('name', 'value'))
	I.setValueByEntry('age', 18, 'value')
	print(I.getValueByEntry('age', 'value'))
	I.addValueByEntry('age', 'value', -1)
	print(I.getValueByEntry('age', 'value'))
	I.save()
