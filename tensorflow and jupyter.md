# Tensorboard

* ssh -L 16006:127.0.0.1:6006 yhong@hostname -p ## 
* 127.0.0.1:16006/#graphs&run=.

-N flag to avoid opening an ssh shell. Adding -f puts process in background

# Jupyter
* Change Theme
* jt -t chesterish

* jupyter notebook --port 8887
* ssh -L localhost:8888:localhost:8887 yhong@192.168.0.17 -p ##

* ~/.jupyter/custom/
  * wget https://raw.githubusercontent.com/draperjames/one-dark-notebook/master/custom.css
## Kill
* fuser 8888/tcp
* kill -9 PID
* or
* jupyter notebook stop 8888

# Jupyter Lab
## Install
* sudo apt-get install curl
* curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
* sudo apt-get install nodejs
## Widgets for Dashboard
* pip install ipywidgets
* jupyter nbextension enable --py widgetsnbextension

## Hotkeys
```
{
    "shortcuts": [        
        {
            "command": "application:toggle-mode",
            "keys": [
                "Accel M"
            ],
            "selector": "body"
        }
    ]
}
```
