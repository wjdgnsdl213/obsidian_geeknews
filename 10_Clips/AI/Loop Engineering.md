---
type: clip
status: processed
source: GeekNews
title: "Loop Engineering"
url: "https://addyo.substack.com/p/loop-engineering"
created: 2026-06-10
category: AI
tags:
  - geeknews
priority: 5
idea_candidate: false
project_candidate: false
reviewed: true
---

# Loop Engineering

**원문:** https://addyo.substack.com/p/loop-engineering

## 요약
코딩 에이전트를 직접 프롬프팅 대신 "루프"를 설계하는 법

## 핵심 포인트
- "Loop engineering"은 에이전트를 직접 프롬프팅하는 대신, 발견→실행→검증→기록→다음 작업 결정을 자동으로 도는 시스템을 설계하는 것. Claude Code와 Codex 모두 5가지 빌딩블록(automations, worktrees, skills, plugins/connectors, sub-agents) + memory(디스크에 남는 상태 파일)를 갖춤
- `/goal`(Claude Code·Codex 공통)은 별도의 작은 모델이 매 턴 종료 조건을 검증해, 작성자와 검증자를 분리(maker-checker)함으로써 무인 실행을 신뢰 가능하게 만듦
- 루프가 좋아져도 ① 검증 책임 ② comprehension debt(이해하지 못한 코드의 누적) ③ cognitive surrender(생각 없이 결과를 그대로 받아들이는 태도)는 더 중요해짐 — "루프를 만들되 엔지니어로 남아라"

## 왜 중요한가
5개 빌딩블록(automations/worktrees/skills/connectors/sub-agents)+memory라는 구체적 아키텍처는 GeekNews 인박스 자동 처리, 인턴 업무(상권분석) 자동화 등 정훈의 실제 워크플로를 "루프"로 재설계할 때 바로 적용할 청사진이며, maker-checker 구조는 포트폴리오에서 "AI 자동화를 신뢰 가능하게 설계했다"는 근거로 쓸 수 있다.

## 내 관심 분야 적용
- 취업/면접: "AI 에이전트를 프로덕션에서 안전하게 운영하는 법"에 대해 maker-checker(작성/검증 분리), 디스크 기반 memory, worktree 기반 병렬 격리를 구체적 용어로 설명
- 공모전: "자동 트리아지 + 검증 서브에이전트" 구조를 적용한 업무 자동화 시스템 아이디어
- 포트폴리오: 이 GeekNews Vault 자체를 automations(스케줄 트리거)+skills(CLAUDE.md)+memory(상태 파일)로 확장한 "개인 지식관리 루프" 데모로 구현
- 사업: 소상공인 반복 업무(리뷰 응답, 재고 알림 등)를 automation+verifier sub-agent 구조로 설계하는 컨설팅 프레임워크

## 다음 액션
- [ ] 이 Vault의 Inbox 처리 작업을 automation(스케줄)+verifier sub-agent 구조로 재설계하는 아이디어 메모 작성

## 연결 노트

---

## 원문 스크랩

**5가지 빌딩블록 + memory**:
1. **Automations**: 일정 주기로 discovery/triage를 자동 수행. Codex의 Automations 탭, Claude Code의 `/loop`, cron, hooks, GitHub Actions. `/goal`은 별도 작은 모델이 매 턴 종료조건("test/auth 전체 통과 & lint clean")을 검증.
2. **Worktrees**: 병렬 에이전트의 파일 충돌 방지를 위한 git worktree 기반 격리. 리뷰 대역폭이 병렬 실행 수의 진짜 한계.
3. **Skills**: `SKILL.md` 폴더로 프로젝트 컨텍스트를 매 세션 재설명하지 않도록 고정 — "이 사고 때문에 이렇게 안 한다" 같은 의도(intent)를 외부화.
4. **Plugins/Connectors**: MCP 기반으로 이슈 트래커·DB·Slack 등에 연결, skills+connectors를 plugin으로 패키징해 팀 공유.
5. **Sub-agents**: 작성자(maker)와 검증자(checker)를 분리 — 보안 리뷰어는 고성능/고추론, 탐색자는 빠른 읽기 전용 모델 등으로 역할 분리. `/goal`도 본질적으로 이 maker-checker 구조.

**루프 예시**: 매일 아침 automation이 CI 실패·이슈·커밋을 triage skill로 분석해 markdown/Linear에 기록 → 처리할 항목마다 worktree에서 sub-agent가 수정안 작성 → 다른 sub-agent가 스킬/테스트 기준으로 리뷰 → connector가 PR 오픈·티켓 갱신 → 상태 파일이 다음날 이어받음.

**한계**: 검증은 여전히 인간 책임("done은 증명이 아니라 주장"), comprehension debt(이해 못한 코드 격차 확대), cognitive surrender(생각 없이 결과 수용) 위험은 루프가 좋아질수록 더 커짐. "루프를 설계하되, 그냥 go를 누르는 사람이 아니라 엔지니어로 남아야 함."
