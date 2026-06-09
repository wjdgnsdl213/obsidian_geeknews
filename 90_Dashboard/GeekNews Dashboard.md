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
