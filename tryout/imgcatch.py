#coding=utf-8   
   
import os   
import sys   
import re   
import urllib.request

URL_REG = re.compile(r'(http://[^/\\]+)', re.I)
IMG_REG = re.compile(r'<img[^>]*?src=([\'"])([^\1]*?)\1', re.I)

def download(dir1,url):
    global URL_REG, IMG_REG

    m = URL_REG.match(url)
    if not m:
        print ('[Error] Invalid URL: ', url)
        return

    if not os.path.isdir(dir1):
        os.mkdir(dir1)

    html = urllib.request.urlopen(url).read().decode("gbk")
    
    with open('C:/Imgs/thefile.txt', 'w') as file_object:
        file_object.write(html)
''' 
    imgs = [item[1].lower() for item in IMG_REG.findall(html)]
    f = lambda path: path if path.startswith('http://') else \
        host + path if path.startswith('/') else url + '/' + path
    imgs = list(set(map(f,imgs)))
    print ('[Info]Find %d images.' % len(imgs))

    for idx, img in enumerate(imgs):
        name = img.split('/')[-1]
        path = os.path.join(dir,name)
        try:
            print ('[Info]Download(%d): %s' % (idx + 1,img))
            urllib.urlretrieve(img,path)
        except:
            print ("[Error]Cant't download(%d): %s" % (idx + 1, img))
'''
def main():
    '''
        if len(sys.argv)!=3:
            print ('Invalid argument count')
            return
        dir,url=sys.argv[1:]
    '''
    download('C:\Imgs','http://www.163.com')

if __name__ == '__main__':
    main() 
