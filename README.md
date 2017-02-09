# circle-cli

These are a set of tools for interacting with
[CircleCI][https://circleci.com].

## Installation

```sh
$ brew install keith/formulae/circle-cli
```

## Authentication

Add a Circle [API token](https://circleci.com/account/api) to your
`~/.netrc` file. The format looks like this:

```
machine circleci.com
  password YOUR_TOKEN
```

## Usage

This repo has a collection of commands for different uses. Here's the
basic use of each of them. Use `circle COMMAND --help` to see all
available options.

### `artifacts`

Download the artifacts from a specific build number:

```sh
$ circle artifacts --repo keith/circle-cli --number 42
```

### `builds`

List the builds for a repo:

```sh
$ circle builds --repo keith/circle-cli --all --count 5
```

Or for a specific branch:

```sh
$ circle builds --repo keith/circle-cli --branch master
```

### `cancel`

Cancel a specific build (`--repo` can be omitted if your current
directory has remote set):

```sh
$ circle cancel --number 42
```

### `cancel-all`

Cancel all builds on the project:

```sh
$ circle cancel-all
```

Cancel all builds for a specific branch:

```sh
$ circle cancel-all -b master
```

### `clear-cache`

Clear your project's build cache:

```sh
$ circle clear-cache -r keith/circle-cli
```

### `open`

Open the Circle web interface for the project:

```sh
$ circle open
```

Or for a specific branch:

```sh
$ circle open master
```

Or a specific build:

```sh
$ circle open 42
```

### `rebuild`

Restart a circle build:

```sh
$ circle rebuild --number 42
```

Restart a build without cache:

```sh
$ circle rebuild --repo keith/circle-cli --number 42 --no-cache
```

### `watch`

Watch a running build a get notified of its output:

```sh
$ circle watch -n 42
```

Or for the newest build running on a branch:

```sh
$ circle watch -b master
```

### `whoami`

Get current info about your logged in user:

```sh
$ circle whoami
```
