---
type: clip
status: processed
source: GeekNews
title: "Shortcat - 마우스없이 키보드로 맥 전체 제어하기"
url: "https://news.hada.io/topic?id=30268"
created: 2026-06-08
category: DevTools
tags:
  - geeknews
priority: 2
idea_candidate: false
project_candidate: false
reviewed: true
---

# Shortcat - 마우스없이 키보드로 맥 전체 제어하기

**원문:** https://news.hada.io/topic?id=30268

## 요약
macOS UI를 인덱싱해 키보드만으로 전체 조작 가능한 커맨드 팔레트 도구

## 핵심 포인트
- UI 요소를 퍼지 검색으로 찾아 클릭·우클릭·더블클릭·모디파이어 조합까지 키보드만으로 실행
- 창 제목 검색, 동의어 매칭(delete=remove=clear=destroy) 등으로 단축키 암기 없이 빠른 멀티태스킹 지원
- 댓글에서 "Claude Code로 직접 만들어 쓴다"는 사례와 경쟁 도구 Homerow가 언급됨

## 왜 중요한가
도구 자체보다 "댓글 작성자가 Claude Code로 유사한 생산성 도구를 직접 만들어 쓴다"는 사례가 흥미로우며, 개인 자동화 도구를 만들어 포트폴리오화하는 아이디어의 좋은 레퍼런스가 된다.

## 내 관심 분야 적용
- 취업/면접: 해당 없음 (macOS 전용 도구)
- 공모전: 해당 없음
- 포트폴리오: "Claude Code로 나만의 생산성 자동화 도구 만들기" 미니 프로젝트 아이디어로 응용 (Windows 환경에 맞는 유사 도구)
- 사업: 해당 없음

## 다음 액션
- [ ] Windows용 키보드 전용 제어 도구를 Claude Code로 만드는 미니 프로젝트 아이디어 구체화

## 연결 노트

---

## 원문 스크랩

Shortcat은 macOS의 사용자 인터페이스를 인덱싱해 강력한 명령 팔레트로 제공하는 도구로, 마우스 없이 키보드만으로 Mac을 조작할 수 있게 한다.

- 클릭하려는 대상의 이름을 입력하면 해당 UI 요소에 접근해 클릭·우클릭·더블클릭 및 Modifier 키 조합 클릭까지 지원 (예: "ok" 입력으로 OK 버튼 클릭)
- 창 제목 검색으로 Command+Tab 없이도 정밀한 멀티태스킹 가능
- Safari/Chrome/Firefox 등 Chromium 기반 브라우저, VS Code/Signal/1Password 8 같은 Electron 앱과도 호환
- 메뉴 항목을 퍼지 검색으로 노출해 단축키를 몰라도 조작 가능, 이모지 모드(💩 → poop/turd/crap)와 동의어 지원(delete=remove=clear=destroy) 제공
- 지원 환경: macOS 13+, Apple Silicon/Intel

**댓글**: 한 사용자는 "claude code로 만들어서 쓰는 중"이라고 밝혔고, 다른 사용자들은 설정창이 닫혀서 복구가 안 됐던 경험이나 한글 입력기 호환성 문제로 다운그레이드한 경험, 경쟁 도구 Homerow(유료, 더 완성도 높음)를 추천하는 의견을 남겼다.
