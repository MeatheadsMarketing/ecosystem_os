
#!/bin/bash
REPO="https://github.com/MeatheadsMarketing/ecosystem_os.git"
git init
git remote add origin $REPO
git add .
git commit -m 'Initial commit: full GPT ingestion system'
git branch -M main
git push -u origin main
