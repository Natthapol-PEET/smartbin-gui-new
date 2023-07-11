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


export PATH="$PATH":"$HOME/.pub-cache/bin"
C:\Users\natth\AppData\Local\Pub\Cache\bin

$ flutter create hello_world
$ cd hello_world
$ flutterpi_tool build --arch=arm --cpu=pi4 --release
$ rsync -a --info=progress2 ./build/flutter_assets/ my-pi4:/home/pi/hello_world_app
$ ssh my-pi4 flutter-pi --release /home/pi/hello_world_app

% windows root path
flutter build bundle

% windows root path
C:\Users\natth\fvm\default\bin\cache\dart-sdk\bin\dart.exe ^
  C:\Users\natth\fvm\default\bin\cache\dart-sdk\bin\snapshots\frontend_server.dart.snapshot ^
  --sdk-root C:\Users\natth\fvm\default\bin\cache\artifacts\engine\common\flutter_patched_sdk_product ^
  --target=flutter ^
  --aot ^
  --tfa ^
  -Ddart.vm.product=true ^
  --packages .dart_tool\package_config.json ^
  --output-dill build\kernel_snapshot.dill ^
  --verbose ^
  --depfile build\kernel_snapshot.d ^
  package:app_37/main.dart


% linux generage aot 
% /mnt/d/ku-csc/smartbin-gui-new/hello_world/flutter-engine-binaries-for-arm/arm/gen_snapshot_linux_x64_release \
%     --causal_async_stacks                                         \
%     --packages=.packages                                          \
%     --deterministic                                               \
%     --snapshot_kind=app-aot-blobs                                 \
%     --vm_snapshot_data=build/vm_snapshot_data                     \
%     --isolate_snapshot_data=build/isolate_snapshot_data           \
%     --vm_snapshot_instructions=build/vm_snapshot_instr            \
%     --isolate_snapshot_instructions=build/isolate_snapshot_instr  \
%     --no-sim-use-hardfp                                           \
%     --no-use-integer-division                                     \
%     build/kernel_snapshot.dill
  

% linux root path -> app.so
/mnt/d/ku-csc/smartbin-gui-new/flutter-engine-binaries-for-arm/arm/gen_snapshot_linux_x64_release \
  --deterministic \
  --snapshot_kind=app-aot-elf \
  --elf=build/flutter_assets/app.so \
  --strip \
  --sim-use-hardfp \
  build/kernel_snapshot.dill


scp -r scp /mnt/d/ku-csc/smartbin-gui-new/app_37/build/flutter_assets pi@192.168.1.105:/home/pi
12345678
