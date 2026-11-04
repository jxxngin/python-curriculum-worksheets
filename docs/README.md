# 파이썬 워크시트 제작 기준

이 폴더는 워크시트를 **만들기 전에 정하는 기준**을 모아 둔 곳이다. 사람이든 에이전트든 제작을 시작하기 전에 이 폴더의 문서를 모두 읽는다.

## 기준 상태

**상태: 초안** (2026-11-04)

- `초안`: 기준을 다듬는 중이다. 새 주차·학기 워크시트를 만들지 않는다. 기준 문서와 템플릿만 고친다.
- `확정`: 기준이 정해졌다. [05-production-workflow.md](05-production-workflow.md)의 절차대로 제작을 시작한다.
- 상태는 저장소 주인이 바꾼다. 에이전트는 바꾸지 않는다.
- 확정 전에 남은 결정은 [decisions.md](decisions.md)의 "결정 대기"에 있다.

## 문서

| 문서 | 내용 |
| --- | --- |
| [curriculum.md](curriculum.md) | 1년 커리큘럼 원본 (학기·주차별 개념과 프로젝트) |
| [01-worksheet-format.md](01-worksheet-format.md) | A4 워크시트의 쪽 구성, 부품, 디자인, 인쇄 규칙 |
| [02-content-rules.md](02-content-rules.md) | 내용 규칙: 개념 범위, 말투, 코드, 워밍업, 디버거, 힌트, 예상 표 |
| [03-files-and-answer-key.md](03-files-and-answer-key.md) | 주차 폴더 파일 구성, 파이썬 파일 규칙, 정답지·교사 가이드 형식 |
| [04-review-checklist.md](04-review-checklist.md) | 만든 뒤 점검: 자동 검사, 코드와 워크시트 대조, 인쇄, 사람 검토 |
| [05-production-workflow.md](05-production-workflow.md) | 제작 절차: 샘플 승인, 진행 기록, 예약 루틴, 커밋 |
| [decisions.md](decisions.md) | 피드백과 결정 기록, 결정 대기 목록 |
| [templates/worksheet-template.html](templates/worksheet-template.html) | 워크시트 틀: 공통 스타일과 쪽별 뼈대, 모든 부품 예시 |

## 문서끼리 어긋날 때

우선순위는 다음 순서다.

1. 저장소 주인의 최근 피드백 ([decisions.md](decisions.md))
2. [curriculum.md](curriculum.md)
3. 01~05 기준 문서
4. 템플릿
5. 이미 만든 워크시트

규칙을 바꾸면 해당 문서와 [decisions.md](decisions.md)에 같이 적는다.
