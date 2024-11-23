import pandas as pd
from src.constants.constants_salaries_data import HEADER_NAMES_SALARIES, EXCEL_FILE_NAME_SALARIES

class MzdyData:
    def __init__(self, excel_file) -> None:
        """
        Načte Excel soubor se mzdami a upraví jej
        :param excel_file: Cesta k Excel souboru
        """
        self.excel_file = excel_file
        self.dataframes = {} 
        self.header = HEADER_NAMES_SALARIES
        self.sheets = self._load_sheets()

    def _load_sheets(self) -> dict:
        """
        Načte všechny listy z Excel souboru.
        :return: Slovník s názvy listů a jejich obsahem jako DataFrame
        """
        return pd.read_excel(self.excel_file, sheet_name=None, header=None)
    
    def _replace_star_with_null(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Nahradí '*' hodnoty v daném DataFrame za NULL (NaN).
        :param df: DataFrame, na kterém má být operace provedena
        :return: Upravený DataFrame
        """
        return df.replace('*', pd.NA)
    
    def _combine_dataframes(self) -> pd.DataFrame:
        """
        Spojí všechny DataFrames do jednoho DataFrame (union).
        :return: Spojený DataFrame
        """
        combined_df = pd.concat(self.dataframes.values(), ignore_index=True)
        return combined_df
    

    def process_adjustments(self) -> pd.DataFrame:
        """
        Hlavní metoda, která orchestruje všechny updates
        :return: vrací finální df
        """
        for sheet_name, df in self.sheets.items():
            df.columns = self.header 
            year = sheet_name.split('_')[-1] 
            df['Rok'] = year
            self.dataframes[sheet_name] = df 
        combined_df = self._combine_dataframes()
        final_df = self._replace_star_with_null(combined_df)
        return final_df

if __name__ == "__main__":
    mzdy_data = MzdyData(EXCEL_FILE_NAME_SALARIES)
    final_df = mzdy_data.process_adjustments()
