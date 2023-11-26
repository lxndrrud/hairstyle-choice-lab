from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from window import Ui_MainWindow
from states import q1, TreeItem
from functools import partial
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.treeStart = q1
        self.currentItem = q1
        self.ui.setupUi(self)
        self.setupCurrentQuestion()
        self.ui.resetStateButton.clicked.connect(self.resetStateButtonClickEvent)

    def flushOptions(self):
        child = self.ui.verticalLayout.takeAt(0)
        while child is not None:
            child.widget().deleteLater()
            child = self.ui.verticalLayout.takeAt(0)

    def resetStateButtonClickEvent(self):
        self.currentItem = q1
        self.ui.textEdit.setText("")
        self.setupCurrentQuestion()

    def optionClickEvent(self, item: TreeItem):
        self.currentItem = item
        self.setupCurrentQuestion()

    def setupCurrentQuestion(self):
        self.flushOptions()
        self.ui.textEdit.setText(
            self.ui.textEdit.toPlainText() + "\n" + self.currentItem.title
        )
        for item in self.currentItem.children:
            button_ = QPushButton(item.title)
            button_.clicked.connect(partial(self.optionClickEvent, item=item))
            self.ui.verticalLayout.addWidget(button_)


if __name__ == "__main__":
    app = QApplication()
    _window = MainWindow()
    _window.show()
    sys.exit(app.exec())
