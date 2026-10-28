# My Application (my-app)

An AI application project based on Streamlit.

## Project Introduction

This is a web application developed using the Streamlit framework, with the main function of loading and running AI agents.

## Tech Stack

- **Streamlit** - Web Application Framework
- **Python** - Programming Language
- **AI Agent** - AI Agent Functionality

## Project Structure

```
my-app/
├── .devcontainer/          # Dev container configuration
│   └── devcontainer.json
├── .env                    # Environment variable configuration
├── .vscode/                # VS Code configuration
│   └── settings.json
└── app/
    ├── 2.py                # Main application (contains AI Agent loading logic)
    └── requirements.txt    # Project dependencies
```

## Quick Start

### Environment Requirements

- Python 3.8+

### Install Dependencies

```bash
cd app
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app/2.py
```

Or

```bash
cd app
streamlit run 2.py
```

The application will open in your browser, typically accessible at `http://localhost:8501`.

## Configuration Instructions

### Environment Variables

Configure necessary environment variables in the `.env` file, with specific content set according to AI Agent requirements.

### Development Container

The project includes a `.devcontainer` configuration, supporting containerized development using the VS Code Remote - Containers extension.

## Dependency Details

Main dependencies are listed in `app/requirements.txt`, including:
- streamlit
- Other AI-related dependencies (based on actual needs)

## License

Please check the LICENSE file in the project root directory for specific license information.

## Author

luoyong0129

---

For any questions or suggestions, feel free to submit an Issue or Pull Request.
