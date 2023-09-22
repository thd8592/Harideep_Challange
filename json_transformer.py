import json_transformer  
import json
from datetime import datetime

def sanitize_key(key):
    return key.strip()

def transform_string(value):
    value = value.strip()
    if value.startswith("RFC3339"):
        try:
            date_str = value.split(" ")[1]
            date_obj = datetime.fromisoformat(date_str)
            return int(date_obj.timestamp())
        except ValueError:
            return None
    return value

def transform_number(value):
    value = value.strip().lstrip('0')  # Remove leading zeros
    try:
        return int(value) if value.isnumeric() else float(value)
    except ValueError:
        return None

def transform_boolean(value):
    value = value.strip().lower()
    if value in ["1", "t", "true"]:
        return True
    elif value in ["0", "f", "false"]:
        return False
    else:
        return None

def transform_null(value):
    value = value.strip().lower()
    if value in ["1", "t", "true"]:
        return None
    return None

def transform_list(value):
    if not isinstance(value, list):
        return None
    transformed_list = []
    for item in value:
        if isinstance(item, str) and item.strip() != "":
            transformed_value = transform_value(item)
            if transformed_value is not None:
                transformed_list.append(transformed_value)
    return transformed_list

def transform_map(value):
    if not isinstance(value, dict):
        return None
    transformed_map = {}
    for key, item in value.items():
        sanitized_key = sanitize_key(key)
        transformed_value = transform_value(next(iter(item.values())))
        if sanitized_key and transformed_value is not None:
            transformed_map[sanitized_key] = transformed_value
    return transformed_map

def transform_value(value):
    if isinstance(value, str):
        return transform_string(value)
    elif isinstance(value, list):
        return transform_list(value)
    elif isinstance(value, dict):
        return transform_map(value)
    else:
        return None

def main(input_json):
    try:
        input_data = json.loads(input_json)
    except ValueError:
        return "Invalid input JSON"

    transformed_data = []
    for key, value in input_data.items():
        sanitized_key = sanitize_key(key)
        transformed_value = transform_value(next(iter(value.values())))
        if sanitized_key and transformed_value is not None:
            transformed_data.append({sanitized_key: transformed_value})

    return json.dumps(transformed_data, indent=2)

# Input JSON
input_json = '''
{
  "number_1": {
    "N": "1.50"
  },
  "string_1": {
    "S": "784498 "
  },
  "string_2": {
    "S": "2014-07-16T20:55:46Z"
  },
  "map_1": {
    "M": {
      "bool_1": {
        "BOOL": "truthy"
      },
      "null_1": {
        "NULL ": "true"
      },
      "list_1": {
        "L": [
          {
            "S": ""
          },
          {
            "N": "011"
          },
          {
            "N": "5215s"
          },
          {
            "BOOL": "f"
          },
          {
            "NULL": "0"
          }
        ]
      }
    }
  },
  "list_2": {
    "L": "noop"
  },
  "list_3": {
    "L": [
      "noop"
    ]
  },
  "": {
    "S": "noop"
  }
}
'''

# Output the transformed JSON
output_json = main(input_json)
print(output_json)
