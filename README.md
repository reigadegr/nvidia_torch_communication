## 测试英伟达显卡能否与torch通信
- 用conda的已经是老登了，我们用现代化的uv

```bash
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
