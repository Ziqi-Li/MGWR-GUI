## Remember to install the entire conda environment which includes the pyinstaller

### import the conda env command

```bash
conda env create -f environment.yml
```

### export the conda env command \*

```bash
conda env export > environment.yml
```

# Compile the software

### We use the following command to compile the software into executable

### Remember to activate the conda env to run the command

```bash
pyinstaller --clean --noconfirm build.spec
```
