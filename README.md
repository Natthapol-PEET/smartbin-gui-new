# Python flet smartbin-ui

### develop in virtualenv
```
source venv/bin/activate
```

### install package
```
pip install requirements.txt
```

### run program for develop
```
flet app.py -d
```

### run program for production
```
flet app.py
```

### build flet app
https://flet.dev/docs/guides/python/packaging-desktop-app/
```
flet pack app.py
or
flet pack app.py --name bundle_name
```

### remote pi
```
ssh pi@192.168.1.101
12345678
```

### Transfer Files Via SSH to Raspberry Pi Using SCP
```
scp -r /Users/70007742/Documents/work/ku-csc/smartbin-gui-new/release pi@192.168.1.101:/home/pi
```

### Configuring your Raspberry Pi
```
sudo raspi-config
```
Advanced Options -> GL Driver -> GL (Fake KMS)