## Pull Docker Image & Run Container
```
sudo docker run -it --rm -p 1880:1880  -v <path-to-data-folder>:/home manojphatak/video_analytics_sandbox:v2 /bin/bash
```

## Start Node-Red Server inside the container
```
$> node-red
```

Node-Red should be accessible at:
```
http://localhost:1880
```

Configure Flow at Node-Red using the Python Node & the Python Script
This can be done by "Import"ing following JSON Flow description into Node-Red
```json
[{
	"id": "a9e2c38e.34ca",
	"type": "tab",
	"label": "Flow 1"
}, {
	"id": "966cc82f.c2d0b8",
	"type": "pythonshell in",
	"z": "a9e2c38e.34ca",
	"name": "Python Program",
	"pyfile": "/home/video_analytics.py",
	"virtualenv": "",
	"continuous": false,
	"stdInData": false,
	"x": 341.5,
	"y": 154,
	"wires": [
		["53df5814.ac72a8"]
	]
}, {
	"id": "cfb395e0.ab4fa8",
	"type": "inject",
	"z": "a9e2c38e.34ca",
	"name": "",
	"topic": "",
	"payload": "",
	"payloadType": "date",
	"repeat": "",
	"crontab": "",
	"once": false,
	"x": 140.5,
	"y": 76,
	"wires": [
		["966cc82f.c2d0b8"]
	]
}, {
	"id": "53df5814.ac72a8",
	"type": "debug",
	"z": "a9e2c38e.34ca",
	"name": "",
	"active": true,
	"console": "false",
	"complete": "false",
	"x": 537.5,
	"y": 233,
	"wires": []
}]
```

### Minified:
```json
[{"id":"a9e2c38e.34ca","type":"tab","label":"Flow 1"},{"id":"966cc82f.c2d0b8","type":"pythonshell in","z":"a9e2c38e.34ca","name":"Python Program","pyfile":"/home/video_analytics.py","virtualenv":"","continuous":false,"stdInData":false,"x":341.5,"y":154,"wires":[["53df5814.ac72a8"]]},{"id":"cfb395e0.ab4fa8","type":"inject","z":"a9e2c38e.34ca","name":"","topic":"","payload":"","payloadType":"date","repeat":"","crontab":"","once":false,"x":140.5,"y":76,"wires":[["966cc82f.c2d0b8"]]},{"id":"53df5814.ac72a8","type":"debug","z":"a9e2c38e.34ca","name":"","active":true,"console":"false","complete":"false","x":537.5,"y":233,"wires":[]}]
```
