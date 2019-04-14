from PySide2.QtWidgets import *


class Overview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):
        top_layout = QHBoxLayout()

        table = QTableWidget(self)
        top_layout.addWidget(table)

        side_bar = QVBoxLayout()
        w = QLabel('BUDGET OVERVIEW PLACEHOLDER', self)
        # w.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        side_bar.addWidget(w)
        side_bar.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        top_layout.addLayout(side_bar)

        self.setLayout(top_layout)


if __name__ == '__main__':
    import sys

    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)

    w = Overview()
    w.show()

    sys.exit(app.exec_())
