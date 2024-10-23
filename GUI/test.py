import os
from OMPython import ModelicaSystem

# 自动获取当前脚本目录并拼接模型文件路径
base_path = os.path.dirname(os.path.abspath(__file__))  # 获取脚本文件的目录
model_path = os.path.join(base_path, 'model', 'VirtualBearingTestBench.mo')

print(f"Model path: {model_path}")  # 调试时输出路径，确保正确

m = ModelicaSystem(model_path, 'Library.VirtualBench_layout_v1')
