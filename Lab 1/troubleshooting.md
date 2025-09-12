## 3. Troubleshooting

### Rust / Cargo not found

```bash
$ cargo build -r
cargo: command not found
```

➡️ Install Rust: [rust-lang.org/tools/install](https://www.rust-lang.org/tools/install).

---

### Energibridge command not found (after installation)

```bash
$ energibridge -h
energibridge: command not found
```

This happens because your OS does not know where to find energibridge (yet). To **fix this** you can use one of the following options:


#### Option 1: Add to PATH temporarily

You can run the following command in a shell:
```bash
export PATH=$PATH:<path_to_energibridge_directory>/target/release
```

Works **only for the current shell** session.

#### Option 2: Add to PATH permanently
Append the line to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`):

```bash
echo 'export PATH=$PATH:~/EnergiBridge/target/release' >> ~/.bashrc
source ~/.bashrc
```

After this, energibridge will be available in all new terminal sessions.

#### Option 3 (RECOMMENDED): Copy binary to a system-wide directory
```bash
sudo cp <path_to_energibridge_directory>/target/release/energibridge /usr/local/bin/
```

After this, you can run `energibridge` from anywhere without modifying configs.

Run `energibridge -h` to check that it works.

---

### Permission error

```bash
$ energibridge sleep 3
Permission denied
```

Run with `sudo`:

```bash
sudo /path/to/energibridge sleep 3
```

**Note:** When running with `sudo`, your user `$PATH` is not loaded. Use the **full path** or copy the binary to a system-wide directory.
