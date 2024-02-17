import sys

if len(sys.argv) < 2:
    input("How to Use: python BlueWater.py your_file_path")
    sys.exit(1)
file_path = sys.argv[1]

key=''
try:
    with open(file_path, 'rb') as f:
        data = f.read().hex()
except:
    input('no such file !!!')
    exit(0)

indexes = []
start_index = 0

while True:
    index = data.find('fefe', start_index)
    if index == -1:
        break
    indexes.append(index)
    start_index = index + 1

print("Indexes of 'fefe':", indexes)

if not indexes:
    print('1.log have no key')
    input('fail >.<')
    exit(0)

for i in indexes:
    hex_data = data[i:i+40]
    key=', '.join(['0x' + hex_data[i:i+2].upper() for i in range(0, len(hex_data), 2)])
    print('key:'+'\033[91m'+key+'\033[0m')
print("Success!!!")

p1='''<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#fafafa" />
    <title>FOSS</title>
    <style>
        body {
            background-color: #fafafa;
        }

        .main {
            position: absolute;
            left: 50%;
            top: 50%;
            -webkit-transform: translate(-50%, -50%);
            transform: translate(-50%, -50%);
            display: flex;
            align-items: center;
            flex-direction: column;
        }

        .misc {
            position: absolute;
            bottom: 0;
            left: 0;
            margin: 10px;
        }
    </style>
</head>

<body>
    <div class="main">
        <noscript>需要启用 JavaScript。</noscript>
        <button id="main-button" onclick="handleButtonClick()" style="margin: 0%;">开启</button>
        <p id="device-name" style="margin-top: 10px; margin-bottom: 10px;">未连接</p>
        <p id="status" style="margin: 0;"></p>
    </div>
    <div class="misc">
        <button id="install-button" hidden>将蓝牙水控器 FOSS 安装到系统</button>
        <p style="font-size: smaller; color: gray; margin: 0%;">
            <a href="" target="_blank">源代码</a> · <a
                href="" target="_blank">疑难解答</a><br>
            <span style="font-size: smaller;">copyright (c) 2023 celesWuff, licensed under MIT License</span>
        </p>
    </div>
    <dialog id="dialog">
        <header>出现错误</header>
        <form method="dialog">
            <p id="dialog-content"></p>
            <menu style="display: flex; justify-content: flex-end;">
                <button onclick="succeeded = false">好</button>
            </menu>
        </form>
    </dialog>
</body>

<script>
    function crc16changgong(data) {
        let crc = 0x1017;
        for (let i = 0; i < data.length; i++) {
            crc ^= data.charCodeAt(i);
            for (let j = 0; j < 8; j++) {
                if ((crc & 0x0001) == 1) {
                    crc >>= 1;
                    crc ^= 0xA001;
                } else crc >>= 1;
            }
        }
        return crc;
    }

    function makePayload(deviceName) {
        const checksum = crc16changgong(deviceName.slice(-5));
        // prettier-ignore
        return new Uint8Array([
            '''

p2='''
        ]);
    }

    let bluetoothDevice;
    let characteristic;
    let isStarted = false;

    function updateUi(stage) {
        const mainButton = document.getElementById("main-button");
        const deviceName = document.getElementById("device-name");
        const status = document.getElementById("status");
        switch (stage) {
            case "pending":
                mainButton.innerText = "请稍后";
                mainButton.disabled = true;
                deviceName.innerText = "已连接：" + bluetoothDevice.name;
                break;
            case "ok":
                mainButton.innerText = "结束";
                mainButton.disabled = false;
                break;
            case "standby":
                mainButton.innerText = "开启";
                mainButton.disabled = false;
                deviceName.innerText = "未连接";
                break;
        }
    }

    async function handleBluetoothError(error) {
        // this is so fucking ugly but i have no choice
        // you would never know how those shitty browsers behave
        if (error.toString().match(/User cancelled/) || error.toString() == "2") return; // "2" is a weird behavior of Bluefy browser on iOS
        const dialogContent = document.getElementById("dialog-content");
        if (error.toString().match(/User denied the browser permission/)) {
            dialogContent.innerText = "蓝牙权限遭拒。请前往手机设置，授予浏览器“位置信息”权限。此权限不会用于定位，详情请参考源代码仓库内的";
            dialogContent.innerHTML += "<a href=''>“疑难解答”</a>。"
        } else if (error.toString().match(/NetworkError/)) {
            dialogContent.innerText = "连接不稳定，无法与水控器建立连接。请重试。";
        } else if (!navigator.bluetooth || error.toString().match(/Bluetooth adapter not available/) || error.toString().match(/NotFoundError/)) {
            dialogContent.innerText = "找不到蓝牙硬件，或浏览器不支持。限于篇幅，详情请参考源代码仓库内的";
            dialogContent.innerHTML += "<a href='' target='_blank'>“疑难解答”</a>。"
        } else {
            dialogContent.innerText = error + "是什么呢（这可能是一个Bug，请截图并";
            dialogContent.innerHTML += "<a href='' target='_blank'>反馈给开发者</a>。）"
        }
        document.getElementById("dialog").showModal();
        if (bluetoothDevice) await bluetoothDevice.gatt.disconnect();
        isStarted = false;
        updateUi("standby");
    }

    async function start() {
        try {
            bluetoothDevice = await navigator.bluetooth.requestDevice({
                filters: [{ namePrefix: "Water" }],
                optionalServices: [window.navigator.userAgent.match(/Bluefy/) ? "generic_access" : 0xF1F0] // workaround for Bluefy
            });
            updateUi("pending");
            const server = await bluetoothDevice.gatt.connect();
            const service = await server.getPrimaryService(0xF1F0);
            characteristic = await service.getCharacteristic(0xF1F1);
            await characteristic.writeValue(makePayload(bluetoothDevice.name));
            isStarted = true;
            updateUi("ok");
        } catch (error) {
            handleBluetoothError(error);
        }
    }

    async function end() {
        try {
            const endPayload = new Uint8Array([0xFE, 0xFE, 0x09, 0xB3, 0x00, 0x00])
            await characteristic.writeValue(endPayload)
            await bluetoothDevice.gatt.disconnect();
            isStarted = false;
            updateUi("standby");
        } catch (error) {
            handleBluetoothError(error);
        }
    }

    function handleButtonClick() {
        isStarted ? end() : start();
    }

    const xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.countapi.xyz/hit/waterctl/visits");
    xhr.responseType = "json";
    xhr.send();

    if (navigator.serviceWorker && !navigator.serviceWorker.controller) {
        navigator.serviceWorker.register('serviceworker.js');
    }

    // pwa install prompt
    const installButton = document.getElementById('install-button');

    window.addEventListener('beforeinstallprompt', (event) => {
        event.preventDefault();
        window.deferredPrompt = event;
        installButton.hidden = false;
    });

    installButton.addEventListener('click', async () => {
        const promptEvent = window.deferredPrompt;
        if (!promptEvent) {
            return;
        }
        promptEvent.prompt();
        const result = await promptEvent.userChoice;
        window.deferredPrompt = null;
        installButton.hidden = true;
    });

    window.addEventListener('appinstalled', (event) => {
        window.deferredPrompt = null;
    });

    // auto resize for desktop
    window.resizeTo(538, 334);
</script>

</html>
'''

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(p1+key+p2)

input('Run index.html in Edge && Chrome !!!    enjoy ^_^')