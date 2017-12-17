from Constant import *
from WinMaster import ExtraWindowsMaster


class PersonalStatementWindow(ExtraWindowsMaster):	
	def __init__(self, caller, *args, **kwargs):
		#inherit from the master of extra windows
		ExtraWindowsMaster.__init__(self, caller)
		
		#set up variables and get data
		self.statementButtons = []
		username, name, phone, email, link, statements, jobs, eds, skillCat = self.User.getUserDetails()
		
		#set variables in master of extra windows (set top frame)
		self.windowLabel.config(text = 'Add or edit your Personal Statements')
		self.middleFrame.config(text = 'Edit Statements')
		
		#populate the midframe
		self.populateMidFrame(statements)

		#populate the bottom frame
		self.addStatemntButton = Button(self.bottomFrame, width=GBUTTONWIDTH, text = 'Add new personal\nstatement', command = self.addStatement)
		self.addStatemntButton.grid(row=0, column=0, padx=SMALLBPADDING, pady=SMALLBPADDING, sticky = W)
		
	def editStatement(self, statement):
		print ("finding and editing statment")
		
	def addStatement(self):
		
		print ('adding new personal statement')
		
	def populateMidFrame(self, statements):
		for item in self.middleFrame.winfo_children():
			item.destroy()
		if statements == []:
			self.middleFrame.config(text = 'No statements have been set')
		else:
			count = 0 
			for statement in statements:
				statementButton = Button(self.middleFrame, text = statement, command = lambda: editStatement(statement))
				statementButton.grid(row=count, column=0)
				self.statementButtons.append(statementButton)
				count = count + 1
				
				
				