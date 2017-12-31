from Constant import *
from WinMaster import ExtraWindowsMaster
import tkinter.scrolledtext as tkst


class PersonalStatementWindow(ExtraWindowsMaster):	
	def __init__(self, caller, *args, **kwargs):
		#inherit from the master of extra windows
		ExtraWindowsMaster.__init__(self, caller)
		
		#set up variables and get data
		self.statementButtons = []
		#username, name, phone, email, link, statements, jobs, eds, skillCat = self.User.getUserDetails()
		userDetails=self.User.getUserDetails()
		
		#set variables in master of extra windows (set top frame)
		self.windowLabel.config(text = 'Add or edit your Personal Statements')
		self.middleFrame.config(text = 'Edit Statements')
		
		#populate the midframe
		self.populateMidFrame()

		#populate the bottom frame
		self.addStatemntButton = Button(self.bottomFrame, width=GBUTTONWIDTH, text = 'Add new personal\nstatement', command = self.editStatement)
		self.addStatemntButton.grid(row=0, column=0, padx=SMALLBPADDING, pady=SMALLBPADDING, sticky = W)
		
		
	def editStatement(self, statement=None):
		previous = None
		entryBox = tkst.ScrolledText(
										master = self.middleFrame,
										wrap= 'word', 
										width = 80, 
										height = 6)
		if statement != None:
			entryBox.insert('insert', statement)
			previous = statement
		entryBox.grid(row=999, column = 0)
		entrybuttonGo = Button(self.middleFrame, text='add Statement', command = lambda: self.updateStatements(entryBox.get(1.0,END),previous))
		entrybuttonGo.grid(row=999, column = 1)

	def updateStatements(self, statement=None, previousStatement=None):
		if statement == previousStatement:
			raise ValueError('statement may not be the same as previousStatement')
		elif previousStatement == None: #adding a novel statement
			#print ('adding statement %s' % statement)
			self.User.addStatement(statement)
			self.populateMidFrame()
		elif statement == None:			#just removing an old statment
			#print ('removing statment: %s' % previousStatement)
			self.User.removeStatement(previousStatement)
			self.populateMidFrame()
		else: 							#replacing a statement
			#print ('replacing %s with %s' % (previousStatement, statement))
			self.User.removeStatement(previousStatement)
			self.User.addStatement(statement)
			self.populateMidFrame()
		
	def populateMidFrame(self):
		#username, name, phone, email, link, statements, jobs, eds, skillCat = self.User.getUserDetails()
		userDetails=self.User.getUserDetails()
		for item in self.middleFrame.winfo_children():
			item.destroy()
		if userDetails['statements'] == []:
			self.middleFrame.config(text = 'No statements have been set')
		else:
			count = 0 
			for statement in userDetails['statements']:
				holder = Frame(self.middleFrame)
				holder.grid(row=count, column=0)
				statementButton = Button(holder, text = statement, wraplength=GMASTERWIDTH, command = lambda name=statement: self.editStatement(name))
				removeButton = Button(holder, text = 'delete', command = lambda name=statement: self.updateStatements(None, name))
				statementButton.grid(row=0, column=0, sticky=W)
				removeButton.grid(row=0, column=1, sticky=E)
				self.statementButtons.append(statementButton)
				count = count + 1
	
	def openWindow(self, User):
		self.caller.buttonsOff()
		self.master.deiconify()	
		self.User = User
		self.populateMidFrame()
				
				