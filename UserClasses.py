class School:

	def __init__(self):
		self.school = ''
		self.gpa = ''
		self.dates = []
		self.coursework = []
		
	def setDates(self, startDate, endDate):
		self.dates = [startDate, endDate]
		return True
	
	def setSchool(self, schoolname, gpa=None, dates=None, classes=None):
		self.school = schoolname
		if dates != None:
			self.setDates(dates[0], dates[1])
		if gpa != None:
			self.gpa = gpa
		if classes != None:
			if isinstance(classes, str):
				self.addCoursework(classes)
			if isinstance(classes, list):
				for eachClass in classes:
					self.addCoursework(eachClass)
		return True

	
	def addCoursework(self, aClass):
		self.coursework.append(aClass)
		return True
		
	def removeCourseWork(self, aClasses):
		if isinstance(aClasses,str):
			self.coursework.remove(aClasses)
		if isinstance(aClasses, list):
			for classes in aClasses:
				self.coursework.remove(classes)
		return True
		
	def getSchool(self):
		return self.school, self.gpa, self.dates, self.coursework
	

class Job:
	
	def __init__(self):
		self.number = 0
		self.title = ''
		self.company = ''
		self.dates = [] 
		self.acomplishments = []
		
	def setDates(self, startDate, endDate):
		self.dates = [startDate, endDate]
		return True
		
	def setBasicJobDetails(self, title, company):
		self.title = title
		self.company = company
		return True
	
	def setAllJobDetails(self, title, company, dates, acmps=None):
		self.setBasicJobDetails(title, company)
		self.setDates(dates[0], dates[1])
		if acmps == None:
			None
		elif isinstance(acmps, str):
			self.addAcomplishment(acmps)
		elif isinstance(acmps, list):
			self.addAcomplishments(acmps)
		else:
			raise ValueError
		return True
		
	def addAcomplishment(self, acomplishment):
		self.acomplishments.append(acomplishment)
		return True
		
	def removeAcomplishment(self, acomplishment):
		if acomplishment in self.acomplishments:
			self.acomplishments.remove(acomplishment)
			return True
		return False
	
	def addAcomplishments(self, acmps):
		self.acomplishments.extend(acmps)
		return True
		
	def getJobDetails(self):
		return self.title, self.company, self.dates, self.acomplishments

		
		
class User:
	
	def __init__(self):
		self.userName = ''
		self.name = ''
		self.phone = ''
		self.email = ''
		self.linkedin = ''
		self.statements = []
		self.jobs = []
		self.education = []
		self.skillCatagories = {}
		
	def setUserName(self, name):
		if isinstance(name, str):
			self.userName = name
			return True
		raise TypeError
	
	def getUserName(self):
		return self.userName
		
	def addNewSkillCatagory(self, catagory):
		catagory = catagory.lower()
		catagory = catagory[0].upper() + catagory[1:]
		if catagory in self.skillCatagories:
			raise ValueError('catagory already exists')
		else:
			self.skillCatagories[catagory] = []
	
	def renameSkillCatagory(self, oldCatName, newCatName):
		
		
		if oldCatName in self.skillCatagories:
			holder = self.skillCatagories[oldCatName]
			del self.skillCatagories[oldCatName]
			newCatName = newCatName.lower()
			newCatName = newCatName[0].upper() + newCatName[1:]
			self.skillCatagories[newCatName] = holder
		else:
			raise IndexError("skill catagory doesn't exist")
			

		
	
	def addSkill(self, catagory, skill, years):
		print ('catagory: %s' % catagory)
		print ('skill: %s' % skill)
		print ('years: %s' % years)
		catagory = catagory.lower()
		catagory = catagory[0].upper() + catagory[1:]
		if catagory in self.skillCatagories:
			self.skillCatagories[catagory].append((skill, years))
		else:
			self.skillCatagories[catagory] = [(skill, years)]
		return True
		
	def removeSkillCatagory(self, catagory):
		if catagory in self.skillCatagories:
			del self.skillCatagories[catagory]
		else:
			raise ValueError('catagory is not in catagory list')

	def removeSkill(self, catagory, skill):
		print('removing %s from catagory %s' % (skill, catagory))
		catagory = catagory.lower()
		catagory = catagory[0].upper() + catagory[1:]
		if catagory not in self.skillCatagories:
			return False
			print ("catagory doesn't exist")
		for eachSkill in self.skillCatagories[catagory]:
			print ('going through skills')
			print (eachSkill)
			if eachSkill[0] == skill:
				print (' fournd skill now removing')
				self.skillCatagories[catagory].remove(eachSkill)
				if self.skillCatagories[catagory] == []:
					self.removeSkillCatagory(catagory)
				return True
		return False
		
	def setUserDetails(self, userName, name, phone, email, linkedin):
		self.setUserName(userName)
		self.name = name
		self.phone = phone
		self.email = email
		self.linkedin = linkedin	
		return True
		
	def addStatement(self, purposeStatement):
		self.statements.append(purposeStatement)
		return True
		
	def removeStatement(self, purposeStatement):
		self.statements.remove(purposeStatement)
		return True
		
	def addJob(self, job, company=None, acmps=None):
		if isinstance(job, Job):
			self.jobs.append(job)
			return True
		elif isinstance(job, str):
			thisJob = Job()
			thisJob.setAllJobDetails(job, company, acmps)
			self.jobs.append(thisJob)
			return True
		else:
			raise ValueError
	
	def removeJob(self, title):
		for job in jobs:
			jobtitle, dummy, dummy2, dummy3 = job.getJobDetails()
			if jobtitle == title:
				jobs.remove(job)
				return True
		return False
		
	def removeJobAcomplishment(self, job, acomplishment):
		for ajob in self.jobs:
			jobtitle, dummy, dummy2, dummy3 = ajob.getJobDetails()
			if jobtitle == job:
				return ajob.removeAcomplishment(acomplishment)
		return False
		
	def addStatement(self, statement):
		self.statements.append(statement)
		return True
	
	def removeStatement(self, statement):
		self.statements.remove(statement)	
		return True
		
	def addSchool(self, school, gpa=None, dates=None, classes=None):
		if isinstance(school, School):
			self.education.append(school)
			return True
		if dates == None:
			dates=['','']
		if gpa == None:
			gpa = ''
		if classes == None:
			classes = []
		thisSchool = School()
		thisSchool.setSchool(school, gpa, dates, classes)
		self.education.append(thisSchool)
		return True
		
	def removeSchool(self, school):
		for eachSchool in self.education:
			name, dummy, dummy2, dummy3 = eachSchool.getSchool()
			if name == school:
				self.education.remove(eachSchool)
				return True
		return False
		
	def getUserDetails(self):
		userDetails={
					'username':self.userName, 
					'name':self.name, 
					'phone':self.phone,
					'email':self.email,
					'linkedIn':self.linkedin,
					'statements':self.statements,
					'jobs':self.jobs,
					'education':self.education,
					'skillSets':self.skillCatagories
					}
		return userDetails
		#self.userName, self.name, self.phone, self.email, self.linkedin, self.statements, self.jobs, self.education, self.skillCatagories
		
