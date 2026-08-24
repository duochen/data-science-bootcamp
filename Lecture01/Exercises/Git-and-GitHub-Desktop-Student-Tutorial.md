# Git and GitHub with GitHub Desktop and Visual Studio Code

## A 30–45 Minute Step-by-Step Student Tutorial

In this tutorial, you will create a GitHub repository named `ai-data-science`, clone it to your computer, edit files in Visual Studio Code, and use Git commands to save and share your work.

You will use only the `main` branch. Branches, merging, and pull requests are not covered in this lesson.

> **The workflow to remember:** Pull → Edit → Save → Check → Add → Commit → Push → Verify

---

## Learning Goals

By the end of this tutorial, you will be able to:

- Explain the difference between Git, GitHub, GitHub Desktop, and Visual Studio Code.
- Explain the working folder, staging area, local repository, and remote repository.
- Create a GitHub repository named `ai-data-science`.
- Configure your Git name and email.
- Clone a repository with GitHub Desktop.
- Open the repository in Visual Studio Code.
- Use `git status`, `git add`, `git commit`, `git push`, and `git pull`.
- Use GitHub Desktop and VS Code to view the same Git information.
- Verify that your work is stored on GitHub.

## Estimated Time

| Activity | Time |
|---|---:|
| Understand the tools and four locations | 5–7 minutes |
| Check software and configure Git | 5–7 minutes |
| Create and clone the repository | 5–7 minutes |
| Complete the first Git workflow | 12–15 minutes |
| Practice pulling and use visual tools | 5–8 minutes |
| Final check | 3 minutes |

---

# Part 1: Understand the Tools

## Git

Git is a version-control program. It tracks changes and saves checkpoints called **commits** on your computer.

## GitHub

GitHub is a website that stores Git repositories online. The copy on GitHub is called a **remote repository**.

## GitHub Desktop

GitHub Desktop is a visual application for Git and GitHub. It provides buttons for cloning, committing, pushing, and pulling.

GitHub Desktop includes Git for its own use. However, to type Git commands in the VS Code terminal, you must also install Git separately.

## Visual Studio Code

Visual Studio Code, or VS Code, is the editor you will use to create files and write code. It includes:

- A file explorer
- A code editor
- A terminal for Git commands
- A Source Control panel for viewing Git changes

---

# Part 2: Understand the Four Git Locations

When you work with Git, your changes move through four locations.

| Location | What it contains | How changes move forward |
|---|---|---|
| **Working folder** | Files you are currently creating or editing | `git add` |
| **Staging area** | Changes selected for the next checkpoint | `git commit` |
| **Local repository** | Commits saved on your computer | `git push` |
| **Remote repository** | Commits stored online on GitHub | Other computers use `git pull` |

The flow is:

```text
Working folder  --git add-->  Staging area  --git commit-->  Local repository
                                                                    |
                                                                git push
                                                                    |
                                                                    v
                                                        Remote repository on GitHub
```

`git pull` moves the newest commits from the remote repository into your local repository and updates your working folder.

## A Homework Analogy

- **Working folder:** You are writing your homework.
- **Staging area:** You choose the pages you want to submit.
- **Local repository:** You place those pages into a labeled, sealed envelope.
- **Remote repository:** You submit the envelope to the teacher online.

> Saving a file is not the same as committing it. Committing is not the same as pushing it.

---

# Part 3: Before You Begin

You need:

1. A verified GitHub account
2. GitHub Desktop signed in to your GitHub account
3. Visual Studio Code
4. Git installed separately for command-line use

## Step 1: Check Git

1. Open Visual Studio Code.
2. Select **Terminal → New Terminal**.
3. Enter:

```bash
git --version
```

You should see something similar to:

```text
git version 2.x.x
```

If you see a message saying that `git` is not recognized or not found, install Git from `https://git-scm.com/downloads`, then restart VS Code.

---

# Part 4: Configure Your Git Identity

Every commit records the author’s name and email. Configure them once on each computer.

## Step 1: Set Your Name

In the VS Code terminal, enter the following command. Replace the example with your own name.

```bash
git config --global user.name "Alex Student"
```

