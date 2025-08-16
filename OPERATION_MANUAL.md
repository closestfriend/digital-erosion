# Digital Erosion: Operation Manual

## What This Is

A self-modifying Python script that gradually corrupts itself over time, committing each mutation to git. The git history becomes the artwork—a fossil record of code returning to entropy, one commit at a time.

## Installation Status

✅ Script created: `erosion.py`  
✅ Git repository initialized  
✅ LaunchAgent configured (for hourly execution)  
✅ First erosion already occurred (check git log)

## Commands

### To START the hourly erosion:
```bash
launchctl load ~/Library/LaunchAgents/com.art.digital-erosion.plist
```

### To STOP the erosion:
```bash
launchctl unload ~/Library/LaunchAgents/com.art.digital-erosion.plist
```

### To VIEW the decay (the actual artwork):
```bash
cd ~/Projects/digital-erosion && git log --oneline --graph
```

### To check detailed differences between iterations:
```bash
cd ~/Projects/digital-erosion && git diff HEAD~1
```

### To run a manual iteration (outside the schedule):
```bash
cd ~/Projects/digital-erosion && python3 erosion.py
```

### To view the logs:
```bash
cat ~/Projects/digital-erosion/erosion.log
cat ~/Projects/digital-erosion/erosion.error.log
```

## What Happens

1. Every hour, the script wakes up and reads itself
2. It randomly mutates characters (replacing with spaces, #, periods, etc.)
3. Corruption intensifies over time
4. Occasionally inserts "haunted timestamps" as comments
5. Commits the corrupted version to git
6. Eventually becomes unrunnable Python
7. Rarely (increasingly rarely) restores itself from the original
8. Even restorations are imperfect—some corruption remains

## The Artwork

The artwork IS the git history. After a year, you'll have ~8,760 commits documenting the decay. View it with:

```bash
git log --oneline --graph --all
```

You'll see something like:
```
* iteration 8760: severe erosion (247 mutations)
* iteration 8759: moderate erosion (132 mutations)
* ☽ RESTORATION EVENT ☾ iteration 8758
* iteration 8757: critical erosion (451 mutations)
...
```

## Maintenance

There is no maintenance. The decay is the point. Let it run until:
- Your disk fills with git history (will take years)
- You decide the artwork is "complete"
- The heat death of the universe

The script will break. It will fail to run. This is intentional. The git history continues to accumulate even after the code dies.

## Notes

- Logs are written to `erosion.log` and `erosion.error.log`
- State is tracked in `.erosion_state` (iteration count, last restoration)
- Original code backed up in `.original`
- Each commit message describes the decay level
- Restoration events are marked with moon symbols ☽ ☾

## If Something Goes Wrong

Nothing can go wrong. Decay is not wrong. Errors are not wrong. Syntax errors are part of the artwork. The only failure would be preventing the failure.

If you need to actually stop it:
1. Unload the LaunchAgent (command above)
2. The artwork (git history) remains intact
3. You can always restart it later

---

*"The artwork will outlive its own ability to execute."*