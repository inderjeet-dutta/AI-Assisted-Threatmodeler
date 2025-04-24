'''
                                                        𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕕 𝕓𝕪 : 🅸🅽🅳🅴🆁🅹🅴🅴🆃 🅳🆄🆃🆃🅰
'''

import sys  
import os
import subprocess
from time import sleep  
from PyQt5.QtWidgets import (  
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox,  
    QGridLayout, QMenuBar, QStatusBar, QTextEdit, QProgressBar  
)  
from PyQt5.QtGui import QPixmap  
from PyQt5.QtCore import QBuffer, QIODevice, Qt  
from openai import AzureOpenAI  
import base64  
import mimetypes  
from fpdf import FPDF
from datetime import datetime 
  
class ThreatModelingApp(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.initUI()  
  
    def initUI(self):  
        self.setWindowTitle('AI-Assisted Threatmodeler')  
        self.resize(1000, 400)  
  
        main_layout = QVBoxLayout()  
  
        # Menu bar  
        menu_bar = QMenuBar(self)  
        file_menu = menu_bar.addMenu('File')  
        help_menu = menu_bar.addMenu('Help')  
        main_layout.setMenuBar(menu_bar)  
  
        # Status bar  
        self.status_bar = QStatusBar(self)  
        self.progress_bar = QProgressBar(self)  
        self.progress_bar.setAlignment(Qt.AlignCenter)  
        self.status_bar.addPermanentWidget(self.progress_bar)  
        main_layout.addWidget(self.status_bar)  
  
        # Grid layout for form fields  
        form_layout = QGridLayout()  
  
        # API Key  
        self.api_key_label = QLabel('OpenAPI Key:')  
        self.api_key_entry = QLineEdit()  
        form_layout.addWidget(self.api_key_label, 0, 0)  
        form_layout.addWidget(self.api_key_entry, 0, 1)  
  
        # API URL  
        self.api_url_label = QLabel('OpenAPI URL:')  
        self.api_url_entry = QLineEdit()  
        form_layout.addWidget(self.api_url_label, 0, 2)  
        form_layout.addWidget(self.api_url_entry, 0, 3)  
  
        # API Model  
        self.api_model_label = QLabel('OpenAPI Model:')  
        self.api_model_entry = QLineEdit()  
        form_layout.addWidget(self.api_model_label, 0, 4)  
        form_layout.addWidget(self.api_model_entry, 0, 5)  
  
        # Diagram Image File  
        self.image_label = QLabel('System Design / DFD:')  
        self.image_entry = QLineEdit()  
        self.image_button = QPushButton('Browse')  
        self.image_button.clicked.connect(self.browse_image_file)  
        self.paste_button = QPushButton('Paste from Clipboard')  
        self.paste_button.clicked.connect(self.paste_from_clipboard)  
        form_layout.addWidget(self.image_label, 1, 0)  
        form_layout.addWidget(self.image_entry, 1, 1)  
        form_layout.addWidget(self.image_button, 1, 2)  
        form_layout.addWidget(self.paste_button, 1, 3)  
  
        main_layout.addLayout(form_layout)  
  
        # Application Details  
        self.details_label = QLabel('Application Details:')  
        self.details_entry = QTextEdit()  
        main_layout.addWidget(self.details_label)  
        main_layout.addWidget(self.details_entry)  
  
        # Generate Report Button  
        self.generate_button = QPushButton('Perform AI-Assisted Threatmodeling')  
        self.generate_button.clicked.connect(self.start_processing)  
        main_layout.addWidget(self.generate_button)  
  
        # Open Report Button (Initially Hidden)  
        self.open_report_button = QPushButton('Open Report')  
        self.open_report_button.clicked.connect(self.open_report)  
        self.open_report_button.setVisible(False)  
        main_layout.addWidget(self.open_report_button)  
  
        self.setLayout(main_layout)  
  
    def browse_image_file(self):  
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.jpg *.png);;All Files (*)")  
        if file_path:  
            self.image_entry.setText(file_path)  
  
    def paste_from_clipboard(self):  
        clipboard = QApplication.clipboard()  
        pixmap = clipboard.pixmap()  
        if pixmap.isNull():  
            QMessageBox.warning(self, "Error", "Clipboard does not contain an image.")  
            return  
        image_data = QBuffer()  
        image_data.open(QIODevice.WriteOnly)  
        pixmap.save(image_data, "PNG")  
        image_path = "clipboard_image.png"  
        with open(image_path, 'wb') as f:  
            f.write(image_data.data())  
        self.image_entry.setText(image_path)  
  
    def start_processing(self):  
        api_key = self.api_key_entry.text().strip()  
        api_url = self.api_url_entry.text().strip()  
        api_model = self.api_model_entry.text().strip()  
        image_path = self.image_entry.text().strip()  
        application_details = self.details_entry.toPlainText().strip()  
  
        if not api_key:  
            QMessageBox.warning(self, "Error", "OpenAPI Key is Required!")  
            return  
        elif not api_url:  
            QMessageBox.warning(self, "Error", "OpenAPI URL is Required!")  
            return  
        elif not api_model:  
            QMessageBox.warning(self, "Error", "OpenAPI Model Name is Required!\nEg: gpt-xx_ver_yyyy-mm-dd")  
            return  
        elif not image_path:  
            QMessageBox.warning(self, "Error", "Provide the Application DFD/Design JPG/PNG image!")  
            return  
        elif not application_details:  
            QMessageBox.warning(self, "Error", "Provide details of the target system/application!")  
            return  
  
        self.status_bar.showMessage("Configuring AI Assisted Threatmodeler...", 5000)  
        self.progress_bar.setValue(10)  
        QApplication.processEvents()  
        sleep(1)  
  
        client = AzureOpenAI(api_key=api_key, api_version="2023-12-01-preview", azure_endpoint=api_url)  
  
        def azure_openai_vision_mode(user_input, system_content, image_content):  
            try:  
                completion = client.chat.completions.create(  
                    model=api_model,  
                    messages=[  
                        {  
                            "role": "user",  
                            "content": [  
                                {  
                                    "type": "text",  
                                    "text": system_content + "\n" + user_input  
                                },  
                                {  
                                    "type": "image_url",  
                                    "image_url": {  
                                        "url": image_content  
                                    }  
                                }  
                            ],  
                        }  
                    ]  
                )  
                return str(completion.choices[0].message.content)  
            except Exception as e:  
                QMessageBox.critical(self, "Error", f"Failed to generate AI response: {e}")  
                return None  
  
        def read_file_contents(file_path):  
            try:  
                with open(file_path, 'r') as file:  
                    return file.read()  
            except Exception as e:  
                QMessageBox.critical(self, "Error", f"Failed to read file {file_path}: {e}")  
                return None  
  
        def read_image_data(image_path):  
            try:  
                mime_type = "application/octet-stream"  
                mime_type, _ = mimetypes.guess_type(image_path)  
                with open(image_path, 'rb') as image_file:  
                    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')  
                image_data = f"data:{mime_type};base64,{encoded_image}"  
                return image_data  
            except Exception as e:  
                QMessageBox.critical(self, "Error", f"Failed to read image {image_path}: {e}")  
                return None  
        # Paths to the files  
        objectives_file_path = os.path.join('data', '1objectives.md')  
        trustzones_file_path = os.path.join('data', '2trustzones.md')  
        analysis_file_path = os.path.join('data', '3analysis.md')  
        countermeasures_file_path = os.path.join('data', '4countermeasures.md')  
  
        # Read file contents  
        objectives_content = read_file_contents(objectives_file_path)  
        trustzones_content = read_file_contents(trustzones_file_path)  
        analysis_content = read_file_contents(analysis_file_path)  
        countermeasures_content = read_file_contents(countermeasures_file_path)  
  
        if not all([objectives_content, trustzones_content, analysis_content, countermeasures_content]):
            self.status_bar.showMessage("Something went wrong! Please verify the configurations and Try again!")  
            self.progress_bar.setValue(0) 
            return   
  
        # Read image data  
        image_content = read_image_data(image_path)  
        if not image_content:
            self.status_bar.showMessage("Something went wrong! Please verify the configurations and Try again!")  
            self.progress_bar.setValue(0) 
            return    
        
        output_file = ''  
  
        # Generate sections  
        sections = [  
            ("Generating security objectives...", 20, objectives_content, "Security Objectives", "objectives"),  
            ("Identifying Trust Zones...", 40, trustzones_content, "Trust Zones", "trustzones"),  
            ("Performing threat analysis...", 60, analysis_content, "Threat Analysis", "analysis"),  
            ("Generating counter measures...", 80, countermeasures_content, "Counter Measures", "countermeasures")  
        ]  
        next_prompt = ''
        for message, progress, content, title, variable_name in sections:  
            self.status_bar.showMessage(message, 5000)  
            self.progress_bar.setValue(progress)  
            QApplication.processEvents()  
  
            print(message)  
            prompt = application_details if variable_name in ("objectives","trustzones") else f"{application_details}\n\n{next_prompt}" 
            result = azure_openai_vision_mode(prompt, content, image_content)  
            if result:
                if variable_name in ("objectives","analysis","countermeasures"):
                    next_prompt = result  
                formatted_result = f"\n\n##_________________________________________________________\n#{title}\n##_________________________________________________________\n{result}"  
                output_file += formatted_result
            else:
                self.status_bar.showMessage("Something went wrong! Please verify the configurations and Try again!")  
                self.progress_bar.setValue(0) 
                return  
  
        watermark = "\n\n##_________________________________________________________\n##Report prepared using AI-Assisted Threatmodeler by Inderjeet Dutta" \
        "https://github.com/inderjeet-dutta\n##_________________________________________________________"
        output_file += watermark
        output_file = output_file.encode("latin-1", errors="replace").decode("latin-1")  
  
        # Generate PDF report
        try:  
            pdf = FPDF()  
            pdf.add_page()
            pdf.set_font("Arial", size=20)
            pdf.set_author("AI-Assisted Threatmodeler by Inderjeet Dutta (https://github.com/inderjeet-dutta)")
            pdf.text(x=50, y=15, txt="AI-Assisted Threatmodeler Report")  
            pdf.set_font('Arial', '', 10)  
            pdf.set_title("AI-Assisted Threatmodeler Report")  
            if image_path:  
                pdf.image(image_path, 15, 20, 180)  
                pdf.ln(150)  
            else:  
                pdf.ln(15)  
            pdf.multi_cell(0, 5, output_file)  
            current_datetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")  
            pdf_output_path = f"AI-Assisted-Threatmodeler-Report_{current_datetime}.pdf"  
            pdf.output(pdf_output_path)
            pdf.output(pdf_output_path)  
            self.status_bar.showMessage("Report generated successfully!")  
            self.progress_bar.setValue(100)  
            QApplication.processEvents()  
            QMessageBox.information(self, "Success", f"Report generated successfully!\nClick on Open Report to access the pdf")  
    
            # Show the "Open Report" button and store the PDF path  
            self.pdf_output_path = pdf_output_path  
            self.open_report_button.setVisible(True)  
    
        except Exception as e:  
            QMessageBox.critical(self, "Error", f"Failed to generate PDF report: {e}")  
  
    def open_report(self):  
        if self.pdf_output_path and os.path.exists(self.pdf_output_path):  
            try:  
                if sys.platform.startswith('darwin'):  
                    subprocess.call(('open', self.pdf_output_path))  
                elif os.name == 'nt':  
                    os.startfile(self.pdf_output_path)  
                elif os.name == 'posix':  
                    subprocess.call(('xdg-open', self.pdf_output_path))  
                else:  
                    QMessageBox.warning(self, "Error", "Unsupported operating system!")  
            except Exception as e:  
                QMessageBox.critical(self, "Error", f"Failed to open PDF report: {e}")  
        else:  
            QMessageBox.warning(self, "Error", "PDF report file not found!")
  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    ex = ThreatModelingApp()  
    ex.show()  
    sys.exit(app.exec_())

'''
                                                       𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕕 𝕓𝕪 : 🅸🅽🅳🅴🆁🅹🅴🅴🆃 🅳🆄🆃🆃🅰
'''