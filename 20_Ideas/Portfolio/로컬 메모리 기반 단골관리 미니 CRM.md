---
type: idea
status: draft
created: 2026-06-12
category: Portfolio
tags:
  - idea
  - ai-consulting
source_clips:
  - "[[supermemory]]"
  - "[[Taste Is the New Moat and Design Decides Which Startups Survive]]"
  - "[[Fable 5로 루프 설계하기]]"
---

# 로컬 메모리 기반 단골관리 미니 CRM

## 한줄설명
소상공인의 단골 고객 선호·이력을 완전 로컬 메모리 엔진에 자동 축적해, 외부 서버로 데이터를 보내지 않으면서도 "이 손님은 항상 아메리카노 연하게" 같은 컨텍스트를 다음 응대에 활용하는 미니 CRM

## 핵심기능
- 카카오 알림톡/POS 메모 등에서 고객 관련 텍스트를 [[supermemory]]의 Memory Engine으로 추출·축적 (사실 추출, 시간에 따른 변화/모순 처리, 자동 망각)
- 고객 ID별 "정적 프로필(선호/체질 등 안정적 사실) + 동적 컨텍스트(최근 방문/이슈)"를 카드 형태로 조회
- 사장님이 고객 응대 전 1초 안에 "이 사람과 관련된 메모"를 확인할 수 있는 간단한 대시보드

## 기술스택
- supermemory local (단일 바이너리, `./.supermemory`에 데이터 보관 — 완전 오프라인)
- 프론트엔드: 간단한 웹 대시보드 (Next.js 또는 Streamlit)
- (선택) 카카오톡 채널 API 연동으로 대화 텍스트 자동 수집

## MVP범위
- 고객 5~10명 가상 데이터로 supermemory에 메모 축적 → 프로필/컨텍스트 조회 데모
- "데이터가 로컬에만 저장된다"는 점을 시각적으로 보여주는 UI (Taste Is the New Moat의 transparency/sourcing 원칙 적용 — "이 정보는 어디서 왔고 언제 저장됐는지" 표시)

## 7일구현계획
- Day 1-2: supermemory local 설치 및 API 동작 확인, 가상 고객 데이터 설계
- Day 3-4: 고객 메모 입력 → memory 저장/검색 파이프라인 구축
- Day 5: 정적/동적 프로필 조회 대시보드 UI 제작
- Day 6: "로컬 전용 운영" 강조하는 신뢰 UX(데이터 위치, 망각 정책 표시) 적용
- Day 7: 데모 시나리오 작성 및 README/발표자료 정리 ([[24 tips for giving S-tier demos]] 참고)
