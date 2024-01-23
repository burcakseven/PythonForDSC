from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def compare_my_country(comparedCampuse,myCampuse: str, dataset: pd.DataFrame):
    country_data = dataset[dataset['country'] == myCampuse]
    compare_my_country = dataset[dataset['country'] == comparedCampuse]

    year = [col for col in dataset.columns if col.isnumeric() and int(col) <= 2050 and int(col) >= 1800]
    selected_years = year[::40]

    plt.plot(year,country_data[year].values[0])
    plt.plot(year,compare_my_country[year].values[0])

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(country_data[selected_years].columns)
    plt.title(' Population Projects')
    plt.show()

def main():
    comparedCampuse = 'Brazil'
    myCampuse = 'France'
    dataset = load('/Users/burcakseven/Desktop/PythonForDSC/DataTable/Compare/population_total.csv')
    compare_my_country(comparedCampuse,myCampuse,dataset)

if __name__ == '__main__':
    main()