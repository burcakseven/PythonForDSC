from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def draw_my_country(myCampuse: str, dataset: pd.DataFrame):
    country_data = dataset[dataset['country'] == myCampuse]

    year = [col for col in dataset.columns if col.isnumeric()]
    print(year,country_data[year])
    selected_years = year[::40]
    plt.plot(year,country_data[year].values[0])
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.xticks(country_data[selected_years].columns)
    plt.title(myCampuse + ' Life Expectancy Projects')
    plt.show()

def main():
    myCampuse = 'Turkey'
    dataset = load('/Users/burcakseven/Desktop/PythonForDSC/DataTable/Draw My Country/life_expectancy_years.csv')
    draw_my_country(myCampuse,dataset)

if __name__ == '__main__':
    main()