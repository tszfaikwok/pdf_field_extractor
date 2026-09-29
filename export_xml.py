import os
import sys
import xml.etree.ElementTree as ET
from pypdf import PdfReader


def main():
    # 1. Determine Input and Output File Paths from Arguments
    if len(sys.argv) >= 3:
        input_pdf = sys.argv[1]
        output_xml = sys.argv[2]
    elif len(sys.argv) == 2:
        input_pdf = sys.argv[1]
        # Auto-generate XML name based on input filename if not specified
        base_name = os.path.splitext(input_pdf)[0]
        output_xml = f"{base_name}.xml"
    else:
        # Default fallback if no arguments are provided
        input_pdf = "your_filled_form.pdf"
        output_xml = "output_data.xml"

    # 2. Check if Input File Exists
    if not os.path.exists(input_pdf):
        print(
            f"Error: Could not find input file '{input_pdf}'", file=sys.stderr
        )
        sys.exit(1)

    try:
        # 3. Read PDF Form Fields
        reader = PdfReader(input_pdf)
        fields = reader.get_fields()

        # 4. Construct XML Tree
        root = ET.Element("FormData")

        if fields:
            for field_name, field_data in fields.items():
                value = field_data.get("/V", "")
                if value:
                    value = str(value).lstrip("/")

                child = ET.SubElement(root, str(field_name))
                child.text = str(value)

        # 5. Write to XML File
        tree = ET.ElementTree(root)
        ET.indent(tree, space="  ")
        tree.write(output_xml, encoding="utf-8", xml_declaration=True)

        print(
            f"Success: Exported '{input_pdf}' -> '{output_xml}'",
            file=sys.stdout,
        )

    except Exception as e:
        print(f"Error processing PDF: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()