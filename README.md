# blepy-subtitle
![image](https://user-images.githubusercontent.com/36142378/81881805-1536c780-95cc-11ea-9c70-a32e978de90b.png)

[블피님 영상](https://youtu.be/-y2exeNNIR8)을 보고 제작해본 파이썬 자동 자막 제작 스크립트입니다.

[ZIP 파일로 다운로드](https://github.com/kimcoreovo/blepy-subtitle/archive/master.zip)
# 필수 라이브러리 설치
Win + R 을 누르시고 `pip install photoshop_python_api` 를 실행하시면 됩니다.
# 실행
Win + R 을 누르시고 `cmd`창에서 `python ble.py`를 실행하시거나 더블클릭 하시면 됩니다.
# 사용법
1. '자막 불러오기' 버튼을 눌러서 자막 TXT 파일을 불러옵니다.
2. '레이어 번호' 칸에 포토샵에서의 자막 레이어 번호를 입력합니다.
3. '자동 자막' 버튼을 누르면 자막 PSD 파일들을 저장할 폴더를 선택하는 창이 나옵니다.
4. 폴더를 선택하면 잠시후에 성공했다는 창이 뜨며 선택한 폴더에 자막이 생성됩니다.
# 주의사항
자막은
```
1
첫번째 자막
2
두번째 자막
```
이런 형식이 아닌
```
첫번째 자막
두번째 자막
```
이런 형식으로 되어있어야 합니다.
