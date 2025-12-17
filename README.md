## 测试英伟达显卡能否与torch通信
- 用conda的已经是老登了，我们用现代化的uv

```bash
git clone --depth 1 https://github.com/reigadegr/nvidia_torch_communication
uv sync
uv run main.py
```

- 我的输出

```txt
2025-12-17 13:41:01.621987: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2.20.0
WARNING:tensorflow:From /home/reigadegr/project/nvidia_torch_communication/main.py:7: is_gpu_available (from tensorflow.python.framework.test_util) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.config.list_physical_devices('GPU')` instead.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1765950064.233102  257422 gpu_device.cc:2020] Created device /device:GPU:0 with 4598 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 2060, pci bus id: 0000:01:00.0, compute capability: 7.5
GPU True
Using device: cuda:0
CUDA available:  True
CUDA device count:  1
CUDA current device:  0
CUDA device name:  NVIDIA GeForce RTX 2060
CUDA version: 13.0
2.9.1+cu130
13.0
True
```
最后一行是true就行
