# EX 3 - Understand the RunTableModel and `RunnerConfig.py`
## Overview

**The RunTableModel** defines an experiment's measurements with *Factors*, their *Treatment* levels, *exclude certain combinations* of Treatments, number of *repetitions* and add *data columns* for storing aggregated data.

**RunnerConfig.py** is the entrance that passes user-defined configuration to Experiment Runner Controller. Experiment Runner will:
- Validate the config
- Output the config's values as read by Experiment Runner in the console for user validation
- Create the experiment folder
- Create the run table (.csv), and persist it in the experiment folder
- Execute the experiment on a per-variation basis, going over each variation with its specified treatments in the run table.

## Example
Part code of `experiment-runner/examples/hello-world-fibonacci
/RunnerConfig.py`:

```python
def create_run_table_model(self) -> RunTableModel:
    """Create and return the run_table model here. A run_table is a List (rows) of tuples (columns),
    representing each run performed"""
    factor1 = FactorModel("fib_type", ['iter', 'mem', 'rec'])
    factor2 = FactorModel("problem_size", [10, 35, 40, 5000, 10000])
    self.run_table_model = RunTableModel(
        factors=[factor1, factor2],
        exclude_combinations=[
            {factor2: [10]},   # all runs having treatment "10" will be excluded
            {factor1: ['rec'], factor2: [5000, 10000]},
            {factor1: ['mem', 'iter'], factor2: [35, 40]},  # all runs having the combination ("iter", 30) will be excluded
        ],
        repetitions = 10,
        data_columns=["energy", "runtime", "memory"]
    )
    return self.run_table_model

```
It is expected to repeat 10 times, generate 60 experiment results in total, and produce `run_table.csv` in the following format (this example was produced on Mac, energy in Watts):

|__run_id | __done | fib_type | problem_size | energy | runtime | memory|
| ------------- | ------------- |-------------| ------------- | ------------- |-------------|-------------|
|run_0_repetition_0 | DONE | rec | 40 | 61.3 | 21.9402 | 10778673152|

Check `experiment-runner/examples/hello-world-fibonacci/experiments/new_runner_experiment/` and explore more details.
