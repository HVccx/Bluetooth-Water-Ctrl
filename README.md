# Bluetooth-Water-Ctrl

## What's the use?
Shenzhen regular electronic "Bluetooth water controller" control program. It is suitable for dormitory water heater in colleges and universities in China.
You need to capture the Bluetooth water controller by yourself (file like ***\*.log***) , this tool can extract the key from the package and generate a web version of the Bluetooth water controller.

## How to capture Bluetooth packets?
You need to use an *Android phone*, enable *Bluetooth HCI information collection log* in *Developer options*, and turn on Bluetooth to boil water on the target device.

## How to extract Bluetooth logs from Android phone?
Use adb in the platform-tools folder to obtain, connect the Android phone to the PC, open the *USB debugging* function, and open the *terminal* in the *platform-tools folder*.

Check the device connection
```sh
adb devices
```
```sh
* daemon not running; starting now at tcp:5037
* daemon started successfully
List of devices attached
WTKDU1**********        device
```
Device connection successful

Get the Bluetooth log file
```sh
adb pull <log_path> <PC_local_path>
```
```sh
/data/log/bt/: 1 file pulled, 0 skipped. 5.3 MB/s (121098 bytes in 0.022s)
```
The Bluetooth log file will appear in the directory you specify.  -->  *\*.log*

## How to use?
use ***BlueWater.py*** && ***BlueWater.exe*** to get key and create ***index.html***
```sh
python BlueWater.py your_file_path
```
```sh
Indexes of 'fefe':[93058, 93390]
key: 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**
key: 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**
Success!!!
Run index.html in Edge && Chrome !!!    enjoy ^_^
```
or
```sh
BlueWater.exe your_file_path
```
```sh
Indexes of 'fefe':[93058, 93390]
key: 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**
key: 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**
Success!!!
Run index.html in Edge && Chrome !!!    enjoy ^_^
```
After Bluetooth is enabled, use Edge or Chrome to open index.html, click the Open button and select the target device.
If not available, you can replace a different key below.Then try again.
```sh
...
return new Uint8Array([
    0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**, 0x**
]);
...
```