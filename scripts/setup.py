"""
GeekNews Knowledge System - 초기 세팅
실행: python scripts/setup.py
역할: 폴더 구조 + Obsidian 템플릿 파일 생성 (최초 1회)
API 없음 - Claude Code가 직접 처리하는 구조
"""

from pathlib import Path
from datetime import date

VAULT = Path(__file__).parent.parent

FOLDERS = [
    "00_Inbox",
    "10_Clips/AI", "10_Clips/DevTools", "10_Clips/Security",
    "10_Clips/Data", "10_Clips/Startup",
    "20_Ideas/Contest", "20_Ideas/Portfolio", "20_Ideas/Business",
    "30_Output/WeeklyReports", "30_Output/BlogDrafts", "30_Output/InterviewMaterials",
    "80_Templates",
    "90_Dashboard",
]

CLIP_TEMPLATE = """\
---
type: clip
status: inbox
source: GeekNews
title: "{{title}}"
url: "{{url}}"
created: {{date}}
category: Unclassified
tags:
  - geeknews
priority: 3
idea_candidate: false
project_candidate: false
reviewed: false
---

# {{title}}

**원문:** {{url}}

## 요약

## 핵심 포인트
-
-
-

## 왜 중요한가

## 내 관심 분야 적용
- 취업/면접:
- 공모전:
- 포트폴리오:
- 사업:

## 다음 액션
- [ ]

## 연결 노트
"""

CONTEST_TEMPLATE = """\
---
type: contest_idea
status: candidate
created: {{date}}
source_clip:
tags: [contest, idea]
score_award: 0
score_feasibility: 0
score_my_fit: 0
---

# 공모전 아이디어: 

## 문제 정의

## 해결 방법

## 사용 데이터
- 공공데이터:
- 외부 데이터:

## 핵심 기능
1.
2.
3.

## 차별점

## MVP 범위

## 다음 액션
- [ ] 관련 공모전 찾기
- [ ] 유사 서비스 조사
- [ ] 데이터셋 확인
"""

PORTFOLIO_TEMPLATE = """\
---
type: portfolio_project
status: idea
created: {{date}}
source_clip:
tags: [portfolio]
stack: []
difficulty: 3
impact: 3
---

# 프로젝트: 

## 한 줄 설명

## 핵심 기능
| 기능 | 설명 | 우선순위 |
|---|---|:---:|
|  |  |  |

## 기술 스택
- Frontend:
- Backend:
- AI:
- DB:

## 7일 구현 계획
- Day 1-2:
- Day 3-4:
- Day 5-7:

## 다음 액션
- [ ]
"""

INTERVIEW_TEMPLATE = """\
---
type: interview_material
status: draft
created: {{date}}
source_clip:
target_role: [IT, Data, AI, Security]
tags: [interview]
---

# 면접 소재: 

## 기술 이슈 요약

## 직무와의 연결

## 내 경험과 연결

## STAR 답변
**Situation:**

**Task:**

**Action:**

**Result:**

## 예상 꼬리질문
1.
2.
3.

## 30초 답변
"""

DASHBOARD = """\
# GeekNews Dashboard

> Dataview 플러그인 필요 (Community Plugins에서 설치)

## 📥 미처리 (00_Inbox)
```dataview
TABLE created, url
FROM "00_Inbox"
WHERE type = "clip" AND reviewed = false
SORT created DESC
```

## ⭐ 아이디어 후보
```dataview
TABLE created, category, priority
FROM "10_Clips"
WHERE idea_candidate = true
SORT priority DESC
```

## 🛠️ 프로젝트 후보
```dataview
TABLE created, category, priority
FROM "10_Clips"
WHERE project_candidate = true
SORT priority DESC
```

## 🏆 공모전 아이디어
```dataview
TABLE created, score_award, status
FROM "20_Ideas/Contest"
SORT score_award DESC
```

## 📊 최근 주간 리포트
```dataview
TABLE created, week
FROM "30_Output/WeeklyReports"
SORT created DESC
LIMIT 5
```
"""

GITIGNORE = """\
.DS_Store
Thumbs.db
.obsidian/workspace.json
.obsidian/workspace-mobile.json
__pycache__/
*.pyc
"""

def main():
    print(f"\n🚀 GeekNews Knowledge System 세팅 시작")
    print(f"📁 Vault: {VAULT}\n")

    for folder in FOLDERS:
        (VAULT / folder).mkdir(parents=True, exist_ok=True)
    print("✅ 폴더 구조 생성")

    templates = {
        "80_Templates/Template - Clip.md": CLIP_TEMPLATE,
        "80_Templates/Template - Contest Idea.md": CONTEST_TEMPLATE,
        "80_Templates/Template - Portfolio Project.md": PORTFOLIO_TEMPLATE,
        "80_Templates/Template - Interview Material.md": INTERVIEW_TEMPLATE,
        "90_Dashboard/GeekNews Dashboard.md": DASHBOARD,
        ".gitignore": GITIGNORE,
    }

    for path, content in templates.items():
        file_path = VAULT / path
        if not file_path.exists():
            file_path.write_text(content, encoding="utf-8")
            print(f"  ✅ {path}")
        else:
            print(f"  ⏭️  {path} (존재, 건너뜀)")

    print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 세팅 완료!

다음 단계:
1. Obsidian Community Plugins 설치:
   - Templater
   - Dataview  
   - Obsidian Git

2. Web Clipper 브라우저 확장 설치
   저장 경로: 00_Inbox

3. 사용법:
   cd ~/ObsidianVault
   claude
   > "Inbox 처리해줘"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

if __name__ == "__main__":
    main()