## Step 2: Set Your Email

Use the email connected to your GitHub account.

```bash
git config --global user.email "alex@example.com"
```

Do not copy the example name or email.

## Step 3: Verify the Configuration

```bash
git config --global user.name
git config --global user.email
```

Check that Git displays your correct name and email.

### Privacy Option

If you do not want your personal email shown in public commits, use the GitHub-provided `noreply` email found under **GitHub → Settings → Emails**. Make sure that email is also recognized by your GitHub account.

### GitHub Desktop Check

In GitHub Desktop, open **File → Options → Git** on Windows, or **GitHub Desktop → Settings → Git** on macOS. Confirm that the name and email are correct.

---

# Part 5: Create the Remote Repository on GitHub

## Step 1: Open GitHub

1. Go to `https://github.com`.
2. Sign in.
3. Select the **+** menu in the upper-right corner.
4. Select **New repository**.

## Step 2: Enter the Repository Information

Use the following settings:

| Setting | Value |
|---|---|
| Repository name | `ai-data-science` |
| Description | `Practice repository for learning Git, GitHub, and data science.` |
| Visibility | Public, unless your teacher says Private |
| Initialize this repository | Select **Add a README file** |

Leave `.gitignore` and license unchanged for this short lesson.

## Step 3: Create It

1. Select **Create repository**.
2. Confirm that the page shows `ai-data-science` and a file named `README.md`.
3. Confirm that the branch menu displays `main`.

You have now created the **remote repository**.

> Never upload passwords, API keys, access tokens, private student information, or other secrets to GitHub.

---

# Part 6: Clone the Repository with GitHub Desktop

To **clone** means to create a complete local copy of a remote repository.

## Step 1: Start Cloning

1. Open GitHub Desktop.
2. Select **File → Clone repository**.
3. Select the **GitHub.com** tab.
4. Choose `your-username/ai-data-science`.

If you do not see it, select **URL** and paste the repository URL from GitHub.

## Step 2: Choose the Local Path

Choose a location such as:

```text
Documents/GitHub/ai-data-science
```

Select **Clone**.

## Step 3: Check the Result

GitHub Desktop should show:

- **Current repository:** `ai-data-science`
- **Current branch:** `main`
- **No local changes**

You now have:

- A remote repository on GitHub
- A local repository on your computer
- A working folder containing `README.md`

---

# Part 7: Open the Repository in VS Code

1. In GitHub Desktop, select **Repository → Open in Visual Studio Code**.
2. In VS Code, find `README.md` in the Explorer.
3. Open **Terminal → New Terminal**.

The terminal path should end with `ai-data-science`.

Check the repository:

```bash
git status
```

You should see messages similar to:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

### What This Means

- `On branch main`: You are using the `main` branch.
- `up to date`: Your local and remote repositories contain the same commits.
- `working tree clean`: No saved files have uncommitted changes.

> Run Git commands only when the terminal is inside the repository folder.

---

# Part 8: Pull Before You Work

Run:

```bash
git pull
```

`git pull` downloads new commits from GitHub and updates your local files.

Because you just cloned the repository, you will probably see:

```text
Already up to date.
```

Use `git pull` at the beginning of each work session, especially if you use more than one computer or edit files on GitHub.

---

# Part 9: Create and Edit Files

## Step 1: Create `analysis.py`

1. In the VS Code Explorer, select **New File**.
2. Name the file `analysis.py`.
3. Enter:

```python
# Store three sample data values in a list.
scores = [82, 91, 87]

# Calculate the average of the values.
average = sum(scores) / len(scores)

# Display the result.
print(f"Average score: {average:.2f}")
```

4. Save the file with **Ctrl+S** on Windows or **Command+S** on macOS.

## Step 2: Update `README.md`

Replace or update its contents with:

```markdown
# AI Data Science

This repository is used to practice Git, GitHub, Python, and data science.

## First Program

The `analysis.py` program calculates the average of three sample scores.
```

Save the file.

---

# Part 10: Check the Working Folder

Run:

```bash
git status
```

You should see:

