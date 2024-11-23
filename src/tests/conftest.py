import pytest
import pandas as pd

@pytest.fixture
def mock_excel_data():
    """
    Mockovaná data pro testování. 
    Simulují dva listy v Excel souboru.
    """
    sheet1 = pd.DataFrame({
        0: ['Praha', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
        1: ['Brno', '*', 7, 8, None, None, None, None, None, None, None, None],
        2: ['Ostrava', 9, '10', '11', None, None, None, None, None, None, None, None]
    })
    sheet2 = pd.DataFrame({
        0: ['Ústí', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
        1: ['Zlín', '*', 7, 8, None, None, None, None, None, None, None, None],
        2: ['Olomouc', 9, '10', '11', None, None, None, None, None, None, None, None]
    })
    return {
        "sheet_2021": sheet1,
        "sheet_2022": sheet2
    }
