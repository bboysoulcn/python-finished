import requests
import os


def mkdir(path):
    print("mkdir调用成功")
    isExists=os.path.exists(path)
    if isExists==True:
        print("目录已经存在,不创建目录")
    else:
        os.mkdir(path)
        print("目录创建成功")


def image_download(image_id_start,image_id_stop):
    for image_id in range(image_id_start,image_id_stop+1):
        img_url="https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-"+str(image_id)+".jpg"
        filename = str(image_id)+".jpeg"
        with open(filename,"wb") as f: # 以只写二进制形式打开文件
            img = requests.get(img_url)# 下载图片
            f.write(img.content)# 写入图片
            f.close()# 关闭文件
            print("第"+str(image_id)+"张图片下载完成") # 提示图片下载完成


image_id_start=int(input("请输入图片开始地址："))
image_id_stop=int(input("请输入图片结束地址："))
path=input("请输入图片存放的文件夹：")
mkdir(path) #创建目录
os.chdir(path) # 修改当前目录
image_download(image_id_start,image_id_stop)
print("所有图片下载完成")



# todo
# 增加创建文件夹功能
# 判断图片大小，如果小于1k那么输出这张图片不存在并且删除文件
# 把日志写入文件
# 下载进度条