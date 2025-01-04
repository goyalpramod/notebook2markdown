# Jupyter Notebook Converter

![](https://github.com/goyalpramod/notebook2markdown/blob/main/assets/sample.gif)

A simple web application built with Gradio that converts Jupyter notebooks (.ipynb) to either Markdown files or Python scripts. This tool makes it easy to convert your notebooks for documentation or code sharing purposes.

## Features

- Convert Jupyter notebooks to:
  - Markdown files (`.md`)
  - Python scripts (`.py`)
- Interactive web interface
- Preview converted content
- Copy to clipboard functionality
- Download converted files
- Preserves markdown cells (as comments in Python output)
- Clean and intuitive user interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/notebook-converter.git
cd notebook-converter
```

2. Create a virtual environment (recommended):
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/MacOS
python -m venv .venv
source .venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python notebook_converter.py
```

2. Open your web browser and navigate to `http://127.0.0.1:7860` (or the URL shown in your terminal)

3. Use the interface:
   - Upload your Jupyter notebook using the file upload button
   - Select your desired output format (Markdown or Python)
   - Click "Convert" to process your notebook
   - Preview the converted content
   - Use the "Copy to Clipboard" button or download the converted file

## Example

**Input Notebook Structure:**
```
Notebook
Cell 1 (Code):
print("Hello World")

Cell 2 (Markdown):
## This is a heading

Cell 3 (Code):
def example():
    return "Example function"
```

**Markdown Output:**
````markdown
```python
print("Hello World")
```

## This is a heading

```python
def example():
    return "Example function"
```
````

**Python Output:**
```python
print("Hello World")

# ## This is a heading

def example():
    return "Example function"
```

## Requirements

- Python 3.8+
- gradio
- nbconvert
- nbformat

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Gradio](https://gradio.app/)
- Uses [nbconvert](https://nbconvert.readthedocs.io/) for notebook processing

## Support

If you encounter any issues or have questions, please file an issue in the GitHub repository.

## Future Enhancements

These are planned features and improvements that would enhance the functionality of the notebook converter:

### LLM Integration
- Integration with local LLMs (avoiding API calls) for code analysis
- Automatic generation of cell-by-cell documentation
- Smart code commenting based on cell content
- Contextual understanding of notebook flow

### User Customization
- Custom prompt support for specialized conversions
- LaTeX equation processing and formatting
- User-defined templates for output formatting
- Batch processing capabilities for multiple notebooks

### Other Potential Features
- Support for additional output formats (e.g., HTML, RST)
- Interactive editing of converted content before download
- Cell dependency visualization
- Metadata preservation options

We welcome contributions to implement any of these features! Feel free to pick up any of these enhancements or suggest new ones via issues.