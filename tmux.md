# tmux
tmux kill-session

* Horz Split
* Ctrl + b %

* Vert Split
* Ctrl + b "

* Close Split
* Ctrl + b x

* Switch
* ctrl + b + arrow
* Detach
* ctrl + b + d

* Color
* tmux -2
* Attach session
* tmux a -t [target]
* NAME
* tmux -s [session name]


## Sessions

### New Session

* `tmux new [-s name] [cmd]` (`:new`) - new session

### Switch Session

* `tmux ls` (`:ls`) - list sessions
* `tmux switch [-t name]` (`:switch`) - switches to an existing session
* `tmux as [id] [-t name]` (`:attach`) - attaches to an existing session
* `<C-a>c` (`:detach`) - detach the currently attached session

### Session Management

* `<C-a>s` - list sessions
* `<C-a>$` - name session

### Close Session

* `tmux kill-session [-t name]` (`:kill-session`)

## Windows

### New Window

* `<C-a>c` (`:neww [-n name] [cmd]`) - new window

### Cursor Movement

* `<C-a>[i]` (`:selectw -t [i]`) - go to window `[i]`
* `<C-a>l` - go to last window
* `<C-a>p` - go to previous window
* `<C-a>n` - go to next window

### Window Management

* `<C-a>T` - rename window
* `<C-a>,` - rename window
* `<C-a>w` - list all windows
* `<C-a>f` - find window by name
* `<C-a>.` - move window to another session (promt)
* `:movew` - move window to next unused number

### Close Window

* `<C-a>&` (`:kill-window`) - kill window

## Panes

### New Pane

* (%) `<C-a>|` (`:splitw [-v] [-p width] [-t focus] [cmd]`) - split current pane vertically
* (") `<C-a>s` (`:splitw -h [-p width] [-t focus] [cmd]`) - split current pane horizontally
