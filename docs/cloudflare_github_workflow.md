# Cloudflare Workers: GitHub Actions Deployment Guide (2026)

This guide provides a production-ready GitHub Actions workflow for deploying Cloudflare Workers with best practices for security, environments, and observability.

## 1. Workflow Configuration (`.github/workflows/deploy.yml`)

```yaml
name: Deploy Cloudflare Worker

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  deploy:
    name: Build & Deploy
    runs-on: ubuntu-latest
    timeout-minutes: 15
    permissions:
      contents: read
      deployments: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install Dependencies
        run: npm ci

      - name: Run Tests
        run: npm test

      - name: Deploy to Cloudflare
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          # Deploy to production on main branch, otherwise create a preview
          command: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' && 'deploy' || 'deploy --dry-run --outdir=dist' }}
          # For PRs, you can use the preview feature
          # command: deploy --name my-worker-pr-${{ github.event.number }}
```

## 2. Best Practices for CI/CD

| Practice | Description |
| :--- | :--- |
| **OIDC Authentication** | Use OpenID Connect for secure, short-lived credentials between GitHub and Cloudflare. |
| **Environment Secrets** | Store `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` in GitHub Repository Secrets. |
| **Wrangler Types** | Run `npx wrangler types` as part of your build process to ensure type safety. |
| **Preview Deployments** | Use `wrangler deploy --name <pr-name>` for pull requests to test changes in isolation. |
| **Gradual Rollouts** | Use Cloudflare's **Gradual Deployments** feature to roll out changes to a percentage of traffic. |

## 3. Security Checklist
- [ ] **No Secrets in Code**: Ensure no API keys or tokens are committed to the repository.
- [ ] **Scoped API Tokens**: Create tokens with the minimum required permissions (e.g., `Edit Cloudflare Workers`).
- [ ] **Branch Protection**: Require status checks (tests and linting) to pass before merging to `main`.
- [ ] **Audit Logs**: Regularly review Cloudflare and GitHub audit logs for unauthorized deployment activity.
