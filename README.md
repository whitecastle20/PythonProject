# PythonProject (2020년)
햄버거가게에서 음식을 주문하는 프로젝트입니다. 배경에는 대표적인 햄버거 회사의 사진을 넣었으며, 가시적으로 보기 좋게 큰 카테고리 옆에 이미지를 첨부하여 사용자가 쉽게 찾을 수 있도록 하였습니다.
 프로그램을 시작할 때 뜨는 주문 화면입니다. 큰 카테고리로 분류했을 때,  메뉴에는 단품 버거, 사이드메뉴, 세트메뉴, 음료, 디저트로 총 5개가 있습니다. (위에서부터 아래순) 이 큰 카테고리는 Button을 이용하여 구현하였고, 버튼을 클릭하면 하위 메뉴가 뜹니다.
 
![image](https://user-images.githubusercontent.com/68242854/221752338-a509865c-34df-4771-a7c6-5cbaa97ebeb7.png)

위에서 언급한 큰 카테고리를 클릭하면 새로운 창이 뜹니다. Radiobutton을 이용해서 한 종류의 음식만을 선택할 수 있도록 하였습니다. ‘선택하지 않음’을 제외하고 3개의 구체적인 음식의 종류가 뜹니다. 그리고 라디오 버튼이 클릭되면, 오른쪽에 선택한 메뉴가 뜹니다. 

![image](https://user-images.githubusercontent.com/68242854/221752349-8e40dffb-967d-4623-a986-12dd6f89b942.png)

▲이 사진은 5가지의 카테고리 중 단품 버거를 클릭했을 때 표시되는 창입니다.

![image](https://user-images.githubusercontent.com/68242854/221752429-bf948d84-92b1-4568-81cd-6062f5c41c03.png)

아래쪽에 ‘주문 취소’ 버튼을 누르면 “주문을 취소하시겠습니까?라는 말이 담긴 확인 메시지 창이 뜨며 예를 누르게 되면 프로그램이 종료됩니다.

![image](https://user-images.githubusercontent.com/68242854/221752442-91e842d6-5651-4df0-ab45-1c7068079d44.png)

모든 옵션을 선택한 후, 주문 완료 버튼을 누르면 주문한 내역에 대한 상세 정보가 새로운 창을 통해 표시가 됩니다. 선택했던 메뉴와 가격, 그리고 총 금액이 뜹니다. 맨 아래에는 주문 번호가 뜨는데, 이는 난수를 생성해서 무작위의 수가 뜨도록 하였습니다. 그리고 이용해주셔서 감사하다는 기분 좋은 메시지가 뜨도록 하였습니다.

주의할 점 : 각 큰 카테고리별 고를 수 있는 음식은 한 종류이며, 개수도 1개입니다.  (radiobutton을 이용하여 구현하였기 때문에 1가지만을 선택할 수 있습니다.)
