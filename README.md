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

## Screenshots

(Optional: Add screenshots here to show the interface and how it works)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Qt and Tkinter documentation for providing useful information.
- Thanks to PyQt5 for making the `.ui` to `.py` conversion possible using `pyuic5`.

---

## Explanation of Sections:

1. **Title and Overview**: Describes the purpose of the project.
2. **Features**: Highlights the core functionalities of the app.
3. **Requirements**: Lists the necessary tools and libraries, such as Python, `pyuic5`, and Tkinter.
4. **How to Run**: Provides clear instructions on how to clone the repository and run the application.
5. **How to Use**: Describes how the user can interact with the app.
6. **Screenshots**: Optionally, you can add screenshots to visually show how the app looks and works.
7. **License**: Includes licensing information (you can adjust this based on your license choice).
8. **Acknowledgments**: Credit to resources or libraries used in the project.

Feel free to modify the instructions according to your repository and project details.
