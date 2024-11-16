def generate_html_form():
    form_name = input("Enter form name: ")
    num_fields = int(input("Enter the number of fields: "))

    fields = []
    for _ in range(num_fields):
        field_name = input("\nEnter field name: ")
        field_type = input("Enter field type (text, password, email, number, date, checkbox, radio): ").lower()
        is_required = input("Is this field required? (yes/no): ").lower() == 'yes'
        max_length = input("Enter max length (or press Enter to skip): ")
        pattern = input("Enter pattern (regex) for validation (or press Enter to skip): ")

        options = None
        if field_type in ['checkbox', 'radio']:
            num_options = int(input(f"Enter the number of options for {field_name}: "))
            options = []
            for i in range(num_options):
                option = input(f"Enter option {i + 1}: ")
                options.append(option)

        fields.append({
            "name": field_name,
            "type": field_type,
            "required": is_required,
            "max_length": max_length,
            "pattern": pattern,
            "options": options
        })

    html_form = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{form_name} Form</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
        }}
        form {{
            background: #fff;
            border-radius: 5px;
            padding: 20px;
            max-width: 400px;
            margin: auto;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }}
        label {{
            font-weight: bold;
            margin-top: 10px;
            display: block;
        }}
        input, button {{
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }}
        button {{
            background-color: #007BFF;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: #0056b3;
        }}
    </style>
</head>
<body>
    <h1>{form_name} Form</h1>
    <form name="{form_name}" action="#" method="POST">
    """

    for field in fields:
        if field["type"] in ['checkbox', 'radio']:
            html_form += f"        <fieldset>\n"
            html_form += f"        <legend>{field['name'].capitalize()}:</legend>\n"
            for option in field["options"]:
                html_form += f"            <input type='{field['type']}' name='{field['name']}' value='{option}' id='{option}'>\n"
                html_form += f"            <label for='{option}'>{option}</label><br>\n"
            html_form += f"        </fieldset>\n"
        else:
            html_form += f"        <label for='{field['name']}'>{field['name'].capitalize()}:</label>\n"
            html_form += f"        <input type='{field['type']}' name='{field['name']}' id='{field['name']}'"

            if field["required"]:
                html_form += " required"
            if field["max_length"]:
                html_form += f" maxlength='{field['max_length']}'"
            if field["pattern"]:
                html_form += f" pattern='{field['pattern']}'"

            html_form += "><br>\n"

    html_form += "        <button type='submit'>Submit</button>\n"
    html_form += "    </form>\n</body>\n</html>"

    file_name = f"{form_name.lower().replace(' ', '_')}_form.html"
    with open(file_name, "w") as file:
        file.write(html_form)

    print(f"\nHTML form successfully saved as '{file_name}'.")
    print(f"Open '{file_name}' in your browser to preview the form.")

generate_html_form()
