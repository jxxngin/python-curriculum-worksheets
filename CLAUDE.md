# 파이썬 1년 커리큘럼 워크시트 저장소

초등 5~6학년 소그룹 파이썬 수업용 주차별 교안(웹에서 보고 인쇄해서도 쓰는 `lesson.html`)을 만든다.

## 먼저 읽을 것

**모든 기준은 [docs/](docs/README.md)에 있다.** 작업을 시작하기 전에 `docs/README.md`와 거기 나열된 문서를 모두 읽는다.

- 커리큘럼: [docs/curriculum.md](docs/curriculum.md)
- 교안 형식: [docs/01-worksheet-format.md](docs/01-worksheet-format.md)
- 내용 규칙: [docs/02-content-rules.md](docs/02-content-rules.md)
- 파일 구성과 정답지: [docs/03-files-and-answer-key.md](docs/03-files-and-answer-key.md)
- 점검 체크리스트: [docs/04-review-checklist.md](docs/04-review-checklist.md)
- 제작 절차: [docs/05-production-workflow.md](docs/05-production-workflow.md)
- 결정 기록: [docs/decisions.md](docs/decisions.md)
- 틀: [docs/templates/lesson-template.html](docs/templates/lesson-template.html)

## 제작 게이트

- `docs/README.md`의 **기준 상태가 `확정`일 때만** 새 워크시트를 만든다.
- `초안`이면 워크시트를 만들지 않는다. 기준 문서와 템플릿만 고친다.
- 기준 상태는 저장소 주인만 바꾼다.

## 작업 원칙

- 저장소 주인의 피드백은 `docs/decisions.md`에 날짜와 함께 기록하고, 관련 기준 문서에도 반영한다.
- 더 나은 대안이 있거나 피드백에 문제가 있어 보이면 그냥 따르지 말고 선택지와 추천을 제시한다.
- 검사 도구: `python tools/check_worksheet.py <lesson.html 또는 worksheet.html>`
