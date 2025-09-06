# EX 1 - Setup and Run Examples
## Setting Up Your Environment

### 1. [Experiment Runner](https://github.com/S2-group/experiment-runner/tree/master)
Experiment Runner is a generic framework to automatically execute measurement-based experiments on any platform. The experiments are user-defined, can be completely customized, and expressed in python code!

**Step 1:** Fork [the repo](https://github.com/S2-group/experiment-runner/tree/master) and **clone the fork** to your computer.

**Step 2:** Follow the installation instructions [here](https://github.com/S2-group/experiment-runner/tree/master)

**Note**: *It is good practice to use separate virtual envrionments for different (Python) projects. Do this is you find any errors setting up / running **Experiment Runner**. If you have never worked with virtual environments in Python, check [venv](https://docs.python.org/3/library/venv.html) or [miniconda](https://docs.anaconda.com/miniconda/).*

**Step 3:** Check if the example program ran correctly (i.e., no errors), this example serves as an equivalent of a "Hello World" program, run:
```
python experiment-runner/ examples/hello-world/RunnerConfig.py
```

The results are generated in the `examples/hello-world/experiments` folder.

### 2. [EnergiBridge](https://github.com/tdurieux/EnergiBridge)
Energibridge is a cross-platform energy measurement utility that provides support for Linux, Windows, and MacOS, as well as Intel, AMD, and Apple ARM CPU architectures.

**Step 1:** Follow the installation instructions for your platform from the [EnergiBrigde repo](https://github.com/tdurieux/EnergiBridge?tab=readme-ov-file#install).

**Step 2:** Check if EnergiBridge is installed using `energibridge -h`

**Step 3:** Track energy consumption of your first program 
```
energibridge --summary -o test.csv sleep 5
```

## Troubleshooting

- `cargo` error:
```bash
$ cargo build -r
cargo: command not found
```
You problably don't have Rust installed, follow the installation instructions [here](https://www.rust-lang.org/tools/install).

- `energibridge` not found:
```bash
$ energibridge -h
energibridge: command not found
```
`energibridge` is not in your `$PATH`. Navigate to the `EnergiBridge` installation directory and you will find the binary under `target/release`. Add this directory to your path or, alternatively, copy the binary to a directory that is already in your path. 

- `energibridge` permission error:
```bash
$ energibridge sleep 3
thread 'main' panicked at src/cpu/intel.rs:34:85:
called `Result::unwrap()` on an `Err` value: Os { code: 13, kind: PermissionDenied, message: "Permission denied" }
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
`energibridge` is trying to access protected files for which it doesn't have permission. Even though you followed [the setup](https://github.com/tdurieux/EnergiBridge) step by step this can happen dependig on your distro. Fast fix is running it as `sudo`.

**Note**: *When you run `energibridge` as `sudo` your user `$PATH` is not loaded, so either you specify the whole path (e.g. `/path/to/energibridge/target/release/energibridge`) or you copy the binary to a system-wide available path (e.g. `/usr/bin`).*

