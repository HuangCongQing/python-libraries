from transformers import pipeline
from PIL import Image
import requests
import os
import numpy as np
import matplotlib.pyplot as plt
# // 设置环境变量
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# load pipe
pipe = pipeline(task="depth-estimation", model="depth-anything/Depth-Anything-V2-Small-hf")

# load image
url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

# inference
depth = pipe(image)["depth"]
# 将 PIL Image 转换为 numpy 数组
depth_np = np.array(depth)
print("Depth shape:", depth_np.shape)
print("Depth:", depth_np)

# 创建保存目录
save_dir = "depth_results"
os.makedirs(save_dir, exist_ok=True)

# 保存原始图像
image.save(os.path.join(save_dir, "original_image.jpg"))

# 保存深度图
plt.figure(figsize=(12, 6))

# 显示原始图像
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# 显示深度图
plt.subplot(1, 2, 2)
plt.imshow(depth_np, cmap='plasma')  # 使用 plasma 颜色映射
plt.colorbar(label='Depth')
plt.title('Depth Map')
plt.axis('off')

plt.tight_layout()

# 保存对比图
plt.savefig(os.path.join(save_dir, "depth_comparison.png"), dpi=300, bbox_inches='tight')

# 单独保存深度图
plt.figure(figsize=(8, 6))
plt.imshow(depth_np, cmap='plasma')
plt.colorbar(label='Depth')
plt.title('Depth Map')
plt.axis('off')
plt.savefig(os.path.join(save_dir, "depth_map.png"), dpi=300, bbox_inches='tight')

plt.show()