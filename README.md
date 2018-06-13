<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

## Airbnb Clone Console

### Contents

#### [Description](https://github.com/MitaliSengupta/AirBnB_clone#description)
#### [Files in This Repository](https://github.com/MitaliSengupta/AirBnB_clone#files-in-this-repository)
#### [Usage](https://github.com/MitaliSengupta/AirBnB_clone#usage)
#### [Installation](https://github.com/MitaliSengupta/AirBnB_clone#installation)
#### [Example Usage](https://github.com/MitaliSengupta/AirBnB_clone#example-usage)
#### [Technologies Used](https://github.com/MitaliSengupta/AirBnB_clone#technologies-used)
#### [Authors](https://github.com/MitaliSengupta/AirBnB_clone#authors)
---

### Description
Over the course of the next few months, we at [Holberton School](https://www.holbertonschool.com/) will be creating a clone of the AirBnb application. This repository contains the code for one of the preliminary steps of this whole project: the console. As can be seen in the following image of the stack and architecture we will be using for this project, the console will serve as the core of the back-end side and will be written in Python. This console will connect directly to storage engines of which there will eventually be two: database and file storage. We focus on file storage in this particular instance.

<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step5.png" alt="Technology" width="629" height="335"></p>

This repository contains several packages that include the various models that will be employed in the application as objects, a file storage schema class, and various tests written using the unittest module of Python.

### Files in This Repository
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

### Usage

#### Basic Usage of The Console
---
| Command    | Usage                                     | Example                                           | Functionality                       |
|------------|-------------------------------------------|---------------------------------------------------|-------------------------------------|
| `help`     | `help`                                    | `help`                                            | displays a list of the commands     |
| `create`   | `create <class>`                          | `create User`                                     | creates a new instance of a class   |
| `show`     | `show <class> <id>`                       | `show User 123-123-123`                           | shows a specific instance           |
| `destroy`  | `destroy <class> <id>`                    | `destroy User 123-123-123`                        | deletes a specific instance         |
| `all`      | `all` or `all <class>`                    | `all User`                                        | shows all instances or a class      |
| `update`   | `update <class> <id> <attribute> <value>` | `update User 123-123-123 email 'hello@hello.com'` | updates an attribute of an instance |
| `count`    | `<class>.count`                           | `User.count`                                      | counts the number of instances      |
| `quit`     | `quit`                                    | `quit`                                            | quits the console                   |
---

#### Advanced Command Usage of The Console
---
| Command         | Usage                                          | Example Usage                                              |
|-----------------|------------------------------------------------|------------------------------------------------------------|
| `show`          | `<class>.show(<id>)`                           | `User.show(123-123-123)`                                   |
| `destroy`       | `<class>.destroy(<id>)`                        | `User.destroy(123-123-123)`                                |
| `all`           | `<class>.all`                                  | `User.all`                                                 |
| `update`        | `<class>.update(<id>, <attribute>, <value>)`   | `User.update(123-123-123, email, 'hello@hello.com')`       |
| `update` (dict) | `<class>.update(<id>, <dictionary>)`           | `User.update(123-123-123, {'email' : 'hello@hello.com'})`  |
---

### Installation
```
git clone git@github.com:MitaliSengupta/AirBnB_clone.git
```

### Example Usage

#### Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$
```
```
$ ./console.py
(hbnb) create BaseModel
5dccfbf9-03a6-45f7-8a75-80094392bf97
(hbnb) show BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97', 'updated_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549740), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699)}
(hbnb) all
[[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97', 'updated_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549740), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699)}]
(hbnb) BaseModel.count
1
(hbnb) update BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97 number 89
(hbnb) show BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}
(hbnb) create User
71e19890-6440-4ca9-9976-59ba61571f09
(hbnb) all
[[User] (71e19890-6440-4ca9-9976-59ba61571f09) {'id': '71e19890-6440-4ca9-9976-59ba61571f09', 'updated_at': datetime.datetime(2018, 6, 13, 23, 12, 39, 71568), 'created_at': datetime.datetime(2018, 6, 13, 23, 12, 39, 71532)}, [BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}]
(hbnb) destroy User 71e19890-6440-4ca9-9976-59ba61571f09
(hbnb) all
[[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}]
(hbnb) destroy BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
(hbnb) all
[]
(hbnb) quit
$
```

#### Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) $
$
$ echo "create BaseModel" | ./console.py
(hbnb) f09bfbad-532d-4bbe-a2c1-815b1958f01e
(hbnb) $
$ echo "all" | ./console.py
(hbnb) [[BaseModel] (f09bfbad-532d-4bbe-a2c1-815b1958f01e) {'id': 'f09bfbad-532d-4bbe-a2c1-815b1958f01e', 'updated_at': datetime.datetime(2018, 6, 13, 23, 16, 30, 420332), 'created_at': datetime.datetime(2018, 6, 13, 23, 16, 30, 420300)}]
(hbnb) $
$ echo "destroy BaseModel f09bfbad-532d-4bbe-a2c1-815b1958f01e" | ./console.py
(hbnb) (hbnb) $
$ echo "all" | ./console.py
(hbnb) []
(hbnb) $
$
```

### Technologies Used
* Language: Python3
* Operating System: Ubuntu 14.04 LTS (Trusty64)
* Style: PEP8 Ver. 1.7

### Authors

Mitali Sengupta - [Twitter: @aadhiBangalan](https://twitter.com/aadhiBangalan)

Derek Kwok - [Twitter: @dlangshk](https://twitter.com/dlangshk)