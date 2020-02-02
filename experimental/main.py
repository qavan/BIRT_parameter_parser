from bs4 import BeautifulSoup
from lxml import html
import re

def filter_empty(e):
    if len(str(e)) > 1:
        return e


def unhtml(x):
    s = re.sub(r'\<[^>]*\>', '', x)
    return s

birtFile = open("SalesInvoice.rptdesign.txt", 'r')
# birtFile = open("TopNPercent.rptdesign.txt", 'r')
# birtFile = open("cascade.rptdesign.xml", 'r')
# birtFile = open("main.py", 'r')
mainSoup = BeautifulSoup("".join(birtFile.readlines()), "lxml")
parameters = mainSoup.find('parameters')
if hasattr(parameters, "len"):
    parametersSoup = BeautifulSoup("".join([str(elem) for elem in parameters]), "lxml")
    scalarParameters = filter(filter_empty, [str(elem) for elem in parametersSoup.find('scalar-parameter')])
    scalarParametersSoup = BeautifulSoup("".join(scalarParameters), "lxml")
    # find_all("p", class_="")
    scalarParametersList = [None for x in range()]
    nameOf = scalarParametersSoup.find_all("text-property", attr={"name": "displayName"})
    descriptionOf = scalarParametersSoup.find_all("text-property", attr={"name": "helpText"})
    typeOf = scalarParametersSoup.find_all("property", attr={"name": "dataType"})
    formatOf = scalarParametersSoup.find_all("property", attr={"name": "format"})
    allowBlank = scalarParametersSoup.find_all("property", attr={"name": "allowBlank"})
    allowNull = scalarParametersSoup.find_all("property", attr={"name": "allowNull"})

    #  TODO EXTRACT BY CLASS FORMATTING
    for index, parameter in enumerate(scalarParameters):
        print("PRM", index, ": $", parameter[:28], "$ with len", len(parameter))
else:
    print("In report file no parameters.")
