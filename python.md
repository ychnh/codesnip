# Set GPU
```python
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" 
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
```

# Set Environpath Library
```python
import sys
sys.path.insert(0,'repnet')
sys.path.append('module')
```

```python
os.environ['LD_LIBRARY_PATH'] = os.environ.get('LD_LIBRARY_PATH','')
os.environ['LD_LIBRARY_PATH'] += ':/usr/local/cuda-10.1/lib64’
```

# BASH
```python
glob.glob('/folder/*')
os.system('rm -r folder')
```
