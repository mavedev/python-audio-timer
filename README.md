# python-audio-timer
Console script that periodically launches sound

# Run as a script
To run as a script:
```shell
$ python3 . <seconds of delay between playing sound>
```

# Build
To build an executable:
```shell
$ mkdir build && cd build
$ pyinstaller --onefile --name='audiotimer' --paths='path/to/venv/Lib/site-packages' --add-data='../resources:resources' ../__main__.py
```
The --add-data delimiter is OS-dependent
<br>Windows: ';'
<br>Linux/OSX: ':'
<br>Then:
```shell
$ ./audiotimer 1200 # Runs with 20min delay.
```
