# 팔구사구 Trade Service

> Kafka 이벤트로 예약 완료와 구매자·판매자의 거래 완료 흐름을 연결하는 마이크로서비스

[← 프로필](https://github.com/kimjuneon) · [저장소 ↗](https://github.com/89-49/trade-service)

| 구분 | 내용 |
| :---: | :--- |
| **Focus** | 이벤트 처리, 동시성 정합성, 아키텍처 규칙, 분산 추적 |
| **Stack** | Java, Spring Boot, Kafka, Docker |
| **Architecture** | Hexagonal Architecture, Port/Use Case/Adapter |

## 핵심 기여

### 이벤트 기반 거래 완료

- Kafka 이벤트를 통해 예약 완료와 구매자·판매자의 거래 완료 흐름을 연결했습니다.
- 이벤트 소비와 도메인 처리의 책임 경계를 분리했습니다.

### 동시성 정합성

- 낙관적 락과 재시도를 적용해 동시에 들어오는 완료 요청의 정합성을 보완했습니다.
- 재시도 범위를 명확히 해 중복 처리와 충돌 상황을 다룰 수 있게 했습니다.

### 구조와 관측성

- 입력·출력 Port, Use Case, Adapter로 계층을 분리했습니다.
- ArchUnit과 계층별 테스트로 아키텍처 규칙을 검증했습니다.
- Zipkin과 Grafana Alloy 기반의 분산 추적 환경을 구성했습니다.

---

<div align="center">

**[← Projects로 돌아가기](https://github.com/kimjuneon#projects)**

</div>
