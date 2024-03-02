#<<--Archivo para leer los datos de los paises del mundo-->>#
import csv


def readData(path):  #Funcion para leer los datos
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    data = []
    for row in reader:
      i = zip(header, row)
      countryDict = {key: value for key, value in i}
      data.append(countryDict)

    return data


def filterCountry(data, country):  #Funcion para filtrar el pais
  result = ""  #Solo para evitar errores
  try:
    result = list(
        filter(lambda item: item["Country/Territory"] == country, data))
  except:
    print("Ese pais no esta en la lista")

  return result


def filterPopulation(country):
  population = {}
  populationKeys = []
  populationValues = []

  try:
    for key, value in country[0].items():
      if "Population" in key:
        population[key] = (value)
    populationKeys = list(population.keys())
    populationValues = list(population.values())

    populationKeys.pop()
    populationValues.pop()
  except:
    print("Error 404, informacion no encontrada")

  return populationKeys, populationValues


countries = readData("data.csv")
country = filterCountry(countries, "Colombia")
pKeys, pValues = filterPopulation(country)

pKeys.reverse()
pValues.reverse()

for item in range(len(pValues)):
  pValues[item] = int(pValues[item])
