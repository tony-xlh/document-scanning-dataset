import os

def list_images(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    image_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_list.append(os.path.join(root, file))
    
    return image_list

folder_path = './'  # 替换为你的文件夹路径
images = list_images(folder_path)
print(images)