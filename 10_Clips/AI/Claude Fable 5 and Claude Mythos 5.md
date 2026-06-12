---
type: clip
status: processed
source: GeekNews
title: "Claude Fable 5 and Claude Mythos 5"
url: "https://www.anthropic.com/news/claude-fable-5-mythos-5"
created: 2026-06-10
category: AI
tags:
  - geeknews
priority: 4
idea_candidate: false
project_candidate: false
reviewed: true
---

# Claude Fable 5 and Claude Mythos 5

**원문:** https://www.anthropic.com/news/claude-fable-5-mythos-5

## 요약
Anthropic, Mythos급 모델 Fable 5/Mythos 5 정식 출시

## 핵심 포인트
- Fable 5는 일반 공개용 Mythos급 모델로, 소프트웨어 엔지니어링·지식노동·비전·과학연구 전 영역에서 SOTA를 기록하며 작업이 길고 복잡할수록 기존 모델 대비 우위가 커짐 (Stripe: 5천만 라인 Ruby 코드베이스 전체 마이그레이션을 1일에 완료)
- 사이버보안·생물/화학·distillation 관련 요청은 분류기가 감지해 Opus 4.8로 자동 전환되며(전체 세션의 5% 미만), Mythos 5는 사이버 가드레일을 해제한 동일 모델로 Project Glasswing 신뢰 파트너에게만 제공
- 가격은 입력 $10/output $50 (백만 토큰당)로 기존 Mythos Preview의 절반 이하; Pro/Max/Team/Enterprise 구독 플랜에는 6/22까지 추가 비용 없이 포함되고 이후 사용 크레딧 필요

## 왜 중요한가
최신 프론티어 모델(Fable 5)의 코딩·에이전트 능력(50M 라인 코드베이스 마이그레이션, 장시간 자율 작업, 비전 기반 코드 복원)은 향후 포트폴리오/공모전에서 "최신 AI 모델을 활용한 자동화"를 설계할 때 구체적 capability 레퍼런스가 되며, 안전장치(분류기·데이터 보존 정책) 설계는 AI 거버넌스/보안 직무 면접에서 최신 사례로 언급할 수 있다.

## 내 관심 분야 적용
- 취업/면접: 최신 LLM의 보안 분류기·jailbreak 방어 구조(레드팀, 30일 데이터 보존 정책)를 AI 보안/거버넌스 관련 질문에 최신 사례로 인용
- 공모전: Fable 5의 장시간 자율 작업·메모리 활용 능력을 활용한 자동화 워크플로 아이디어 설계 시 기술적 근거로 활용
- 포트폴리오: Claude Code/Fable 5급 모델을 활용한 코드베이스 마이그레이션·리팩토링 자동화 데모 제작 시 참고
- 사업: 소상공인 컨설팅에서 Fable 5의 비용(토큰당 가격)과 구독 정책 변화를 안내해 AI 도구 선택 가이드 제공

## 다음 액션
- [ ] Claude Code에서 Fable 5 사용 가능 여부 확인 후 인턴 업무(상권분석) 자동화 작업에 시험 적용

## 연결 노트

---

## 원문 스크랩

**Fable 5 출시**: Mythos급 모델 중 일반 공개용으로 안전장치를 적용한 버전. 거의 모든 벤치마크에서 SOTA, 작업이 길고 복잡할수록 우위가 커짐. Stripe는 5천만 라인 Ruby 코드베이스 전체 마이그레이션을 팀이 2개월 걸릴 작업을 1일에 완료했다고 보고. Cognition FrontierCode 평가에서 최고 점수.

**Mythos 5**: Fable 5와 동일 모델이나 일부 안전장치 해제, Project Glasswing(미국 정부 협력 사이버 방어)을 통해 제한적으로 제공. 세계 최강 사이버보안 능력 보유. 생물학(신약 설계 10배 가속, AAV 설계 등) 연구에도 활용.

**비전/메모리**: 스크린샷만으로 웹앱 소스 복원, 비전만으로 Pokémon FireRed 클리어. 파일 기반 영구 메모리로 Slay the Spire 성능 3배 향상.

**안전장치**: 사이버보안·생물화학·distillation 관련 요청은 별도 분류기가 감지해 Opus 4.8로 자동 전환(5% 미만 세션에서만 발생). 1,000시간 이상의 외부 버그바운티에서 범용 jailbreak 미발견(UK AISI는 일부 진전). Mythos급 모델 트래픽은 30일 데이터 보존 의무화(학습 미사용, 안전 목적 한정).

**가격/제공**: 입력 $10/output $50 per 백만 토큰, Mythos Preview 대비 절반 이하. API·소비형 Enterprise는 즉시 전체 제공, 구독 플랜(Pro/Max/Team/Enterprise)은 6/22까지 무료 포함 후 사용 크레딧 필요.
