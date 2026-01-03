# Folder Structre
```
CV_Roadmap/
 └── Week1/
      └── Day1/
```

# Pre-qualities:

* [Notebook](https://dev.to/nazanin_ashrafi/getting-marimo-up-and-running-on-windows-with-uv-4982)
  * Installing Marimo:
   ```python
    uv init
    ```
   ```python
   uv add marimo
   ```
   ```python
   uv run marimo edit my_notebook.py
   ```

* Install `numpy`
  ```python
  uv pip install numpy
  ```

* Install `OpenCV`

* Anaconda <br>
  To see a list of all of your environments:
  ```python
  conda env list
  ```

  Create a new Conda environment:
  ```python
  conda create -n opencv python=3.10
  ```

  Activate the environment:
  ```python
  conda activate opencv
  ```

  Install OpenCV from conda-forge:
  ```python
  conda install -c conda-forge opencv
  ```
