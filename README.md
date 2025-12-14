## 测试英伟达显卡能否与torch通信
- 用conda的已经是老登了，我们用现代化的uv

```bash
git clone --depth 1 https://github.com/reigadegr/nvidia_torch_communication
uv sync
uv run main.py
```

- 我的输出

```txt
2.9.1+cu130
13.0
True
```
第三行是true就行
