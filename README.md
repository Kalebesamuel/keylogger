# Keylogger

![Keylogger](https://t3.ftcdn.net/jpg/10/20/25/22/360_F_1020252214_jlf1xkZ2ZH75vSWwAFINeuU6iT4sVUJ0.jpg)

**Keylogger** is a Python-based project designed to capture and log keystrokes. It demonstrates how key-logging can be used for various purposes, such as monitoring typing activity for research, troubleshooting keyboard issues, or learning how keyloggers work for cybersecurity education.

⚠️ **Note**: This project is for **educational purposes only**. Please use responsibly and only on systems you have permission to monitor.

---

## 🚀 Features

- **Capture Keystrokes**: Records every keystroke made on the keyboard.
- **Logs to File**: Saves keystrokes into a log file for later analysis.
- **Hidden Execution**: Runs in the background without user interference.
- **Modular Design**: Built with functions that can be easily customized or extended.

---

## 📦 Project Structure

The project contains the following main files:

- **`keylogger.py`** - The main script that initiates the keylogger.
- **`requirements.txt`** - Lists all the Python libraries needed for this project.

---

## </> Technologies Used
[![Techs Used](https://skillicons.dev/icons?i=git,github,pycharm,py,md,bash&theme=light)](https://skillicons.dev)
---

## 🛠️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- **Python 3.x**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: (Optional) To clone the repository from GitHub.

### Installation

#### 1. Clone the Repository

```bash
  git clone https://github.com/Kalebesamuel/keylogger.git
  cd keylogger
```

#### 2. Install/Upgrade python

Run this commands to install or upgrade python and install tkinter:

```bash
  brew install python
  brew install python-tk@3.13
```

Or run this commands install using arch -arm64 (for M1 Mac) 

```bash
 arch -arm64 brew install python-tk@3.13
```

#### 2. Set Up Virtual Environment

Run this command to create and activate a virtual environment (recommended):

```bash
  python3 -m venv env
```

#### 3. Activate the Virtual Environment

- Windows:

```bash
  env\Scripts\activate
```

- MacOS/Linux:
```bash
  source env/bin/activate
```

#### 4. Install Requirements

Install the required dependencies:

```bash
  pip install -r requirements.txt
```

## 🔍 Usage

Once you've set up the environment, you're ready to run the keylogger.

#### 1. Run the Keylogger

- To start logging keystrokes, run:

```bash
  python3 keylogger.py
```

#### 2. Check Logs

- Keystrokes are saved in a file (specified within the script). Open this file to view the logged keystrokes.

#### 3. How it works?

- Refer [Code.md](./Code.md)

## ⚠️ Disclaimer

- This keylogger is intended for educational and research purposes only. Unauthorized keylogging is illegal and unethical. Only run this on systems you have permission to monitor.

## 💡 Customization and Expansion
- Logging Format: You can adjust how keystrokes are logged (timestamps, formatting, etc.) within the script.
- Additional Features: Try adding email reporting, screenshots, or encryption to further enhance functionality.

## 🧑‍💻 Contributing
- Contributions are welcome! Feel free to open issues or submit pull requests to improve the project. Always ensure compliance with ethical guidelines and project goals.

## 📄 License
- This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙋‍♂️ Questions?
- If you have any questions or need clarification, feel free to reach out via the GitHub Issues section.

- This **README** provides a friendly, clear, and ethical overview, and ensures users understand both setup and legal considerations.


## ✨ Show your support
Give a ⭐ if you like this repository!

Happy Logging! 🔍

<!-- [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?&logo=buy-me-a-coffee&logoColor=black)]() -->
