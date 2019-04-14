from PySide2.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget

from .month_switcher import MonthSwitcher
from .overview import Overview


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)

        month_switcher = MonthSwitcher(self)
        tabs = QTabWidget(self)

        overview = Overview(self)
        db = Overview(self)
        charts = Overview(self)
        tabs.addTab(overview, 'Overview')
        tabs.addTab(db, 'DB')
        tabs.addTab(charts, 'Charts')

        top_layout = QVBoxLayout()
        top_layout.addWidget(month_switcher)
        top_layout.addWidget(tabs)

        central_widget.setLayout(top_layout)
        self.setCentralWidget(central_widget)
