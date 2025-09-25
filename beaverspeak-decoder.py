import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt5.QtWidgets import QHeaderView

class DecoderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.alpha_dict = {
            "a":"b", "b":"a", "c":"d", "d":"c", "e":"f", "f":"e", "g":"h", "h":"g",
            "i":"j", "j":"i", "k":"l", "l":"k", "m":"n", "n":"m", "o":"p", "p":"o",
            "q":"r", "r":"q", "s":"t", "t":"s", "u":"v", "v":"u", "w":"x", "x":"w",
            "y":"z", "z":"y"
        }

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Beaverspeak Decoder')
        self.resize(600, 400)  # Set default window size

        self.input_label = QLabel('Enter the phrase you wish to decode:', self)
        self.input_text = QLineEdit(self)

        self.decode_button = QPushButton('Decode', self)
        self.decode_button.clicked.connect(self.decode_text)

        self.clear_button = QPushButton('Clear History', self)
        self.clear_button.clicked.connect(self.clear_history)
        
        self.clear_text_button = QPushButton('Clear Text', self)
        self.clear_text_button.clicked.connect(self.clear_text)

        self.output_label = QLabel('', self)
        self.history_label = QLabel('History:', self)
        self.history_table = QTableWidget(self)
        self.history_table.setColumnCount(2)
        self.history_table.setHorizontalHeaderLabels(["Input", "Output"])
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Layouts
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_text)
        input_layout.addWidget(self.clear_text_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.decode_button)
        button_layout.addWidget(self.clear_button)

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.output_label)
        layout.addWidget(self.history_label)
        layout.addWidget(self.history_table)

        self.setLayout(layout)
        self.show()

    def decode_text(self):
        input_string = self.input_text.text().lower()
        output_string = ""
        
        if input_string == "":
            self.output_label.setText("Input can not be blank.")
            return

        for letter in input_string:
            if letter.isspace():
                output_string += letter
            elif letter in self.alpha_dict:
                output_string += self.alpha_dict[letter]

        self.output_label.setText("")

        row_position = self.history_table.rowCount()
        self.history_table.insertRow(row_position)
        self.history_table.setItem(row_position, 0, QTableWidgetItem(input_string))
        self.history_table.setItem(row_position, 1, QTableWidgetItem(output_string))

    def clear_history(self):
        self.history_table.setRowCount(0)

    def clear_text(self):
        self.input_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DecoderApp()
    sys.exit(app.exec_())
