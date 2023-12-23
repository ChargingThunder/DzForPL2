from PyQt6.QtWidgets import QApplication, QMainWindow
import random, sys

def main():
    app = QApplication(sys.argv)
    import proga
    
    win = QMainWindow()
    win.resize(800, 600)
    win.setCentralWidget(proga.centralwidget)

    proga.pushButton.clicked.connect(throw)

    win.show()
    sys.exit(app.exec())

def throw():
    import proga
    throws = []
    statistics = []
    proverka = 0
    sumthrows = int(proga.lineEdit.text())

    for i in range(sumthrows):
        throws.append(random.randint(1,6))
    
    for j in range(1, 7):
        proverka += throws.count(j)/sumthrows
        statistics.append(throws.count(j)/sumthrows)
    
    proga.label_8.setText(str(statistics[0]))
    proga.label_9.setText(str(statistics[1]))
    proga.label_10.setText(str(statistics[2]))
    proga.label_11.setText(str(statistics[3]))
    proga.label_12.setText(str(statistics[4]))
    proga.label_13.setText(str(statistics[5]))

if __name__ == "__main__":
    main()