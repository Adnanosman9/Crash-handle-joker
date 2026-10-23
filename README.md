# Joke with crash

A python script that controls Python's default error handler (`sys.excepthook`). Whenever any Python script on your computer crashes, it intercept the error message and prints a cowsay drawing giving a randomized developer excuse combined with a programming joke.

## Here is a crash

<img width="856" height="311" alt="Screenshot 2026-10-23 131533" src="https://github.com/user-attachments/assets/f1655028-4358-4ba2-a115-5696a89d0fe3" />


## Set up

### 1. Clone down the repository files.
  
### 2. Install the required dependencies:
   ```bash
   pip install faker pyjokes cowsay
   ```


### 3. Paste this in your cmd
   ```bash
   python -m site --user-site
   ```
   **This will give something like "C:\Users\adnan\AppData\Roaming\Python\Python314\site-packages"**

### 4. Go to the location and past the downloaded **"usercustomize.py"** file in the **site-packages** folder

<br>

## Test
* Make a random crash code.
  ```bash
   x = 1 / 0
   ```
* Save and run it. It will automatically give a cow joke.



## Behind the Build & Logic
I used `sys.excepthook` to override the standard system traceback prints. When Python hits an unhandled exception, it diverts the data nodes straight to my `excuse()` module. The generator picks a random enterprise buzzword, calls `pyjokes` to grab a random line, and draws a name and company from `Faker` before packaging the string payload inside the `cowsay.cow` text canvas buffer.

License: MIT
