import random
import tkinter as tk
from PIL import Image, ImageTk

# 表示文字配列
kekka = ['カレーライス', 'ハンバーグ', 'パスタ', 'ラーメン', '寿司']

# 画像ファイル名配列
file = [
    './data/curry.jpg',
    './data/hamburger.jpg',
    './data/pasuta.jpg',
    './data/ramen.jpg',
    './data/sushi.jpg',
]

# 「ガチャを引く」ボタンの処理
#1 random.choice()を使って、配列kekkaから文字をランダム取得
#2 label.configure()でボタン押下後、ラベルを料理名に変更する処理
#3 command= は、ボタン押下に実行する関数(title)を記述
#4 itemconfigure(初期画像, image=表示する画像, ラベルの文字と画像を紐付けて表示)
#5 .index(取得したインデックスと同じインデックスにあるファイル名を取得)
def gamenmoji():
    # ランダムで表示文字取得
    randomResult = random.choice(kekka) #1
    # ラベル変更
    label.configure(text=randomResult, font=('', 80)) #2
    # ボタン変更
    button.configure(text='タイトルへ', font=('', 30), command=title) #3
    #画像変更（ランダム文字に紐づく画像に変更）
    canvas.itemconfigure(canvasImage, image=fileList[kekka.index(randomResult)]) #4 #5

# 「タイトルへ」ボタンの処理
def title():
    # ラベル変更
    label.configure(text='今日、何食べる？', font=('', 30))
    # ボタン変更
    button.configure(text='ガチャを引く', font=('', 30), command=gamenmoji)
    # 画像変更（初期画像に戻す）
    canvas.itemconfig(canvasImage, image=cooking)


# 画面作成
gamen = tk.Tk()
# 画面タイトル名
gamen.title('何食べるガチャ')
# 画面サイズ
gamen.geometry('790x750')

# 画像表示領域
canvas = tk.Canvas(bg='white', width=780, height=516)
# 画面上の表示位置
canvas.place(x=0, y=200)

# ラベル
label = tk.Label(text='今日、何食べる？', font=('', 30))
# ボタン
button = tk.Button(text='ガチャを引く', font=('', 30), command=gamenmoji)

# ラベル配置
label.pack()
# ボタン配置
button.pack()

# 画像取得＆リサイズ処理
#1 Image.open()---画像取得
#2 ImageTk.PhotoImage()---'tkinter'で扱える画像ファイル形式に変換
#3 resize()---画面サイズ変更、size=(幅、高さ)と指定
def openAndResize(sozai):
    open_jpg = Image.open(sozai) #1
    change_jpg = ImageTk.PhotoImage(open_jpg.resize(size=(768,512))) #2 #3
    return change_jpg

# 初期画像
#1 canvas.create_image()---画像領域に画像表示, (左端から'x'、上端から'ｙ')
#2 anchor---画像のどの箇所から座標を合わせるか指定
#3 anchor=tk.NW---画像の左上を座標に合わせる
cooking = openAndResize('./data/kitchen.jpg')
canvasImage = canvas.create_image(10, 0, image=cooking, anchor=tk.NW) #1 #2 #3

# 取得した画像ファイルのオブジェクト格納配列
fileList = []

# 画像ファイルを全て読み込み配列に格納
#1 定義した関数を使って、全ての画像取得とリサイズをする
#2 取得した画像をobjに格納し、append()でfileList配列に追加
for name in file:
    obj = openAndResize(name) #1
    fileList.append(obj) #2

#tkinter使用後、ソースコードの最後にmainloop()を記入
gamen.mainloop()

