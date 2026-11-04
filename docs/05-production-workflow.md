# 05. 제작 절차

## 시작 조건

- [README.md](README.md)의 기준 상태가 **확정**일 때만 제작한다.
- `초안`이면 워크시트를 만들지 않고 기준 문서와 템플릿만 고친다.

## 학기 제작 순서

1. **준비:** 학기 진행 파일 `PROGRESS.md`를 만든다. 주차별 줄, 미니 / 확장 프로젝트 이름을 적는다.
2. **샘플:** 그 학기 1주차를 먼저 만들고 점검한 뒤 저장소 주인의 승인을 받는다(P2).
3. **본 제작:** 승인되면 나머지 주차를 앞에서부터 차례로 만든다. 샘플에서 받은 피드백은 먼저 기준 문서에 반영한다.
4. **학기 점검:** 다 만들면 학기 전체를 다시 점검한다. 주차 사이 개념 누적, 오류 종류 분배, 난이도 흐름을 본다.

## 한 주차 만들기

1. [curriculum.md](curriculum.md)에서 그 주차 개념, 미니 / 확장 프로젝트, 보완 메모를 확인한다.
2. 이전 주차 결과물을 훑어서 말투와 난이도를 이어 간다.
3. 파이썬 파일을 먼저 만든다: warmup → starter → solution
4. [templates/lesson-template.html](templates/lesson-template.html)을 복사해 `lesson.html`을 만든다. 코드는 파이썬 파일에서 그대로 옮긴다.
5. `README.md`(교안 요약), `answer_key.md`, `teacher_guide.md`를 만든다.
6. [04-review-checklist.md](04-review-checklist.md)를 모두 통과시킨다.
7. 진행 파일의 그 주차 줄을 `[x]`로 바꾸고 날짜를 적는다.
8. 커밋하고 푸시한다. 커밋 메시지는 `N학기 N주차 워크시트: <미니 프로젝트 이름>`이다.

## 설계 파일과 생성 도구

교안 파일은 손으로 쓰지 않고 **주차 설계 파일**(`lesson_spec.py`)로 만든다. 단계 코드를 한 곳에서 정의하므로 교안·starter·solution이 자동으로 일치한다.

```bash
python tools/lesson_gen.py worksheets/semester1/weekNN/lesson_spec.py
```

- 만드는 파일: `lesson.html`, `README.md`, `answer_key.md`, (개념 주차) `mini_starter.py`, `mini_solution.py`
- 손으로 쓰는 파일: `lesson_spec.py`, `warmup.py`, `extension_*.py`, `teacher_guide.md`, (프로젝트 주차) 주제별 starter/solution
- 기준 예시: `week01/lesson_spec.py`(3단계), `week04/lesson_spec.py`(4단계, 무작위 값 고정)

`SPEC` 주요 필드

| 필드 | 뜻 |
| --- | --- |
| `week`, `title`, `badge`, `story` | 주차, 프로젝트 이름, 부제("~하기"), 미션 이야기 |
| `demo_inputs`, `demo_randoms` | 완성 화면을 만들 때 넣을 입력, 고정할 무작위 값 |
| `warm_title`, `warm_tip` | 워밍업 제목, 오류 이름 팁 (`warmup.py`는 따로 쓴다) |
| `steps` | 단계 목록. 단계마다 `name`, `tool`(도구 카드: 이름, 언제 쓰나요, 예시 줄, 결과), `lines`(새로 쓰는 3~6줄), `sol_lines`(solution에서만 다를 때), `ok`(성공 체크), `trace`(따라가기), `extra_todo`, `small` |
| `change` | 바꾸기: 표 머리, 예시 행, `must`(★ 최대 3개), `more`(더 해 보기) |
| `change_example` | solution 맨 아래에 주석으로 넣을 바꾸기 예시 |
| `new_ideas`, `brag` | 새로 만들기 아이디어, 마무리 질문 |
| `challenge` | 도전 프로젝트: `name`, `design`, `story`, `tool`, `body`(표 등 HTML), `checks`, `more` |
| `hints` | 힌트 카드: (이름, ●○○, 내용 HTML) |
| `key` | 정답지: `warm`(줄, 오류, 고친 방법), `warm_note`, `steps`(단계별 실행 결과), `trace`(표), `change`, `challenge` |
| 프로젝트 주차용 | `mini=False`, `complete=(실행할 파일, 입력, 무작위 값)`, `file`(학생이 이어 쓸 파일), `h1`, `week_label`, `mission_todo`; 단계에 `lines` 대신 `todo`, `body`(기획서 표 등), `write`, `readme` |

## 프로젝트 주차 (5, 9, 10~11주)

새 블록 종류를 만들지 않고 기존 블록을 쓴다. 블록 순서는 개념 주차와 같다.

- `mission`: 이번 주에 할 일(기획 → 만들기 → 발표)과 예시 완성 화면
- `warmup`: 그대로
- `step`: 프로젝트 단계. 예) 중간: 주제 고르기·기획서 → 만들기 1·2 → 발표 준비. 설계와 보충: 설계도 ①·② → 보충 문제. 기말: 명령 카드 → 만들기(일정표) → 친구 테스트 → 발표 준비
- `change`: 최소 완성 기준(★ 최대 3개 + 더 해 보기)과 평가표
- `new`, `challenge`, `hints`: 그대로(필요 없으면 `new`·`challenge`는 빼도 된다)

## 중간에 끊긴 경우

- 진행 파일에서 `[ ]`인데 주차 폴더에 파일이 일부만 있으면 이전 실행이 끊긴 것이다.
- 처음부터 다시 만들지 않는다. 있는 파일을 점검하고 빠진 파일만 채운 뒤 검사를 통과시킨다.

## 예약 루틴 (컴퓨터를 켜 두지 않고 클라우드에서 제작)

- 루틴 `파이썬 1학기 워크시트 자동 생성`(trig_0199fS7hXeHRHQM9Cs5uxqSY)은 1학기 제작을 마치고 꺼져 있다.
- 새 학기를 루틴으로 만들 때는 루틴 지시문을 이 문서 기준으로 새로 쓴다(지금 지시문은 옛 경로 `curriculum/curriculum.md`를 가리킨다).
- 루틴 지시문에 넣을 것:
  - 시작 전에 `docs/` 전체와 템플릿을 읽는다.
  - 한 주차를 끝낼 때마다 바로 커밋·푸시한다(사용량이 떨어져도 이어서 할 수 있게).
  - 쓰기 권한이 없으면(403) 즉시 멈춘다.
  - 다 끝나면 루틴을 끈다.
- 실행 기간은 cron 날짜 범위로 제한한다. 루틴이 스스로 꺼지지 못할 때를 대비한다.

## 1학기 전체 수정 (P5)

- 1학기 주차는 새 교안 형식(`lesson.html`)으로 다시 만든다. 파이썬 파일도 단계별 쓰기 방식(단계 표시 starter, 단계 주석 solution)에 맞게 고친다.
- 예전 `worksheet.html`을 지울지 보관할지는 그때 저장소 주인에게 확인한다.
- 순서는 위 "학기 제작 순서"와 같다(1주차 샘플 승인 → 나머지).

## 이미 만든 워크시트를 고칠 때

- 기준 문서를 바꿔서 고치는 것이면, 먼저 문서와 [decisions.md](decisions.md)를 고친다.
- 고친 주차는 [04-review-checklist.md](04-review-checklist.md)로 다시 점검하고, `answer_key.md`도 같이 고친다.
