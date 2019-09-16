# Plot Multiple Large Image
```python
plt.figure(figsize=(12,12))
f, axarr = plt.subplots(4,8)
for i in range(4):
    for j in range(8):
        axarr[i,j].imshow(img[8*i+j])
```
