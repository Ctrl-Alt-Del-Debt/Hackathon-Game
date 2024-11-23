import pandas as pd

#formátování zobrazení pandas
pd.options.display.float_format = '{:.2f}'.format

#zpracování csv data
def process_csv(csv_file_name: str) -> pd.DataFrame:
    """
    Takes in csv file that includes Date and Close column
    and returns dataframe with year and avg value per year.
    """
    df = pd.read_csv(csv_file_name)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df = df[["Year", "Close"]]
    result_df = df.groupby("Year", as_index = False).mean()
    return result_df

#rozšíření dataframu o future values
def extend_values(csv_file_name: str, years_to_extend: int, drop_rate: float, rate_freq: int) -> pd.DataFrame:
    """
    Takes a csv file name with Date and Close columns.
    Extends the dataset by set numnber of years depending on avg
    yearly return. Allows to set a drop of value (to add risk aspect)
    on set frequency. If no drop is desired set drop_rate to 0.
    Returns extended dataframe with original and new data.
    """
    df = process_csv(csv_file_name)
    df = df.sort_values("Year").reset_index(drop = True)#seřazení dat
    df["Growth"] = df["Close"].pct_change() * 100       #sloupec na % změnu
    avg_growth = df["Growth"].mean()                    #průměrný růst
    last_year = df["Year"].iloc[-1]                     #poslední rok
    last_close = df["Close"].iloc[-1]                   #poslední close hodnota
    new_years = []                                      #list na nové roky
    new_values = []                                     #list na nové hodnoty

    for i in range(1, years_to_extend):
        next_year = last_year + i                                   #jaký rok počítá
        next_close = last_close * (1 + (avg_growth/i)/100)          #jaká je nová hodnota + dělení počtem iterací na srovnání křivky růstu
        if i % rate_freq == 0:
            next_close = last_close - (last_close * drop_rate)      #cena padne o x% jednou za x let
        new_years.append(next_year)                                 #nový rok do listu
        new_values.append(round(next_close, 2))                     #nový hodnota do listu
        last_close = next_close                                     #nová hodnota pro poslední rok
    new_data = pd.DataFrame({"Year": new_years, "Close": new_values})                     #nová data
    final_data = pd.concat([df[["Year", "Close"]], new_data], ignore_index = True)  #spojení starých a nových dat
    return final_data

#přidání sloupce procentuální změny
def add_perc_change(df: pd.DataFrame) -> pd.DataFrame:
    """
    Takes in df create by process_csv() or extende_values()
    and returns df with added column showing year on year percentage diff.
    """
    df = df.sort_values("Year").reset_index(drop = True)        #seřadí df
    df["Perc YoY diff"] = df["Close"].pct_change() * 100        #přidá sloupec pomocí fce pct_change()
    return df

#changing initial year
def set_initial_year(df: pd.DataFrame, init_year: int) -> pd.DataFrame:
    """
    Takes in df that has Year columns and sets starting year
    as needed.
    """
    min_year = df["Year"].min()
    df["Year"] = df["Year"] - min_year + init_year
    return df

spx_data = set_initial_year(add_perc_change(process_csv("SPX.csv")), 2006)
btc_data = set_initial_year(add_perc_change(extend_values("BTC-USD.csv", 80, 0.15, 8)), 2006)
us_gen_bonds_data = set_initial_year(add_perc_change(extend_values("US_Gen_TR.csv", 50, 0.025, 15)), 2006)
em_gen_bonds_data = set_initial_year(add_perc_change(extend_values("EM_Gen_TR.csv", 70, 0.05, 25)), 2006)
emea_gen_bonds_data = set_initial_year(add_perc_change(extend_values("EMEA_Gen_TR.csv", 70, 0.05, 25)), 2006)