<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

### Airbnb Clone Console

#### Description
Over the course of the next few months, we at [Holberton School](https://www.holbertonschool.com/) will be creating a clone of the AirBnb application. This repository contains the code for one of the preliminary steps of this whole project: the console. As can be seen in the following image of the stack and architecture we will be using for this project, the console will serve as the core of the back-end side and will be written in Python. This console will connect directly to storage engines of which there will eventually be two: database and file storage. We focus on file storage in this particular instance.

<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step5.png" alt="Technology" width="42" height="22"></p>

This repository contains several packages that include the various models that will be employed in the application as objects, a file storage schema class, and various tests written using the unittest module of Python.

#### Files in This Repository
---
| File                   | File Hierarchy                                       | Description
|------------------------|------------------------------------------------------|--------------------------------------|
| `console.py`           | [console.py](console.py)                                        | The main console file                |
| `amenity.py`           | [models/amenity.py](models/amenity.py)                                  | The amenity subclass                 |
| `base_model.py`        | [models/base_model.py](models/base_model.py)                               | The base model superclass            |
| `city.py`              | [models/city.py](models/city.py)                                     | The city subclass                    |
| `place.py`             | [models/place.py](models/place.py)                                    | The place subclass                   |
| `review.py`            | [models/review.py](models/review.py)                                   | The review subclass                  |
| `state.py`             | [models/state.py](models/state.py)                                    | The state subclass                   |
| `user.py`              | [models/user.py](models/user.py)                                     | The user subclass                    |
| `file_storage.py`      | [models/engine/file_storage.py](models/engine/file_storage.py)                      | The file storage class               |
| `test_console.py`      | [tests/test_console.py](tests/test_console.py)                              | The unittest module for console      |
| `test_amenity.py`      | [tests/test_models/test_amenity.py](tests/test_models/test_amenity.py)                  | The unittest module for amenity      |
| `test_base_model.py`   | [tests/test_models/test_base_model.py](tests/test_models/test_base_model.py)               | The unittest module for base model   |
| `test_city.py`         | [tests/test_models/test_city.py](tests/test_models/test_city.py)                     | The unittest module for city         |
| `test_place.py`        | [tests/test_models/test_place.py](tests/test_models/test_place.py)                    | The unittest module for place        |
| `test_review.py`       | [tests/test_models/test_review.py](tests/test_models/test_review.py)                   | The unittest module for review       |
| `test_state.py`        | [tests/test_models/test_state.py](tests/test_models/test_state.py)                    | The unittest module for state        |
| `test_user.py`         | [tests/test_models/test_user.py](tests/test_models/test_user.py)                     | The unittest module for user         |
| `test_file_storage.py` | [tests/test_models/test_engine/test_file_storage.py](tests/test_models/test_engine/test_file_storage.py) | The unittest module for file storage |
---

#### Basic Usage of The Console
---
| Command    | Usage                                    | Example                                           | Functionality                       |
|------------|------------------------------------------|---------------------------------------------------|-------------------------------------|
| `help`     | `help`                                   | `help`                                            | displays a list of the commands     |
| `create`   | `create <class>`                         | `create User`                                     | creates a new instance of a class   |
| `show`     | `show <class> <id>`                      | `show User 123-123-123`                           | shows a specific instance           |
| `destroy`  | `destroy <class> <id>`                   | `destroy User 123-123-123`                        | deletes a specific instance         |
| `all`      | `all` or `all <class>`                   | `all User`                                        | shows all instances or a class      |
| `update`   | `update <class> <id> <attribute> <value> | `update User 123-123-123 email 'hello@hello.com'` | updates an attribute of an instance |
| `quit`     | `quit`                                   | `quit`                                            | quits the console                   |
---

#### Advanced Usage of The Console
---
| Command    | Usage                   | Functionality                    |
|------------|-------------------------|----------------------------------|
| `help`     |                         |                                  |
| `create`   |                         |                                  |
| `show`     |                         |                                  |
| `destroy`  |                         |                                  |
| `all`      |                         |                                  |
| `update`   |                         |                                  |
| `quit`     |                         |                                  |
| `EOF`      |                         |                                  |
---

#### Installation



#### Example Usage



### Technologies Used
* Language: Python3
* Operating System: Ubuntu 14.04 LTS (Trusty64)
* Style: PEP8 Ver. 1.7

### Authors
Mitali Sengupta
Derek Kwok