# GeekNews Knowledge System

## 프로젝트 목적
GeekNews 수동 스크랩을 취업 / 공모전 / 포트폴리오 / 사업 아이디어로 변환하는 Obsidian 지식 관리 시스템.
- 스크랩(수동, Web Clipper) → 처리(Claude Code 직접 수행) → 판단(정훈, 체크박스만)

---

## 폴더 구조
```
ObsidianVault/
├── CLAUDE.md              ← 이 파일
├── 00_Inbox/              ← Web Clipper 저장 위치 (미처리)
├── 10_Clips/              ← 처리 완료 스크랩
│   ├── AI/
│   ├── DevTools/
│   ├── Security/
│   ├── Data/
│   └── Startup/
├── 20_Ideas/              ← 정훈이 수동 승격
│   ├── Contest/
│   ├── Portfolio/
│   └── Business/
├── 30_Output/
│   ├── WeeklyReports/
│   ├── BlogDrafts/
│   └── InterviewMaterials/
├── 80_Templates/
└── 90_Dashboard/
```

---

## Clip 노트 Frontmatter 스펙
```yaml
---
type: clip
status: inbox          # inbox → processed
source: GeekNews
title: ""
url: ""
created: YYYY-MM-DD
category: AI           # AI | DevTools | Security | Data | Startup
tags: [geeknews]
priority: 3            # 1~5
idea_candidate: false  # 정훈이 체크
project_candidate: false
reviewed: false        # 처리 후 true로 변경
---
```

---

## 작업 명세 (Claude Code가 직접 수행)

### [TASK-1] Inbox 처리
트리거: "Inbox 처리해줘" / "새 스크랩 처리해줘"

수행 절차:
1. 00_Inbox/*.md 파일 목록 확인
2. frontmatter의 reviewed=false 파일만 대상
3. 각 노트 내용 분석 후 아래 섹션 채우기:
   - ## 요약: 한 줄 (50자 이내)
   - ## 핵심 포인트: 3개 불릿
   - ## 왜 중요한가: 2-3문장
   - ## 내 관심 분야 적용: 취업/공모전/포트폴리오/사업 각 1줄
   - ## 다음 액션: 체크박스 1개 이상
4. frontmatter 업데이트: status=processed, category=분류값, priority=1~5, reviewed=true
5. 파일을 10_Clips/{category}/ 로 이동
6. 처리 완료 후 결과 요약 출력

카테고리 판단 기준:
- AI: LLM, 에이전트, 머신러닝, 생성형AI
- DevTools: IDE, 개발환경, CLI, 개발 자동화
- Security: 보안사고, 취약점, 암호화, 인증
- Data: 데이터엔지니어링, 분석, 시각화, DB
- Startup: 스타트업, 서비스, 비즈니스모델, 투자

priority 기준:
- 5: 취업/공모전/사업에 즉시 활용 가능
- 4: 조만간 실행 가능한 아이디어 포함
- 3: 참고할 만한 트렌드
- 2: 흥미롭지만 지금 당장 활용 어려움
- 1: 나중에 볼 것

---

### [TASK-2] 주간 리포트 생성
트리거: "이번 주 리포트 만들어줘" / "주간 리포트"

수행 절차:
1. 10_Clips/**/*.md 에서 이번 주(최근 7일) 파일 수집
2. 전체 분석 후 30_Output/WeeklyReports/Weekly-YYYY-WNN.md 생성
3. 리포트 구성:
   - 이번 주 핵심 트렌드 3개
   - 반복 등장 키워드 테이블
   - 스크랩 TOP 5 (이유 포함)
   - 공모전 아이디어 후보 (수상 가능성/난이도 포함)
   - 포트폴리오 프로젝트 후보
   - 취업/면접 소재
   - 다음 주 실행 과제 체크박스

---

### [TASK-3] 아이디어 변환
트리거: "{파일명 또는 내용}을 공모전/포트폴리오/면접 소재로 변환해줘"

공모전 → 20_Ideas/Contest/ 에 새 노트 생성
포트폴리오 → 20_Ideas/Portfolio/ 에 새 노트 생성
면접 소재 → 30_Output/InterviewMaterials/ 에 새 노트 생성

공모전 노트 구성: 문제정의 / 해결방법 / 사용데이터 / 핵심기능 / 차별점 / MVP범위 / 다음액션
포트폴리오 노트 구성: 한줄설명 / 핵심기능 / 기술스택 / MVP범위 / 7일구현계획
면접 소재 구성: 기술이슈요약 / 직무연결 / STAR답변 / 예상꼬리질문3개 / 30초답변

---

### [TASK-4] 대시보드 현황 요약
트리거: "현황 알려줘" / "대시보드"

수행 절차:
1. 00_Inbox 미처리 파일 수 확인
2. 10_Clips 카테고리별 파일 수 확인
3. idea_candidate=true, project_candidate=true 파일 목록 출력
4. 20_Ideas 파일 수 확인
5. 텍스트로 현황 요약 출력

---

## 정훈 관심 분야 (분석 시 참고)
- 취업 타겟: 공공기관/금융권 IT직 (KRX, KDB, 금융보안원, KOSCOM 등)
- 기술 배경: 보안(악성코드탐지, TLS SNI, 다크웹), 데이터엔지니어링, NLP
- 관심사: AI 자동화, 퀀트, 공모전, 소상공인 AI 컨설팅 사업
- 현재: 소상공인시장진흥공단 빅데이터팀 인턴 (상권분석 플랫폼)

아이디어 적용 우선순위: 공모전 수상 > IT공기업 취업 소재 > 포트폴리오 > 사업아이템
