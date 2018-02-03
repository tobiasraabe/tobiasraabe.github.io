
echo "Deploying updates to tobiasraabe.github.io..."

# Build website
hugo

# Go to dir with published content
cd publish

# Add all content to git
git add -A

# Commit changes
$msg = "Rebuilding site $(Get-Date -Format G)"
git commit -m "$msg"

# Push source files to github
git push origin master

# Come back
cd ..