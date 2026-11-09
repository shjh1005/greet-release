# Changelog

이 파일은 이 프로젝트의 주목할 만한 변경을 기록한다.

형식은 [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)을 따르며,
버전 번호는 [유의적 버전](https://semver.org/lang/ko/)을 따른다.

## [Unreleased]

### Added

- `greet()`에 `punctuation` 인수를 더해 끝 문장부호를 고를 수 있다(기본값 `!`).

### Fixed

- `greet()`가 빈 이름이나 공백뿐인 이름에 `Hello, !`를 내던 것을 `Hello, world!`로 고쳤다.

## [0.1.0] - 2026-11-09

### Added

- `greet()`와 명령행 인사말: 이름을 인수로 받아 `Hello, <name>!`을 한 줄 출력한다.
