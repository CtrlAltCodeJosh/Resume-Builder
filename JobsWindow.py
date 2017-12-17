from Constant import *
from WinMaster import ExtraWindowsMaster

class ExperienceWindow(ExtraWindowsMaster):
	def __init__(self, caller, *args, **kwargs):
		ExtraWindowsMaster.__init__(self, caller)