from app.salaries_data_preprocessing import MzdyData

from unittest.mock import patch
from src.tests.constants import TEST_HEADER_NAMES_SALARIES, TEST_YEAR_1, TEST_YEAR_2

import pandas as pd
from pandas.testing import assert_frame_equal

@patch("pandas.read_excel")
def test_process_adjustments(mock_read_excel, mock_excel_data) -> None:
    """
    Testuje hlavní metodu process_adjustments, která orchestruje preprocessing.
    """
    mock_read_excel.return_value = mock_excel_data
    mzdy_data = MzdyData(excel_file="mock_path.xlsx")
    mzdy_data.header = TEST_HEADER_NAMES_SALARIES 
    final_df = mzdy_data.process_adjustments()
    assert all(final_df.columns == TEST_HEADER_NAMES_SALARIES + ["Rok"])
    assert final_df['Rok'].iloc[0] == TEST_YEAR_1
    assert final_df['Rok'].iloc[-1] == TEST_YEAR_2
    