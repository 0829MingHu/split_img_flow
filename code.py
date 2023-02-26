import os
import shutil

# 创建目标文件夹
file_data = r'D:\kaust\file'
file_img_flow = r'D:\kaust\data/'
if not os.path.exists(file_img_flow):
    os.mkdir(file_img_flow)
if not os.path.exists(file_img_flow+'img'):
    os.mkdir(file_img_flow+'img')
if not os.path.exists(file_img_flow+'flow'):
    os.mkdir(file_img_flow+'flow')

# 遍历rgb_flow1目录下的所有video_id的目录
for video_dir in os.listdir(file_data):
    video_id_dir = os.path.join(file_data, video_dir)
    if not os.path.isdir(video_id_dir):
        continue
        
    img_dir = os.path.join(file_img_flow+'img', video_dir)
    flow_dir = os.path.join(file_img_flow+'flow', video_dir)
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(flow_dir, exist_ok=True)

    # 遍历video_id目录下的所有文件
    for filename in os.listdir(video_id_dir):
        if filename.startswith('img'):
            # 如果是img前缀的文件，将其移动到img目录下的video_id目录中
            src_file = os.path.join(video_id_dir, filename)
            dst_file = os.path.join(img_dir, filename)
            shutil.move(src_file, dst_file)
        elif filename.startswith('flow'):
            # 如果是flow前缀的文件，将其移动到flow目录下的video_id目录中
            src_file = os.path.join(video_id_dir, filename)
            dst_file = os.path.join(flow_dir, filename)
            shutil.move(src_file, dst_file)
