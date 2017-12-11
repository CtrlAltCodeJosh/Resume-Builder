from Constant import *


class MasterWindow(Tk):
	'''Although this window is never seen, it is the master window behind
		all the other windows'''
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs) #initialize TKinter
		self.container = Frame(self) #make a container for all windows
		self.container.pack(side='top', fill = 'both', expand = True) #pack the windows into the frame as needed
		self.title("Resume Builder")#, font = VERDANA12)
		
		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)
		self.frames = {} # a library for all the frames
		self.User = UserClasses.User()
		
		#for each window, create it and place it in the frames
		for window in (LoginWindow, NewUserWindow, ReturningUserWindow, DataLoadingWindow): 
			frame = window(self.container, self, self.User) 
			self.frames[window] = frame
			frame.grid(row=0, column=0, sticky='nsew')
		self.show_frame(LoginWindow)
		
	def show_frame(self, controller):
		''' Switches frames for different UI'''
		frame = self.frames[controller]
		frame.updateFrame(self.User)
		frame.tkraise()

	def storeDataAndExit(self, User):
		'''stores data into the database and then exits the program, should be linked
		to all closing activities'''
		try:
			self.User = User
			self.storeUserInFile()
			Tk.destroy(self)
		except ValueError as e:
			print(e)
			print('need to question user about really doing this in store Data and exit functtion if userName is not given')
			Tk.destroy(self)
			
	def retriveUserFromFile(self, UserName):
		'''retrives the data from a given user file, attaches Postfix itself functions need not attach this'''
		if UserName != '':
			fileName = UserName + POSTFIX
			UserFile = open(fileName, 'rb')
			self.User = pickle.load(UserFile)
			UserFile.close()
			return self.User
		else:
			print ('retrive user from file raised an error')
			raise ValueError('UserName may not be blank')
	
	def storeUserInFile(self):
		'''stores the user in the file,  should be done periodically incase of errors in program'''
		fileName = self.User.getUserName()
		if fileName != '':
			fileName = fileName + POSTFIX
			UserFile = open(fileName, 'wb')
			pickle.dump(self.User, UserFile)
			UserFile.close()
		else:
			raise ValueError('filename is not given')
			
	def validateUserName(self, UserName):
		'''validates the username only'''
		fileName = UserName + POSTFIX
		if not os.path.exists(fileName) or UserName == '\n' or UserName == '':
			return False
		else:
			return True
		
	def updateUser(self, User, account=None):
		'''updates the User for all the windows'''
		self.User = User

			
	def getUser(self):
		'''returns the user to all the windows'''
		return self.User
		
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------			


class LoginWindow(Frame):
	''' This Window contains three buttons for the user to select
	if they are returning, or new.  It also allows them to exit'''
	def __init__(self, parent, controller, User):
		Frame.__init__(self, parent)
		box = Frame(self)
		box.pack()
		returningUser = Button(box, text = 'Returning User', font = VERDANA12,
							   command = lambda: controller.show_frame(ReturningUserWindow))
		returningUser.config(height = GBUTTONHEIGHT, width = GBUTTONWIDTH)
		newUser = Button(box, text = 'New User', font = VERDANA12, 
						 command = lambda: controller.show_frame(NewUserWindow))
		newUser.config(height = GBUTTONHEIGHT, width = GBUTTONWIDTH)
		exit = Button(box, text = 'Save all and Exit', font = VERDANA12,
					  command = lambda: controller.storeDataAndExit(User))
		exit.config(height = GBUTTONHEIGHT, width = GBUTTONWIDTH)
		returningUser.grid(row=0, pady = BPADDING, padx = BPADDING)
		newUser.grid(row=2, pady = BPADDING, padx = BPADDING)
		exit.grid(row=4, pady = BPADDING, padx = BPADDING)
		
	def updateFrame(self, User):
		'''not needed as there are no fields to update, however is 
		required to be here for other windows that do'''
		None
		

		
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------	
		
