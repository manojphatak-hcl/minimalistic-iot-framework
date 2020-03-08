## Copy the sample data & code into folder called "data"

## Run Docker Container
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
