class Program:
	def __init__(self):
		self.toSearch = {}
		self.variables = {}
	
	def addToken(self, tokToAdd, func, args):
		self.toSearch[tokToAdd] = (func,args)
	
	def addBuiltInVariable(self, varName, varValue):
		self.variables[varName] = varValue
	
	def interperate(self, text):
		tok = ""
		toS = self.toSearch
		variables = self.variables
		i = 0
		for char in text:
			tok += char
			if tok in toS:
				fnc,args = toS[tok]
				fnc(args)
				tok = ""
