# Screen

## Basics

- Start `screen` session and give it a name: `screen -S ScreenTest`
- Detach from current session: `Ctrl-A d`
- List sessions: `screen -ls`
- Re-attach to an existing session: `screen -r <PID>`
- Re-attach session, if necessary detach or create: `screen -dRR ScreenTest`
- Force-exit screen: `Ctrl-A Ctrl-\`
- Kill session: `screen -S ScreenTest -X quit`
- Clean all dead screen sessions: `screen -wipe`
