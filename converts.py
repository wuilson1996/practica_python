
class Convert:

	def __init__(self, num):

		self.num = num


	def binary(self):
		coci = self.num
		fact = 1
		print(fact)
		while coci != 0:
			
			rest = coci % 2
			coci = coci // 2
			print(rest, coci)

			if coci != 0:
				fact = fact*10

				if rest == 1:
					#rest = rest*10
					fact = fact+rest

				else:
					


		print(fact)

		return fact
			


	def hexa(self):
		pass

	def octal(self):
		pass

	def Deci(self):
		pass


convert = Convert(6)
num = convert.binary()
print(num)