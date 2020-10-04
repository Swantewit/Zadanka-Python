import os, shutil, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
  
print("Wpisz ścieżkę do folderu, z którego chcesz usunąć największe pliki") 
path1 = os.path.abspath(input())
print("Wpisz ścieżkę, gdzie chcesz utworzyć folder, z usuniętymi plikami")
path2 = os.path.abspath(input())
path3 = path2 + '/DoUsunięcia'

#Definicje zmiennych
size = 0
sizeList = []
fileList = []
fileListoList = []
fullList = 0

maxSize = 0
filePath = ''
bigFile = ''
bigFilePath = ''
bigFilePathRem = ''

#Funkcja znajdź i usuń
def SeekNDelete():
    for folder, subfolders, files in os.walk(path1):
      
        for file in files:
            size = os.stat(os.path.join( folder, file )).st_size
            sizeList.append(size)
            filePath = os.path.join( folder, file )
            fileList = [file, filePath, size]
            fileListoList.append(fileList)
            
    sizeListSort = sorted(sizeList)

    for j in range (3):
        maxSize = sizeListSort[-1]
        for i in fileListoList:
            if maxSize in i:
                bigFilePath = i[1]
                bigFile = i[0]
                bigFilePathRem = os.path.join( path3, bigFile )
                shutil.move( bigFilePath, bigFilePathRem )
                print('Przesuwam ' + str(bigFile) + ' do ' + str(path3))
                fileListoList.remove(i)
                sizeListSort.remove(maxSize)

try:
    os.mkdir(path3)
except OSError as error: 
    print('Folder został już wcześniej utworzony')
    SeekNDelete()
    

SeekNDelete()







        
            

