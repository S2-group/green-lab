# Environment Setup Guide

Follow these steps to prepare your environment for running experiments.

## 1. Install [Experiment Runner](https://github.com/S2-group/experiment-runner/tree/master)

Experiment Runner is a framework to automatically execute measurement-based experiments on any platform. Experiments are customizable and defined in Python.

### Steps

1. **Fork & Clone**

   * Fork the repository [here](https://github.com/S2-group/experiment-runner/tree/master).
   * Clone your fork to your local machine.

2. **Install**

   * Ensure you are using **Python ≥ 3.8**.
   * Follow the installation instructions in the [README](https://github.com/S2-group/experiment-runner/tree/master).
   * 💡 *Tip:* Use a virtual environment (`venv` or [Miniconda](https://docs.anaconda.com/miniconda/)) to avoid dependency issues.
        * Run `python3 -m venv venv` in your project directory;
        * Run `source ./venv/bin/activate` to activate the environment;
        * Run `pip install -r ./experiment-runner/requirements.txt`

        * **Note**: Whenever you want to run experiment runner in this case, you must run it from the activated environment.

3. **Run Example**

   * Test the setup by running the Hello World example:

     ```bash
     python experiment-runner/examples/hello-world/RunnerConfig.py
     ```
   * Results will be stored in:

     ```
     examples/hello-world/experiments/new_runner_experiment
     ```
   * ✅ If it runs without errors, your installation is successful.


## 2. Install [EnergiBridge](https://github.com/tdurieux/EnergiBridge)

EnergiBridge is a cross-platform tool to measure energy consumption and resource usage. It supports Linux, Windows, macOS, and multiple CPU architectures.

### Steps

1. **Install**

   * Follow the platform-specific installation instructions from the [EnergiBridge README](https://github.com/tdurieux/EnergiBridge?tab=readme-ov-file#install).

2. **Verify Installation**

   * Run:

     ```bash
     energibridge -h
     ```
   * ✅ If the help message appears, EnergiBridge is installed correctly.


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
