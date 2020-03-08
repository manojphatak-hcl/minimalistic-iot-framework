## Run Docker Container
Copy the sample data & code into folder called "data"
```
sudo docker run -it --rm -p 1880:1880  -v <path-to-data-folder>:/home manojphatak/video_analytics_sandbox:v2 /bin/bash
```


## Install Node inside container
```
# update 
apt-get update
# install curl 
apt-get install curl
# get install script and pass it to execute: 
curl -sL https://deb.nodesource.com/setup_10.x | bash
# and install node 
apt-get install nodejs
# confirm that it was successful 
node -v
# npm installs automatically 
npm -v
```

## Install node-red and custom nodes
```
npm install -g --unsafe-perm node-red
```

```
npm install -g node-red-contrib-pythonshell
npm install -g  node-red-contrib-python-function
npm install -g node-red-node-openweathermap
```

## Access node-red
```
http://localhost:1880
```


## Configure Flow for node-red
```json
[{"id":"a9e2c38e.34ca","type":"tab","label":"Flow 1"},{"id":"966cc82f.c2d0b8","type":"pythonshell in","z":"a9e2c38e.34ca","name":"Python Program","pyfile":"/home/video_analytics.py","virtualenv":"","continuous":false,"stdInData":false,"x":341.5,"y":154,"wires":[["53df5814.ac72a8"]]},{"id":"cfb395e0.ab4fa8","type":"inject","z":"a9e2c38e.34ca","name":"","topic":"","payload":"","payloadType":"date","repeat":"","crontab":"","once":false,"x":140.5,"y":76,"wires":[["966cc82f.c2d0b8"]]},{"id":"53df5814.ac72a8","type":"debug","z":"a9e2c38e.34ca","name":"","active":true,"console":"false","complete":"false","x":537.5,"y":233,"wires":[]}]
```

