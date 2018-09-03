import sys

"""
When running locally, meaning non-AWS, use the new Python3.7 DataClasses.  When running on AWS, which requires
Python3.6, use NamedTuples.

"""


python_version = sys.version_info

if python_version[0] == 3 and python_version[1] == 7:
    print("*** Using Python3.7 DataClasses for models")
    from dataclasses import dataclass
    import json

    @dataclass
    class UserModel:
        username: str
        password: str

        def __str__(self):
            return json.dumps({"username": self.username, "password": self.password})
else:
    print("*** Using Python3.6 NamedTuples for models")
    from collections import namedtuple

    UserModel = namedtuple('UserModel', ['username', 'password'])
