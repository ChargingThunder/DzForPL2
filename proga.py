from PyQt6 import QtCore, QtGui, QtWidgets

centralwidget = QtWidgets.QWidget()
centralwidget.setObjectName("centralwidget")
label = QtWidgets.QLabel(parent=centralwidget)
label.setGeometry(QtCore.QRect(300, 40, 191, 41))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(14)
font.setBold(True)
font.setWeight(75)
label.setFont(font)
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
label.setObjectName("label")
label_2 = QtWidgets.QLabel(parent=centralwidget)
label_2.setGeometry(QtCore.QRect(50, 130, 151, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_2.setFont(font)
label_2.setObjectName("label_2")
label_3 = QtWidgets.QLabel(parent=centralwidget)
label_3.setGeometry(QtCore.QRect(50, 160, 151, 20))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_3.setFont(font)
label_3.setObjectName("label_3")
label_4 = QtWidgets.QLabel(parent=centralwidget)
label_4.setGeometry(QtCore.QRect(50, 190, 151, 20))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_4.setFont(font)
label_4.setObjectName("label_4")
label_5 = QtWidgets.QLabel(parent=centralwidget)
label_5.setGeometry(QtCore.QRect(50, 220, 151, 20))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_5.setFont(font)
label_5.setObjectName("label_5")
label_6 = QtWidgets.QLabel(parent=centralwidget)
label_6.setGeometry(QtCore.QRect(50, 250, 151, 20))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_6.setFont(font)
label_6.setObjectName("label_6")
label_7 = QtWidgets.QLabel(parent=centralwidget)
label_7.setGeometry(QtCore.QRect(50, 280, 151, 20))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_7.setFont(font)
label_7.setObjectName("label_7")
label_8 = QtWidgets.QLabel(parent=centralwidget)
label_8.setGeometry(QtCore.QRect(220, 130, 51, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_8.setFont(font)
label_8.setObjectName("label_8")
label_9 = QtWidgets.QLabel(parent=centralwidget)
label_9.setGeometry(QtCore.QRect(220, 160, 51, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_9.setFont(font)
label_9.setObjectName("label_9")
label_10 = QtWidgets.QLabel(parent=centralwidget)
label_10.setGeometry(QtCore.QRect(220, 190, 51, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_10.setFont(font)
label_10.setObjectName("label_10")
label_11 = QtWidgets.QLabel(parent=centralwidget)
label_11.setGeometry(QtCore.QRect(220, 220, 51, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_11.setFont(font)
label_11.setObjectName("label_11")
label_12 = QtWidgets.QLabel(parent=centralwidget)
label_12.setGeometry(QtCore.QRect(220, 250, 51, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_12.setFont(font)
label_12.setObjectName("label_12")
label_13 = QtWidgets.QLabel(parent=centralwidget)
label_13.setGeometry(QtCore.QRect(220, 280, 51, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_13.setFont(font)
label_13.setObjectName("label_13")
lineEdit = QtWidgets.QLineEdit(parent=centralwidget)
lineEdit.setGeometry(QtCore.QRect(320, 340, 113, 20))
lineEdit.setObjectName("lineEdit")
label_14 = QtWidgets.QLabel(parent=centralwidget)
label_14.setGeometry(QtCore.QRect(300, 310, 151, 20))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(10)
label_14.setFont(font)
label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
label_14.setObjectName("label_14")
pushButton = QtWidgets.QPushButton(parent=centralwidget)
pushButton.setGeometry(QtCore.QRect(320, 370, 111, 31))
pushButton.setObjectName("pushButton")

label.setText("Миллион бросков")
label_2.setText("Вероятность выпадения 1:")
label_3.setText("Вероятность выпадения 2:")
label_4.setText("Вероятность выпадения 3:")
label_5.setText("Вероятность выпадения 4:")
label_6.setText("Вероятность выпадения 5:")
label_7.setText("Вероятность выпадения 6:")
label_8.setText("0")
label_9.setText("0")
label_10.setText("0")
label_11.setText("0")
label_12.setText("0")
label_13.setText("0")
label_14.setText("Количество бросков:")
pushButton.setText("Подбросить")