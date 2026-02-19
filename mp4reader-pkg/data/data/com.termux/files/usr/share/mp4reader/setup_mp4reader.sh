#!/data/data/com.termux/files/usr/bin/bash

# ===== CONFIG =====
REPO_NAME="MP4Reader"
GITHUB_USER="KKAU789"

echo "Enter GitHub Personal Access Token:"
read -s GITHUB_PAT

echo
echo "Setting remote with token..."

git remote set-url origin https://$GITHUB_USER:$GITHUB_PAT@github.com/$GITHUB_USER/$REPO_NAME.git

echo "Pushing to GitHub..."
git branch -M main
git push -u origin main

echo
echo "✅ MP4Reader pushed successfully!"
