from Constant import *
from WinMaster import ExtraWindowsMaster


class SkillsWindow(ExtraWindowsMaster):		
	def __init__(self, caller, *args, **kwargs):
		#inherit from the master of extra windows
		ExtraWindowsMaster.__init__(self, caller)
		
		#set up variables and get data
		self.statementButtons = []
		#username, name, phone, email, link, statements, jobs, eds, skillCat = 
		userDetails=self.User.getUserDetails()
		
		#set variables in master of extra windows (set top frame)
		self.windowLabel.config(text = 'Add or edit your Skills')
		self.middleFrame.config(text = 'Edit Skills')
		
		#populate the midframe
		self.populateMidFrame()

		#populate the bottom frame
		self.addSkillsButton = Button(
									self.bottomFrame, 
									width=GBUTTONWIDTH, 
									text = 'Add new skill\ncatagory', 
									command = lambda: self.makeNewSkillCat()
									)
		self.addSkillsButton.grid(row=0, column=0, padx=SMALLBPADDING, pady=SMALLBPADDING, sticky = W)
	
	def makeNewSkillCat(self):
		'''This function allows the user to create a new skill catagory for the user
		no parameters are taken as it is prompting the user for the information'''
		def buttonEvent(catagory):
			'''adds the new catagory and refreshes the frame to the new user info'''
			self.User.addNewSkillCatagory(catagory)
			self.populateMidFrame()
		
		lastBox = Frame(self.middleFrame)
		topLabel = Label(lastBox, text = 'Create skill catagory:')
		bottomLabel = Label(lastBox, text = '')
		catEntry = Entry(lastBox, text= '', width=GBUTTONWIDTH*2)
		goButton = Button(lastBox, text = 'Create', command = lambda: buttonEvent(catEntry.get()))
		clearButton = Button(lastBox, text='I changed my mind', command = self.changedMind)
		topLabel.config(text = 'Create skill catagory:')
		topLabel.grid(row=0, column=0)
		catEntry.grid(row=0, column=1)
		goButton.grid(row=2, column=0)
		clearButton.grid(row=2, column=1)
		catString = catEntry.get()
		lastBox.grid(row=999, column=0)
		
	def addSkillToExistingCat(self, cat):
		'''This function allows the user to add a skill to an existing catagory'''
		def buttonEvent(skill, months):
			'''The acutal updating of the user'''
			self.User.addSkill(cat, skill, months)
			self.populateMidFrame()
		lastBox = Frame(self.middleFrame)
		topLabel = Label(lastBox, text = "add skill to the '%s' catagory:" % cat)
		bottomLabel = Label(lastBox, text = 'how many months of this skill?:')
		skillEntry = Entry(lastBox, text= '', width=GBUTTONWIDTH*2)
		monthEntry = Entry(lastBox, text = '', width=GBUTTONWIDTH*2)
		goButton = Button(lastBox, text = 'Add Skill', command = lambda: buttonEvent(skillEntry.get(), monthEntry.get()))
		changedMind = Button(lastBox, text = 'I changed my mind', command = self.changedMind)
		topLabel.grid(row=0, column=0)
		skillEntry.grid(row=0, column=1)
		bottomLabel.grid(row=1, column=0)
		monthEntry.grid(row=1, column=1)
		goButton.grid(row=0, column=2)
		lastBox.grid(row=999, column=0)
		
	def editSkillInCat(self, cat, skill, months):
		def GoButtonEvent(thisSkill, time):
			self.User.removeSkill(cat, skill)
			self.User.addSkill(cat, thisSkill, time)
			self.populateMidFrame()
		def deleteButtonEvent():
			self.User.removeSkill(cat, skill)
			self.populateMidFrame()
			
		lastBox = Frame(self.middleFrame)
		veryTopLabel = Label(lastBox, text = 'editing skill from catagory %s' % cat)
		topLabel = Label(lastBox, text = 'Skill Name:')
		bottomLabel = Label(lastBox, text='Months of skill:')
		skillEntry = Entry(lastBox, width=GBUTTONWIDTH*2)
		monthEntry = Entry(lastBox, width=GBUTTONWIDTH*2)
		goButton = Button(lastBox, text = 'Change', command = lambda: GoButtonEvent(skillEntry.get(), monthEntry.get()))
		deleteButton = Button(lastBox, text = 'Remove', command = deleteButtonEvent)
		changedMind = Button(lastBox, text = 'I changed my mind', command = self.changedMind)
		skillEntry.insert(0, str(skill))
		monthEntry.insert(0, str(months))
		veryTopLabel.grid(row=0, columnspan=2)
		topLabel.grid(row=1, column=0)
		bottomLabel.grid(row=2, column=0)
		skillEntry.grid(row=1, column=1)
		monthEntry.grid(row=2, column=1)
		goButton.grid(row=1, column=2)
		deleteButton.grid(row=2, column=2)
		changedMind.grid(row=3, columnspan=2)
		lastBox.grid(row=999, column=0)
					

	def populateMidFrame(self):
		'''Mid Frame is the frame in the middle of this window that holds the actual user details'''
		#username, name, phone, email, link, statements, jobs, eds, skillCat = 
		userDetails = self.User.getUserDetails()
		for item in self.middleFrame.winfo_children():
			item.destroy()
		if userDetails['skillSets'] == {}:
			self.middleFrame.config(text = 'No skills have been set')
		else:
			self.middleFrame.config(text = 'Add or edit your skills here')
			count = 0 
			self.sectionFrames = {}
			for catagory in userDetails['skillSets']:
				sectionHolder = Frame(self.middleFrame)
				catagoryHolder = Frame(sectionHolder)
				skillsHolder = Frame(sectionHolder)
				catagoryButton = Button(catagoryHolder, text=catagory, command=lambda name=catagory: self.renameCatagory(name))
				deleteCatButton = Button(catagoryHolder, text='delete', command=lambda name=catagory: self.deleteCat(name))
				addSkillButton = Button (catagoryHolder, text='add skill', command=lambda name=catagory: self.addSkillToExistingCat(name))
				sectionHolder.grid(row=count, column=0)
				catagoryHolder.grid(row=0, column=0)
				skillsHolder.grid(row=1, column=0)
				catagoryButton.grid(row=0, column=0)
				deleteCatButton.grid(row=0, column=2)
				addSkillButton.grid(row=0, column=1)
				buttonHolder = {}
				self.sectionFrames[catagory] =(count, {})
				skillCount = 0
				for skillGroup in userDetails['skillSets'][catagory]:
					skill = skillGroup[0]
					years = skillGroup[1]
					skillsButton = Button(skillsHolder, 
										text='skill: %s\nyears: %s' % (skill, years), 
										command = lambda 
											cat=catagory,
											name=skill, 
											year = years: 
											self.editSkillInCat(cat, name, year)
										  )
					skillsButton.grid(row=0, column=skillCount)
					skillCount = skillCount + 1
					self.sectionFrames[catagory][1][skill] = skillsButton
				count = count + 2
				
	def renameCatagory(self, name):
		frameHolder = Frame(self.middleFrame)
		renameLabel = Label(frameHolder, text = 'Catagory:')
		newCatEntry = Entry(frameHolder, text = name, width=GBUTTONWIDTH*2)
	
		def updateUser(oldName, newName):
			print('updating user')
			self.User.renameSkillCatagory(oldName, newName)
			self.populateMidFrame()
		changedMindButton = Button(frameHolder, text='I changed my mind', command=self.changedMind)
		goButton = Button(frameHolder, text = 'Save', command = lambda: updateUser(name, newCatEntry.get()))
		renameLabel.grid(row=0, column=0)
		newCatEntry.grid(row=0, column=1)
		goButton.grid(row=0, column=2)
		changedMindButton.grid(row=1, columnspan=2)
		frameHolder.grid(row=25, column=0)
		
	def changedMind(self):
		self.populateMidFrame()	
	
	def deleteCat(self, catagory):
		self.User.removeSkillCatagory(catagory)
		self.populateMidFrame()
	
	def addSkill(self, name):
		frameHolder = Frame(self.middleFrame)
		renameLabel = Label(frameHolder, text = 'Add Skill:')
		newCatEntry = Entry(frameHolder, text = name, width=GBUTTONWIDTH*2)
	
		def updateUser(oldName, newName):
			print('updating user')
			self.User.renameSkillCatagory(oldName, newName)
			self.populateMidFrame()
			
		goButton = Button(frameHolder, text = 'Save', command = lambda: updateUser(name, newCatEntry.get()))
		renameLabel.grid(row=0, column=0)
		newCatEntry.grid(row=0, column=1)
		goButton.grid(row=0, column=2)
		frameHolder.grid(row=25, column=0)
	
	
	def openWindow(self, User):
		self.caller.buttonsOff()
		self.master.deiconify()	
		self.User = User
		self.populateMidFrame()		