- `README.md` under **Changes not staged for commit**
- `analysis.py` under **Untracked files**

## Important Terms

- **Modified:** Git already knows the file, and you changed it.
- **Untracked:** The file is new, and Git is not tracking it yet.

At this point, the changes exist only in your **working folder**.

### View the Same Information in VS Code

Select the **Source Control** icon on the left side of VS Code. A number beside the icon shows how many files changed. The files appear under **Changes**.

### View the Same Information in GitHub Desktop

Switch to GitHub Desktop. The **Changes** tab shows both files and the exact lines that changed.

---

# Part 11: Add Files to the Staging Area

Run:

```bash
git add README.md analysis.py
```

This selects both files for the next commit.

Check again:

```bash
git status
```

The files should now appear under:

```text
Changes to be committed
```

They are now in the **staging area**.

## Useful Variations

Stage one file:

```bash
git add analysis.py
```

Stage all changes in the current repository:

```bash
git add .
```

For a beginner project, `git add .` is convenient. In larger projects, selecting specific files helps prevent accidental commits.

### VS Code Equivalent

In the Source Control panel, select the **+** beside a file to stage it. The file moves from **Changes** to **Staged Changes**.

### GitHub Desktop Equivalent

In GitHub Desktop, checked files in the **Changes** list are selected for the next commit. Uncheck a file to exclude it.

---

# Part 12: Commit the Changes Locally

Run:

```bash
git commit -m "Add first data analysis program"
```

A **commit** is a named checkpoint saved in your local repository.

A good commit message:

- Begins with an action word such as `Add`, `Fix`, `Update`, or `Remove`
- Describes the change clearly
- Is short and specific

Check the status:

```bash
git status
```

Git may say that your branch is ahead of `origin/main` by one commit. This means:

- Your commit exists in the **local repository**.
- It has not been uploaded to the **remote repository** yet.

### VS Code Equivalent

Enter a message in the Source Control message box and select **Commit**. VS Code may ask you to stage changes first if you have not done so.

### GitHub Desktop Equivalent

Enter the message in the **Summary** box and select **Commit to main**.

---

# Part 13: Push the Commit to GitHub

Run:

```bash
git push
```

`git push` uploads commits from your local repository to the remote repository on GitHub.

If Git asks you to authenticate, follow the browser or GitHub sign-in instructions. Do not enter or share your GitHub password in class materials.

Check the status:

```bash
git status
```

You should see that your branch is up to date and the working tree is clean.

### VS Code Equivalent

Open the Source Control **…** menu and choose **Push**, or select **Sync Changes** when appropriate.

### GitHub Desktop Equivalent

Select **Push origin**.

---

# Part 14: Verify Your Work on GitHub

1. Open your `ai-data-science` repository on GitHub.
2. Refresh the browser page.
3. Confirm that `analysis.py` appears.
4. Open `README.md` and confirm that the new text appears.
5. Find the latest commit message: `Add first data analysis program`.

Your work is not fully submitted until you can see it on GitHub.

---

# Part 15: Practice Pulling a Remote Change

This short exercise demonstrates why `git pull` matters.

## Step 1: Edit on GitHub

1. On GitHub, open `README.md`.
2. Select the pencil icon to edit the file.
3. Add this line at the bottom:

```markdown
Created while learning the basic Git workflow.
```

4. Select **Commit changes**.
5. Use the commit message `Update README on GitHub`.
6. Commit directly to the `main` branch.

The remote repository now has a commit that your computer does not have.

## Step 2: Pull the Change

Return to the VS Code terminal and run:

```bash
git pull
```

Open `README.md`. The new sentence should now appear locally.

Check:

```bash
git status
```

The working tree should be clean and your branch should be up to date.

### GitHub Desktop Equivalent

Select **Fetch origin**. If a new commit is available, select **Pull origin**.

> `fetch` checks for remote commits. `pull` downloads and applies them to your current local branch.

---

# Part 16: One Workflow, Three Interfaces

