import yaml

from jinja2 import Environment, FileSystemLoader

if __name__== "__main__":

	with open("both.yaml", mode='r') as f:
		content = f.read()
	
	with open(('config-4.yaml'), 'x') as f:
		f.write(content.replace('{{ id }}', '4'))
