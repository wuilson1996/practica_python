class Convert:

	def __init__(self, num):

		self.num = num


	def binary(self):
		coci = self.num
		Bin = []

		while coci != 0:
			
			rest = coci % 2
			coci = coci // 2
			
			Bin.append(rest)

		result = []
		for i in range(len(Bin)-1,-1,-1):
			result.append(Bin[i])

		return result
			


	def hexa(self):
		pass

	def octal(self):
		pass

	def Deci(self):
		pass

num = int(input("ingrese numero: "))
convert = Convert(num)
num = convert.binary()
print(num)