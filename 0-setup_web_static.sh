#!/usr/bin/env bash
# Sets up web servers for deployment of `web_static`
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html><head></head><body>Hello Holberton</body></html>" | sudo tee --append /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown ubuntu:ubuntu /data/
sudo sed -i "37 i \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
