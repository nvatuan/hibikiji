# Contributing

## Git workflow

Always work on a branch and open a pull request — never push directly to `main`.

```bash
git checkout -b your-branch-name
git add -A && git commit -m "your message"
git push -u origin HEAD
gh pr create
```
