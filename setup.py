from setuptools import setup

setup(name='dev_aberto_joaopmjm',
      version='0.1',
      packages=['dev_aberto'],
      install_requires=[
            'requests'
      ],
      scripts=[
            'scripts/hello.py'
      ],
      author='Joao Pedro Montefeltro Junqueira Meirelles',
      author_email='joaopmjm@al.insper.edu.br'
)
