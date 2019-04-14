from PySide2.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QDateEdit, QSpacerItem, QSizePolicy, QStyle)
from PySide2.QtCore import (SIGNAL, Slot, QDate)


class MonthSwitcher(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.date_widget = None

        self.setup_ui()

    def setup_ui(self):
        top_layout = QHBoxLayout()

        left = QPushButton('<', self)
        right = QPushButton('>', self)

        self.date_widget = QDateEdit(self)
        self.date_widget.setDisplayFormat('yyyy MMM')
        self.date_widget.setDate(QDate().currentDate())

        self.connect(
            left, SIGNAL('clicked()'),
            self.subtractMonth
        )
        self.connect(
            right, SIGNAL('clicked()'),
            self.addMonth
        )

        top_layout.addWidget(left)
        top_layout.addWidget(self.date_widget)
        top_layout.addWidget(right)
        top_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum))

        self.setLayout(top_layout)

    @Slot()
    def addMonth(self):
        self.date_widget.setDate(
            self.date_widget.date().addMonths(1)
        )

    @Slot()
    def subtractMonth(self):
        self.date_widget.setDate(
            self.date_widget.date().addMonths(-1)
        )

    def getDate(self):
        return self.date_widget.date()


if __name__ == '__main__':
    import sys

    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)

    w = MonthSwitcher()
    w.show()

    sys.exit(app.exec_())
