#coding=utf-8

import os
import time

import sys_bios
import lib_standardDataFormat

class Game:

	storyPath = 'story\\'

	currentStory = ''
	currentMap = ''
	currentUser = ''
	tmpBuffer = []

	cmd = lib_standardDataFormat.cmdLoader()
	info = lib_standardDataFormat.infoLoader()

	#Public function
	def __init__(self):
		os.system('cls')
		os.system('title Pandora_Company[Beta]')
		self.checkSelf()
		self.readSave()

	def run(self):
		self.isRunning = True
		self.enterStory('main')
		while self.isRunning:
			self.readin = input(self.currentUser + '>')
			cmd = self.readin.split(' ')
			if cmd[0] == '':
				pass
			elif self.cmd.isExist([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.currentUser + '\\bin', cmd[0]]):
				self.cmd.load([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.currentUser + '\\bin', cmd[0]])
				for each in self.cmd.content[2]:
					self.doCMD(each)
			else:
				print('No cammand called \'' + cmd[0] + '\', please type \'help\' to view aviliable commands.')


	#Private function
	def checkSelf(self):
		pass

	def readSave(self):
		pass

	def enterStory(self, storyName):
		self.currentStory = storyName
		self.cmd.load([self.storyPath + self.currentStory, 'storyCMD.cmd'])
		for each in self.cmd.content[2]:
			self.doCMD(each)

	def enterMap(self, mapName):
		self.currentMap = mapName
		self.cmd.load([self.storyPath + self.currentStory + '\\' + self.currentMap, 'mapCMD.cmd'])
		for each in self.cmd.content[2]:
			self.doCMD(each)

	def enterUser(self, userName):
		self.currentUser = userName
		self.cmd.load([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.currentUser, 'userCMD.cmd'])
		for each in self.cmd.content[2]:
			self.doCMD(each)

	def doCMD(self, line):
		cmd = line.split(' ')
		if cmd[0] == '':
			pass
		elif cmd[0] == '#':
			pass
		elif cmd[0] == 'echo':
			print(line[5:])
		elif cmd[0] == 'help':
			tmp = sys_bios.BIOS().getVFolder([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.currentUser + '\\bin', ''])
			for each in tmp[3]:
				info = self.getHelpInfo(each)
				print(each[1] + ' - ' + info)
		elif cmd[0] == 'ls':
			tmp = sys_bios.BIOS().getVFolder([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.currentUser + '\\storage', ''])
			for each in tmp[3]:
				print(each[1])
		elif cmd[0] == 'cat':
			if self.cmd.isExist([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.currentUser + '\\storage', self.readin[4:]]):
				self.info.load([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.currentUser + '\\storage', self.readin[4:]])
				for each in self.info.content[2]:
					print(each)
			else:
				print('The file you find is not exist.')
		elif cmd[0] == 'ssh':
			if self.cmd.isExist([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.readin[4:], 'password']):
				self.info.load([self.storyPath + self.currentStory + '\\' + self.currentMap + '\\' + self.readin[4:], 'password'])
				tmp = input('Password:')
				if self.info.content[2][0] == tmp:
					self.enterUser(self.readin[4:])
				else:
					print('Wrong password.')
			else:
				self.enterUser(self.readin[4:])
		elif cmd[0] == 'setmap':
			self.enterMap(cmd[1])
		elif cmd[0] == 'setuser':
			self.enterUser(cmd[1])
		elif cmd[0] == 'login':
			tmp = input('Password:')
			if tmp == cmd[1]:
				self.currentUser = cmd[2]
			else:
				print('Wrong password.')
		else:
			print('[WARN][Game-doCMD]No cammand called \'' + cmd[0] + '\'.')

	def getHelpInfo(self, vFile):
		helpInfo = ''
		for each in vFile[2]:
			cmd = each.split(' ')
			if cmd[0] == '#':
				helpInfo = each[2:]
		return helpInfo

	def addBuffer(self, newBuffer):
		self.tmpBuffer.append(newBuffer)

	def cleanBuffer(self):
		self.tmpBuffer = []

if __name__ == '__main__':
	I = Game()
	I.run()
