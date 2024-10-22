import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox, QVBoxLayout
from PIL import Image

class ImageConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("JPEG to PNG Converter")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        single_file_button = QPushButton("Convert Single File")
        single_file_button.clicked.connect(self.select_single_file)
        layout.addWidget(single_file_button)

        batch_file_button = QPushButton("Convert Batch Files")
        batch_file_button.clicked.connect(self.select_batch_files)
        layout.addWidget(batch_file_button)

        self.setLayout(layout)

    def jpeg_to_png(self, input_file_path, output_file_path):
        try:
            with Image.open(input_file_path) as img:
                img.save(output_file_path, format="PNG")
            print(f"Successfully converted {input_file_path} to {output_file_path}")
        except Exception as e:
            print(f"Error converting image: {e}")

    def batch_convert_jpeg_to_png(self, input_directory, output_directory):
        try:
            for filename in os.listdir(input_directory):
                if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                    input_file = os.path.join(input_directory, filename)
                    output_file = os.path.join(output_directory, filename.replace(".jpg", ".png").replace(".jpeg", ".png"))
                    self.jpeg_to_png(input_file, output_file)
            QMessageBox.information(self, "Success", "Batch conversion completed.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error during batch conversion: {e}")

    def select_single_file(self):
        input_file, _ = QFileDialog.getOpenFileName(self, "Select JPEG File", "", "JPEG files (*.jpg *.jpeg)")
        if input_file:
            output_file, _ = QFileDialog.getSaveFileName(self, "Save as PNG", "", "PNG files (*.png)")
            if output_file:
                self.jpeg_to_png(input_file, output_file)

    def select_batch_files(self):
        input_directory = QFileDialog.getExistingDirectory(self, "Select Input Directory")
        if input_directory:
            output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
            if output_directory:
                self.batch_convert_jpeg_to_png(input_directory, output_directory)

if __name__ == "__main__":
    app = QApplication([])
    converter = ImageConverterApp()
    converter.show()
    app.exec_()
