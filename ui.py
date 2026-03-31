import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import sys
from regenerate import generate_full_page
from art_manager import load_from_filepath, save_artwork
from artworkDialog import ArtworkDialog
import webbrowser
import pathlib

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.window = QtWidgets.QMainWindow()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)


        self.add_button = QtWidgets.QPushButton("add new artwork")
        self.regen_button = QtWidgets.QPushButton("regen gallery")
        self.preview_button = QtWidgets.QPushButton("preview gallery")

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.regen_button)
        self.layout.addWidget(self.preview_button)

        self.add_button.clicked.connect(self.load_artwork)
        self.regen_button.clicked.connect(self.regenerate_gallery)
        self.preview_button.clicked.connect(self.preview_gallery)

    @QtCore.Slot()
    def preview_gallery(self):
                
        path = pathlib.Path("index.html").resolve().as_uri()
        webbrowser.open(path)


    @QtCore.Slot()
    def regenerate_gallery(self):
        generate_full_page()

    @QtCore.Slot()
    def load_artwork(self):
        """
        opens a file dialog to select an image, then prompts the user for title, year, medium, availability, and extra tags. 
        Then it adds the artwork to the json file and regenerates the gallery.
        """

        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.window,
            "Open File",           # Dialog title
            "",                    # Default directory
            "All Files (*);;Text Files (*.txt)"
        )

        if file_path:
           
            dialog = ArtworkDialog(self)

            if dialog.exec(): 
                data = dialog.get_data()
                title = data["title"]
                year = data["year"]
                medium = data["medium"]
                available = data["available"]
                collection = data["collection"]
                price = data["price"]
                extra_tags = data["extra_tags"]
                print(title, year, medium, available, collection, extra_tags)
            else:
                return
            save_artwork({
                "title": title, 
                "year": year,
                "medium": medium,
                "available": available,
                "collection": collection,
                "price": price,
                "extra_tags": extra_tags,
                "file_path": file_path    
            })
            


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()