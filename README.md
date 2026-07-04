![](./docs/assets/hibikiji.png)

[_icon source_](https://twitter.com/huwahuwahibiki/status/1784625749414285368)

---

My personal blog — an all-in-one hub for coding, travel, cooking, and hobbies.
Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), deployed to GitHub Pages.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000/

## Deploy

Pushing to `main` triggers a GitHub Actions workflow that builds and deploys to GitHub Pages automatically.

## Writing

Posts live in `docs/blog/posts/`. Each file needs front-matter:

```yaml
---
date: YYYY-MM-DD
categories:
  - Platform Engineering   # or: Software Development | Hobby Projects | Travel | General
tags:
  - your-tag
---
```