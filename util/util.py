import pandas as pd
import matplotlib.pyplot as plt

def loadExcel(fileName, sheetName=0,  headerIndex = 1, dropHeader=[0,1,2]):
    """
    Loads an Excel file and returns a cleaned DataFrame.

    Parameters:
    ----------
    fileName : str
        The path to the Excel file.
    sheet_name : int or str, optional (default=0)
        The sheet to read. Can be the sheet name or index.
    headerIndex : int, optional (default=1)
        The row index to use as column headers (0-based).
    dropHeader : list of int, optional (default=[0, 1, 2])
        A list of row indices to drop from the DataFrame (typically header rows above the actual data).

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with updated column headers and specified rows dropped.
    """
    
    df = pd.read_excel(fileName, sheet_name=sheetName, header= None)
    df.columns = df.iloc[headerIndex]
    dfNew = df.drop(index = dropHeader).reset_index(drop=True)
    return dfNew