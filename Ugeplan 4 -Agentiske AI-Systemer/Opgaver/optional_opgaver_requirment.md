# 🛠️ Optional: Set Up Your Local Environment for the Ungraded Labs

If you would like to run the **ungraded labs** on your own computer instead of using the online environment, follow the steps below.

> **💡 Note**
>
> When downloading an ungraded lab, make sure you also download **all supporting files**, such as:
>
> - Helper Python scripts (`.py`)
> - Configuration files
> - Datasets
> - Images
> - Any additional resources used by the notebook

---

# 📥 Step 1: Download the Lab Files

1. Open the lesson that contains the coding lab.
2. Open the embedded **Jupyter Notebook**.
3. From the top menu, select:

```
File → Open
```

4. Download:
   - The Jupyter Notebook (`.ipynb`)
   - All related helper files
   - Configuration files
   - Data files

Your folder structure may look like this:

```
Ungraded-Lab/
│
├── lab.ipynb
├── helper.py
├── config.py
├── data/
│   ├── dataset.csv
│   └── sample.json
├── images/
└── requirements.txt
```

---

# 🐍 Step 2: Install Python

Ensure you have **Python 3.10 or newer** installed.

Check your Python version:

```bash
python --version
```

Example output:

```
Python 3.12.2
```

Download Python from:

https://www.python.org/downloads/

---

# 📂 Step 3: Create a Project Folder

Create a folder for your lab.

Example:

```text
AI-Labs/
```

Move all downloaded files into this folder.

---

# 🌱 Step 4: Create a Virtual Environment (Recommended)

Using a virtual environment keeps project dependencies isolated.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, your terminal should look similar to:

```text
(venv) C:\AI-Labs>
```

---

# 📄 Step 5: Create the `requirements.txt` File

Inside your project folder, create a file named:

```text
requirements.txt
```

Copy the following content into the file.

```txt
# ==========================================================
# Agent + Large Language Model (LLM) Libraries
# ==========================================================

aisuite==0.1.11
anthropic
docstring-parser
markdown
mistralai
openai
qrcode
tavily-python>=0.7.12
textstat
vertexai

# ==========================================================
# Web Framework and API Development
# ==========================================================

fastapi
pydantic
pydantic[email]
python-dotenv
python-multipart
requests
sqlalchemy
uvicorn

# ==========================================================
# Jupyter Notebook Environment
# ==========================================================

ipywidgets
jupyter_server
nbclassic
notebook

# ==========================================================
# Data Analysis and Visualization
# ==========================================================

duckdb
matplotlib
pandas
seaborn
tabulate
tinydb

# ==========================================================
# Machine Learning and NLP
# ==========================================================

jinja2
psycopg2-binary
scikit-learn
Wikipedia
```

---

# 📦 Step 6: Install the Required Packages

Open a terminal inside your project folder and run:

```bash
pip install -r requirements.txt
```

This command installs all required Python packages automatically.

---

# 📚 Step 7: Register the Virtual Environment with Jupyter (Optional)

If you want to use the virtual environment inside **Jupyter Notebook** or **VS Code**, run:

```bash
python -m ipykernel install --user --name=venv
```

You should see a message similar to:

```
Installed kernelspec venv
```

---

# 💻 Step 8: Open the Project in VS Code

Open Visual Studio Code:

```bash
code .
```

or

```
File → Open Folder
```

Select your project folder.

---

# ▶️ Step 9: Start Jupyter Notebook

Launch Jupyter Notebook by running:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

Open your downloaded notebook (`.ipynb`) and begin experimenting.

---

# 📁 Recommended Project Structure

```text
AI-Labs/
│
├── venv/
├── notebooks/
│   ├── Lab01.ipynb
│   └── Lab02.ipynb
│
├── data/
│   ├── dataset.csv
│   └── sample.json
│
├── images/
│
├── helper.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ✅ Verify the Installation

Run the following command:

```bash
pip list
```

You should see packages similar to:

```
openai
fastapi
pandas
matplotlib
notebook
uvicorn
scikit-learn
```

---

# 🚀 You're Ready!

Once everything is installed successfully, you can:

- ✅ Run the Jupyter notebooks locally
- ✅ Experiment with the ungraded labs
- ✅ Modify the code
- ✅ Install additional packages
- ✅ Build your own AI and LLM projects

Happy coding! 🎉