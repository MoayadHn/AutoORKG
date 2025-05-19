
# 📊 Excel Loader Utility (Jupyter Edition)

This notebook-based utility allows you to easily add coded papers into ORGK.


---

## 📁 Project Structure

```
project-root/
├── main.ipynb
├── data/
│   └── OpenSource_Papers_Coding_Schema_Data.xlsx
├── util/
│   └── util.py         # Contains the loadExcel function
└── README.md
│
└── requirement.txt
│
└── ORKG_Automate.PDF # Project info and requirement
```

---

## 🚀 Getting Started

### 📦 Requirements

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Pandas
- Numpy

Install dependencies if needed:

```bash
pip install -r requirements.txt

---

## 🧠 Function Overview

The `loadExcel` function in `util/util.py` provides the following interface:

```python
loadExcel(
    fileName,            # Path to Excel file (e.g., 'data/myfile.xlsx')
    sheet_name=0,        # Sheet index or name (default: first sheet)
    headerIndex=1,       # Row to use as DataFrame header
    dropHeader=[0,1,2],  # Rows to drop (e.g., title/info rows)
    verbose=True,        # Show logs in console
    log_file="load_excel.log",       # Log file name
    timestamp_logfile=True           # Add timestamp to log file name
)
```

---

## 📝 Example Usage in Notebook

```python
from util.util import loadExcel

df = loadExcel(
    "data/your_excel_file.xlsx",
    sheet_name="Sheet1",
    headerIndex=2,
    dropHeader=[0,1,2],
    verbose=True,
    log_file="logs/load_excel.log"
)
```

This will load the data, set proper headers, drop metadata rows, and create a timestamped log file.

---

## ✅ Features

- Interactive-friendly for notebooks
- Logs with timestamps for reproducibility
- Clean handling of messy Excel headers

---

## 📎 License

MIT License. Use freely and adapt to your project.

---

## 🤝 Contributions

Feel free to suggest improvements or report issues.
