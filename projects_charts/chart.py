#<<--Grafica de la poblacion del pais elegido-->>#
import matplotlib.pyplot as plt
import read as data


def generateBarChart(labels, values):
  plt.bar(labels, values)
  plt.xlabel("Año")
  plt.ylabel("Poblacion")
  plt.title("Grafica de poblacion")
  plt.yticks(range(10000000, 70000000, 10000000),
             ['10M', '20M', '30M', '40M', '50M', '60M'])
  plt.savefig("result.png")


if __name__ == "__main__":
  generateBarChart(data.pKeys, data.pValues)
