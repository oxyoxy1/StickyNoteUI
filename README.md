# Sticky Notes UI - oxy

Sticky Notes UI is a lightweight, easy-to-use desktop application that allows you to create, edit, and manage sticky notes on your computer. The application offers a user-friendly interface with features such as saving notes, saving them under a new name, and pinning them on top of other windows. It also supports drag-and-drop functionality for moving the sticky notes around.

## Features

- Create new sticky notes with user-defined titles.
- Open and edit existing sticky notes.
- Save sticky notes and save them under new names.
- Pin sticky notes on top of other windows.
- Drag-and-drop functionality for moving sticky notes.
- Auto-saves the content to a text file.

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- pyinstaller (for packaging as an executable)

## Installation

1. Clone or download the repository to your local machine.

    ```bash
    git clone https://github.com/oxyoxy1/StickyNotesUI.git
    ```

2. Navigate to the project directory:

    ```bash
    cd StickyNotesUI
    ```

3. Install the necessary dependencies (if not already installed):

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python main.py
    ```

   Alternatively, if you have built the executable using PyInstaller, you can simply double-click the executable to run the application.

## Building the Executable

To create a standalone executable of the application:

1. Make sure you have PyInstaller installed:

    ```bash
    pip install pyinstaller
    ```

2. Run PyInstaller with the following command to package the application:

    ```bash
    pyinstaller --onefile --noconsole --icon=icon.ico main.py
    ```

3. The executable will be created in the `dist` folder within your project directory.

## File Structure

```plaintext
StickyNotesUI/
│
├── main.py               # Main application script
├── icon.ico              # Application icon
├── requirements.txt      # Required Python dependencies
├── Notes/                # Directory to store sticky notes
└── README.md             # This file
