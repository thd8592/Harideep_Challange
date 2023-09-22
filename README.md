# Harideep_Challange
For SED Challange 2

# JSON Transformer

This Python script transforms a schema-less JSON input into a desired output following specific transformation criteria. The input JSON may contain various data types and keys with leading/trailing whitespace, and the script sanitizes the data, transforms it, and omits invalid fields to generate the desired output.

## Usage

1. Clone the repository:

   ```bash
   git clone <repository-url>

Navigate to the directory containing the script:
cd <repository-directory>

Open the json_transformer.py script in a text editor and replace the input_json variable with your actual input JSON data.

Run the script:
python3 json_transformer.py

The script will print the transformed JSON to the console.

Transformation Criteria

    All Nth level values in the input are represented as Strings with pertinent data type information.

JSON Field Keys

    Keys are sanitized to remove trailing and leading whitespace.

Data Types

    S represents the String data type.
        Transforms value to the String data type.
        Sanitizes the value of trailing and leading whitespace.
        Transforms RFC3339 formatted Strings to Unix Epoch in Numeric data type.
        Omits fields with empty values.

    N represents the Number data type.
        Transforms to the relevant Numeric data type.
        Sanitizes the value of trailing and leading whitespace.
        Strips leading zeros.
        Omits fields with invalid Numeric values.

    BOOL represents the Boolean data type.
        Transforms to the Boolean data type.
        Transforms 1, t, T, TRUE, true, or True to true.
        Transforms 0, f, F, FALSE, false, or False to false.
        Sanitizes the value of trailing and leading whitespace.
        Omits fields with invalid Boolean values.

    NULL represents the Null data type.
        Represents null when the value is 1, t, T, TRUE, true, or True.
        Omits the field when the value is 0, f, F, FALSE, false, or False.
        Sanitizes the value of trailing and leading whitespace.
        Omits fields with invalid Boolean values.

    L represents the List data type.
        Transforms into appropriate data types.
        Does not contain empty Strings.
        Maintains the input order.
        Omits fields with unsupported data types.
        Omits fields with empty List.
        May contain duplicates.

    M represents the Map data type.
        Adheres to all data type criteria.
        Lexically sorted.
        Omits fields with empty Map.
