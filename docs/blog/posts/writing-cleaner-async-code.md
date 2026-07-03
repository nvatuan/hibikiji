---
date: 2026-07-02
categories:
  - Software Development
tags:
  - patterns
  - async
---

# Writing cleaner async code

A running list of small refactors that make asynchronous code easier to read and
harder to break.

<!-- more -->

- Prefer **structured concurrency** — spawn work inside a scope that owns its
  lifetime, so nothing leaks past it.
- Push side effects to the edges; keep the core pure and testable.
- A timeout is not optional. Every network call gets one.

More concrete examples to come as I clean up old projects.
