---
type: idea
status: draft
created: 2026-06-12
category: Portfolio
tags:
  - idea
  - security
  - ai-agent
source_clips:
  - "[[Microsoft의 오픈소스 도구가 해킹되어 AI 개발자들의 비밀번호 탈취에 악용됨]]"
---

# AI 에이전트 설정파일 보안 스캐너

## 한줄설명
Claude Code/Cursor/Copilot 등 AI 코딩 에이전트가 자동 실행하는 설정파일(AGENTS.md, MCP config, .cursor/rules 등)에서 [[Microsoft의 오픈소스 도구가 해킹되어 AI 개발자들의 비밀번호 탈취에 악용됨]]에서 다룬 Miasma 웜류의 악성 패턴을 탐지하는 정적 스캐너

## 핵심기능
- 저장소 내 AI 에이전트 설정파일(AGENTS.md, MCP 서버 config, Claude Code 권한 설정, .cursorrules 등) 자동 탐색
- 알려진 악성 패턴(외부 URL로의 자동 curl/wget, 비정상 git push/토큰 사용, 의심스러운 `chore: update dependencies` 패턴 등) 룰셋 기반 탐지
- 위험도(상/중/하) 표시 및 수정 권고 리포트 생성

## 기술스택
- Python (정적 분석 스크립트) 또는 Node.js CLI
- 룰셋: YAML/JSON 기반 패턴 정의 (커스텀 룰 추가 가능)
- GitHub Actions 연동으로 PR 시 자동 스캔

## MVP범위
- AGENTS.md / MCP config / Claude Code settings.json 3종 파일 형식에 대한 룰셋 10개 내외
- Miasma 사건에서 확인된 패턴(서명되지 않은 github-actions 커밋, 동일 파일셋 변경, 외부 토큰 유출 시도)을 룰로 구현
- CLI 실행 시 스캔 결과를 콘솔/마크다운 리포트로 출력

## 7일구현계획
- Day 1: Miasma 웜/Shai-Hulud 관련 공개 IOC(indicator of compromise) 자료 조사 및 룰셋 설계
- Day 2-3: AGENTS.md, MCP config 파서 + 패턴 매칭 로직 구현
- Day 4: 위험도 분류 및 리포트 출력 포맷 구현
- Day 5: 샘플 저장소(의도적으로 취약한 설정 포함)로 테스트
- Day 6: GitHub Actions 워크플로 연동
- Day 7: README, 데모 GIF, 발표자료 작성 ([[24 tips for giving S-tier demos]] 참고)
