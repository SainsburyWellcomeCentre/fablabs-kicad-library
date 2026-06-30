# FabLabs Global KiCAD Library

Welcome — this repository contains the shared KiCAD symbol, footprint and design-block libraries used by FabLabs projects. This README will get you up and running, show how to add the libraries into KiCAD, and explain a simple, beginner-friendly Git workflow for contributing.

The guide is written for Windows users (PowerShell), but the Git and KiCAD steps are the same on macOS or Linux except where noted.

## What you will find in this repo

- `!fablabs-kicad-library.kicad_sym` — symbol library file
- `!fablabs-kicad-library.pretty` — footprint collection
- `!fablabs-kicad-library.kicad_blocks` — design blocks library
- `docs/` — All supporting documentation resources including the images used in this README

If you're new to KiCAD: the symbol library is for schematic symbols, footprints are for PCB land patterns, and design blocks are saved schematic/PCB snippets you can reuse.

## Quick start (summary)

1. Install KiCAD and Git (see full steps below).
2. Clone this repo to a folder you control.
3. Configure a KiCAD library path to point at this repo clone with the name `FABLABS_KICAD_LIBRARY`.
4. Add symbol, footprint and design-block libraries into KiCAD (Preferences → Manage ... Libraries).
5. Contribute by using Git to create a branch at the start of your day, make small commits during the day, keep updated with the main branch, then push your branch.

## Step 1 — Install Required Software

1. Download and install KiCAD for Windows: <https://www.kicad.org/download/windows/>
2. Download and install GitHub Desktop: <https://desktop.github.com/>
   - This gives you a friendly visual interface for Git operations
   - It also installs Git for command-line use if you need it later

When KiCAD opens you should see its main project window (example screenshot in `docs/images/kicad-open.png`).

## Step 2 — Clone this repository

Using GitHub Desktop (recommended for beginners):

1. Open GitHub Desktop
2. Go to File → Clone repository
3. Select URL tab
4. Enter: `https://github.com/SainsburyWellcomeCentre/fablabs-kicad-library.git`
5. Choose where to save it (e.g., `C:/git/SainsburyWellcomeCentre`)
6. Click Clone

Alternative: If you prefer the command line, open PowerShell in your chosen folder and run:

```powershell
git clone https://github.com/SainsburyWellcomeCentre/fablabs-kicad-library.git
```

**Tip:** Pin the folder to Quick Access in File Explorer for fast navigation (screenshot: `docs/images/library-quick-access.png`).

## Step 3 — Configure KiCAD library path

This allows your KiCAD installation to find the libraries inside your clone regardless of where other people place their clones.

1. In KiCAD, go to Preferences → Configure Paths...
2. Click the `+` button.
3. Set `Name` to `FABLABS_KICAD_LIBRARY` and `Path` to the folder where you cloned this repository.
4. Click OK.

Example screenshot: `docs/images/configure-paths.png`.

## Step 4 — Add the symbol, footprint and design-block libraries

Open the following dialogs in KiCAD and add the corresponding files from the repository using the folder button:

- Preferences → Manage Symbol Libraries → Add existing library → select `!fablabs-kicad-library.kicad_sym` (`docs/images/select-symbol-library.png`).
- Preferences → Manage Footprint Libraries → Add existing library → select the `!fablabs-kicad-library.pretty` folder (`docs/images/footprint-library.png`).
- Preferences → Manage Design Blocks Libraries → Add existing library → select `!fablabs-kicad-library.kicad_blocks` (`docs/images/design-blocks-library.png`).

## Step 5 — Keep your copy up-to-date

Before starting work each day, get the latest changes:

Using GitHub Desktop (recommended):

1. Click "Current Branch"
2. Click "Choose a branch to merge into your current branch"
3. Select "main"
4. Click "Merge into current branch"

Alternative using command line:

```powershell
git fetch origin
git pull origin main
```

## Step 6 — Daily Git Workflow with GitHub Desktop

Follow these simple steps to contribute to the library:

1. Start your day by creating a new branch:
   - In GitHub Desktop, click "Branch"
   - Click "New Branch"
   - Name it something descriptive like `add-motor-driver`
   - Click "Create Branch"

