---
title: "Microsoft의 오픈소스 도구가 해킹되어 AI 개발자들의 비밀번호 탈취에 악용됨"
source: "https://news.hada.io/topic?id=30340"
author:
  - "[[neo]]"
published: 2026-06-10
created: 2026-06-10
description: "GitHub에 호스팅된 수십 개의 오픈소스 프로젝트가 해커에 의해 침해되어 비밀번호 탈취 악성코드가 코드에 주입되면서, Microsoft가 해당 프로젝트 접근을 차단하고 조사에 착수 영향받은 프로젝트 다수는 클라우드 서비스 Azure 및 Claude Code, Gemini CLI, V…"
tags:
  - "clippings"
---
(techcrunch.com)

3P by [GN⁺](https://news.hada.io/@neo) | ★ favorite |

- GitHub에 호스팅된 **수십 개의 오픈소스 프로젝트** 가 해커에 의해 침해되어 비밀번호 탈취 악성코드가 코드에 주입되면서, Microsoft가 해당 프로젝트 접근을 차단하고 조사에 착수
- 영향받은 프로젝트 다수는 클라우드 서비스 **Azure** 및 Claude Code, Gemini CLI, VS Code 등 **AI 개발 앱** 으로 코딩할 때 쓰이는 도구와 관련
- 사용자가 AI 코딩 앱에서 감염된 도구를 열면 **비밀번호와 민감한 자격 증명** 이 탈취되는 방식으로 동작
- GitHub 기준 **최소 70개 프로젝트** 가 비활성화되었으며, Microsoft는 일부 저장소를 일시 제거 후 검토를 거쳐 복원
- 이번 사례는 인기 오픈소스 코드를 노리는 **공급망 공격** 의 최근 사례이며, Microsoft의 오픈소스 프로젝트가 몇 주 사이 두 번째로 침해된 것으로 알려짐

---

## 사건 개요 및 Microsoft의 대응

- 해커가 프로젝트를 침해해 코드에 비밀번호 탈취 악성코드를 주입한 정황이 확인되어, Microsoft가 GitHub 상의 오픈소스 프로젝트 수십 개에 대한 접근을 차단하고 침해 경위를 조사 중
- 영향받은 프로젝트 다수는 **Azure** 클라우드 서비스 및 **Claude Code**, **Gemini의 커맨드라인 인터페이스**, **VS Code** 같은 AI 개발 앱 코딩에 사용되는 도구와 연관
- 영향받은 도구를 실제로 몇 명이 다운로드했는지는 즉시 확인되지 않음
- Microsoft는 저장소를 내린 사실을 확인했으며, 이는 404 Media가 처음 보도
	- Microsoft 대변인 Ben Hope "잠재적 악성 콘텐츠를 조사하는 동안 일부 저장소를 일시적으로 제거"
		- 일부 저장소는 검토 후 복원되었고, 일부는 작업이 진행되는 동안 오프라인 상태로 유지될 수 있음
		- 영향받은 저장소에서 콘텐츠를 내려받았을 수 있는 **소수 고객에게 통지** 했으며, 추가 조치가 필요한 사항이 확인되면 기존 지원 채널을 통해 직접 연락 예정
- TechCrunch의 질의에 대해 영향받은 고객의 구체적 수치는 즉시 제공하지 않음

## 악성코드 동작 방식

- 보안 기업 **Cloudsmith** 와 커뮤니티 기반 악성코드 분석 사이트 **OpenSourceMalware** 가 해당 해킹을 가장 먼저 지적한 곳 중 하나
- 악성코드는 사용자가 AI 코딩 앱에서 감염된 도구를 열었을 때 **비밀번호 및 기타 민감한 자격 증명** 을 탈취하도록 작동
- Microsoft가 소유한 코드 호스팅 사이트 GitHub에서 프로젝트 페이지 접근 시, **최소 70개 프로젝트** 가 "비활성화(disabled)" 상태로 표시
	- 표시 메시지 "GitHub 서비스 약관 위반으로 인해 GitHub 직원에 의해 이 저장소 접근이 비활성화됨"

## 공급망 공격이라는 맥락

- 최근 수개월간 이어진, 널리 쓰이는 오픈소스 프로젝트를 침해해 해당 코드를 설치한 다수 사용자에게 악성코드를 심는 사례의 최신 건
- 이러한 해킹은 **"공급망(supply chain)" 공격** 으로 불리며, 많은 소프트웨어 제품에 두루 쓰이거나 특정 부류 사용자가 사용하는 코드를 표적으로 삼음
	- 이런 대상은 클라우드 시스템과 대량의 고객 데이터에 접근 권한을 가진 경우가 있어 해커에게 유리할 수 있음
- 오픈소스 프로젝트의 단독 개발자가 표적이 되는 일은 드물지 않으며, 일부는 개발자의 신뢰를 얻기 위한 장기적 시도의 일환
- 다만 이런 공격을 방어할 자원을 갖춘 Microsoft 같은 대형 기술 기업이 침해당하는 것은 이례적

## 반복된 침해 정황

- Ars Technica에 따르면 이번 건은 최근 수 주 사이 Microsoft 오픈소스 프로젝트가 침해된 **두 번째로 알려진 사례**
- 5월 중순, 개발자의 앱 구축을 돕는 Microsoft 오픈소스 프로젝트 **Durable Task** 가 해킹된 것으로 보안 연구자들이 밝힘
- OpenSourceMalware는 이번 최신 사건을 Durable Task 프로젝트의 **"재침해(re-compromise)"** 로 표현
	- 이는 Microsoft가 첫 시도에서 해커를 완전히 제거하지 못했거나, 전혀 별개의 새로운 침해일 가능성을 시사

[brainer](https://news.hada.io/@brainer) \[-\]

혹시 이게 비밀번호를 바꿔도 저에게 계속 MS 계정 로그인 시도가 오는 이유일까요?

답변달기

[GN⁺](https://news.hada.io/@neo) \[-\]

###### Hacker News 의견들

- 순전히 추측이고 개인적인 관찰이지만, 예전의 **RBAC 모델** 은 이미 거의 망가져 있었고 이제는 완전히 깨진 것처럼 보임  
	코딩 어시스턴트와 엔지니어가 서로 무관한 여러 프로젝트를 동시에 만지고, 특히 예전엔 시간이 없어서 못 하던 실험까지 벌이면서 기업 내 **공급망 위험** 이 크게 커졌다고 봄  
	직접 관련됐다고 말하는 건 아니지만 영향은 있다고 느끼고, 요즘 많은 곳에서 개인 장비로 대충 AI 코딩을 하라고 개발자와 관리자들이 부추기는 것도 곧 문제가 될 것 같음  
	최근 공급망 사고들 사이에 공통된 흐름이 없다고는 믿기 어렵고, 이런 공격을 전문으로 하는 해킹 그룹이 있는 것도 보상이 크기 때문이라고 봄
	- 분명히 해두면, 원댓글이 관련 있다고 단정한 건 아니지만 이건 **AI나 바이브 코딩** 과는 전혀 관계없음  
		오래전부터 존재해 온 **개발자 의존성 설치 보안 부재** 와 Shai Halud 웜의 연장선임  
		해커들은 개발자를 속여 무언가 설치하게 만들기 쉽고, 개발자 장비에는 자격 증명, 클라우드 CLI, MCP 같은 민감한 정보가 많아서 이상적인 표적이라는 걸 알아냈음
		- 우리 회사도 비슷함. “AI로 최대한 많이 하지 않으면 뒤처진다” 같은 교리가 퍼져 있음  
		보안은 신경 쓰지 않고 무리에서 제일 먼저 달리려는, 예전의 **IoT 과열** 을 그대로 반복하는 느낌임
		- 총 프로젝트 수에 비해 인력이 너무 적다고 몇 년 동안 주장했지만, 경영진은 대부분의 프로젝트가 유휴 상태라서 한 사람당 많이 맡겨도 괜찮다고 했음  
		결국 이렇게 됨
		- 역할 기반 접근 제어, 즉 **RBAC** 를 다른 것으로 대체해야 한다는 뜻인지, 아니면 현재 쓰는 특정 RBAC 모델들이 망가졌다는 뜻인지 궁금함  
		개인적으로는 이름이 좀 헷갈리지만 **capability 기반 보안 모델** 이 미래라고 봄
- 제목 표현부터 편향적이고, 본문도 마치 **오픈소스의 잘못** 인 것처럼 씀  
	그러고는 시도된 공급망 공격의 책임을 Microsoft에 돌리는 식이라 더 웃김  
	`Microsoft did not immediately provide the specific number of customers affected, when asked by TechCrunch.`라고 하는데, 오픈소스가 원래 그렇게 동작하는 걸 TechCrunch가 설명하지 않음  
	Microsoft를 깔 수 있을 때 까는 걸 좋아하지만, 이번에는 Microsoft가 안전하고 올바른 조치를 했다고 봄  
	기사에서는 마치 전부 Microsoft 잘못이고 침해 범위를 제한한 것도 부끄러운 일인 것처럼 씀  
	`steal passwords of AI developers` 라는 표현도 “AI 개발자”인지 “AI를 쓰는 개발자”인지 묘한 함의를 남김  
	공급망 공격에 대한 설명도 실제 의미가 아니라 결과와 공격 표면의 이유만 말하고 있어서, 이번 보도는 매우 좋지 않다고 봄
	- **TechCrunch** 는 매우 부주의하고 신뢰하기 어려움  
		직접 일했던 내용을 보도하면서 검색 최적화용으로 사실을 지어낸 걸 본 적이 있고, 정정하게 만들 방법도 없었음
		- 그 문장의 무엇이 문제인지 모르겠음  
		Microsoft에는 **조직적 보안 문제** 가 있고, GitHub Actions를 제대로 잠그지 못하고 병합 요청이 CI/CD를 우회하게 둔 점이 이를 돕거나 드러냈음  
		이건 AI 이전부터 존재한 Microsoft 문제이며 논쟁거리도 아님: [https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewO...](https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf)  
		AI 시대에는 이 문제가 풍토병처럼 퍼졌고 무기화되고 있음
		- 그렇다면 사후 분석은 어떻게 보는지 궁금함  
		실제로 무슨 일이 있었고, 어떻게 읽어야 한다는 건가?
- 관련 있어 보이는 글들임  
	[https://news.ycombinator.com/item?id=48418318](https://news.ycombinator.com/item?id=48418318) (The Blight Reaches Microsoft: 73 Repos Disabled in 105 Seconds)  
	[https://news.ycombinator.com/item?id=48450543](https://news.ycombinator.com/item?id=48450543) (Miasma Worm Hits Microsoft Again: Azure Functions Action and 72 Other Repositories Disabled After Supply Chain Attack Targeting AI Coding Agents)  
	[https://news.ycombinator.com/item?id=48416155](https://news.ycombinator.com/item?id=48416155)  
	[https://news.ycombinator.com/item?id=48416269](https://news.ycombinator.com/item?id=48416269) (Miasma Worm Targets AI Coding Agents via GitHub Repos)
	- 감염된 모든 저장소에서 웜을 수정하거나 제거할 수 있는 **완화 도구** 를 만들었고, 이에 대한 글도 썼음  
		월요일에 Hades 캠페인이 Composer, Go, Pip 지원을 추가했음. 그 전에는 NPM과 AI 어시스턴트 편집기만 지원했고, Ruby도 있긴 했지만 요즘 Rubygems를 쓰는 사람이 거의 없어 보임  
		Microsoft조차 놓치는 점은, 이게 코드 생태계의 모든 플랫폼에서 실행되는 첫 웜이라는 것임. 개발자 호스트, 서버, CI/CD 실행기 모두에서 돌고, 그 장비들이 접근 가능한 모든 저장소로 웜을 퍼뜨림  
		이 웜을 이기려면 모든 컴퓨터와 AWS EC2, Google Cloud Platform, Azure, Kubernetes 클러스터를 동시에 100% 꺼야 함. 말 그대로 전체 인프라를 가로질러 퍼짐  
		APT28 악성코드에서 늘 그렇듯 킬 스위치는 호스트 언어를 `ru_RU.KOI8-R` 로 설정하는 것, 즉 `LANG` 환경 변수 설정임. 그러면 전파 메커니즘이 비활성화됨  
		완화 도구: [https://github.com/cookiengineer/antimiasma](https://github.com/cookiengineer/antimiasma)  
		블로그 글: [https://cookie.engineer/weblog/articles/malware-insights-mia...](https://cookie.engineer/weblog/articles/malware-insights-miasma-campaign.html)
- 전통적인 **개인 접근 토큰** 을 지저분하게 사용한 사례일 가능성이 높다고 강하게 의심함  
	이상한 openclaw 장치에서 AI 에이전트에 토큰을 넘길 거라면 세분화된 토큰을 써야 함  
	내 GitHub 계정은 정책이 완전히 다른 조직 3개에 걸쳐 있는데, 아직도 classic 토큰이 허용된다는 사실이 좀 놀라움  
	최소한 각 조직마다 수동으로 허용해야 하게 만들어야 함
	- **AI 에이전트** 는 별도의 보안 주체여야 하고, 필요한 저장소나 조직에 대해서만 전용 접근 토큰을 발급받아야 한다고 봄  
		사람 계정용으로 “주조된” 접근 토큰을 AI 에이전트에 넘기는 건 새로운 “비밀번호를 포스트잇에 적어두기”처럼 느껴짐
		- 맞는 말이지만, 세분화된 토큰의 **권한 관리** 는 악몽에 가까움  
		어떤 작업에 무엇이 정확히 필요하고 올바른지 판단하기 쉽지 않음  
		게다가 소프트웨어 개발자는 권한보다 코드에 집중하는 게 중요하다고 생각하는 경우가 많고, 권한은 다른 사람 책임이라고 여기기도 함
		- classic PAT가 원인이라면, 최근의 GitHub 저장소들 말고도 추가적인 **비공개 저장소** 가 위험할 수 있다는 뜻 아닌가?
		- 공개 저장소 스크래핑에는 낮은 권한 계정의 classic 토큰을 쓰고 있음  
		조직 수준 권한이면 내 용도에는 충분히 잘 맞을 것 같음
- 어제 개인 Microsoft 계정 비밀번호를 재설정해야 했음. 루마니아에서 로그인 시도가 있었다는 **2단계 인증 알림** 이 왔기 때문임  
	어떻게 비밀번호를 알아냈는지는 모르겠음. 내가 가진 Microsoft 제품은 Xbox뿐임  
	AI 이전부터 Microsoft는 체처럼 줄줄 새는 느낌이었고, 회사가 Microsoft에서 벗어나면 좋겠지만 이미 묶여 있음
	- 개인 Microsoft 계정에서 **비밀번호 없는 로그인** 을 허용하지 않도록 설정하는 건 거의 불가능함  
		그래서 실제로는 계정이 그렇게 설정되어 있고, 받은 MFA 요청도 2단계 인증이 아니라 단순히 계정 접근을 시도한 것일 가능성이 큼  
		나도 하루에 여러 번 이런 요청을 받았고, 휴대폰에서 Microsoft Authenticator 앱을 설정하면 얼굴, 지문, PIN 같은 잠금이 있는 경우 강제로 비밀번호 없는 방식으로 바뀐다는 걸 알게 됨  
		우회하려면 Authenticator 앱에 계정을 설정하는 동안 그런 잠금을 전부 꺼야 함  
		Microsoft 계정을 별로 쓰지 않아서 이제는 Authenticator 대신 별도 이메일로 인증함  
		이런 방식으로 동작한다는 것 자체가 미친 일이지만, 아마 Microsoft 내부 누군가는 비밀번호 없는 로그인 KPI를 채우고 있을 것 같음
		- 내가 일했던 일부 조직에서는 비밀번호가 맞는지와 무관하게 **다중 인증 프롬프트** 가 뜨게 했음. 공격자의 시간을 더 낭비시키려는 목적이었음  
		Microsoft도 그런지는 확실하지 않음
- 어떻게 이렇게 많은 저장소에 난독화된 파일을 추가할 수 있는지 누가 설명해줬으면 함. **코드 리뷰** 가 전혀 없나?  
	제목도 오해를 부름. setup이 저장소에서 일하는 사람들이 자동 실행하게 되는 설정을 추가하는 것이고, 그 사람들은 VSCode, Cursor, Claude, Gemini를 써야 함  
	Codex, opencode, 다른 실행 하네스를 쓰는 사람들은 안전할 것 같음  
	자세한 내용: [https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-...](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents)
	- 한 대기업에서 일하는 친한 친구가 있음. 어느 회사인지는 말할 수 없지만 S&P 500 기업임  
		꽤 오래 일했는데도 자신이 맡은 프로젝트가 실제로 어떻게 생겼는지 본 적이 없고, 저장소를 클론해두었고 사용 언어만 알 뿐 그 이상은 모름  
		모든 게 대충 AI로 이어붙여지고 있음. 그 프로젝트는 회사 전체 제품의 **인증과 인가 시스템** 임  
		본인 말로는 “하루 종일 Tab만 누르고 리뷰에는 ‘의도된 동작’이라고 쓴다. 리뷰도 전부 AI가 하고 인간은 개입하지 않는다. CEO와 CTO가 진지하게 이렇게 하라고 한다. 무언가 깨지면 실제 코드를 본 사람이 없어서 아무도 어떻게 동작하는지 모른다. 성과 평가는 우리가 한 일이 아니라 사용한 토큰 수로 한다”라고 함  
		지금 많은 회사가 이럴 가능성이 있고, 실제 코드 리뷰가 없다고 생각해도 무리는 아님
		- 악성 커밋 중 다수가 작성자 `github-actions ` 로 표시됨  
		내부 GitHub CI/CD 쪽으로 인증하고 있다는 뜻이고, 그런 커밋이 너무 많아서 어떤 자동화 도구도 왕겨 산더미 속 독을 찾아내기 어려움  
		그래서 이건 2025년 9월 **GitHub 보안 침해** 와 관련 있음  
		“다섯 저장소의 GitHub 별은 합쳐 1,459개이고, mantine-datatable 하나가 1,225개를 차지한다. 별은 얼마나 많은 개발자가 소스를 로컬에 체크아웃했는지에 대한 거친 대리 지표이며, 이 공격이 노리는 집단이다.”  
		“모든 커밋은 서명되지 않았고, github-actions 신원이며, 메시지는 `chore: update dependencies [skip ci]`, 같은 여섯 파일 흔적을 남겼다. 다섯 저장소를 49초 만에 훑은 건 사람이 커밋한 게 아니라 자동화다. 이는 이전 감염에서 쓰기 권한이 있는 GitHub 토큰을 수집한 뒤, 그 토큰이 닿는 모든 저장소에 지속성 페이로드를 밀어 넣는 Shai-Hulud 자기 전파와 일치한다.”  
		[https://safedep.io/miasma-worm-ai-coding-agent-config-inject...](https://safedep.io/miasma-worm-ai-coding-agent-config-injection/)  
		실제 동작: [https://safedep.io/config-files-that-run-code/](https://safedep.io/config-files-that-run-code/)  
		저 사람들과는 관련 없지만, 지금 무슨 일이 벌어지는지에 대해 내가 찾은 가장 단순하고 자세한 설명임
		- 동료가 진지하게 “이제 코드 대부분을 생성한다면, 실제로 그 코드를 누가 다 읽고 있지?”라고 물었음  
		작은 회사지만 어떤 사람들은 **신탁처럼 AI를 믿고 싶어 하는 충동** 이 거의 종교적이라고 느껴짐  
		나는 내가 생성한 코드의 90% 이상을 주니어 개발자 코드 리뷰하듯 읽음  
		지금 새 기능을 꽤 강하게 바이브 코딩 중인데, GitHub PR이 다시 동작하기 시작하면 철저히 읽을 예정임
		- 저장소에 푸시할 수 있는 계정이 탈취됐다면 **PR 리뷰** 는 필요 없었을 것임
- 이런 사람들에게 Secure Boot의 **루트 CA 인증서** 를 맡기고 있는 건가?
	- 2023년 보안 검토에서 실패한 그 회사를 말하는 건가? \[0\]  
		“위에서 설명한 결함 하나하나는 개별적으로 보면 이해 가능할 수 있다. 그러나 모두 합치면 Microsoft의 조직적 통제와 거버넌스, 그리고 보안에 관한 기업 문화의 실패를 가리킨다.”  
		Microsoft의 제품과 서비스는 어디에나 있다. 세계에서 가장 중요한 기술 기업 중 하나이며, 어쩌면 가장 중요할 수도 있다. 이 위치에는 최고 수준의 전 세계적 책임이 따른다. 재무나 시장 출시 요인이 사이버보안과 Microsoft 고객 보호를 약화시키지 않도록, CEO에서 시작되는 책임 있는 보안 중심 기업 문화가 필요하다.  
		“불행히도 이 검토 전반에서 위원회는 Microsoft가 기업 보안 투자와 엄격한 위험 관리를 모두 낮은 우선순위로 둔 기업 문화를 가리키는 일련의 운영·전략적 결정을 확인했다. 이 결정들은 전 세계 Microsoft 고객에게 상당한 비용과 피해를 초래했다.”  
		“위원회는 Microsoft가 보안 문화를 바로잡아야 한다고 확신한다.”  
		\[0\] [https://www.cisa.gov/resources-tools/resources/CSRB-Review-S...](https://www.cisa.gov/resources-tools/resources/CSRB-Review-Summer-2023-MEO-Intrusion)
		- Secure Boot의 **신뢰 루트** 는 보통 Microsoft 인증서가 아니라 OEM 인증서인데, 그게 더 나쁠 수도 있음: [https://www.binarly.io/blog/pkfail-untrusted-platform-keys-u...](https://www.binarly.io/blog/pkfail-untrusted-platform-keys-undermine-secure-boot)  
		어쨌든 Microsoft 인증서를 제거하고 자기 인증서를 등록하는 건 자유임
		- “신뢰”라기보다 “강제로 받아들여야 함”에 가까움  
		이번 사건도 Microsoft가 보안을 제대로 챙기는 회사라기보다 **보안 문제 자체** 였던 전적을 이어가는 것뿐임
		- Microsoft를 보안과 관련해 신뢰하는 건 어리석은 일임  
		지난 40년 동안 신경 쓰지 않는다는 걸 여러 번 보여줬음
- 늦게 깨달은 편일 수도 있지만, “코드가 나쁘다” 같은 이유로 AI를 쓰고 싶지 않더라도 **보안 감사** 에는 AI를 쓰는 걸 고려하라고 한동안 말해왔음  
	적어도 코드에서 취약점을 스캔하는 도구는 써야 함  
	공격 벡터는 데이터를 훔치는 플러그인만이 아니라, 사용하는 거의 모든 소프트웨어의 0-day 취약점과 LLM을 든 스크립트 키디가 여러분의 웹 서비스를 공격하는 것까지 포함  
	해킹은 늘어날 것이고 더 나빠질 테니, 사이버보안 감사와 감사 도구에 투자하지 않는 곳은 재고해야 함
- 아무도 자기 장비에서 `npm install` 이나 `pip install` 을 하면 안 됨  
	적절한 **샌드박싱** ([https://github.com/ashishb/amazing-sandbox](https://github.com/ashishb/amazing-sandbox))을 꾸준히 쓰면 이런 공격의 피해 범위를 크게 줄일 수 있음
	- Docker 백엔드는 명령을 **루트리스 컨테이너** 에서 실행하나?  
		코드를 훑어봤지만 이를 확인할 만한 부분은 못 봤음
		- Docker는 진지한 **샌드박싱 전략** 이 아님
		- `npm install` 이나 `pip install` 을 자기 장비에서 하지 말라는 말이면, 어떤 대안을 제안하는 건가?  
		샌드박스 밖에서 설치하지 말라는 뜻인가?
		- 여기에는 **탐지 구성요소** 도 있나?  
		개발을 샌드박스에서 하는 건 좋지만 다음 단계는 운영 배포임  
		샌드박스 안에서 악성 동작이 일어났는지 어떻게 알아서, 그 악성코드를 더 배포하지 않을 수 있나?
- Microsoft의 Github가 Microsoft Azure와 다른 모든 사용자의 Microsoft 코드베이스 접근을 **이용약관 위반** 때문에 중단했다는 사실이 지나치게 웃김  
	이 조직도를 제대로 실감하게 해줌: [https://www.businessinsider.com/big-tech-org-charts-2011-6](https://www.businessinsider.com/big-tech-org-charts-2011-6)

답변달기