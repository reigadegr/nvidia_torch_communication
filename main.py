import tensorflow as tf
import torch


def main():
    print(tf.__version__)
    print("GPU", tf.test.is_gpu_available())

    # 检查是否有可用的 GPU，并设置使用的 GPU
    device_id = 0  # 设置为要使用的 GPU 的 ID
    if torch.cuda.is_available():
        device = torch.device(f"cuda:{device_id}")
    else:
        device = torch.device("cpu")
    print(f"Using device: {device}")

    # 打印 CUDA 相关信息
    print("CUDA available: ", torch.cuda.is_available())
    print("CUDA device count: ", torch.cuda.device_count())
    if torch.cuda.is_available():
        print("CUDA current device: ", torch.cuda.current_device())
        print("CUDA device name: ", torch.cuda.get_device_name(device_id))
        print(f"CUDA version: {torch.version.cuda}")

    print(torch.__version__)
    print(torch.version.cuda)
    print(torch.cuda.is_available())  # 输出为True，则安装无误


if __name__ == "__main__":
    main()
