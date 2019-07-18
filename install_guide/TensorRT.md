# Steps

* install numpy
* install pycuda
* install tensorflow-gpu
* get the tarfile tensorflowRT
* follow instructions on https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html#installing-tar

# Results
```
pycuda (2019.1.1)  
NOTE: UFF has been tested with TensorFlow 1.12.0. Other versions are not guaranteed to work

TensorRT test
================================================================== warnings summary ===================================================================
/home/sijin/.conda/envs/tensorRT/lib/python3.6/site-packages/pytest-5.0.1-py3.6.egg/_pytest/mark/structures.py:332
  /home/sijin/.conda/envs/tensorRT/lib/python3.6/site-packages/pytest-5.0.1-py3.6.egg/_pytest/mark/structures.py:332: PytestUnknownMarkWarning: Unknown pytest.mark.cuda - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

-- Docs: https://docs.pytest.org/en/latest/warnings.html
======================================================= 29 passed, 1 warnings in 42.76 seconds ====


export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/sijin/local/TensorRT-5.1.5.0/lib
```
