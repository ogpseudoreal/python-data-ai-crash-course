# Package notes

Open `index.html` or `COURSE.html` locally in your browser. The reading pages use bundled HTML/CSS and embedded notebook charts; they do not load external scripts, fonts, analytics, or model services. External resource links open the original providers' sites.

To study, you only need the reading pages and the notebooks/data. To execute notebooks, follow Module 0 and install `requirements.txt`. The eight core notebooks have been run; see `VALIDATION.md`. Notebook 4 saves derived CSV files to `outputs/`.

Maintainer utilities:

- `build_notebooks.py` regenerates the original notebooks and synthetic data. **It overwrites notebook files**, so do not run it over your personal answers.
- `validate_notebooks.py` executes notebooks and updates saved outputs and verification metadata. It uses a temporary local Jupyter kernel, which may require local-port permission in a restricted environment.
- `build_handbook.py` regenerates HTML pages and notebook reading previews. It additionally needs the `markdown` package, which is not required for studying or running the notebooks.
- `environment-freeze.txt` records the complete validation environment, including maintainer tools; use the shorter direct `requirements.txt` for the course notebooks.

The ZIP omits Python environments, caches, and temporary validation files. Extract the entire ZIP before opening the handbook so relative links continue to work. The root folder inside the ZIP is `python-data-ai-course/`.

The reading pages received structural/link checks. Browser automation could not preview local HTML because the browser's URL policy blocks local-file navigation; no browser-based layout validation is claimed. The three executed chart images were inspected directly for readable labels and layout. Markdown versions are included as an alternative reading format.
