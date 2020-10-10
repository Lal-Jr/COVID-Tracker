from covid import Covid
import matplotlib.pyplot as pyplot
country = input("Enter Country Name : ")
covid = Covid()
data = covid.get_status_by_country_name(country)
cadr = {
    key: data[key]
    for key in data.keys
}
