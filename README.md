# BallsDex V3 Battle Package

Battle system for **BallsDex V3**. Players battle eachother using their countryballs.

## Commands

| Command | Description |
|---|---|
| `/battle start user` | Starts a battle with another user |
| `/battle add ball` | Adds a single countryball to your battle deck with support for searching for a specific special using the special parameter |
| `/battle remove ball` | Removes a single countryball from your battle deck with support for searching for a specific special using the special parameter |

## Installation

### 1 — Important Notes

**Special buffs are matched by emoji** - Any special whose emoji appears in `SPECIAL_BUFFS` will receive the configured battle buff.

You may change the following in the code to suit your dex better:

- MAXSTATS, ordered as HP, ATK.
- SPECIAL_BUFFS, ordered as HP, ATK.

### 2 — Configure extra.toml

**If the file doesn't exist:** Create a new file `extra.toml` in your `config` folder under the BallsDex directory.

**If you already have other packages installed:** Simply add the following configuration to your existing `extra.toml` file. Each package is defined by a `[[ballsdex.packages]]` section, so you can have multiple packages installed.

Add the following configuration:

```toml
[[ballsdex.packages]]
location = "git+https://github.com/MapsDex-Team/BallsDex-Battle-Pack.git@0.0.1#master"
path = "battle"
enabled = true
```

**Example of multiple packages:**

```toml
# First package
[[ballsdex.packages]]
location = "git+https://github.com/example/other-package.git"
path = "other"
enabled = true

# Collector Package
[[ballsdex.packages]]
location = "git+https://github.com/MapsDex-Team/BallsDex-Battle-Pack.git@0.0.1#master"
path = "battle"
enabled = true
```

### 3 — Rebuild and start the bot

```bash
docker compose build
docker compose up -d
```

This will install the package and start the bot.
