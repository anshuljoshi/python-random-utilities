## python-random-utilities

* Simple generic JSON parser (jsonParser/genericJSONParser.py)
* Simple encryption-decryption program (crypt/pySimpleCrypt.py)
* Command line - Todo (todo/todo)
* Youtube Playlist downloader (youtube/youplaydl.py)

Install requirements before using. Clone the repo and do:
```
pip install -r requirements.txt
```

For ease of use:
```
python -m compileall <pythonprogram.py>
```

It will generate a .pyc file. You can put the .py and .pyc in your Python library to access them from anywhere.

For example, if I want to use youplaydl from any directory I can now do:
```
python -m youplaydl <playlisturl>
```
