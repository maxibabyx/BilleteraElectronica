from BilleteraElectronica import BilleteraElectronica
import unittest

class BilleteraTest(unittest.TestCase):
	
	def setUp(self):		
		identificador = "03023424"
		nombre = "Gabriel"
		apellido = "Gimenez"
		ci = "V24313661"
		pin = "1343"
		self.me = BilleteraElectronica(identificador, nombre, apellido, ci, pin)
	
	def tearDown(self):
		self.me = None
	
	def testRecargar(self):
		self.me.recargar(50,31)
		self.assertEqual(self.me.saldo(), 50)
	
	def testRecargar1(self):
		self.me.recargar(0, -1)
		self.assertEqual(self.me.saldo(), 0)
	
	def testConsumir(self):
		with self.assertRaises(ValueError) as cm:
			self.me.consumir(-1, 31, 1343)
		self.assertEqual(cm.exception.args[0], 0)
		
	
if __name__ == "__main__":
	unittest.main()
		
