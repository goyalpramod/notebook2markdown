import gradio as gr
import nbformat
import tempfile
import os

def convert_to_markdown(notebook_content):
    """Convert notebook cells to markdown format."""
    if isinstance(notebook_content, str):
        return "Please upload a valid notebook file."
    
    markdown_output = ""
    
    for cell in notebook_content.cells:
        if cell.cell_type == 'code':
            # Add code cells with Python syntax highlighting
            markdown_output += f"```python\n{cell.source}\n```\n\n"
        elif cell.cell_type == 'markdown':
            # Add markdown cells as is
            markdown_output += f"{cell.source}\n\n"
    
    return markdown_output

def convert_to_python(notebook_content):
    """Convert notebook cells to Python script format."""
    if isinstance(notebook_content, str):
        return "Please upload a valid notebook file."
    
    python_output = ""
    
    for cell in notebook_content.cells:
        if cell.cell_type == 'code':
            # Add code cells
            python_output += f"{cell.source}\n\n"
        elif cell.cell_type == 'markdown':
            # Add markdown cells as comments
            commented_lines = [f"# {line}" if line.strip() else "#" 
                             for line in cell.source.split('\n')]
            python_output += f"{'\n'.join(commented_lines)}\n\n"
    
    return python_output

def save_temp_file(content, extension):
    """Save content to a temporary file and return the path."""
    # Create a temporary file with the proper extension
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, f"converted_notebook.{extension}")
    
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return temp_path

def process_notebook(file, output_format):
    """Process the uploaded notebook file."""
    try:
        # Read the notebook
        if file is None:
            return "Please upload a notebook file.", None
        
        # Read the content based on file type
        if hasattr(file, 'name'):
            # If it's a file object
            with open(file.name, 'r', encoding='utf-8') as f:
                notebook_content = nbformat.read(f, as_version=4)
        else:
            return "Invalid file format", None
        
        if output_format == "Markdown":
            converted_content = convert_to_markdown(notebook_content)
            file_extension = "md"
        else:  # Python
            converted_content = convert_to_python(notebook_content)
            file_extension = "py"
        
        # Save to temporary file
        temp_path = save_temp_file(converted_content, file_extension)
        
        return converted_content, temp_path
    
    except Exception as e:
        return f"Error processing notebook: {str(e)}", None

def copy_to_clipboard(text):
    return text, gr.Info("Copied to clipboard!")

# Create the Gradio interface
with gr.Blocks(title="Notebook Converter") as iface:
    gr.Markdown("# Jupyter Notebook Converter")
    gr.Markdown("Convert your Jupyter notebooks to Markdown or Python files.")
    
    with gr.Row():
        # Input components
        file_input = gr.File(label="Upload Notebook", file_types=[".ipynb"])
        format_input = gr.Radio(["Markdown", "Python"], 
                              label="Output Format", 
                              value="Markdown")
    
    # Convert button
    convert_btn = gr.Button("Convert")
    
    with gr.Column():
        # Output components
        output_text = gr.Textbox(label="Preview", lines=10)
        copy_btn = gr.Button("Copy to Clipboard")
        download_output = gr.File(label="Download Converted File")
    
    # Handle conversion
    convert_btn.click(
        fn=process_notebook,
        inputs=[file_input, format_input],
        outputs=[output_text, download_output]
    )
    
    # Handle copy to clipboard
    copy_btn.click(
        fn=copy_to_clipboard,
        inputs=[output_text],
        outputs=[output_text],
        js="async (text) => { await navigator.clipboard.writeText(text); return text; }"
    )

# Launch the app
if __name__ == "__main__":
    iface.launch()