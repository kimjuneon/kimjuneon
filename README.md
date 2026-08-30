<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&height=180&color=0:1E293B,100:0F766E&text=kimjuneon&fontColor=FFFFFF&fontSize=42&fontAlignY=35&desc=Java%2FSpring%20Backend%20%7C%20Data%20%C2%B7%20Events%20%C2%B7%20Reliability&descAlignY=58&descAlign=50)

### 안녕하세요, 백엔드 개발자 김준언입니다 👋

대량 데이터 처리와 이벤트 흐름을 안정화하고, 변화가 생겨도 확장·유지보수하기 쉬운 구조를 설계합니다.

기능이 한 번 동작하는 데서 끝내지 않고, 데이터와 사용량이 늘어도 안정적으로 운영되며 다음 개발자가 안전하게 수정할 수 있는 서비스를 지향합니다.

[![GitHub followers](https://img.shields.io/github/followers/kimjuneon?style=social)](https://github.com/kimjuneon?tab=followers)
[![Profile views](https://visitor-badge.laobi.icu/badge?page_id=kimjuneon.kimjuneon)](https://github.com/kimjuneon)
[![Velog](https://img.shields.io/badge/Tech%20Blog-Velog-20C997?style=flat-square&logo=velog&logoColor=white)](https://velog.io/@juneon/posts)

</div>

---

## About Me

- **대량 데이터·트래픽 대응** — pagination, batch, idempotency, concurrency, cache를 활용해 부하와 정합성 문제를 해결합니다.
- **유지보수 가능한 설계** — 도메인 경계와 책임을 명확히 하고, Hexagonal Architecture와 Port/Adapter 구조로 변경 범위를 줄입니다.
- **안정성과 테스트** — 단위·통합·이벤트 테스트와 retry/recovery, 예외 처리, 로그·관측성을 함께 설계합니다.
- **배포와 운영** — Docker와 GitHub Actions 기반 파이프라인을 구성하고 클라우드 환경에서 배포 이후의 운영까지 확인합니다.

## Tech Stack

**Backend**

`Java` `Spring Boot` `Spring Data JPA` `Spring Security`

**Data & Messaging**

`MySQL` `PostgreSQL` `Kafka` `Firebase FCM`

**Architecture & Quality**

`Hexagonal Architecture` `REST API` `JUnit` `ArchUnit`

**Delivery & Operations**

`Docker` `GitHub Actions` `GCP` `AWS`

## Projects

### [머니헌터](https://github.com/kimjuneon/money-hunter)

Apps in Toss 기반의 캐릭터 성장형 리워드 서비스입니다.

- 성장·자동사냥·던전·보상 정책을 운영 중 변경 가능한 구조로 설계
- Toss 로그인/IAP, 광고 보상 세션과 프로모션 흐름 구현
- 관리자 API와 접속·리텐션 지표를 구축하고 Cloud Run에 배포
- DAU 100명대에서 200명대로 성장

`Java` `Spring Boot` `Docker` `GCP`

### [쿠링](https://github.com/ku-ring/ku-ring-backend-web)

건국대학교 공지를 수집·검색하고 Firebase FCM으로 알림을 전달하는 API 서버입니다.

- 1,000건 이상의 공지를 페이지 단위로 수집·병합하도록 개선
- HTML 구조 차이와 파싱 실패를 fallback parser와 예외 처리로 보완
- 메시지 조합과 Firebase 전송 책임을 Port/Adapter 구조로 분리
- 빈 페이지, I/O 오류, 파싱 실패 테스트와 retry/recovery 보강

`Java` `Spring Boot` `JPA` `Firebase FCM`

### [팔구사구 Trade Service](https://github.com/89-49/trade-service)

Kafka 이벤트로 예약 완료와 구매자·판매자의 거래 완료 흐름을 연결하는 마이크로서비스입니다.

- 입력/출력 Port, Use Case, Adapter를 분리한 Hexagonal Architecture 적용
- 낙관적 락과 재시도로 동시 완료 요청의 정합성 보완
- ArchUnit과 계층별 테스트로 아키텍처 규칙 검증
- Zipkin·Grafana Alloy 기반의 분산 추적 환경 구성

`Java` `Spring Boot` `Kafka` `Docker`

### [만나봄](https://github.com/mannabom/mannabomServer)

프로필·연애관 기반 매칭 이후의 호감, 메시지, 평가, 결제와 관리자 운영을 연결한 서버입니다.

- 요청 출처를 프로필/연애관으로 구분하도록 도메인 모델과 DB 마이그레이션 보완
- `FileStoragePort` 중심으로 로컬·S3·GCS 저장소 Adapter 분리
- JWT 인증·권한·감사 로그와 관리자 운영 기능 구현
- GitHub Actions와 GCP 기반 배포 워크플로 구성

`Java` `Spring Boot` `JPA` `Docker` `GCP`

## Learning & Writing

- [Today I Learned](https://github.com/kimjuneon/TIL) — 프로젝트에서 마주친 문제와 해결 과정을 짧고 재현 가능한 기록으로 정리합니다.
- [Velog](https://velog.io/@juneon/posts) — 문제 상황 → 선택지 비교 → 구현 → 테스트 → 결과와 한계 순서로 기술 글을 작성합니다.

주요 기록 주제:

- 페이지 단위 공지 수집과 fallback parser
- Kafka 이벤트 처리의 멱등성·낙관적 락·재시도 경계
- 외부 시스템 의존성을 Port/Adapter로 분리하는 방법

## GitHub Stats

<div align="center">

![GitHub stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=kimjuneon&theme=github_dark)
![Repositories per language](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=kimjuneon&theme=github_dark)

</div>

---

<div align="center">

꾸준히 만들고, 운영하고, 배운 것을 기록합니다.

</div>