def ClassTest():
	print ('Class Tester!')
	print ('User Classes!')
	
	name = 'myName'
	phone = '555-555-5555'
	email = 'email1__@email.com'
	linked = 'linkedin\linked'
	statement1 = 'Move fast and break things'
	statement2 = 'I get fired a lot because I dont show up for work'
	
	jobName = 'company1'
	jobtitle = 'some guy'
	startDate = '1Nov15'
	endDate = '12Dec16'
	acomp1 = 'I didnt swallow any frogs'
	acomp2 = 'I only broke a few things'
	acomp3 = 'Im not cleaning this up'
	aJob = Job()
	aJob.setAllJobDetails(jobtitle, jobName, [startDate, endDate], statement1)
	print (aJob.removeAcomplishment(statement1))
	aJob.addAcomplishments([acomp1, acomp2, acomp3])
	
	jobName2 = 'company2'
	jobtitle2 = 'doing the same things'
	
	school1 = 'High school High'
	gpa = '5.0'
	schoolStart = '1Dec11'
	schoolEnd = '12Dec12'
	course1 = 'rockbreaking'
	course2 = 'not licking things'
	course3 = 'stareing blankly into space'
	
	school2 = 'crap College'
	gpa2 = '3.5'
	aschool = School()
	aschool.setSchool(school2, gpa2, [schoolStart, schoolEnd], [course1, course2, course3])
	
	aUser = User()
	aUser.setUserDetails(name, name, phone, email, linked)
	aUser.addStatement(statement1)
	aUser.addStatement(statement2)
	aUser.removeStatement(statement2)
	aUser.addJob(aJob)
	aUser.addJob(jobtitle2, jobName2, [acomp1, acomp2])
	aUser.removeJobAcomplishment(jobtitle2, acomp1)
	aUser.addSchool(school1, gpa, [schoolStart, schoolEnd], [course1,course2, course3])
	aUser.addSchool(aschool)
	aUser.removeSchool(school2)
	aUser.addSkill(course1, jobtitle2, '1 year')
	aUser.addSkill(course2, course3, '25 years')
	aUser.removeSkill(course1, jobtitle2)

	#need to fix this test (old  return protocol)
	#nameTest, phoneTest, emailTest, linkedTest, statementTest, jobsTest, educationTest, skillsTest = aUser.getUserDetails()
	print (nameTest)
	print (phoneTest)
	print (emailTest)
	print (linkedTest)
	print (statementTest)
	for ajob in jobsTest:
		details = ajob.getJobDetails()
		for detail in details:
			print (detail)
	for eachSchool in educationTest:
		item = eachSchool.getSchool()
		for each in item:
			print (each)
		
	print (skillsTest)
	


		
if __name__ == "__main__":
		ClassTest()
	
