from setuptools import setup

setup(name='cbpi4-TeleNotify',
      version='0.0.1',
      description='CraftBeerPi Plugin',
      author='Guy Lev',
      author_email='',
      url='https://github.com/madhatguy/cbpi4-TeleNotify',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.yaml'],
      'cbpi4-TeleNotify': ['*.yaml']},
      packages=['cbpi4-TeleNotify'],
     )