class NewUserWindow(Frame):
	'''This window allows a new user to input their
	base information befor moving on to input more 
	advanced information.  It is used by both new user
	and edit account'''
	def __init__(self, parent, controller, User):
		self.UserName = StringVar()
		self.name = StringVar()
		self.phone = StringVar()
		self.email = StringVar()
		self.LinkedIn = StringVar()
		Frame.__init__(self, parent)
		box = Frame(self)
		self.controller = controller
		self.instructionLabel = Label(self, font = VERDANA12)
		userNameLabel = Label(box, text = 'User Name:')
		self.userNameEntry = Entry(box, text = self.UserName, width = GBUTTONWIDTH)
		self.NameEntry = Entry(box, text = self.name, width = GBUTTONWIDTH)
		NameLabel = Label(box, text='Name:')
		userPhoneLabel = Label(box, text='Phone:')
		self.userPhoneEntry = Entry(box, text = self.phone, width = GBUTTONWIDTH)
		userEmailLabel = Label(box, text='Email:')
		self.userEmailEntry = Entry(box, text = self.email, width = GBUTTONWIDTH)
		userLinkLabel = Label(box, text='LinkedIn:')
		self.userLinkEntry = Entry(box, text = self.LinkedIn, width = GBUTTONWIDTH)
		go = Button(box, text = 'GO!', command=self.packUpUser)
		back = Button(box, text = 'Back', command = lambda: controller.show_frame(LoginWindow))
		self.instructionLabel.pack()
		box.pack()
		userNameLabel.grid(row=0, column=0)
		self.userNameEntry.grid(row=0, column=1)
		NameLabel.grid(row=1, column=0)
		self.NameEntry.grid(row=1, column=1)
		userPhoneLabel.grid(row=2, column=0)
		self.userPhoneEntry.grid(row=2, column=1)
		userEmailLabel.grid(row=3, column=0)
		self.userEmailEntry.grid(row=3, column=1)
		userLinkLabel.grid(row=4, column=0)
		self.userLinkEntry.grid(row=4, column=1)
		go.grid(row=5, column=0)
		back.grid(row=5, column=1)

	def updateFrame(self, User):
		'''updates the frame before opening the window'''
		self.User = User
		username, name, phone, email, link, statements, jobs, eds, skillCat = self.User.getUserDetails()
		self.UserName = username
		self.name = name
		self.phone = phone
		self.email = email
		self.LinkedIn = link
			
	def packUpUser(self):
		'''packs up the user data into a user object and calls the 
		data loading window where they can insert more information'''
		#should also ensure User does not already exist
		userName = self.userNameEntry.get() 
		name = self.NameEntry.get()
		phone = self.userPhoneEntry.get()
		email = self.userEmailEntry.get()
		linkedin = self.userLinkEntry.get()
		print (userName, name, phone, email, linkedin)
		self.User.setUserDetails(userName, name, phone, email, linkedin)
		self.controller.updateUser(self.User)
		self.controller.show_frame(DataLoadingWindow)


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------			

		
class ReturningUserWindow(Frame):
	'''This window allows the returning user to retrieve their 
	data by entering their username'''
	def __init__(self, parent, controller, User):
		Frame.__init__(self, parent)
		self.fileName = StringVar()
		self.controller = controller
		self.User = User
		requestLabel = Label(self, text = 'Please enter your user Name:')
		UserNameEntry = Entry(self, textvariable = self.fileName)
		#UserNameEntry.bind('<Return>', lambda: self.validateUser)
		goButton = Button(self, text = 'GO', font = VERDANA12, command = self.validateUser)
		loginReturnButton = Button(self, text = 'Back', font = VERDANA12,	
					command = lambda: controller.show_frame(LoginWindow))	
		self.dataValidationLabel = Label(self, text = '')
		requestLabel.grid(row=0)
		UserNameEntry.grid(row=1, column = 0)
		goButton.grid(row=1, column=1)
		loginReturnButton.grid(row=2)
		self.dataValidationLabel.grid(row=3)
		self.dataValidationLabel.grid_remove()		
	
	def validateUser(self):
		'''Checks to see if the user has an account already
		if they do, populates it and returns the User'''
		UserName=self.fileName.get()
		#try:
		if self.controller.validateUserName(UserName):
			self.User = self.controller.retriveUserFromFile(UserName)
			self.controller.show_frame(DataLoadingWindow)
		else:
			self.dataValidationLabel.config(text = 'Returning User\n User not found', fg = 'red', font = VERDANA12)
			self.dataValidationLabel.grid()
		#except ValueError as e:
			
		
	def updateFrame(self, User):
		'''not needed as there are no fields to update, however is 
		required to be here for other windows that do'''
		None
			
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------		
		
class DataLoadingWindow(Frame):
	'''Allows the user access windows that will populate more advanced
	User data, already contains basic user info from either new user
	or from returning user window'''
	def __init__(self, parent, controller, User):
		self.User = User
		self.name = StringVar()
		self.phone = StringVar()
		self.linkedin = StringVar()
		self.email = StringVar()
		Frame.__init__(self, parent)
		box = Frame(self)
		titleBox = Frame(box)
		titleBox.grid(row=0, column=0)
		buttonBox = LabelFrame(box, text='add or modify your general resume information', pady = 15)
		buttonBox.grid(row=1, column=0)
		acctNExitBox = Frame(box)
		acctNExitBox.grid(row=2, column=0)
		box.pack()
		accountButton = Button(acctNExitBox, text = 'Account', 
						command = lambda: controller.show_frame(NewUserWindow))
		accountButton.grid(row=0, column=0, sticky='sw', pady=25)
		saveAndExitButton = Button(acctNExitBox, text = 'Save and Exit', command = lambda: controller.storeDataAndExit(self.User))
		saveAndExitButton.grid(row=0, column=1)

		self.personalLabel = Label(titleBox, font = VERDANA12, pady = 15)
		self.personalInfoLabel = Label(titleBox)
		self.personalLabel.grid(row=0, column=0)
		self.personalInfoLabel.grid(row=1, column=0, padx=15, pady=15)
		
		#these will be whole other windows and will pass around the user objects
		#self.skillsWindow = skillsWindow()
		#self.perstateWindow = perstateWindow()
		#self.edwindow = educationWindow()
		#self.jobWindow = experienceWindow()
		
		self.skillsButton = Button(buttonBox, text='Skills')
		self.jobButton = Button(buttonBox, text='Experience')
		self.educationButton = Button(buttonBox, text='Education')
		self.statementButton = Button(buttonBox, text='Personal Statements')
		self.jobButton.grid(row=0, column=0, padx=5, pady=5)
		self.skillsButton.grid(row=0, column=1, padx=5, pady=5)
		self.educationButton.grid(row=1, column=0, padx=5, pady=5)
		self.statementButton.grid(row=1, column=1, padx=5, pady=5)
		
	def updateFrame(self, User):
		'''updates all updateable fields of the frame when called'''
		self.User = User
		username, name, phone, email, link, statements, jobs, eds, skillCat = self.User.getUserDetails()
		self.personalLabel.config(text = 'Welcome %s!' % name)
		self.personalInfoLabel.config(text = 'email: %s\tLinkedIn: %s\tPhone: %s' % (email, link, phone))
		

if __name__ == '__main__':
	
	app = MasterWindow()
	app.mainloop()


