import matplotlib.pyplot as plt
import numpy as np
from load_csv import load
import pandas as pd

def pair_the_datas(year: int, df_gdp, df_life_expec):
    # gdp_1900 = df_gdp[['country','1900']].rename(columns={'1900':'gdp_90'})
    # life_expec_1900 = df_life_expec[['country','1900']].rename(columns={'1900':'life_ex_90'})
    # total_df = gdp_1900.merge(life_expec_1900, left_on= 'country', right_on= 'country')
    plt.scatter(df_gdp['1900'],df_life_expec['1900'])
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.legend()
    plt.title('1900')
    plt.show()
    # total_df.plot(total_df[''])
    


def main():
    df_gdp = load('/Users/burcakseven/Desktop/PythonForDSC/DataTable/Draw Year/income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df_life_expec = load('/Users/burcakseven/Desktop/PythonForDSC/DataTable/Draw Year/life_expectancy_years.csv')
    pair_the_datas(1900,df_gdp,df_life_expec)


if __name__ == '__main__':
    main()