2. Make your changes in KiCAD:
   - Add or modify symbols, footprints, or design blocks
   - Save your changes in KiCAD
   - GitHub Desktop will automatically show what changed

3. Commit your changes frequently:
   - In GitHub Desktop, you'll see changed files on the left
   - Write a short description of what you did (e.g., "Add symbol for ABC123")
   - Click "Commit to add-motor-driver"

4. Keep in sync with main:
   - Click the "Current Branch" dropdown
   - Click "Choose a branch to merge into add-motor-driver"
   - Select main
   - Click "Merge into add-motor-driver"

5. Share your changes:
   - Click "Push origin" (or "Publish branch" for first push)

At the end of your day:

1. Make sure all changes are committed and pushed
2. Let a maintainer know your branch is ready to be merged

At the end of the day, your branch should be pushed and ready for merge. Only select team members have permission to merge branches into `main` — they will pull your branch, run any checks, and merge it. If you are one of the authorized maintainers, see the merge checklist below.

## Git quick reference (beginner-friendly)

- `git status` — see what's changed
- `git add <file>` — stage a file for commit
- `git commit -m "message"` — save staged changes
- `git branch` — list branches
- `git checkout -b <name>` — create and switch to a new branch
- `git fetch` — download remote changes (does not change local branches)
- `git pull` — fetch + merge (or use `git pull --rebase`)
- `git push` — upload your commits
- `git log --oneline --graph --decorate` — compact history view

## Handling merge conflicts

1. You tried to rebase or merge and Git reports conflicts. Run:

```powershell
git status
```

2. Open the files with conflict markers in an editor (VS Code shows a helpful UI for resolving conflicts).
3. Edit the file to the final desired content, then:

```powershell
git add <file-with-conflict>
# if rebasing:
git rebase --continue
# if merging:
git commit
```

If you're unsure, ask in the PR comments or ping a maintainer — it's better to ask than to guess.

## How to add a new component

1. Create or verify a footprint in `!fablabs-kicad-library.pretty`.
2. Add a symbol to `!fablabs-kicad-library.kicad_sym` and link it to the footprint.
3. Create a design block showing the symbol + basic connections.
4. Test in a sample schematic and PCB (place the footprint, check footprints' 3D models if available and DRC rule compatibility).
5. Commit small changes with clear messages and push your branch. At the end of the day notify a maintainer that your branch is ready to merge.

Merge checklist for maintainers (end-of-day)

- [ ] Branch is up-to-date with `main` (rebase or merge completed).
- [ ] All new symbols have matching footprints and naming follows conventions.
- [ ] Basic local tests done (part placed in a sample schematic/PCB and DRC run).
- [ ] No unresolved merge conflicts.
- [ ] Commit messages are reasonable and atomic enough to review.

For maintainers using GitHub Desktop to merge:

1. Fetch origin to get latest changes
2. Switch to the branch you want to merge
3. Update branch from main if needed
4. Switch back to main branch
5. Choose Branch → Merge into current branch
6. Select the branch to merge
7. Click "Merge into main"
8. Click "Push origin"

Only authorized maintainers should perform merges into main.

## Troubleshooting

KiCAD issues:

- Can't find library after adding path: confirm `FABLABS_KICAD_LIBRARY` points exactly at the repo root and restart KiCAD.
- Missing footprint in PCB: ensure symbol's footprint field matches a footprint in the `.pretty` folder.

GitHub Desktop issues:

- "Authentication failed": Click Repository → Repository settings → GitHub.com and sign in again
- Can't push changes: Click Fetch origin to get latest updates, then try pushing again
- Branch is behind: Use Current Branch → Choose branch to merge → main to update your branch
- Merge conflicts: Follow the conflict resolution steps above

## Images

Screenshots used in this README live in `docs/images/`. If you update screenshots, keep them in that folder and reference them with relative paths (already used throughout this document).

## License and Code of Conduct

This repository follows the project's main license. If you are contributing, make sure you agree to the repository's license and contribution rules.

## Help and contact

If you get stuck, open an issue on the GitHub repository or ask a maintainer directly. For workflow or merge-related questions, contact one of the authorized maintainers.
