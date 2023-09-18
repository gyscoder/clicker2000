import time #importa a data do sistema
import threading # fazer com que a sua aplicação execute tarefas de forma assíncrona
from pynput.mouse import Button, Controller #controlar e monitorar o mouse.
from pynput.keyboard import Listener, KeyCode #controlar e monitorar o teclado

delay = 0.01 #  atraso entre cada clique no botão
button = Button.left # botão para clicar  'Button.left', 'Button.right' ou até 'Button.middle'
start_stop_key = KeyCode(char='k') # é a chave para iniciar e parar o auto clicker
exit_key = KeyCode(char='f') # é a chave para fechar o programa

class ClickMouse(threading.Thread): #  permitirá controlar os cliques do mouse.
	def __init__ (self, delay, button): 
		super().__init__()
		self.delay = delay
		self.button = button
		self.running = False
		self.program_running = True
	def start_clicking(self):
		self.running = True
	def stop_clicking(self):
		self.running = False
	def exit(self):
		self.stop_clicking()
		self.program_running = False
	def run(self):
		while self.program_running:
			while self.running:
				mouse.click(self.button)
				time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
	if key == start_stop_key:
		if click_thread.running:
			click_thread.stop_clicking()
		else:
			click_thread.start_clicking()
	elif key == exit_key:
		click_thread.exit()
		listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()