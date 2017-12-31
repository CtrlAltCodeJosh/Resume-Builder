from Constant import *
from WinMaster import ExtraWindowsMaster

class EducationWindow(ExtraWindowsMaster):
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
		self.addEducationButton = Button(
									self.bottomFrame, 
									width=GBUTTONWIDTH, 
									text = 'Add new Education', 
									command = lambda: self.educationAddEdit()
									)
		self.addEducationButton.grid(row=0, column=0, padx=SMALLBPADDING, pady=SMALLBPADDING, sticky = W)
		
	def educationAddEdit(self, school=None):
		def newEd():
			schoolHolder = UserClasses.School()
			schoolHolder.setSchool(nameEntry.get(), gpaEntry.get(), [startedEntry.get(), finishedEntry.get()])#, courses)
			self.User.addSchool(schoolHolder)
			self.populateMidFrame()
		def editEd():
			self.User.removeSchool(school)
			newEd()
		def choice():
			if school!=None:
				editEd()
			else:
				newEd()
		
		
		lastSpotFrame = Frame(self.middleFrame)
		nameLabel = Label(lastSpotFrame, text = 'School Name: ')
		gpaLabel = Label(lastSpotFrame, text = 'GPA: ')
		startedLabel = Label(lastSpotFrame, text = 'Date Began: ')
		finishedLabel = Label(lastSpotFrame, text = 'Date Completed: ')
		saveButton = Button(lastSpotFrame, text = 'Save', command = choice)
		changedMind = Button(lastSpotFrame, text = 'I changed my mind', command = self.populateMidFrame)
		coursesFrame = LabelFrame(lastSpotFrame, text = 'Add or edit course work')
		addCourseButton = Button(coursesFrame, text = 'Add')
		nameEntry = Entry(lastSpotFrame)
		gpaEntry = Entry(lastSpotFrame)
		startedEntry = Entry(lastSpotFrame)
		finishedEntry = Entry(lastSpotFrame)
		lastSpotFrame.grid(row=999, column=0)
		nameLabel.grid(row=0, column=0)
		nameEntry.grid(row=0, column=1)
		gpaLabel.grid(row=1, column=0)
		gpaEntry.grid(row=1, column=1)
		startedLabel.grid(row=2, column=0)
		startedEntry.grid(row=2, column=1)
		finishedLabel.grid(row=3, column=0)
		finishedEntry.grid(row=3, column=1)
		saveButton.grid(row=0, column = 2)
		changedMind.grid(row=1, column=2)
		coursesFrame.grid(row=4, columnspan=2)
		addCourseButton.grid(row=0, column=999)
		
		
	def addNewEd(name, gpa, started, finished, courses):
		None
		
		
		
	def populateMidFrame(self):	
		'''Mid Frame is the frame in the middle of this window that holds the actual user details''' 
		userDetails = self.User.getUserDetails()
		for item in self.middleFrame.winfo_children():
			item.destroy()
		if userDetails['education'] == {}:
			self.middleFrame.config(text = 'No education has been added')
		else:
			self.middleFrame.config(text = 'Add to or edit your education here')
			count = 0 
			self.sectionFrames = {}
			for school in userDetails['education']:
				schoolInfo = school.getSchool()
				sectionHolder = Frame(self.middleFrame)
				edHolder = Frame(sectionHolder)
				edButton = Button(
								  edHolder, 
								  text='School Name: %s\nFrom: %s\tTo: %s' % (schoolInfo['schoolName'], schoolInfo['datesAttended'][0], schoolInfo['datesAttended'][1]), 
								  command = lambda 
											thisSchool=school: 
											self.educationAddEdit(thisSchool)
								 )
				sectionHolder.grid(row=count, column=0)
				edHolder.grid(row=0, column=0)
				edButton.grid(row=0, column=0)
				count = count + 2
		