# CONTRIBUTING.md

We welcome contributions from everyone and appreciate your consideration in helping us to improve our code, tests, and documentation. Please read through the [Code of Conduct](https://github.com/KingOfOrikid/DATA551_proj/blob/main/CODE_OF_CONDUCT.md) before making any contributions.

## Reporting security flaws

If you find a flaw in our project that can hurt users or provide unauthorized access, please contact our maintainer privately, as follows.

Contact: yuxin.yuki.chen@gmail.com

## Bug reporting

We encourage people to report bugs. Please read [How to Submit a Good Bug Report](https://github.com/theopensourceway/guidebook/blob/master/bug_report.adoc) before submitting your report.        
The most important advice from there is: 1) do as thorough a search as you can to see whether the bug has already been reported, and 2) be as precise and complete as you can when reporting a new bug.

To report a bug:
1. Go to the appropriate project.
2. Click the Issues button on the left of the window.
3. Click the "New issue" button.
4. Fill out the Title and Description. You don't need to fill out the other fields.

## Cloning, Branching, and Merging

### Commit guide

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:
```
    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."
```

### Pull request workflow

The [Introduction to GitLab Flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html) provides useful background. Please use the following workflow when submitting merge requests.

### Creating the material for a pull request

1. Fork our project into your personal namespace or group.

2. Create a feature branch in your fork. If possible, include the title of the issue or the issue number that the merge request corresponds to.

3. Write appropriate continuous integration tests.

4. Push the commit(s) to your working branch in your fork.
  - Squash commits into a small number of logically organized commits, keeping the commit history intact on shared branches.
  - Please try to have fewer than 15 commit messages per merge request.

### Testing

Unit tests should be written for all package functions.

### The merge request

Submit a merge request (MR) to our projects default branch, following these criteria.

  - Refer to the issue that defines the bug you are fixing or the feature you are adding.
  - Include a test or tests.
  - Include updates to any relevant or affected documentation.
  - The merge request title should describe the change you wish to make.
  - The merge request description should give the reason for the change.
  - Use complete URLs to issues and other merge requests, milestones, etc.
  - Include the complete path when referring to files within this repository (no URL required).
  - Try to keep the amount of changes you make in a single merge request as small as possible.
  - Do not include emoji in commit messages.

Please follow Chris Beam's seven rules for writing a good commit messages:

- Separate subject from body with a blank line.
- Limit the subject line to 50 characters.
- Capitalize the subject line.
- Do not end the subject line with a period.
- Use the imperative mood in the subject line.
- Wrap the body at 72 characters.
- Use the body to explain what and why versus how.

For examples and additional explanation of these seven rules, please read [Chris Beam's blog post](https://chris.beams.io/posts/git-commit/).

### Merge request acceptance criteria

Your merge request needs at least one approval from a maintainer on the project, but depending on your change you might need additional approvals. Merge requests that fix a regression are usually accepted quickly and usually only require a single approval, whereas a new feature may require approval from multiple maintainers and our project leads.