---
type: clip
status: processed
source: GeekNews
title: "supermemoryai/supermemory: Memory and context engine + app, extremely fast, scalable, fully local"
url: "https://github.com/supermemoryai/supermemory"
created: 2026-06-11
category: AI
tags:
  - geeknews
priority: 5
idea_candidate: false
project_candidate: true
reviewed: true
---

# supermemoryai/supermemory: Memory and context engine + app, extremely fast, scalable, fully local

**원문:** https://github.com/supermemoryai/supermemory

## 요약
AI용 메모리/컨텍스트 엔진, 단일 바이너리로 완전 로컬 실행 가능

## 핵심 포인트
- LongMemEval/LoCoMo/ConvoMem 3대 메모리 벤치마크 1위. 대화에서 사실을 추출하고, 시간에 따른 변화·모순을 해결하며, 만료된 정보는 자동으로 잊는 "Memory Engine" + 정적/동적 정보로 구성된 "User Profile"(약 50ms) 제공
- `curl -fsSL https://supermemory.ai/install | bash` 한 줄로 로컬 실행(`localhost:6767`), OpenAI/Anthropic/Ollama 등 어떤 모델도 연결 가능 — 완전 오프라인 운영 가능, 데이터는 `./.supermemory` 디렉토리에 보관
- Claude Code/Cursor/VS Code 등에 MCP로 설치하면 `memory`(저장/삭제), `recall`(검색), `context`(프로필 주입) 3개 툴 제공, Google Drive/Gmail/Notion/GitHub 커넥터로 실시간 동기화

## 왜 중요한가
[[Fable 5로 루프 설계하기]]와 [[Loop Engineering]]에서 강조한 "memory(디스크 기반 상태)"를 직접 구현한 오픈소스 도구로, 정훈의 GeekNews Vault 자동화(인박스 처리 시 카테고리/우선순위 판단 일관성, 과거 처리 패턴 기억)에 즉시 적용 가능한 실제 인프라이며, "AI 메모리 시스템 구축 경험"은 면접/포트폴리오에서 구체적인 기술 스택으로 어필 가능하다.

## 내 관심 분야 적용
- 취업/면접: "RAG와 Memory의 차이"(문서 검색 vs 시간에 따라 변하는 사용자 사실 추적)를 구체적 사례로 설명하고, 직접 셀프호스팅 경험을 기술 스택으로 제시
- 공모전: 소상공인 상담 챗봇에 "고객별 선호/이력 기억 + 자동 망각" 기능을 supermemory 로컬 서버로 구현한 공모전 출품작
- 포트폴리오: 이 Obsidian Vault의 Inbox 처리 자동화에 supermemory를 연동해 "과거에 어떤 글을 어떤 category/priority로 분류했는지"를 메모리로 축적, 분류 일관성을 개선하는 미니 프로젝트
- 사업: 소상공인 AI 컨설팅에서 "고객 데이터를 외부로 보내지 않는 완전 로컬 메모리 서버"라는 프라이버시 강점을 차별화 포인트로 제시

## 다음 액션
- [ ] `npx supermemory local`로 로컬 서버 실행해보고 GeekNews Vault 자동화와 연동 가능성 테스트
- [ ] Claude Code용 supermemory 플러그인(claude-supermemory) 설치해 인박스 처리 작업에 메모리 적용

## 연결 노트
[[Fable 5로 루프 설계하기]]
[[Loop Engineering]]

---

## 원문 스크랩

**개요**: Supermemory는 AI를 위한 메모리/컨텍스트 레이어로, LongMemEval(81.6%, #1), LoCoMo(#1), ConvoMem(#1) 등 3대 메모리 벤치마크에서 1위. 대화에서 자동으로 사실을 추출해 사용자 프로필을 구축하고, 지식 업데이트·모순을 처리하며, 만료된 정보를 자동으로 잊고, 적절한 시점에 적절한 컨텍스트를 제공. RAG·커넥터·파일 처리를 포함한 전체 컨텍스트 스택을 하나의 시스템으로 제공.

**핵심 기능**: ① Memory — 대화에서 사실 추출, 시간적 변화·모순·자동 망각 처리 ② User Profiles — 안정적 사실+최근 활동을 자동 유지, 1회 호출 ~50ms ③ Hybrid Search — RAG+Memory를 단일 쿼리로 ④ Connectors — Google Drive·Gmail·Notion·OneDrive·GitHub 실시간 웹훅 동기화 ⑤ Multi-modal Extractors — PDF/이미지(OCR)/비디오(transcription)/코드(AST 기반 청킹).

**사용 방법**: ① 일반 사용자는 앱/브라우저 확장/MCP 서버로 설치, Claude Code·Cursor·Windsurf·VS Code 등에서 `/context`로 프로필 주입. ② 개발자는 `npm install supermemory`/`pip install supermemory`로 API 사용 — `client.add()`, `client.profile()`, `client.search.memories()` 등. Vercel AI SDK, LangChain, LangGraph, Mastra 등 주요 프레임워크 드롭인 래퍼 제공. ③ 셀프호스팅은 `curl -fsSL https://supermemory.ai/install | bash` 한 줄로 로컬 바이너리 실행, OpenAI/Anthropic/Gemini/Groq/Ollama 등 어떤 모델도 연결 가능, 완전 오프라인 운영 가능, 데이터는 `./.supermemory`에 보관.

**Memory vs RAG**: RAG는 문서 청크를 검색하는 무상태(stateless) 방식으로 모두에게 동일한 결과를 주지만, Memory는 시간에 따라 변하는 사용자에 대한 사실을 추적("뉴욕에 산다"가 "SF로 이사했다"로 갱신됨을 이해). Supermemory는 기본적으로 둘을 함께 실행.

**자동 망각**: "내일 시험 있음" 같은 일시적 사실은 날짜가 지나면 만료되고, 모순은 자동으로 해결되어 노이즈가 영구 메모리로 남지 않음.
