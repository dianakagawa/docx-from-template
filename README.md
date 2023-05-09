# Generate .docx files using python-docx-template

## Description

### This script generates a .docx file using a .docx template.

For this project's purpose, I used two templates: one in case the .json file has all the data needed to fill the template, and another one in case the .json file doesn't. The template has placeholders in the form of `{{ jinja2_sintax }}`. These are replaced with data from a .json file.

## Installation

#### Don't forget to create your virtual environment before installing the dependencies.

```bash
pip install docxtpl
```
