# Surprise Me! API
The purpose of the API is to return a surprising response, according to the parameters passed by the client.
The surprising response will be chosen from a list of surprising response types, each type has its own internal logic and conditions.

## Getting Started

The App Menu module displays the entire program.
it is associated with:
   ### 1) Surprise Module 
      #### (core of the program) (/api/surprise?name=Ryan%20Gosling&birth_year=1980)
        1.a) Surprise Module- Chuck Norris- randomize Chuck Norris joke
        1.b) Surprise Module- Kanye West- randomize Kanye West quote
        1.c) Surprise Module- num-sum- calculate the value of the username letters (a=1=A, b=2=B...)
        1.d) Surprise Module- Animals- Randomize an animal that the first char of it and the username are same
   ### 2) Stats
      #### dry stats on how many requests have been called (/api/stats)
   ### 3) Demographics
      #### calculations of stats as age of the users, their probably gender, percentiles etc... (api/demographics)
    
    

### Prerequisites

   1)Python3 \
   2) Python Modules \
   3) Internet Connection
          

### Installing

Installing python3

```
Open Terminal 
brew install python3 //OSX
python-3.8.0.exe InstallAllUsers=0 Include_launcher=0 Include_test=0SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite." //Windows
get-install python3 //linux
```

Installing Python packages-

```
Open Terminal
Navigate to the directory of SurpriseMe Projet-
   ~cd <path to the project directory>
Run SetUp.py (will install all the relevant modules)
   ~python3 SetUp.py

```



## Running the tests
```
Open Terminal
Navigate to the directory of SurpriseMe Projet
   ~cd <path to the project directory>
Run pytest 
   ~pytest Tests.py

```

## Running 

```
Open Terminal
Navigate to the directory of SurpriseMe Projet
   ~cd <path to the project directory>
Run App.py 
   ~python3 App.py
Browse to the server
   http://localhost:3000/api/<one of the following options>
      /api/surprise?name=<first name>%<last name>&birth_year=<year>
      /stats
      /demographics
repeat it
when you want to stop- ctrl+c 
```

## Integrate new Route
In case of updating that require new route- you need to integrate the next following steps:
``` Create the Route logic in a new module ``` \
``` Add to App.py- import the <new route module> and build function that call this class ``` \
``` Add Your own tests to tests.py file``` \
``` Add new modules if are needed to SetUp.py``` \

## Integrate new Surprise
In case of updating that require new surprise- you need to integrate the next following steps:
``` Create the Surprise in a new module ```\ 
``` Add to ChooseSurprise- Function that check all the condtions that are required to choose this surprise ```\
``` Add to SingleSurprise- 
         \t\t 1) import new surprise 
         \t\t 2) add class instance to DICT_SURPRISES
``` Add to Stats module to self.__dict.stats this class object and the type is needed```\
``` Add Your own tests to tests.py file```\
``` Add new modules if are needed to SetUp.py```\



## Authors

* **Noam Kesten** - *Interview work* - [Noam Kesten](https://github.com/kestennoam)


## License

This project is not licensed



