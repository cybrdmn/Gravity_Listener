# Shell Continued

## Aliases
It can become tiresome typing long commands that involve many flags or verbose options. For this reason, most shells support **aliasing**. A shell alias is a short form for another command that your shell will replace automatically for you.

For instance, an alias in `zsh` has the following structure:

```bash
alias alias_name="command_to_alias arg1 arg2"
```
> **Note:** There is no space around the equal sign `=`, because `alias` is a shell command that takes a single argument.

Aliases have many convenient features:

- **Make shorthands for common flags:**
  ```bash
  alias ll="ls -lh"
  ```

- **Save a lot of typing for common commands:**
  ```bash
  alias gs="git status"
  alias gc="git commit"
  alias v="vim"
  ```

- **Save you from mistyping:**
  ```bash
  alias sl=ls
  ```

- **Overwrite existing commands for better defaults:**
  ```bash
  alias mv="mv -i"       # -i prompts before overwrite
  alias mkdir="mkdir -p" # -p make parent dirs as needed
  alias df="df -h"       # -h prints human readable format
  ```

- **Aliases can be composed:**
  ```bash
  alias la="ls -A"
  alias lla="la -l"
  ```

### Managing Aliases

- **To ignore an alias**, run it prepended with `\`:
  ```bash
  \ls
  ```

- **To disable an alias altogether**, use `unalias`:
  ```bash
  unalias la
  ```

- **To get an alias definition**, just call `alias` with the alias name:
  ```bash
  alias ll
  # Will print ll='ls -lh'
  ```

> **Note:** Aliases do not persist shell sessions by default. To make an alias persistent you need to include it in shell startup files, like `.bashrc` or `.zshrc`.

---

## 🎨 Shell Customization

One of the great advantages of the shell is its high level of customizability. You can tailor your shell environment to fit your workflow, making you more productive and your terminal more informative. Customization is typically done by editing shell startup files.

### Startup Files

When a shell session starts, it reads configuration from specific files. For `bash`, this is often `~/.bashrc` or `~/.bash_profile`. For `zsh`, it's `~/.zshrc`. These files are scripts that run every time you open a new terminal, setting up your environment.

-   `~/.bashrc`: Executed for interactive non-login shells.
-   `~/.bash_profile`: Executed for login shells. Often sources `~/.bashrc`.
-   `~/.zshrc`: The main configuration file for Zsh.

You can edit these files with any text editor, like `nano` or `vim`.

```bash
nano ~/.zshrc
```

### Making Aliases Persistent

As mentioned in the aliases section, to make your aliases available in every shell session, you need to add them to your shell's startup file.

For example, to make the `ll` alias permanent in `zsh`, add this line to your `~/.zshrc` file:

```bash
alias ll="ls -lh"
```

### Customizing the Prompt

You can change the appearance of your shell prompt by modifying the `PS1` environment variable. This allows you to display useful information like the current directory, username, or git branch.

**Example:** A simple custom prompt for `zsh`:
```bash
# In ~/.zshrc
PS1='%n@%m:%~%# '
```
- `%n`: Username
- `%m`: Hostname
- `%~`: Current directory (e.g., `~` for home)
- `%#`: A `%` for normal users, a `#` for root.

Frameworks like "Oh My Zsh" make prompt customization even easier with themes.

### Environment Variables

You can set your own environment variables in the startup files. Use `export` to make the variable available to child processes started from the shell.

```bash
# In ~/.zshrc

# A simple variable
EDITOR="vscode"

# An exported variable that programs can see
export BROWSER="firefox"
```

### Applying Changes

After editing your startup file, you need to apply the changes. You can do this by:
1.  Closing and reopening your terminal.
2.  Using the `source` command to reload the configuration in the current session:

```bash
source ~/.zshrc
```

---

## 🌐 Basic Networking Commands

The shell provides powerful tools for interacting with networks and the internet. These commands are essential for testing connectivity, downloading files, and accessing remote systems.

### `ping`
The `ping` command is used to test the reachability of a host on an Internet Protocol (IP) network. It sends ICMP ECHO_REQUEST packets to the target host and waits for an ICMP ECHO_RESPONSE.

**Usage:**
```bash
ping google.com
```
This will continuously send packets to `google.com`. You can stop it with `Ctrl+C`. To send a specific number of packets, use the `-c` flag:
```bash
ping -c 5 google.com  # Sends 5 packets
```

### `curl`
`curl` is a versatile tool to transfer data from or to a server, using any of the supported protocols (HTTP, FTP, IMAP, etc.). It is often used for testing APIs or downloading content.

**Examples:**
- **Fetch the content of a webpage:**
  ```bash
  curl https://www.example.com
  ```

- **Download a file:**
  ```bash
  curl -O https://www.example.com/file.zip
  ```
  The `-O` flag saves the file with its original name.

- **Make a POST request with JSON data:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/submit
  ```

### `wget`
`wget` is a free utility for non-interactive download of files from the web. It supports HTTP, HTTPS, and FTP protocols, as well as retrieval through HTTP proxies. It can resume aborted downloads, and recursively download websites.

**Examples:**
- **Download a file:**
  ```bash
  wget https://www.example.com/file.zip
  ```

- **Download and save with a different name:**
  ```bash
  wget -O new_name.zip https://www.example.com/file.zip
  ```

- **Recursively download a website (be careful with this):**
  ```bash
  wget --recursive --no-parent https://www.example.com
  ```

### `ssh`
The `ssh` (Secure Shell) command is a protocol used to securely log onto remote systems. It provides a secure channel over an unsecured network in a client-server architecture.

**Usage:**
```bash
ssh username@remote_host
```
For example, to connect to a server with the IP `192.168.1.100` as user `admin`:
```bash
ssh admin@192.168.1.100
```
You can also run commands directly on the remote server:
```bash
ssh username@remote_host "ls -l"
```
---