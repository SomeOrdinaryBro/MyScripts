# my-scripts

This repo contains simple Python scripts I've written to help automate or simplify common tasks. These scripts are intended for internal use by non-technical users as well, with clear instructions included.

Each folder contains:
- A `.py` script (the code file)
- A `.txt` file with step-by-step instructions on how to run it

## What You Need First

Before using any of the scripts, make sure the following are set up on your computer:

1. **Python Installed**  
   Download and install Python (version 3.11 or newer):  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Python Added to PATH**  
   During installation, make sure to select the option that says "Add Python to PATH" — this allows you to run Python from the terminal.

3. **Install Required Tools**  
   Some scripts may require extra tools or libraries (like Tesseract or Poppler). These are mentioned clearly in the `.txt` instruction files or inside the code as comments. Links are provided where needed.

## How to Use These Scripts

1. Download or clone this repository to your computer
2. Open the folder where the script is saved
3. Open a terminal (Command Prompt or PowerShell)
4. Use the `cd` command to go into the script folder. Example:
   ```
   cd C:\Users\YourName\Downloads\my-scripts\folder-name
   ```
5. Run the script using this command:
   ```
   py script_name.py
   ```

If the script gives an error that a package is missing, install it with:
```
py -m pip install package-name
```

## Notes

- You don’t need to understand Python to use these scripts. Just follow the steps in the `.txt` file.
- Each script has comments and explanations in case someone technical needs to review or change it.
- If you're not sure what a script does, read the `.txt` first — it explains the purpose, steps, and any setup needed.

No coding knowledge required. These are made to be simple and straightforward to run.
