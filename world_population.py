import json
from country_codes import get_country_code

filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)
	
	for pop_dic in pop_data:
		if pop_dic['Year'] == '2010':
			country_name = pop_dic['Country Name']
			population = int(float(pop_dic['Value']))
			code = get_country_code(country_name)
			if code:
				print(code + " : " + str(population))
			else:
				print('Error - ' + country_name)
			
