"""
In case we have encoded the complex number into JSON Object as list, it will not be possible
 to decoded or convert to pyth complex datatype
 In this example we want to encode and decode complex and datetime
JSON Object below:

 {
    "signal": {
        "place": "Uppsala",
        "stamp": {
            "__class": "datetime",
            "y": 2025,
            "month": 4,
            "d": 19,
            "h": 16,
            "minute": 23,
            "s": 51
        },
        "samples:": [
            {
                "__class": "complex",
                "real": -2.0,
                "imag": 5.0
            },
            {
                "__class": "complex",
                "real": 3.0,
                "imag": 1.0
            },
            {
                "__class": "complex",
                "real": 2.0,
                "imag": 5.0
            }
        ]
    }
}


You can see the samples is a list of complex numbers and we have stamps
Use the examples in the previous files (module)  to Decode and Encode the above JSON file
You can see the Python object structure below.
Try to debug your result so you can inspect and see how dictionary is format from the JSON object String
"""

import json
from datetime import datetime


class Signal:
    def __init__(self, _place: str, _stamp: datetime, _samples: list[complex]):
        self._place = _place
        self._stamp = _stamp
        self._samples = _samples

    @property
    def place(self):
        return self._place

    @property
    def stamp(self):
        return self.stamp

    @property
    def samples(self):
        return self._samples


class ComplexDateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {"__class": "complex", "real": obj.real, "imag": obj.imag}
        if isinstance(obj, datetime):
            return {
                "__class": "datetime",
                "y": obj.year,
                "month": obj.month,
                "d": obj.day,
                "h": obj.hour,
                "minute": obj.minute,
                "s": obj.second,
            }
        # In case we don't have complex object; let the base c lass default method raise the TypeError
        return super().default(obj)


def decode_data_complex(dic):
    if dic.get("__class") == "complex":
        return complex(dic.get("real"), dic.get("imag"))
    if dic.get("__class") == "datetime":
        return datetime(
            dic["y"], dic["month"], dic["d"], dic["h"], dic["minute"], dic["s"]
        )
    return dic


data = """{
    "signal": {
        "place": "Uppsala",
        "stamp": {
            "__class": "datetime",
            "y": 2025,
            "month": 4,
            "d": 19,
            "h": 16,
            "minute": 23,
            "s": 51
        },
        "samples": [
            {
                "__class": "complex",
                "real": -2.0,
                "imag": 5.0
            },
            {
                "__class": "complex",
                "real": 3.0,
                "imag": 1.0
            },
            {
                "__class": "complex",
                "real": 2.0,
                "imag": 5.0
            }
        ]
    }
}"""
decoddata = json.loads(data, object_hook=decode_data_complex)
print(type(decoddata))
print(decoddata)

jsondata = json.dumps(decoddata, cls=ComplexDateEncoder)
print(type(jsondata))
print(jsondata)
