[![Build Status](https://travis-ci.org/dennisdnyce/Questioner.svg?branch=develop)](https://travis-ci.org/dennisdnyce/Questioner)  [![Coverage Status](https://coveralls.io/repos/github/dennisdnyce/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/dennisdnyce/Questioner?branch=develop) [![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

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

### Implemented V1 Endpoints

| Endpoint       | Prefix     | Description     |
| :------------- | :----------: | -----------: |
| **[POST /auth/signup]**   | `/api/v1` | _signs up a user_ |
| **[GET /auth/users]**   | `/api/v1` | _retrieves all registered users_ |
| **[GET /auth/users/<int:userId>/]**   | `/api/v1` | _retrieves a single registered user_ |
|  **[POST /meetups]** | `/api/v1`   | _posts a meetup_    |
|**[GET /meetups/<int:meetupId>]**   | `/api/v1` | _retrieves a meetup_  |
| **[GET /meetups/upcoming]**   | `/api/v1` | _gets all upcoming meetups_ |
| **[POST /meetups/<int:meetupId>/questions]**   | `/api/v1` | _posts a meetup's question_ |
| **[POST /meetups/<int:meetupId>/rsvps]**   | `/api/v1` | _makes an RSVP to a meetup_ |
| **[PATCH /questions/<int:questionId>/upvote]**   | `/api/v1` | _upvotes a meetup question_ |
| **[PATCH /questions/<int:questionId>/downvote]**   | `/api/v1` | _downvotes a meetup question_ |

### Implemented V2 Endpoints

| Endpoint       | Prefix     | Description     |
| :------------- | :----------: | -----------: |
| **[POST /auth/signup]**   | `/api/v2` | _signs up a user_ |
| **[POST /auth/login]**   | `/api/v2` | _logs in a user_ |
| **[GET /auth/users]**   | `/api/v2` | _retrieves registered users_ |
| **[GET /auth/users/<int:userId>/]**   | `/api/v2` | _retrieves a single registered user_ |
|  **[POST /meetups]** | `/api/v2`   | _posts a meetup_    |
|  **[GET /meetups/<int:meetupId>]**  | `/api/v2` | _retrieves a meetup_  |
|**[DELETE /meetups/<int:meetupId>]**   | `/api/v2` | _deletes a meetup_  |
| **[GET /meetups/upcoming]**   | `/api/v2` | _Gets all upcoming meetups_ |
| **[POST /meetups/<int:meetupId>/questions]**   | `/api/v2` | _posts a meetup's question_ |
| **[POST /meetups/<int:meetupId>/rsvps]**   | `/api/v2` | _makes an RSVP to a meetup_ |
| **[PATCH /questions/<int:questionId>/upvote]**   | `/api/v2` | _upvotes a meetup question_ |
| **[PATCH /questions/<int:questionId>/downvote]**   | `/api/v2` | _downvotes a meetup question_ |
| **[POST /meetups/<int:meetupId>/questions/<int:questionId>/comments]**   | `/api/v2` | _post a comment_ |


### Prerequisites
The things you need to setup the project and its relevant configuration.

```
1. Python3
2. Flask Microframework
3. Postman for testing the API endpoints

```
### Installation


`step 1: git clone` http://github.com/dennisdnyce/Questioner.git
```
step 2: _cd Questioner_
step 3: git checkout develop
step 4: install dependencies :~$ sudo apt install python-pip
step 5: install virtualenv :~$ sudo pip install virtualenv
step 6: create a virtual environment :~$ virtualenv myvenv
step 7: activate the virtual environment :~$ source myvenv/bin/activate
step 8: install project dependencies :~$(myenv) pip install -r requirements.txt
step 9: set up the project running environment from your terminal
                           :~$(myenv)export FLASK_ENV = development
                           :~$(myenv)export FLASK_DEBUG = 1
                           :~$(myenv)export FLASK_APP = run.py
step 10: run the project :~$(myenv)flask run  
Finaly, test the endpoints on Postman                                        
```
## Running Tests
```
- pytest :~$(myenv)py.test --cov app/ tests/

- checking test coverage :~$(myenv)coverage report -m

```

## Authors

* **Dennis Juma**

## Acknowledgments

* The Almighty for the awesome gift of life
* Andela-Nairobi Cycle-36 Cohorts
* Endless Motivation from family and friends

## Licence
The Questioner project is licenced under the <a href="https://opensource.org/licenses/MIT" target="_blank">MIT</a> licence
