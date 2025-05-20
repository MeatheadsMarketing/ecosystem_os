#!/bin/bash

echo "⚠️  This will force-push your local main branch to GitHub."

REPO="https://github.com/MeatheadsMarketing/ecosystem_os.git"

echo "🔁 Re-adding origin and pushing with --force..."
git remote set-url origin $REPO
git add .
git commit -m "🔁 Force sync: replacing GitHub content with local repo"
git push --force origin main

echo "✅ Force push complete. Repo now synced with local scaffold."
