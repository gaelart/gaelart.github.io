from PySide6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit,
    QDialogButtonBox, QApplication
)

class ArtworkDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Artwork")

        self.title_edit = QLineEdit()
        self.year_edit = QLineEdit()
        self.medium_edit = QLineEdit()
        self.available_edit = QLineEdit()
        self.collection_edit = QLineEdit()
        self.price = QLineEdit()
        self.tags_edit = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Title:", self.title_edit)
        layout.addRow("Year:", self.year_edit)
        layout.addRow("Medium:", self.medium_edit)
        layout.addRow("Availability:", self.available_edit)
        layout.addRow("Collection:", self.collection_edit)
        layout.addRow("Price:", self.price)
        layout.addRow("Extra Tags:", self.tags_edit)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)
        self.setLayout(layout)

    def get_data(self):
        return {
            "title": self.title_edit.text(),
            "year": self.year_edit.text(),
            "medium": self.medium_edit.text(),
            "available": self.available_edit.text(),
            "collection": self.collection_edit.text().lower() if self.collection_edit.text() != "" else "none",
            "price": self.price.text(),
            "extra_tags": self.tags_edit.text().split("-") if self.tags_edit.text() != "" else []
        }