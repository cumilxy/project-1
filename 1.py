import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
 
from PIL import Image


from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask
)
app = QApplication([])

'''Інтерфейс програми'''
window = QWidget()
window.setWindowTitle('Фотошопчик')
window.resize(900,600)

move_left = QPushButton('Вліво')
move_left.setStyleSheet("background-color:lightgreen; color:olive")
move_right = QPushButton('Вправо')
move_right.setStyleSheet("background-color:lightgreen; color:olive")
mirrorro = QPushButton('Дзеркало')
mirrorro.setStyleSheet("background-color:lightgreen; color:olive")
blur_knopka = QPushButton('Різкість')
blur_knopka.setStyleSheet("background-color:lightgreen; color:olive")
BandW_knopka = QPushButton('Ч\Б')
BandW_knopka.setStyleSheet("background-color:lightgreen; color:olive")
folderrr = QPushButton('ПАПКА')
folderrr.setStyleSheet("background-color:lightgreen; color:olive")
list_things = QListWidget()
list_things.setStyleSheet("background-color:wheat; color:black")

krashcha_rizkist = QPushButton('Різкість')
krashcha_rizkist.setStyleSheet("background-color:lightgreen; color:olive")
kontur = QPushButton('Контур')
kontur.setStyleSheet("background-color:lightgreen; color:olive")
gladko = QPushButton('Зглажування')
gladko.setStyleSheet("background-color:lightgreen; color:olive")
detal = QPushButton('Деталізація')
detal.setStyleSheet("background-color:lightgreen; color:olive")
BandW_knopka2 = QPushButton('Ч\Б')
BandW_knopka2.setStyleSheet("background-color:lightgreen; color:olive")
folderrr2 = QPushButton('ПАПКА')
folderrr2.setStyleSheet("background-color:lightgreen; color:olive")
list_things2 = QListWidget()
list_things2.setStyleSheet("background-color:wheat; color:black")

pole_with_kartinka = QLabel()
pole_with_kartinka.setStyleSheet("background-color:wheat; color:black")

v1 = QVBoxLayout()
v1.addWidget(folderrr)
v1.addWidget(list_things)

h1 = QHBoxLayout()
h1.addWidget(move_left)
h1.addWidget(move_right)
h1.addWidget(mirrorro)
h1.addWidget(blur_knopka)
h1.addWidget(BandW_knopka)

h1.addWidget(move_left2)
h1.addWidget(move_right2)
h1.addWidget(mirrorro2)
h1.addWidget(Sharpness_knopka2)
h1.addWidget(BandW_knopka2)

v2 = QVBoxLayout()
v2.addWidget(pole_with_kartinka)
v2.addLayout(h1)

h2 = QHBoxLayout()
h2.addLayout(v1)
h2.addLayout(v2)
window.setLayout(h2)
window.show()

def choise_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def filter(files, extensions):
    result = []
    for f in files:
        for e in extensions:
            if f.endswith(e):
                result.append(f)
    return result

def showfiles():
    extensions = ['jpeg','png','svg','jpg']
    choise_workdir()
    filenames = filter(os.listdir(workdir),extensions)
    list_things.clear()
    for f in filenames:
        list_things.addItem(f)
folderrr.clicked.connect(showfiles)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    
    def loadImage(self, filename):
        ''' під час завантаження запам'ятовуємо шлях та ім'я файлу '''
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)
    
    def saveImage(self):
        ''' зберігає копію файлу у підпапці '''
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
    
        self.image.save(fullname)
    #kponky#
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def vpravo(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def vlivo(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def dzerkalo(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    #############################################
    def showImage(self, path):
        pole_with_kartinka.hide()
        pixmapimage = QPixmap(path)
        w, h = pole_with_kartinka.width(), pole_with_kartinka.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        pole_with_kartinka.setPixmap(pixmapimage)
        pole_with_kartinka.show()
 
def showChosenImage():
   if list_things.currentRow() >= 0:
       filename = list_things.currentItem().text()
       workimage.loadImage(filename)
       workimage.showImage(os.path.join(workdir, workimage.filename))
 
workimage = ImageProcessor() #поточне робоче зображення для роботи
list_things.currentRowChanged.connect(showChosenImage)
BandW_knopka.clicked.connect(workimage.do_bw)
move_right.clicked.connect(workimage.vpravo)
move_left.clicked.connect(workimage.vlivo)
mirrorro.clicked.connect(workimage.dzerkalo)
blur_knopka.clicked.connect(workimage.blur)


app.exec()
