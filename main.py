import torch


def main():
    print(torch.__version__)
    print(torch.version.cuda)
    print(torch.cuda.is_available())  # 输出为True，则安装无误


if __name__ == "__main__":
    main()
