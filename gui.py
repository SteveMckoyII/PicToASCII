import sys
import os
import main

from PyQt5.QtWidgets import *
from PIL import Image

input_file = ''

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'Pic To ASCII'
		self.left = 700
		self.top = 400
		self.width = 800
		self.height = 600
		self.window = QWidget()
		self.layout = QVBoxLayout()
		self.initUI()

	def initUI(self):
		self.window.setWindowTitle(self.title)
		self.window.setGeometry(self.left, self.top, self.width, self.height)

		import_button = QPushButton("import picture", self)
		import_button.clicked.connect(self.import_button_click)
		import_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

		export_button = QPushButton("export picture", self)
		#export_button.clicked.connect(self.export_button_click)
		export_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

		self.layout.addWidget(import_button)
		self.layout.addWidget(export_button)

		self.window.setLayout(self.layout)

		self.window.show()

	def import_button_click(self):
		global input_file
		dialog = QFileDialog.getOpenFileName(self, 'Picture Files', './', 'Image Files(*.png *.jpg *.gif)')
		print(dialog)
		if dialog:
			input_file = dialog[0]

	def export_button_click(self):
		def message_box():
				os_command = 'notepad.exe' + output_file
				os.system(os_command)
		
		global input_file
		if input_file:
			file_type = input_file[len(input_file) - 3: len(input_file)]
			if file_type == 'jpg' or file_type == 'png':
				dialog = QFileDialog.getSaveFileName(self, 'Text Files', './', 'Text Files(*.txt)')
				if dialog:
					output_file = dialog[0]
					if main.convert_image(input_file, output_file):
						msg_box = QMessageBox()
						msg_box.setIcon(QMessageBox.Information)
						msg_box.setText('Click OK to open the file.')
						msg_box.setWindowTitle('Convert Succsesful')
						msg_box.buttonClicked.connect(message_box)
						msg_box.exec_()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
