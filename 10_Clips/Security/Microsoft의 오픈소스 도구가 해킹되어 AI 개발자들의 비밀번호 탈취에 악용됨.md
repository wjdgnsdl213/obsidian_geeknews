---
type: clip
status: processed
source: GeekNews
title: "Microsoft의 오픈소스 도구가 해킹되어 AI 개발자들의 비밀번호 탈취에 악용됨"
url: "https://news.hada.io/topic?id=30340"
created: 2026-06-10
category: Security
tags:
  - geeknews
priority: 4
idea_candidate: false
project_candidate: false
reviewed: true
---

# Microsoft의 오픈소스 도구가 해킹되어 AI 개발자들의 비밀번호 탈취에 악용됨

**원문:** https://news.hada.io/topic?id=30340

## 요약
"Miasma" 웜, AI 코딩 에이전트 설정파일 통해 70+ 저장소 감염

## 핵심 포인트
- GitHub 호스팅된 Microsoft 오픈소스 프로젝트 최소 70개가 해킹되어 비밀번호 탈취 악성코드가 주입됨, Azure·Claude Code·Gemini CLI·VS Code 등 AI 코딩 도구 관련 프로젝트가 다수 영향받음(Durable Task 프로젝트는 "재침해")
- "Miasma" 웜은 AI 코딩 에이전트(VSCode/Cursor/Claude/Gemini)가 자동 실행하는 설정 파일(config-as-code)을 감염 경로로 악용하며, 이전 감염에서 탈취한 쓰기 권한 GitHub 토큰으로 자기 전파(Shai-Hulud 계열) — github-actions 명의의 서명되지 않은 커밋으로 49초에 5개 저장소를 감염시킨 사례도 확인됨
- HN 반응: "AI 에이전트는 별도 보안 주체로서 세분화된 전용 토큰을 가져야 한다", "코드 대부분을 AI가 생성·리뷰하면서 실제로 코드를 읽는 사람이 없다"는 구조적 위험 지적, npm/pip install은 샌드박스에서만 하라는 권고

## 왜 중요한가
정훈의 보안 배경(악성코드 탐지)과 직접 연결되는 최신 공급망 공격 사례로, "AI 코딩 에이전트 설정 파일을 통한 자동실행 악성코드"라는 신종 공격 벡터는 면접에서 최신 보안 트렌드 소재로 쓸 수 있고, "AI 에이전트 전용 세분화 토큰/샌드박싱" 같은 대응책은 보안 컨설팅이나 공모전 아이디어로 발전 가능하다.

## 내 관심 분야 적용
- 취업/면접: 금융보안원/공공기관 IT 보안 면접에서 "AI 코딩 에이전트發 공급망 공격(Miasma/Shai-Hulud)"을 최신 위협 사례로 인용
- 공모전: "AI 코딩 에이전트 설정 파일(AGENTS.md, MCP config 등) 자동 악성코드 스캐너" 아이디어
- 포트폴리오: 악성코드 탐지 경험을 살려 AI 에이전트 설정파일 기반 악성 페이로드 탐지 룰셋/스캐너 미니 프로젝트
- 사업: 소상공인이 AI 코딩 도구(Cursor, Claude Code 등) 사용 시 권장 보안 설정(세분화 토큰, 샌드박싱) 가이드 컨설팅

## 다음 액션
- [ ] Miasma 웜 완화 도구(antimiasma) 및 동작 원리 분석해 탐지 룰 아이디어 정리

## 연결 노트

---

## 원문 스크랩

**사건 개요**: GitHub의 Microsoft 오픈소스 프로젝트 수십 개가 침해되어 비밀번호 탈취 악성코드가 주입됨. Azure, Claude Code, Gemini CLI, VS Code 등 AI 개발 도구 관련 프로젝트가 다수. 최소 70개 저장소가 "GitHub 서비스 약관 위반"으로 비활성화됨. Durable Task 프로젝트는 5월 중순에 이미 침해됐던 것이 "재침해"로 확인됨.

**Miasma 웜 동작**: AI 코딩 에이전트(VSCode/Cursor/Claude/Gemini)가 자동 실행하는 config-as-code 파일을 감염 경로로 사용. 이전 감염에서 수집한 쓰기 권한 GitHub 토큰으로 닿는 모든 저장소에 지속성 페이로드 주입(Shai-Hulud 자기전파 계열). 5개 저장소(총 1,459 star, mantine-datatable이 1,225)를 49초 만에 감염 — github-actions 명의 서명되지 않은 커밋, `chore: update dependencies [skip ci]` 메시지, 동일 6개 파일 변경 패턴. 6월 1주차에 Composer/Go/Pip까지 지원 확대.

**HN 반응**: ① RBAC가 깨졌고 capability 기반 보안 모델이 미래라는 주장 ② classic PAT(개인 접근 토큰)를 AI 에이전트에 넘기는 관행이 새로운 "비밀번호 포스트잇"이라는 비판, AI 에이전트는 세분화된 전용 토큰을 가진 별도 보안 주체여야 한다는 제안 ③ "AI가 코드 대부분을 생성·리뷰하고 인간은 'intended behavior'만 적는다"는 증언 — 실제 코드를 읽는 사람이 없는 조직 구조의 위험 ④ npm/pip install은 반드시 샌드박스에서, 보안 감사에는 AI 취약점 스캐너 활용 권고 ⑤ 이 사건이 2025년 9월 GitHub 보안 침해 및 Microsoft의 2023년 CSRB 보안 문화 비판 보고서와 연속선상에 있다는 지적.
