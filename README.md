# Hackathon Financial Game

## Installation

### Clone repositories

```
git clone https://github.com/Ctrl-Alt-Del-Debt/Hackathon-Game.git
cd Hackathon-Game
```

### Install prerequisites

##### Linux:

```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install -e .
```

##### Windows Powershell:

```powershell
python -m venv env
.\env\Scripts\activate
def main():
    set_page_config()
    show_game_ui()

if __name__ == "__main__":
    main()```

### VS Code settings

For getting rid of the import errors, it might be needed to implement following into settings.json (assuming working in VS Code)
```powershell
"terminal.integrated.env.windows": {"PYTHONPATH": "${workspaceFolder}"}
```


### How to run

```
python -m streamlit run main.py
```