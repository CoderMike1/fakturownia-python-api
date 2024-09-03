from setuptools import setup, find_packages

setup(
    name='fakturowniaAPI',  # nazwa pakietu
    version='0.1',  # wersja pakietu
    #author='Twoje Imię',  # autor pakietu
    #author_email='twojemail@example.com',  # e-mail autora
    description='python api',  # krótki opis
    long_description=open('README.md').read(),  # dłuższy opis (np. z README)
    long_description_content_type='text/markdown',
    #url='https://github.com/twojprofil/mypackage',  # link do repozytorium (opcjonalnie)
    packages=find_packages(),  # automatycznie znajdź wszystkie pakiety
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  # wymagania dotyczące wersji Pythona
    install_requires=[
        # tutaj możesz dodać zależności, np. 'requests', 'numpy'
    ],
)