from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def get_details(fileName = ''):
        '''
        传入图片名，显示基础参数
        '''
        im = Image.open(fileName)
        #im.show()
        print("图片类型为\t%s" % im.format)
        print("图片大小为\t" + str(im.size))
        print("图片颜色通道模式为\t" + im.mode)
        #r,g,b = im.split()     #通道分割
        #im = Image.merge("RGB", (g,r,b))       #rgb翻转
        #im.save('lena_rgb.jpg')

def disRGB():
   NO = 0

#   int(r[NO]),int(0),int(0)
   
   for i in range(0,length):
       for j in range(0,width):
           r_im.putpixel((i,j),(  ))#rgb转化为像素
           NO += 1
   r_im.show()

    
   NO = 0
   for i in range(0,length):
       for j in range(0,width):
           g_im.putpixel((i,j),(int(0),int(g[NO]),int(0)))#rgb转化为像素
           NO += 1
   g_im.show()
    
   NO = 0
   for i in range(0,length):
       for j in range(0,width):
           b_im.putpixel((i,j),(int(0),int(0),int(b[NO])))#rgb转化为像素
           NO += 1
   b_im.show()
    
def toGray(fileName=''):
    #img = Image.open(fileName)
    img = Image.open(fileName)
    length, width = img.size

    r_im = Image.new("RGB",(length, width))
    g_im = Image.new("RGB",(length, width))
    b_im = Image.new("RGB",(length, width))
    r = getRGB(sw='r', fileName=fileName)
    g = getRGB(sw='g', fileName=fileName)
    b = getRGB(sw='b', fileName=fileName)
    
    Gray = R*0.299 + G*0.587 + B*0.114
  
def getRGB(sw='', fileName=''):
    img = Image.open(fileName)
    im = img.load()
    length, width = img.size

    r_list = []
    g_list = []
    b_list = []
    
    for i in range(0, length):
        for j in range(0, width):
            r, g, b = im[i, j]
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)

    if (sw == 'r'):
        return r_list
    #    te = input
    if (sw == 'g'):
        return g_list
   #     te = input
    if (sw == 'b'):
        return b_list
    #    te = input    
    return 0

def do2(T = '',fileName = ''):
        '''
        传入t，用给定t进行二值化
        '''
        if len(fileName) == 0:
                print('未传入图片名')
                return False
        print('开始二值化,T=' + str(T))
        img = np.array(Image.open(fileName).convert('L'))
        rows, cols = img.shape
        for i in range(rows):
                for j in range(cols):
                        if (img[i, j] <= T):
                                img[i, j] = 0
                        else:
                                img[i, j] = 1
        
        processName = fileName + "的二值化图, T=" + str(T)
        plt.figure(processName)
        plt.imshow(img, cmap='gray')
        plt.axis('off')
        plt.show()


def otsu(fileName = ''):
        '''
        类判别分析法（otsu）求二值化的阈值T

        假设我们使用阈值T将灰度图像分割为前景和背景
        size：图像总像素个数
        u：图像的平均灰度
        w0：前景像素点占整幅图像大小的比例
        u0：前景像素点的平均值
        w1：背景像素点占整幅图像大小的比例
        u0：背景像素点的平均值
        g：类间方差
        u = w0 * u0 + w1 * u1  (1)
        g = w0*(u - u0)^2 + w1*(u - u1)^2 (2)
        将(1)代入(2)得：
        g = w0 * w1 * (u0 - u1)^2
        采用遍历的方法，遍历所有阈值，当g最大时，该阈值就是我们所求的认为最合适的阈值了。 
        '''
        if len(fileName) == 0:
                print('otsu函数，未接收到图片名')
                return False
        im = Image.open(fileName)
        im_gray = im.convert('L') 
        size = im_gray.size[0] * im_gray.size[1]

        max_g = 0
        suitable_th = 0

        im_gray = np.array(im_gray)     #图像转numpy中ndarray

        for threshold in range(0, 255, 1):
                bin_img = im_gray > threshold
                bin_img_inv = im_gray <= threshold
                #大于和小于等于给定临时T，通过比较获取两个大于或者小于等于临时T的nparray，两个数组的组成元素为True和False
                fore_pix = np.sum(bin_img)
                back_pix = np.sum(bin_img_inv)
                #统计True个数，即当前大于或者小于等于T的像素点个数
                if 0 == fore_pix:
                #如果前景中的像素点统计为0，由于T从0-255递增，如果没有大于T最大值，即255的像素点时，即代表遍历完毕。
                        break
                if 0 == back_pix:
                #如果背景像素点为0个，即没有小于临时T的像素点，跳过本轮，让T自增1继续进行统计
                        continue

                w0 = float(fore_pix) / im_gray.size
                #求前景所有像素点个数/所有像素点的比例
                u0 = float(np.sum(im_gray * bin_img)) / fore_pix
                #im_gray * bin_img，[true, false]*[1,2]=[1, 0],false对应转化为0，其余不变.
                #np.sum的axis默认为0，所以统计本行统计非0的累计和，np.sum([1,2,3,0])结果为6
                w1 = float(back_pix) / im_gray.size
                u1 = float(np.sum(im_gray * bin_img_inv)) / back_pix
                g = w0 * w1 * (u0 - u1) * (u0 - u1)
                #套用公式，求出类间方差g
                if g > max_g:
                #过滤出最大的类间方差，并提取对应的T
                        max_g = g
                        suitable_th = threshold
        return suitable_th
        #返回最大的T，即为OTSU法求出的最合适T
        




def gethist(fileName = ''):
        '''
        输出指定文件的直方图
        '''
        im = pylab.array(Image.open(fileName).convert('L'))
        processName = fileName + '直方图'
        plt.figure(processName)
        arr = im.flatten()
        n, bins, patches = plt.hist(arr, bins=256, facecolor='red', alpha=0.75)
        plt.show()




if __name__ == '__main__':
        fileName = './lena.png'
        #gethist(fileName)
        toGray(fileName)
 #       T = otsu(fileName)
 #       do2(T, fileName)


