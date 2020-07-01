# Surprise Me! API
The purpose of the API is to return a surprising response, according to the parameters passed by the client.
The surprising response will be chosen from a list of surprising response types, each type has its own internal logic and conditions.

## Getting Started

The App Menu module displays the entire program.
it is associated with:
   ### 1) Surprise Module (core of the program) (/api/surprise?name=Ryan%20Gosling&birth_year=1980)
        1.a) Surprise Module- Chuck Norris- randomize Chuck Norris joke
        1.b) Surprise Module- Kanye West- randomize Kanye West quote
        1.c) Surprise Module- num-sum- calculate the value of the username letters (a=1=A, b=2=B...)
        1.d) Surprise Module- Animals- Randomize an animal that the first char of it and the username are same
   ### 2) Stats- dry stats on how many requests have been called (/api/stats)
   ### 3) Demographics- calculations stats as age of the users, their probably gender, percentiles etc... (api/demographics)
    
    

### Prerequisites

1)Python3 
2) Python Modules-  
              bottle
              requests
              json
              datetime
              numpy
3) Internet Connection
          

### Installing

Installing python

```
Open Terminal
brew install python3 //OSX
python-3.8.0.exe InstallAllUsers=0 Include_launcher=0 Include_test=0
    SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite." //Windows
get-install python3
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

