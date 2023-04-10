import utils
import read_csv
import charts
import pandas as pd


def run():
  '''
  
  data = list(filter(lambda x : x['Continent'] == 'South America', data))
  countries = list(map(lambda x : x['Country/Territory'], data))
  percentage = list(map(lambda x : x['World Population Percentage'], data))
 
  
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentage = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentage)

  data = read_csv.read_csv('data.csv')
  country = input('Indicame un pais del mundo ')
  country = country.capitalize()
  
  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  

  
  

  print(result)

  
  
if __name__ == '__main__':
  run()

#ese ultimo if es el que permite que main pueda ejecutarse como scrip desde la terminal o como modulo desde otro archivo sin problemas