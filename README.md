# PDF Field Extractor

A Python script that extracts filled form field data from PDF documents and exports it to XML format.

## Features

- Extracts all interactive form fields from a PDF
- Outputs clean, well-formatted XML
- Auto-generates output filename from input filename
- Handles both filled and empty fields

## Prerequisites

- Python 3.7+
- [`pypdf`](https://pypi.org/project/pypdf/) library

Install the dependency:

```bash
pip install pypdf
```

## Usage

### Command Line

```bash
python export_xml.py <input_pdf> [output_xml]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `input_pdf` | Yes | Path to the source PDF file |
| `output_xml` | No | Path for the output XML file. If omitted, a file with the same name as the PDF will be created in the same directory |

### Examples

```bash
# Generate output.xml next to the input file
python export_xml.py form.pdf

# Specify custom output path
python export_xml.py form.pdf data/output.xml
```

### Output Format

The script produces an XML file with the following structure:

```xml
<?xml version='1.0' encoding='utf-8'?>
<FormData>
  <FieldName1>value</FieldName1>
  <FieldName2>value</FieldName2>
  ...
</FormData>
```

Only fields with values are included in the output. Empty fields are skipped.

## Building the Standalone Executable

An `export_xml.exe` is provided for Windows users who do not have Python installed.

```bash
export_xml.exe <input_pdf> [output_xml]
```

## Notes

- The script uses `pypdf` to parse PDF AcroForm fields. It works with standard fillable PDF forms.
- PDF values are stripped of their leading `/` character (a pypdf convention for PDF string objects).
- If the input PDF has no fillable form fields, the output will contain an empty `<FormData></FormData>` element.
