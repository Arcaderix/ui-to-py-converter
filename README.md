# UI to PY Converter

A simple Tkinter-based GUI application that allows users to convert Qt Designer `.ui` files to `.py` files using the `pyuic5` command-line tool. This tool also provides functionality to open a `.ui` file, display logs, show conversion progress, and save the converted `.py` file to a user-specified location.

## Features

- **Open `.ui` file**: Allows users to browse and select a `.ui` file for conversion.
- **Conversion to `.py`**: Converts the `.ui` file to a Python file using `pyuic5`.
- **Progress bar**: Displays the conversion progress.
- **Log window**: Shows detailed logs of the conversion process inside the app.
- **Save the converted file**: Lets users save the converted `.py` file to any desired location.

## Requirements

- Python 3.x
- `pyuic5` (PyQt5) installed. You can install it via pip:

```bash
pip install pyqt5
```

- Tkinter (usually included with Python, but if not, install it with):

```bash
sudo apt-get install python3-tk
```



Navigate to the project directory:

```bash
cd ui-to-py-converter
```

Run the Python script:

```bash
python app.py
```

## How to Use

- **Open File**: Click the "Open File" button to select a `.ui` file.
- **Convert**: Click the "Convert" button to convert the selected `.ui` file into a `.py` file. The conversion progress will be displayed.
- **Save**: Once the conversion is complete, click the "Save" button to save the `.py` file to your chosen directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
