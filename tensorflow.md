# Tensorboard

ssh -L 16006:127.0.0.1:6006 yhong@hostname -p ## 
127.0.0.1:16006/#graphs&run=.

-N flag to avoid opening an ssh shell. Adding -f puts process in background


jupyter notebook --port 8887
ssh -N -L localhost:8888:localhost:8887 yhong@192.168.0.17