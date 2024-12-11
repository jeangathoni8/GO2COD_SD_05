# Temperature Converter CLI

## 🌡️ Project Overview
Temperature Converter is a robust, user-friendly command-line interface (CLI) utility designed to simplify temperature conversions between Celsius and Fahrenheit. Built with Python, this application demonstrates best practices in software engineering, including input validation, error handling, and intuitive user experience.

## ✨ Features

- 🔄 Convert temperatures between Celsius and Fahrenheit
- 🛡️ Comprehensive input validation
- 🚦 User-friendly menu-driven interface
- 🛑 Robust error handling
- 🔢 Support for floating-point and integer temperatures

## 📦 Prerequisites

- Python 3.8+
- pip (Python package manager)

## 🚀 Installation

1. Clone the Repository
```bash
git clone https://github.com/jeangathoni8/GO2COD_SD_05.git
cd temperature-converter
```

2. Create Virtual Environment (Recommended)
```bash
# On Unix/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Running the Application
```bash
python -m src.temperature_converter
```

### Conversion Options
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit the application

### Example Interactions
```
--- Temperature Converter ---
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit

Enter your choice (1-3): 1
Enter temperature in Celsius: 25
25.00°C = 77.00°F

--- Temperature Converter ---
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
```

## 🧪 Testing

### Running Tests
```bash
# Ensure you're in the project root directory
pytest tests/
```

### Test Coverage
- Conversion accuracy
- Input validation
- Error handling scenarios

## 🛠️ Development

### Project Structure
```
temperature-converter/
│
├── src/
│   └── temperature_converter.py
├── tests/
│   └── test_temperature_converter.py
├── venv/
├── README.md
└── requirements.txt
```

### Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Coding Standards
- Follow PEP 8 guidelines
- Use type annotations
- Write comprehensive docstrings
- Maintain minimal global state

## 🔍 Limitations
- Currently supports Celsius and Fahrenheit conversions
- Requires manual input for each conversion

## 🚀 Future Roadmap
- ⭐ Add Kelvin conversions
- 📊 Implement persistent conversion history
- ⚙️ Create configuration options
- 🎨 Add color-coded console output
- 📦 Support batch conversions

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

## 🙏 Acknowledgements
- Python Software Foundation
- All contributors and supporters
