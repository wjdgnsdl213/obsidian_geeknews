---
type: clip
status: processed
source: GeekNews
title: "Fable 5로 루프 설계하기"
url: "https://news.hada.io/topic?id=30390"
created: 2026-06-12
category: AI
tags:
  - geeknews
priority: 4
idea_candidate: false
project_candidate: false
reviewed: true
---

# Fable 5로 루프 설계하기

**원문:** https://news.hada.io/topic?id=30390

## 요약
Claude Fable 5 활용 핵심: self-correction loop와 memory 설계

## 핵심 포인트
- 직접 프롬프팅보다 "goal/rubric → 실행 → 피드백 수집 → 자가수정" 루프를 설계하는 게 효과적이며, Parameter Golf(ML 엔지니어링 챌린지)에서 Fable 5는 Opus 4.7 대비 학습 파이프라인을 약 6배 더 개선
- 채점은 모델의 self-critique보다 독립된 context의 verifier sub-agent가 더 정확하며, 9개 체크리스트 rubric으로 최대 8시간 자율 실행을 허용
- memory는 세션을 넘나드는 outer loop로, "fail→investigate→verify→distill→consult" 5단계로 효과가 강화됨 — Fable 5는 검증 커버리지 최대 73%까지 도달해 일반 규칙으로 distill하는 데 성공(Sonnet 4.6은 1단계, Opus 4.7은 3단계에서 정체)

## 왜 중요한가
"모델을 직접 조종하지 말고 goal/rubric과 memory로 루프를 설계하라"는 방법론은 AI 에이전트 기반 자동화(인턴 업무인 상권분석 데이터 처리 등)를 설계할 때 바로 적용할 수 있는 실전 패턴이며, 포트폴리오 프로젝트에서 "단순 프롬프팅"이 아닌 "에이전트 루프/평가 체계 설계" 역량을 보여줄 수 있는 근거가 된다.

## 내 관심 분야 적용
- 취업/면접: "AI 에이전트를 어떻게 안정적으로 운영하는가"라는 질문에 self-correction loop + memory + rubric 기반 채점 구조로 답변
- 공모전: rubric 기반 자가수정 루프를 적용한 데이터 처리/분석 자동화 공모전 아이디어의 기술적 근거
- 포트폴리오: 이 GeekNews 인박스 처리 자동화 자체를 "goal/rubric + memory distill" 구조로 재설계해 미니 프로젝트화
- 사업: 소상공인 컨설팅 자동화 워크플로에 fail→investigate→verify→distill→consult 패턴을 적용해 운영 매뉴얼/스킬로 인코딩

## 다음 액션
- [ ] 인박스 처리 작업에 memory(distill된 규칙) 개념을 적용해 카테고리/우선순위 판단 일관성 높이기

## 연결 노트

---

## 원문 스크랩

**Self-correction loop**: bcherny(Anthropic)의 "내 일은 루프를 작성하는 것"이라는 언급처럼, Claude Code의 /goal, Claude Managed Agent의 Outcomes는 "goal/rubric → 실행 → 피드백 → 자가수정 → 목표 충족까지 반복" 패턴의 primitive. Parameter Golf(16MB artifact, 8xH100에서 10분 내 최고 성능 모델 학습) 챌린지에서 Fable 5는 9개 체크리스트 rubric과 최대 8시간 실행 환경에서 Opus 4.7 대비 약 6배 더 개선된 파이프라인을 만듦. Fable 5는 구조적 변경(아키텍처)에 베팅하고 회복하는 경향, Opus 4.7은 스칼라 조정만 반복.

**채점 주체**: 모델 자신의 self-critique는 신뢰도가 낮고, 독립 context window의 verifier sub-agent(Outcomes의 grader)가 더 정확하게 채점.

**Memory**: Continual Learning Bench 1.0(pgasawa 팀)으로 Fable 5·Opus 4.7·Sonnet 4.6을 SQL DB 질의 과제로 비교. 효과적 memory 활용은 fail(기록)→investigate(원인 파악)→verify(검증)→distill(규칙화)→consult(참조) 5단계. Sonnet 4.6은 1단계에서 멈춤(미해결 추측만 쌓임), Opus 4.7은 3단계(검증 커버리지 7~33%), Fable 5는 최대 73% 검증 커버리지로 일반 규칙 distill까지 완료.

**종합**: Fable 5를 직접 조종하기보다 환경 피드백(/goal, Outcomes)과 memory로 루프를 설계해 자가 수정·문맥 관리를 맡기는 방식이 더 효과적.
