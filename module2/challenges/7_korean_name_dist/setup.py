from setuptools import setup


setup(
	name='korean_name',
	version='1.0.0',
	description='Your name in korean',
	author='Jose Antonio Cerván García',
	url='https://github.com/josecervan/Korean-Name-Generator',
	packages=[
		'korean_name',
		'korean_name.back',
		'korean_name.data',
		'korean_name.front.pages'
	],
	package_dir={'korean_name': 'korean_name'}
)