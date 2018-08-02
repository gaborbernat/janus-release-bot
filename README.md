# janus-release-bot

This bot accomplishes the following release operation:

1. Track a repository for newly created issues.
2. If an administrator (has merge rights) of the repository
   creates an issue with "release <commit sha> as <version>"
   trigger release flow
3. Create a release commit (e.g. run towncrier - will invoke a tox env for this)
4. Push and create a PR
5. Wait for all PR checks to complete with success
6. Tag the release commit with the version
7. Do release (call tox env), this is also where you would do release notification.
8. Merge release PR via a merge commit
9. Close release issue

For every interaction the logs will be commented onto the release issue. 
