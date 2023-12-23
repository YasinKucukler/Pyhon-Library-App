from google.colab import drive
drive.mount('/content/drive/')

dosya = open("/content/drive/My Drive/EssentialAIBootcamp/Book_List.txt","w")
dosya.close()

dosya = open("/content/drive/My Drive/EssentialAIBootcamp/Menu.txt","w", encoding  ="utf8")
menü = """

\tPython Kütüphane Uygulamasına Hoş Geldiniz


1) Kütüphaneye Kitap Ekle
2) Kitap Al
3) Kitap Teslim Et
4) Güncel Kitap Listesi
5) Genel Kütüphane Listesi (Tüm kitaplar => Okuyucuda olanlar ve kütüphanede bulunanlar.)
Q) Çıkış


"""
dosya.write(menü)
dosya.close()
dosya = open("/content/drive/My Drive/EssentialAIBootcamp/Menu.txt","r",encoding = "utf8")
print(dosya.read())
dosya.close()
personalKey = "123"

dosya = open("/content/drive/My Drive/EssentialAIBootcamp/MainLibrary.txt","w")
dosya.write("")
dosya.close()

dosya = open("/content/drive/My Drive/EssentialAIBootcamp/MainLibrary.txt","a",encoding = "utf8")
dosya.close()

def showBookList():
  with open("/content/drive/My Drive/EssentialAIBootcamp/Book_List.txt","r",encoding = "utf8") as dosya:
    books = dosya.readlines()
    for book in books:
      print(book, end = "")

def addBookToLibrary(bookName):

  with open("/content/drive/My Drive/EssentialAIBootcamp/Book_List.txt","a",encoding = "utf8") as dosya:
    dosya.write(f"{bookName}\n")

  with open("/content/drive/My Drive/EssentialAIBootcamp/MainLibrary.txt","a",encoding = "utf8") as dosya:
    dosya.write(f"{bookName}\n")

  print(bookName + " isimli kitap kütüphane listesine eklendi")

def deliverBookToLibrary(bookName):
  with open("/content/drive/My Drive/EssentialAIBootcamp/MainLibrary.txt","r",encoding = "utf8") as mainLib:
    check = any(bookName in line for line in mainLib.readlines())

  if check:
    with open("/content/drive/My Drive/EssentialAIBootcamp/Book_List.txt","a",encoding = "utf8") as dosya:
      dosya.write(f"{bookName}\n")
      print(f"{bookName} kütüphaneye teslim edildi ve mevcut kitap listesine eklendi.")
  else:
    print(f"{bookName} kütüphaneye ait bir kitap değildir, Kitabı kütüphaneye eklemek istiyorsanız \" 1 \" seçeneğinden ilerleyiniz.")


def receiveBookFromLibrary(bookName):
  with open("/content/drive/My Drive/EssentialAIBootcamp/Book_List.txt","r",encoding = "utf8") as dosya:
    books = dosya.readlines()
  #Kitap listede var ise true döndüreceğiz
  isAvailable = False
  with open("/content/drive/My Drive/EssentialAIBootcamp/Book_List.txt","w",encoding = "utf8") as dosya:
    for book in books:
      if book.strip("\n") != bookName:
        dosya.write(book)
        print("Böyle bir kitap kütüphanede bulunmamaktadır!!")

      else:
        isAvailable = True
        print(f"{bookName} kitabı okuyucuya teslim edildi. Ve elde kütüphanede mevcut kitaplar listesinden çıkartıldı.")

  dosya.close()
def showWholeLibrary():
  with open("/content/drive/My Drive/EssentialAIBootcamp/MainLibrary.txt","r",encoding = "utf8") as dosya:
    books = dosya.readlines()
    for book in books:
      print(book)


def quitFromMenu():
  print("------Bizi tercih ettiğiniz için teşekkür ederiz--------")
  quit()



#User Interface
while 1:
  dosya = open("/content/drive/My Drive/EssentialAIBootcamp/Menu.txt","r", encoding = "utf8")

  menuOption = input("Lütfen yapmak istediğiniz operasyonu seçiniz(1  -  5): ")

  if menuOption == "1":

    newBook = input("Eklemek istediğiniz kitaba ait bilgileri giriniz : ")
    addBookToLibrary(newBook)
  elif menuOption == "2":
    book = input("Kütüphaneden teslim almak istediğiniz kitabın adını giriniz : ")
    receiveBookFromLibrary(book)
  elif menuOption == "3":
    book = input("Kütüphaneye teslim etmek istediğiniz kitabın ismini giriniz : ")
    deliverBookToLibrary(book)
  elif menuOption == "4":
    showBookList()
  elif menuOption == "5":
    showWholeLibrary()
  elif menuOption == "q" or menuOption == "Q":
    quitFromMenu()
    break
  else:
    print("Hatalı bir işlem girdiniz lütfen tekrar deneyiniz !!!")
dosya.close()


