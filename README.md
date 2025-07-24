# Auto-Report Maker
Automatic report generator for the CISCAT PRO Assessor

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project was created during my time as an intern for the COH. I was inspired to make this program to ease the manual process of going through each and every section of a CISCAT Pro Assessor report and creating manually creating a Word document consisting of the section titles and their respective table data

## Installation
### Build From Source
1. Change current working directory to your CISCAT Pro Assessor reports folder
```powershell
cd $HOME\path\to\CISCAT\Pro\Assessor\reports
```
2. Clone the repository:
```powershell
git clone https://github.com/butterbanes/auto-ciscat-report.git
```

3. Make sure that pyinstaller
```powershell
pip install pyinstaller
```

4. Build the exe from source using PyInstaller with the following command
```powershell
pyinstaller .\auto-ciscat-report\auto-report.py --onefile --strip --optimize=2
```

## Usage
To run the project, use the following command inside your main reports folder:
```powershell
.\dist\auto-parse.exe
```
##### Note: you can move the exe directly into the reports folder to prevent having to list the path

## Contributing
1. Fork the repo
2. Create a new branch: 'git checkout -b feature-name'
3. Make your changes
4. Push your branch: 'git push origin feature-name'
5. Create pull request

## License
This project is licensed under the [BBCL](https://github.com/butterbanes/butterbanes-custom-license)
