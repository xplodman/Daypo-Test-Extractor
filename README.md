# Daypo Test Extractor

This project is designed to automate the process of extracting tests from the Daypo website using Python and Selenium. It captures screenshots of each question and their respective answers, then compiles them into a single PDF document. This tool is particularly useful for educators, students, or professionals who need to gather test material efficiently for study or record-keeping purposes.

## Features

- Automatically navigate through test questions on Daypo.
- Capture screenshots of each question and answer.
- Compile all screenshots into a well-formatted PDF file.
- Use of Chrome extensions (e.g., ad blockers) to enhance browsing experience during extraction.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher installed on your system.
- Google Chrome browser installed.
- ChromeDriver compatible with the version of your Chrome browser.

## Installation

Follow these steps to get your development environment set up:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/daypo-test-extractor.git
   cd daypo-test-extractor
   ```

2. **Set up a Python virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### `requirements.txt`

Make sure your `requirements.txt` includes:
```
selenium
Pillow
fpdf
```

## Usage

To run the script, execute:

```bash
python daypo_extractor.py
```

The script will navigate through the Daypo test URL you have set, capture each page as a screenshot, and compile these into a PDF. Make sure to adjust the `daypo_extractor.py` with your specific test URL and any other parameters as necessary.

## Configuring ChromeDriver

- Download the ChromeDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/).
- Ensure the path to `chromedriver` is correctly set in the script.

## Output

The output PDF will be saved in the project directory under the name `Questions_and_Answers.pdf`, and individual screenshots will be available in the `screenshots` folder.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, or create issues if you find any bugs or have suggestions.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

Make sure to customize the above README according to the actual paths, filenames, and configurations used in your project. Adjust the repository URL and any specific details about how to run the script or configure the environment as necessary.