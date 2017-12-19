from Constant import *
	
class ExtraWindowsMaster:	
	
	def __init__(self, caller):
		self.User = caller.User
		self.master = Toplevel()
		self.topFrame = Frame(self.master)#, width = GMASTERWIDTH/4, height=GMASTERHEIGHT/4)
		self.middleFrame = LabelFrame(self.master, text = '', width = GMASTERWIDTH, height=GMASTERHEIGHT)
		self.bottomFrame = Frame(self.master)#, width = GMASTERWIDTH/4, height=GMASTERHEIGHT/4)
		self.topFrame.pack(side='top', fill = 'both', expand = True)
		self.middleFrame.pack(side='top', fill = 'both', expand = True)
		self.bottomFrame.pack(side='top', fill = 'both', expand = True)
		self.returnButton = Button(self.bottomFrame, text = 'Main Window', command = self.closeAndUpdate)
		self.returnButton.grid(row = 0, column = 99)
		self.caller = caller
		self.master.withdraw()
		self.master.protocol("WM_DELETE_WINDOW", self.closeAndUpdate)
		self.windowLabel = Label(self.topFrame, text = '')
		self.windowLabel.grid(row=0, column=0, padx=SMALLBPADDING, pady=SMALLBPADDING, sticky=NSEW)
		
	def openWindow(self, User):
		self.caller.buttonsOff()
		self.master.deiconify()	
		self.User = User
		
	def closeAndUpdate(self):
		self.caller.buttonsOn()
		self.caller.controller.updateUser(self.User)
		self.caller.updateFrame(self.User)
		self.master.withdraw()

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------				
		