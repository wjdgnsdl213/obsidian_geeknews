---
type: clip
status: processed
source: GeekNews
title: "LLMs are eroding my software engineering career and I don't know what to do"
url: "https://human-in-the-loop.bearblog.dev/llms-are-eroding-my-software-engineering-career-and-i-dont-know-what-to-do/"
created: 2026-06-08
category: AI
tags:
  - geeknews
priority: 4
idea_candidate: false
project_candidate: false
reviewed: true
---

# LLMs are eroding my software engineering career and I don't know what to do

**원문:** https://human-in-the-loop.bearblog.dev/llms-are-eroding-my-software-engineering-career-and-i-dont-know-what-to-do/

## 요약
10년차 백엔드 개발자가 LLM에 의해 도메인 지식·디버깅·코드품질 역량이 잠식되는 경험을 고백

## 핵심 포인트
- 도메인 전문지식(결제·금융 시스템 설계)이 LLM에게 "프롬프트 가능한" 지식으로 평준화되며 차별성을 잃음
- Claude 4.5~4.7 등장 이후 분산 시스템 버그의 90%를 에이전트가 원샷으로 해결, "디버깅 역량"이라는 마지막 보루도 무너짐
- 마지막 보루였던 "코드 품질/아키텍처"마저 "taste"로 격하되며, 사람이 읽기 위한 코드보다 LLM이 다루기 좋은 코드가 우선되는 흐름이 등장

## 왜 중요한가
AI가 시니어 엔지니어의 핵심 역량(도메인 지식, 디버깅, 코드 설계)까지 대체하는 현실은 "AI 시대에 어떤 전문성을 키워야 살아남는가"를 묻는다. 정훈의 보안·데이터 전문성을 AI로 대체되기 어려운 영역으로 포지셔닝하는 데 참고할 수 있는 위기감 있는 1차 자료다.

## 내 관심 분야 적용
- 취업/면접: "AI가 대체하기 어려운 직무 역량은 무엇인가"라는 질문에 이 글의 사례(도메인 지식의 평준화)를 인용해 본인의 차별화 전략 설명
- 공모전: 해당 없음
- 포트폴리오: 해당 없음
- 사업: 소상공인 컨설팅에서 "AI가 대체 못하는 부분(현장 맥락, 신뢰 관계)"을 가치제안에 어떻게 반영할지 고민하는 참고 자료

## 다음 액션
- [ ] "AI 시대에 살아남는 직무 역량"을 주제로 한 면접 예상 답변 초안 작성

## 연결 노트

---

## 원문 스크랩

10년차 소프트웨어 엔지니어(결제/금융 도메인)가 자신의 전문성이 차례로 무너지는 과정을 3개의 "기둥"으로 정리한다.

**첫 번째 기둥의 붕괴 — 도메인 지식**: PCI 컴플라이언스, 복식부기, 에스크로, 정산, 멱등성 같은 결제 도메인 지식을 수년간 쌓았으나, 회사가 AI 도입을 강제하면서 LLM이 "트레이드오프를 연결하는" 자신의 핵심 역량을 빠르게 따라잡는 것을 목격. "그래도 디버깅만큼은 사람의 영역"이라 믿었다.

**두 번째 기둥의 붕괴 — 디버깅과 분산 시스템**: Claude Code, MCP, 에이전틱 워크플로의 등장 이후 상황이 급변. Claude 4.5는 스택 트레이스만으로 버그의 60%를 해결했고, 4.6~4.7과 GPT 5.5, Opus 4.8에 이르러서는 분산 시스템 버그의 90%를 원샷으로 해결한다. "이제 나는 그저 그런 평범한 엔지니어가 되었다 — 다른 시니어가 LLM을 조종해도 내 도메인 전문성과 차이가 없다."

**세 번째 기둥, 아직 무너지지 않은 것 — 코드 품질과 아키텍처**: 좋은 코드, 리팩터링, DDD/Clean Architecture에 대한 애정이 마지막 보루였으나, 이마저 "taste"라는 단어로 격하되고 있다. 에이전트는 코드베이스를 잘 정리하지 못하지만(순환 의존성, 중복, 불필요한 주석 등), 이제 "C나 D 등급" 코드도 괜찮다는 분위기 — "코드는 더 이상 사람이 아니라 기계가 읽기 위해 쓰여진다."

**결론 — 이제 어떻게 해야 하나**: 8개월 전 레이오프에서 동료들이 "도메인 전문성만으로는 더 이상 차별화가 안 된다"는 같은 문제를 겪었다. 채용 공고도 "Software Engineer - 분야"에서 그냥 "Software Engineer"로 바뀌었다. 수학·통계·ML을 다시 공부해 프론티어랩 연구직으로 가는 것도 고려했지만 현실적 제약이 많고, "그때쯤이면 RSI가 연구자마저 대체했을지도 모른다"고 자조한다. 이 글은 화제가 되어 후속 글(댓글 답변)도 작성되었다.
