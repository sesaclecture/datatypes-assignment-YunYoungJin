# ==========================
# assignment_drama_template.py (학생용 템플릿)
# 조건: 함수/조건문/반복문 금지. 변수 선언과 input(), print()만 사용.
# ==========================

drama1 = {
    "제목": "서초동",
    "장르": "법정, 오피스, 로맨스, 휴먼, 청춘, 성장, 일상", 
    "주제": "어쏘 변호사 5인방의 희로애락 성장기",
    "방영기간": "2025-07-05 ~ 2025-08-10",
    "배우": ["이종석", "문가영", "강유석", "류혜영", "임성재"],
    "명대사": "\"자꾸 중요한 이야기를 뒤에 하시네.\""
}

drama2 = {
    "제목": "에스콰이어",
    "장르": "법정, 오피스, 성장, 휴먼, 로맨스",
    "주제": "정의롭고 당차지만 사회생활에 서툰 신입 변호사, 완전한 변호사로 성장해 나가는 이야기", 
    "방영기간": "2025-08-02 ~ 2025-09-07",
    "배우": ["이진욱", "정채연", "이학주", "전혜빈"],
    "명대사": "\"링 안에서 불리하면 링 밖으로 끌고 와서 한판 붙어봐야죠.\""
}

new_title = input("새 드라마 제목: ")  

new_genre = input("새 드라마 장르: ")
new_theme = input("새 드라마 주제: ")
new_period = input("새 드라마 방영기간(예: 2024-01-01 ~ 2024-02-01): ")
new_actors_input = input("새 드라마 배우들(쉼표로 구분): ")
new_quote_raw = input("인상 깊었던 대사(따옴표 없이 입력): ")

new_actors = new_actors_input.split(",")
new_quote = f"\"{new_quote_raw}\""

drama3 = {
    "제목": new_title,
    "장르": new_genre,
    "주제": new_theme,
    "방영기간": new_period,
    "배우": new_actors,
    "명대사": new_quote
}


upd_title = input("수정(덮어쓰기)할 제목(대상: drama2): ")  
upd_genre = input("수정할 장르: ")
upd_theme = input("수정할 주제: ")
upd_period = input("수정할 방영기간: ")
upd_actors_input = input("수정할 배우들(쉼표로 구분): ")
upd_quote_raw = input("수정할 명대사(따옴표 없이 입력): ")

upd_actors = upd_actors_input.split(",")
upd_quote = f"\"{upd_quote_raw}\""

drama2["제목"] = upd_title
drama2["장르"] = upd_genre
drama2["주제"] = upd_theme
drama2["방영기간"] = upd_period
drama2["배우"] = upd_actors
drama2["명대사"] = upd_quote

print("\n[드라마 1]")
print(f"제목: {drama1['제목']}")
print(f"장르: {drama1['장르']}")
print(f"주제: {drama1['주제']}")
print(f"방영기간: {drama1['방영기간']}")
print(f"배우: {drama1['배우']}")
print(f"명대사: {drama1['명대사']}")

print("\n[드라마 2]  # 수정 후")
print(f"제목: {drama2['제목']}")
print(f"장르: {drama2['장르']}")
print(f"주제: {drama2['주제']}")
print(f"방영기간: {drama2['방영기간']}")
print(f"배우: {drama2['배우']}")
print(f"명대사: {drama2['명대사']}")

print("\n[드라마 3]  # 새로 추가")
print(f"제목: {drama3['제목']}")
print(f"장르: {drama3['장르']}")
print(f"주제: {drama3['주제']}")
print(f"방영기간: {drama3['방영기간']}")
print(f"배우: {drama3['배우']}")
print(f"명대사: {drama3['명대사']}")
