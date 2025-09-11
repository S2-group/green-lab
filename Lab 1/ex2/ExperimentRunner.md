# Getting Familiar with [Experiment Runner](https://github.com/S2-group/experiment-runner/tree/master)

## Overview

In this exercise, you will learn how to configure and run experiments using **Experiment Runner**. The focus is on understanding:

* The role of `RunnerConfig.py`
* The nine execution stages
* How to define an experiment using `RunTableModel`
* How measurement data is collected and aggregated

By the end, you’ll be able to design your own small experiments and extend them with different factors, treatments, and measurement outputs.

## RunnerConfig.py

`RunnerConfig.py` defines how your experiment should be conducted, including the subjects (programs to run) and the output data to be collected. Based on this configuration, Experiment Runner will:

* Create the experiment folder
* Generate the run table (`.csv`) inside the experiment folder
* Execute the experiment across all defined variations
* Follow **9 execution stages** during the lifecycle of each experiment

## Execution Stages

Execution stages are represented by methods inside the `RunnerConfig` class. They allow you to add setup, cleanup, or measurement actions before, during, and after runs.

### The 9 Stages

* **before\_experiment()**: Runs once before the entire experiment begins. Useful for cleanup, configuring CPU governors, or warming up the machine.

For each run:

* **before\_run()**: Invoked before a run starts.
* **start\_run()**: Marks the beginning of a run.
* **start\_measurement()**: Begins the measurement phase.
* **interact()**: Lets you interact with the target system during a run.
* **stop\_measurement()**: Stops measurements.
* **stop\_run()**: Called once a run finishes.
* **populate\_run\_data()**: Processes results and fills the data columns.

Finally:

* **after\_experiment()**: Runs once after all runs complete. Useful for cleanup and final reporting.

⚠️ *Note: These stages are optional—you don’t need to implement them all for an experiment to run.*


## RunTableModel

The `RunTableModel` specifies:

* **Factors** and their **treatment levels**
* The number of **repetitions**
* Whether runs should be **shuffled**
* Any **excluded combinations** of treatments
* **Data columns** to store results

The definition happens in the `create_run_table_model()` function.

### Example 1: Defining the Run Table

```python
def create_run_table_model(self) -> RunTableModel:
    factor1 = FactorModel("fib_type", ['iter', 'mem', 'rec'])
    factor2 = FactorModel("problem_size", [10, 35, 40, 5000, 10000])
    self.run_table_model = RunTableModel(
        factors=[factor1, factor2],
        exclude_combinations=[
            {factor2: [10]},   # exclude all runs with treatment "10"
            {factor1: ['rec'], factor2: [5000, 10000]}, # exclude ('rec', 5000) and ('rec', 10000)
        ],
        shuffle=True,
        repetitions=10,
        data_columns=["energy", "runtime", "memory"]
    )
    return self.run_table_model
```

This experiment repeats runs **10 times each**, producing **60 total results**. The results are stored in `run_table.csv`, for example:

| \_\_run\_id           | \_\_done | fib\_type | problem\_size | energy | runtime | memory      |
| --------------------- | -------- | --------- | ------------- | ------ | ------- | ----------- |
| run\_0\_repetition\_0 | DONE     | rec       | 40            | 61.3   | 21.9402 | 10778673152 |

---

### Example 2: Measurement Stages

```python
def start_measurement(self, context: RunnerContext) -> None:
    fib_type = context.execute_run["fib_type"]
    problem_size = context.execute_run["problem_size"]

    self.profiler = EnergiBridge(
        target_program=f"python examples/hello-world-fibonacci/fibonacci_{fib_type}.py {problem_size}",
        out_file=context.run_dir / "energibridge.csv"
    )

    self.profiler.start()
```

```python
def populate_run_data(self, context: RunnerContext) -> Optional[Dict[str, Any]]:
    eb_log, eb_summary = self.profiler.parse_log(
        self.profiler.logfile, 
        self.profiler.summary_logfile
    )

    return {
        "energy": list(eb_log["PACKAGE_ENERGY (J)"].values())[-1] - list(eb_log["PACKAGE_ENERGY (J)"].values())[0],
        "runtime": eb_summary["runtime_seconds"],
        "memory": max(eb_log["USED_MEMORY"].values())
    }
```

The final `run_table.csv` combines all repetitions and aggregates results from each `energibridge.csv`. The computation logic follows what’s defined in `populate_run_data()`.

## Run it yourself

* Change factor levels (e.g., add more Fibonacci sizes) and rerun.
* Increase or decrease repetitions to see how result stability changes.
* Add new data columns (e.g., `cpu_temp`) and extend `populate_run_data()`.
* Compare performance between Fibonacci implementations (`iter` vs `mem` vs `rec`).

### Small experiments

1. Predict which Fibonacci type (`iter`, `mem`, or `rec`) performs best at large problem sizes. Run the experiment and check if your prediction holds.
2. Try disabling shuffling—does the order of runs affect performance or stability?
3. Visualize your results (runtime vs. problem size) in a simple plot.


## Notes

* Code snippets are taken from `examples/hello-world-fibonacci/RunnerConfig.py`.
* Explore additional examples in the [examples folder](https://github.com/S2-group/experiment-runner/tree/master/examples) for inspiration.
