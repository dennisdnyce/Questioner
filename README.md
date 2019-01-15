[![Build Status](https://travis-ci.org/dennisdnyce/Questioner.svg?branch=develop)](https://travis-ci.org/dennisdnyce/Questioner)  [![Coverage Status](https://coveralls.io/repos/github/dennisdnyce/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/dennisdnyce/Questioner?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  [![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

# QuestionerAPI
Questioner is a mock of a meetup platform where any user is allowed to register for an account and pose questions on scheduled meetups by an admin user that he/she is interested in attending or nonetheless, comment on posted questions relating to meetups. The more a meetup question is upvoted, the more it qualifies to be objectified during the meetup. An admin user can create and delete meetups and a regular user can pose questions on posted meetups and schedule to attend the meetup if possible.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Watch out for the deployment notes on how to deploy the project on a live system.

### NOTE
- The project's normal user UI can be found here <a href="https://dennisdnyce.github.io/Questioner/UI/" target="_blank">gh-pages</a>
- The project's admin user UI can be found here <a href="https://dennisdnyce.github.io/Questioner/UI/admin" target="_blank">admin gh-pages</a>
- The project is managed by the PivotalTracker software management platform, preview it at <a href="https://www.pivotaltracker.com/n/projects/2235504" target="_blank">PivotalTracker</a>
- The app is hosted on <a href="https://jumaquestioner.herokuapp.com/" target="_blank">Heroku</a>
- The project documentation can be found <a href="https://documenter.getpostman.com/view/6005626/RznJmcEC" target="_blank">Here</a>

### Implemented Endpoints

- [POST /meetups]
- [GET /meetups/<int:meetupId>]
- [GET /meetups/upcoming]

- [POST /meetups/<int:meetupId>/questions]

- [POST /meetups/<int:meetupId>/rsvps]

- [PATCH /questions/<int:questionId>/upvote]
- [PATCH /questions/<int:questionId>/downvote]

- [POST /auth/signup]
- [GET /auth/users]
- [GET /auth/users/<int:userId>]


### Prerequisites
The things you need to setup the project and its relevant configuration.

```
1. Python3
2. Flask Microframework
3. Postman for testing the API endpoints

```
### Installation

```
- git clone http://github.com/dennisdnyce/Questioner.git
- cd Questioner
- git checkout develop
- install dependencies :~$ sudo apt install python-pip
- install virtualenv :~$ sudo pip install virtualenv
- create a virtual environment :~$ virtualenv myvenv
- activate the virtual environment :~$ source myvenv/bin/activate
- install project dependencies :~$(myenv) pip install -r requirements.txt
- set up the project running environment :~$(myenv)export FLASK_ENV = development
                                         :~$(myenv)export FLASK_DEBUG = 1
                                         :~$(myenv)export FLASK_APP = run.py
- run the project :~$(myenv)flask run  

-test endpoints on Postman                                        
```
## Running Tests
```
- pytest :~$(myenv)py.test --cov app/ tests/

- checking test coverage :~$(myenv)coverage report -m
```

## Contributing
> To get Started...

### Step 1
- **Option 1**

      - 🍴 Fork this repo!

- **Option 2**   

      - 👯 Clone this repo to your local machine using `https://github.com/dennisdnyce/Questioner.git`

### Step 2
- **Hack away with one of your branches or you can use one of my many branches.**

### Step 3
- 🔃 Create a new pull request using <a href="https://github.com/dennisdnyce/Questioner/compare/" target="_blank">`https://github.com/dennisdnyce/Questioner/compare/`</a>.

## Authors

* **Dennis Juma**

## Acknowledgments

* The Almighty for the awesome gift of life
* Andela-Nairobi Cycle-36 Cohorts
* A Hat tip to anyone whose code was referenced
* Endless Motivation from family and friends

## Licence
The Questioner project is licenced under the <a href="https://opensource.org/licenses/MIT" target="_blank">MIT</a> licence
