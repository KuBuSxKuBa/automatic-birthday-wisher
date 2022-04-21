import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QInputDialog, QFileDialog, QMessageBox,
                             QGridLayout, QLabel, QPushButton, QFrame)
import sys
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
class InputDialog(QWidget):
    def __init__(self):
        super(InputDialog,self).__init__()

        label1 = QLabel("E-mail")
        label2 = QLabel("Month")
        label3 = QLabel("Name")
        label4 = QLabel("Day")

        self.e1 = QLineEdit()
        self.e1.setAlignment(Qt.AlignLeft)
        self.e1.setFont(QFont("Arial", 20))

        self.e2 = QLineEdit()
        self.e2.setMaxLength(15)
        self.e2.setAlignment(Qt.AlignLeft)
        self.e2.setFont(QFont("Arial", 20))

        self.e3 = QLineEdit()
        self.e3.setMaxLength(2)
        self.e3.setAlignment(Qt.AlignLeft)
        self.e3.setFont(QFont("Arial", 20))

        self.e4 = QLineEdit()
        self.e4.setMaxLength(2)
        self.e4.setAlignment(Qt.AlignLeft)
        self.e4.setFont(QFont("Arial", 20))

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.resize(150,50)
        self.b1.setStyleSheet("color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8;")
        # self.b1.setStyleSheet("QPushButton::hover"
        #                      "{"
        #                      "background-color : lightgreen;"
        #                      "}")
        self.b1.setText("Confirm")
        self.b1.clicked.connect(self.update_list)

        mainLayout = QGridLayout()

        mainLayout.addWidget(label1,          0, 0)
        mainLayout.addWidget(self.e1,  0, 1)

        mainLayout.addWidget(label3,          1, 0)
        mainLayout.addWidget(self.e2,1, 1)

        mainLayout.addWidget(label2,          2, 0)
        mainLayout.addWidget(self.e3,   2, 1, 1, 1)

        mainLayout.addWidget(label4, 3, 0)
        mainLayout.addWidget(self.e4, 3, 1, 1, 1)

        mainLayout.addWidget(self.b1 , 4, 1, 1, 1)
        # mainLayout.setRowMinimumHeight(2, 40)
        mainLayout.addWidget(QLabel(), 3, 0)
        mainLayout.setRowStretch(3, 1)
        mainLayout.setColumnMinimumWidth(1, 200 )
        mainLayout.setSpacing(5)

        self.setLayout(mainLayout)

    def update_list(self):
        # name = self.e2.text()
        # new_data = {
        #     name: {
        #         "email":self.e1.text(),
        #         "month":self.e3.text(),
        #         "day":self.e4.text()
        #     }
        # }
        #
        # with open("data.json", "w") as file:
        #     json.dump(new_data, file, indent=4)
        email = self.e1.text()
        month = self.e3.text()
        day = self.e4.text()
        name = self.e2.text()
        if len(email) == 0 or len(month) == 0 or len(day) == 0 or len(name) == 0:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Dont leave blank!")
            self.msg.setText("Dont leave blank fields!")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()
        else:
            if int(month) > 0 and int(month) <= 12 and int(day) > 0 and int(day) <= 31:
                with open("data.txt" , "a") as file:
                    file.write(f"{email}:{month}:{day}:{name}\n")
            else:
                self.message = QMessageBox()
                self.message.setWindowTitle("Provide correct data")
                self.message.setText("Provide correct month and day data!")
                self.message.setIcon(QMessageBox.Critical)
                self.message.exec_()

        self.close()


if __name__=="__main__":
    import sys
    app    = QApplication(sys.argv)
    myshow = InputDialog()
    myshow.setWindowTitle("InputDialog")
    myshow.show()
    sys.exit(app.exec_())