import _ctypes
from tkinter import *  # UI 라이브러리
from tkinter.ttk import *  # UI 라이브러리
from tkinter.messagebox import *  # UI 라이브러리
from tkinter.filedialog import askopenfilename  # 파일 열기 창 띄우는 함수
from tkinter.filedialog import askdirectory  # 폴더 열기 창 띄우는 함수
import photoshop.api as ps  # 포토샵 연계 라이브러리


def open_subtitle():  # 자막 파일을 불러오는 함수
    global subtitles  # 함수 밖의 subtitles 변수를 사용하겠다는 선언
    filename = askopenfilename()  # 파일 열기 창
    if filename == "":  # 사용자가 취소
        return
    elif not filename.endswith(".txt"):  # TXT 파일이 아닐 경우
        showerror("에러", "자막 파일은 TXT 형식이여야 합니다.")
        return
    label['text'] = filename.split("/")[-1]  # 버튼위의 파일명 텍스트를 파일명으로 변경
    subtitles = open(filename, 'r', encoding='utf-8').read().splitlines()  # 불러온 자막파일을 줄별로 나눔


def do():  # 포토샵 연계로 자막을 넣는 함수
    if len(subtitles) == 0:  # subtitles 함수가 비어있을때
        showerror("에러", "자막 파일을 불러오지 않았거나 자막 파일이 비어있어요.")
        return
    if entry.get() == "":  # 자막 레이어 번호를 입력하지 않았을때
        showerror("에러", "먼저 자막 레이어의 번호를 입력해주세요.")
        return
    try:
        photoshop = ps.Application()  # 포토샵 연계, 포토샵이 실행되지 않았을 경우 실행
    except FileNotFoundError:
        showerror("에러", "포토샵이 설치되어 있지 않은 것 같습니다. 참고로 포터블은 지원되지 않습니다.")
        return
    try:
        doc = photoshop.activeDocument  # 열려있는 PSD 파일 불러오기
    except _ctypes.COMError:
        showerror("에러", "먼저 포토샵에서 PSD 파일을 열어주세요.")
        return
    layer = doc.ArtLayers[int(entry.get()) - 1]  # 레이어 번호로 레이어 불러오기
    folder = askdirectory()  # 자막을 저장할 폴더 묻기
    i = 1
    for subtitle in subtitles:  # 자막 리스트의 자막마다 실행
        layer.TextItem.Contents = subtitle  # 자막 레이어 텍스트 변경
        path = folder + "\\" + str(i) + ".psd"  # 자막 파일명
        options = ps.PhotoshopSaveOptions()
        options.embedColorProfile = True
        options.alphaChannels = True
        doc.saveAs(path, options, False)  # 다른 이름으로 저장
        i += 1
    showinfo("성공", str(i - 1) + "개의 자막 PSD 파일을 생성했습니다.")


def validate(value):  # 레이어 번호 입력시마다 숫자인지 아닌지 체크하는 함수
    if value == "":  # 비어있으면 통과
        return True
    elif value:
        try:
            int(value)
            return True
        except ValueError:
            return False
    else:
        return False


root = Tk()  # UI
root.title("자동 자막")  # UI 제목
root.geometry("250x150")  # UI 크기
root.resizable(False, False)  # 사용자가 UI 크기 조정을 못하게 막음
vcmd = (root.register(validate))  # 레이어 번호 숫자 체크 함수
label = Label(root, text="")  # 버튼위의 파일명 텍스트
label.place(relx=0.5, rely=0.1, anchor=CENTER)
button = Button(root, text="자막 불러오기", command=open_subtitle)  # 자막 불러오기 버튼, 클릭시 open_subtitle() 함수 실행
button.place(relx=0.5, rely=0.3, anchor=CENTER)
label2 = Label(root, text="레이어 번호")  # 레이어 번호 텍스트
label2.place(relx=0.4, rely=0.5, anchor=CENTER)
entry = Entry(root, width=5, validate='all', validatecommand=(vcmd, '%P'))  # 레이어 번호 입력
entry.place(relx=0.65, rely=0.5, anchor=CENTER)
button2 = Button(root, text="자동 자막", command=do)  # 레이어 번호 입력, 클릭시 do() 함수 실행
button2.place(relx=0.5, rely=0.7, anchor=CENTER)
subtitles = []  # 자막 리스트
root.mainloop()  # UI 실행
