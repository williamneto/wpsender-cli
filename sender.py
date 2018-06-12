# ENVIANDO MENSAGENS PARA MULTIPLOS NUMEROS
# 
# Importante consultar o arquivo README.md

# -*- coding: utf-8 -*-
import csv
import subprocess
import time
import random
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class YSender(object):
	def __init__(self):
		# variaveis usadas na definiçao do intervalo entre mensagens
		self.starttime=time.time()
		self.timers = [1,3,2,4,7,5,6,9]

		# numero que vai enviar as mensagens 
		self.nfrom = "##########"
		# ao registrar o numero com o yowsup vc pega uma senha
		self.pwd = "Ixhn0YDeTIltd7TiFs6gTP2TRPg="

		# irao guardar os numeros retirados do arquivos, e
		# quais envios tiveram sucesso e quais falharam
		self.numeros = []
		self.fails = []
		self.success = []

	# funçao para pegar os numeros do arquivo CSV	
	def getNumbers(self):
		numeros = []		
		with open('n.csv') as csvfile:
			csvreader = csv.reader(csvfile)

			for row in csvreader:
				numeros = [x for x in row if x]

		self.numeros = numeros		
		return numeros

	def getMessage(self):	
		mensagens = []
		with open('m.csv') as csvfile:
			csvreader = csv.reader(csvfile)

			for row in csvreader:
				mensagens = [x for x in row if x]

		return random.choice(mensagens)

	# mostra o relatorio de quantos envios foram bem 
	# sucedidos e quantos falharam	
	def report(self):
		if len(self.success) > 0:
			print("\n A mensagem foi entregue a %d numeros >" % len(self.success))

		if len(self.fails) > 0:
			print("\n A mensagem nao foi entregue a %d numeros >" % len(self.fails))
			for f in fails:
				print("-- %s" % f)					
	
	# envia as mensagens	
	def send(self):	
		i = 0
		print("------------------------------------------------------\n>>>>Iniciando envio para %d numeros" % len(self.numeros))
		for n in self.getNumbers():
			if not n == "-":
				i += 1
				
				print("\n -------------------------------------------") 
				print(str(i) + ") Enviando para " + n)

				l = "%s:%s" % (self.nfrom, self.pwd)
				
				# aqui e onde o envio acontece, executando um comando da 
				# CLI do Yowsup
				cmd = "yowsup-cli demos -l %s -s %s '%s'" % (l, n, self.getMessage())
				r = subprocess.call(cmd, shell=True)
				
				# verifica se o envio foi bem sucedido e registra
				if r != 0:
					self.fails.append(n) 
					print("O envio para %s falhou" % n)
				else:
					self.success.append(n)
					print("Enviado com sucesso para %s" % n) 	

				print("----------------------------------------------") 

				# define um intervalo de espera aleatorio
				v  = random.choice(self.timers)
				time.sleep(v - ((time.time() - self.starttime) % v))

		# mostra o relatorio		
		self.report()	

y = YSender()
y.send()			

		

						