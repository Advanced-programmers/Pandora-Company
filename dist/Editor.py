#coding=utf-8

import os

import sys_bio
import lib_cloud
import lib_standardFileFormat
import lib_bte

class Editors:
	'''
	1. Show stories.
	2. Waiting for input.
	function-loop handles user input.
	TODO achieve command in function-loop.
	There are 4 MODE:
		story: A independent file.
			new: New a story.
			del: Delete a story.
			open: Open a story & turn into MODE-map & show maps.
			exit: Exit program.
		map: A independent map.
			new: New a map.
			del: Delete a map.
			open: Open a map  & show content.
			close: Exit a map & turn into MODE-story & show stories list.
			show: Show logic overview & customTags.
			prev: Show previous branches and offer to choose one & open it.
			next: Show next branches and offer to choose one & open it.
			setTag: Set custom tags to make story line clear.
			delTag: Delete a tag from a map.
			editText: turn into text editor.
			editCMD: turn into command editor.
		text editor:
			init: Initialize text part.
			add: Add a line in certain place.
			overWrite: overWrite a certain line.
			del: Delete a certain line.
			close: Exit & turn into MODE-map.
		command editor(based on text editor):
			init: Initialize command part.
			add: Add a command in certain place.
			overWrite: overWrite a certain command.
			del: Delete a certain command.
			close: Exit & turn into MODE-map.
	'''
	isRunning = True
	storyDir = 'story\\'
	currentStoryDir = ''
	currentStoryName = ''
	currentMapName = ''
	initMap = 'init.map'

	folderLoader = sys_bio.BIOFolderLoader()
	mapCloud = lib_cloud.mapCloud()
	textEditor = lib_bte.BTextEditor()

	# map专有属性
	currentIndex = []
	currentValue = []
	lastMap = []
	nextMap = []
	currentStatus = 'story'
	def __init__(self):
		os.system('title Crazy_Engine_Editor(ADV)[Beta]')

	# Public function
	def run(self):
		self.showStories()
		while self.isRunning:
			cmd = input('>')
			os.system('cls')
			self.loop(cmd)

	# Private core function
	def loop(self, cmd):
		if self.currentStatus == 'story':
			self.showStories()
			cmd = cmd.split(' ')
			if cmd[0] == 'new':
				pass
			elif cmd[0] == 'open':
				self.currentStatus = 'map'
				self.openStory(cmd[1])
		elif self.currentStatus == 'map':
			self.showMaps()
			cmd = cmd.split(' ')
			if cmd[0] == 'new':
				self.newMap(cmd[1])
			elif cmd[0] == 'open':
				self.openMap(cmd[1])
		elif self.currentStatus == 'line':
			cmd = cmd.split(' ')
			if cmd[0] == 'new':
				self.newLine(cmd[1])
			elif cmd[0] == 'open':
				self.openLine(cmd[1])
		elif self.currentStatus == 'text':
			pass

	# Private function
	def analyzeMap(self):
		pass
	def showStories(self):
		self.folderLoader.load(self.storyDir)
		textList = self.numberList(self.folderLoader.getEveryContentFolder())
		for line in textList:
			print(line)
	def showMaps(self):
		list = []
		for each in self.mapCloud.cloud:
			list.append(each.fileName.split('.')[0] + '\t->\t' + str(each.tag))
		textList = self.numberList(list)
		for each in textList:
			print(each)
	def showLine(self):
		pass
		self.currentMapName
	def newStory(self, storyName):
		pass
	def newMap(self, mapName):
		pass
	def newLine(self, mapName):
		pass
	def openStory(self, storyNumber):
		self.currentStoryName = self.getUnitNameByNumber(self.folderLoader.getEveryContentFolder(), storyNumber)
		self.currentStoryDir = self.storyDir + self.currentStoryName + '\\'
		self.mapCloud.setCloudDir(self.currentStoryDir)
		self.mapCloud.setInitMap(self.initMap)
		self.mapCloud.generate()
		self.showMaps()
	def openMap(self, mapNumber):
		list = []
		for each in self.mapCloud.cloud:
			list.append(each.fileName)
		self.currentMapName = self.getUnitNameByNumber(list, mapNumber)
		self.textEditor.load(self.currentStoryDir + self.currentMapName)
		self.textEditor.run()
	def openLine(self, mapName):
		pass
	#四级函数
	def numberList(self, list):
		currentNumber = 1
		textList = []
		for each in list:
			textList.append(str(currentNumber) + ':\t' + each)
			currentNumber += 1
		return textList
	def getUnitNameByNumber(self, list, numberAsString):
		currentNumber = 1
		if numberAsString.isdigit():
			for each in list:
				if str(currentNumber) == numberAsString:
					return each
				currentNumber += 1
			print('[WARN]... I have nothing to say...')
		else:
			print('[WARN]Function only recive story number as string!')
if __name__ == '__main__':
	I = Editor()
	I.run()
