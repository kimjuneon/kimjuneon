<div align="center">

# 쿠링

건국대학교 공지를 수집·검색하고 Firebase FCM으로 알림을 전달하는 API 서버

**[Repository ↗](https://github.com/ku-ring/ku-ring-backend-web)** · **[← Profile](../README.md)**

</div>

| 문제 | 해결 | 결과 |
| :--- | :--- | :--- |
| 공지 수집량 증가 | 페이지 단위 수집·병합 | 1,000건 이상의 공지 처리 |
| HTML 구조 차이 | Fallback parser와 예외 처리 | 파싱 실패 경로 보완 |
| 메시지·전송 책임 결합 | Port/Adapter로 책임 분리 | 변경 범위와 테스트 경계 축소 |
| 외부 I/O 실패 | 실패 테스트와 retry/recovery | 복구 가능한 수집·전송 흐름 |

<h2 align="center">핵심 기여</h2>

### 페이지 단위 공지 수집

- 여러 페이지의 공지를 순차적으로 수집하고 병합하도록 수집 흐름을 개선했습니다.
- 빈 페이지와 I/O 오류가 전체 수집 실패로 이어지지 않도록 경계를 보완했습니다.

### 파서 안정성

- 공지 소스별 HTML 구조 차이를 처리하는 fallback parser를 적용했습니다.
- 파싱 실패와 예외 케이스를 테스트로 고정해 변경 시 회귀를 확인할 수 있게 했습니다.

### 알림 구조 분리

- 메시지 조합과 Firebase 전송 책임을 Port/Adapter 구조로 분리했습니다.
- 외부 전송 시스템 변경이 핵심 로직에 미치는 영향을 줄였습니다.

---

<div align="center">

**[← Projects로 돌아가기](../README.md#projects)**

</div>
