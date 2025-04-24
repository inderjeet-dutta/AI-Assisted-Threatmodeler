# AI-Assisted Threatmodeler  
  
## Overview  
AI-Assisted Threatmodeler is a tool designed to assist with threat modeling by leveraging AI capabilities. It generates reports based on provided images and application details. Built to rapidly perform a threat model of an application, this tool helps security teams quickly identify potential threats and implement countermeasures, ensuring that security objectives are met efficiently. This application follows the guidelines and principles outlined in NIST Special Publication 800-154 for Threat Modeling and uses the STRIDE model for threat categorization, covering Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service (DoS), and Elevation of Privilege.  
  
## NIST SP 800-154 Context  
NIST Special Publication 800-154, titled "Guide to Data-Centric System Threat Modeling," provides comprehensive guidance on how to effectively identify, assess, and mitigate threats to information systems. This publication emphasizes the importance of understanding the system's architecture, data flow, and potential vulnerabilities to implement appropriate security measures.  
  
### NIST Threat Modeling Chain  
The NIST SP 800-154 threat modeling process can be summarized in the following steps:  
  
1. **Define Security Objectives**: Identify and define the security goals for the system, such as confidentiality, integrity, and availability.  
2. **Identify Trust Boundaries**: Determine the trust boundaries within the system, where data moves between different trust levels.  
3. **Threat Analysis**: Analyze potential threats to the system by considering various threat sources and methods.  
4. **Countermeasures**: Identify and implement countermeasures to mitigate the identified threats.  
  
Our AI-Assisted Threatmodeler uses these principles to automate and enhance the threat modeling process, making it easier for security teams to generate thorough and accurate threat models.  
  
## Features  
- Upload or paste DFD/Design images.  
- Configure OpenAPI keys, URLs, and model names.  
- Generate PDF reports with security objectives, trust boundaries, threat analysis, and countermeasures.  
  
## Requirements  
- Python 3.x  
- PyQt5  
- OpenAI  
- FPDF  
  
## Installation  
1. Clone the repository:  
    ```sh  
    git clone https://github.com/inderjeet-dutta/AI-Assisted-Threatmodeler.git 
    ```  
  
2. Install the required dependencies:  
    ```sh  
    pip install -r requirements.txt  
    ```  
  
## Usage  
1. Run the application:  
    ```sh  
    python threatmodeler.py  
    ```  
  
2. Configure the necessary fields and generate the report.  
  
## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  