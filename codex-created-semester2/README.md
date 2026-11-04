# Codex 제작 · 2학기 1~4주차

2026-11-04 사용자 요청으로 만든 별도 제작본이다. 원본 docs와 1학기 폴더·도구·진행 기록은 수정하지 않는다. 검토 후 이 폴더만 커밋·푸시하도록 사용자에게 요청받았다.

원본 기준은 초안 상태다. 이번 요청 범위만 별도로 제작했으며 기준 상태를 확정으로 바꾸지 않았다. 1주차 샘플과 2~4주차를 함께 검토할 수 있도록 제공한다.

| 주차 | 미니 | 도전 | 교안 |
|---|---|---|---|
| 1 | 기분 이모지 | 국기 그리기 챌린지 | [열기](worksheets/semester2/week01/lesson.html) |
| 2 | 바람개비 | 스피로그래프 만다라 | [열기](worksheets/semester2/week02/lesson.html) |
| 3 | 롤리팝 가게 | 제너러티브 아트 배경화면 | [열기](worksheets/semester2/week03/lesson.html) |
| 4 | 세계의 산 높이 정렬 | 우리 반 설문 막대그래프 | [열기](worksheets/semester2/week04/lesson.html) |

각 주차: lesson.html, README.md, lesson_spec.py, warmup.py, mini_starter.py, mini_solution.py, mini_change_solution.py, extension_starter.py, extension_solution.py, answer_key.md, teacher_guide.md.

lesson.html을 브라우저에서 열면 교안, 인쇄하면 학습지다. A4·배경 그래픽 켜기·머리글/바닥글 끄기를 권한다. 실습은 그림 창을 지원하는 데스크톱 Python에서 진행한다.

터틀 주차는 각 단계 실행 때 마지막에 t.done()을 한 번 둔다. 다음 단계는 그 줄 위에 이어 쓴다. 원래 템플릿의 스타일을 유지했고 힌트 한 열·인쇄 여백을 별도 스타일로 조정했다. 완성 그림은 실제 미니 코드의 이동 명령으로 생성한 정적 인라인 SVG이며 앱 화면 캡처는 아니다. 외부 그림 파일이나 웹 스크립트를 사용하지 않는다.

제작 근거: 원본 docs의 curriculum, 01~05 기준, decisions, lesson-template 및 1학기 설계 파일. 내용 수정은 각 주차 lesson_spec.py에서 하고 저장소 루트에서 `python codex-created-semester2/build.py`를 실행한다. 생성기는 설계 파일을 덮어쓰지 않는다. mini_change_solution.py는 교사용 바꾸기 완성 예시다. 원본 도구와 별도로 둔 생성기를 사용한다. 검증 범위와 결과는 VALIDATION.md에 기록한다.

교육 콘텐츠 검토 결과는 REVIEW.md에 있다. 내용 검사는 저장소 루트에서 `python codex-created-semester2/check_content.py`로 다시 실행한다. 학생과의 실제 수업 검증은 아직 수행하지 않았다.