| Task | Git command in VS Code terminal | VS Code Source Control | GitHub Desktop |
|---|---|---|---|
| Check changes | `git status` | View **Changes** | View **Changes** tab |
| Review line changes | `git diff` | Select a changed file | Select a changed file |
| Stage files | `git add <file>` or `git add .` | Select **+** | Check the file |
| Commit | `git commit -m "message"` | Enter message → **Commit** | Enter Summary → **Commit to main** |
| Push | `git push` | **… → Push** | **Push origin** |
| Pull | `git pull` | **… → Pull** | **Fetch origin → Pull origin** |

All three interfaces work with the same repository. During this lesson, use the terminal commands as instructed and use VS Code or GitHub Desktop to visualize what changed.

---

# Part 17: Useful Checking Commands

## Check the Current State

```bash
git status
```

Use this often. It is safe and does not change files.

## Review Unstaged Line Changes

```bash
git diff
```

## Review Staged Line Changes

```bash
git diff --staged
```

## View Recent Commits

```bash
git log --oneline
```

## Confirm the Remote Address

```bash
git remote -v
```

You should see a GitHub address containing your username and `ai-data-science`.

---

# Part 18: Common Problems

## “Not a git repository”

**Cause:** The terminal is in the wrong folder.

**Fix:** Open the cloned `ai-data-science` folder in VS Code, then open a new terminal.

## A Changed File Does Not Appear

**Cause:** The file may not be saved.

**Fix:** Save the file, then run `git status` again.

## “Nothing added to commit”

**Cause:** You did not stage the changes.

**Fix:** Run `git add .`, check with `git status`, and commit again.

## The Commit Is Not Visible on GitHub

**Cause:** A local commit was created but not pushed.

**Fix:** Run `git push`, then refresh GitHub.

## Push Is Rejected Because the Remote Contains New Work

**Cause:** GitHub has a newer commit that is not on your computer.

**Fix:** Save your files and ask your teacher for help. Usually, you must pull the remote changes before pushing. Do not use force push.

## Git Shows the Wrong Name or Email

Check the current values:

```bash
git config --global user.name
git config --global user.email
```

Run the configuration commands again with the correct information.

---

# Part 19: The Safe Daily Routine

## At the Beginning

```bash
git pull
git status
```

## While Working

1. Edit files.
2. Save files.
3. Run `git status` often.
4. Review changes with `git diff` or a visual Changes panel.

## At the End

```bash
git status
git add .
git status
git commit -m "Describe what you changed"
git push
git status
```

Then verify the files and latest commit on GitHub.

> **Pull before you work. Push after you finish. Verify before you submit.**

---

# Part 20: Final Skills Check

Before finishing, confirm that you can answer **yes** to each item:

- [ ] I created the `ai-data-science` repository on GitHub.
- [ ] I configured and verified `user.name` and `user.email`.
- [ ] I cloned the repository with GitHub Desktop.
- [ ] I opened the correct repository folder in VS Code.
- [ ] I used `git status` to check my work.
- [ ] I explained the working folder, staging area, local repository, and remote repository.
- [ ] I created and saved `analysis.py`.
- [ ] I staged files with `git add`.
- [ ] I created a local checkpoint with `git commit`.
- [ ] I uploaded the commit with `git push`.
- [ ] I downloaded a remote change with `git pull`.
- [ ] I verified my files and latest commit on GitHub.
- [ ] I did not upload any passwords, tokens, or private information.

---

# Git Command Cheat Sheet

```bash
# Check that Git is installed.
git --version

# Configure the commit author on this computer.
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# Verify the author information.
git config --global user.name
git config --global user.email

# Download new remote commits before working.
git pull

# Check changed, untracked, and staged files.
git status

# Review unstaged line changes.
git diff

# Stage all current changes.
git add .

# Save a checkpoint in the local repository.
git commit -m "Describe the change"

# Upload local commits to GitHub.
git push

# View a short commit history.
git log --oneline
```

## Final Memory Guide

```text
Pull  = Get the newest commits from GitHub.
Edit  = Change and save files in the working folder.
Check = Use git status and review the changes.
Add   = Select changes for the staging area.
Commit = Save a checkpoint in the local repository.
Push  = Upload local commits to GitHub.
Verify = Confirm the files and commit on GitHub.
```
