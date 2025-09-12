# Getting familiar with [EnergiBridge](https://github.com/tdurieux/EnergiBridge)

In this exercise, we will start with a simple experiment using **one factor** and **one level**. Later on, we will explore how to run more complex experiments.

The goal here is to demonstrate how `EnergiBridge` can act as a **profiler** within the `experiment-runner` framework. 

For now, we just want to run a single command and observe the results.

## Step 1: Run a Basic Command

Execute the following command:

```bash
energibridge --summary -o test.csv sleep 5
```

This will:

* Run the command `sleep` for 5 seconds
* Record resource usage data
* Save results in `test.csv`

## Step 2: Observe Terminal Output

When the process finishes, you should see a message similar to:

```bash
Energy consumption in joules: 253.86045820617682 for 5.1230927 sec of execution.
```

⚠️ Note: The energy consumption value is **system dependent** and will vary.

## Step 3: Inspect the CSV Output

Open the generated `test.csv` file to view detailed raw EnergiBridge data. Example header format:

```
Delta,Time,CPU_FREQUENCY_0,CPU_FREQUENCY_1,...,SYSTEM_POWER (Watts),TOTAL_MEMORY,TOTAL_SWAP,USED_MEMORY,USED_SWAP
```

Example first two rows:

```
0,1697704464320,0,0,0,0,0,0,0,0,0,0,46.529457092285156,44.31881332397461,43.83422088623047,47.03656005859375,44.67115783691406,43.856910705566406,41.333412170410156,41.268951416015625,44.348262786865234,43.08387756347656,46.37215805053711,45.429779052734375,15.021618843078613,8.819367408752441,5.0954484939575195,3.514699935913086,2.9715969562530518,1.5818228721618652,1.1069598197937012,0.9475208520889282,11.58033275604248,34359738368,0,10188488704,0
104,1697704464321,0,0,0,0,0,0,0,0,0,0,46.529457092285156,44.31881332397461,43.83422088623047,47.03656005859375,44.67115783691406,43.856910705566406,41.333412170410156,41.268951416015625,44.348262786865234,43.08387756347656,46.37215042114258,45.429771423339844,15.021615982055664,8.819366455078125,5.095447063446045,3.514699697494507,2.9715967178344727,1.5818227529525757,1.1069598197937012,0.9475207924842834,11.58033275604248,34359738368,0,10189275136,0
```

---

## 🔎 Optional Exploration

You can run the following examples if you want to see the difference in consumption for tasks with different stress targets.

* **CPU-bound workload**:

```bash
energibridge --summary -o cpu_test.csv -m 5 sha1sum /dev/zero
```

* **Memory-bound workload**:

```bash
energibridge --summary -o mem_test.csv -m 5 python -c "a = [0]*10**7"
```

* **Disk I/O workload**:

```bash
energibridge --summary -o io_test.csv dd if=/dev/zero of=testfile bs=1M count=500
```

### Discussion Points

* Compare energy use across `sleep`, `cpu_test.csv`, `mem_test.csv`, and `io_test.csv`.
* Which workloads consume more CPU energy? Which stress memory or I/O?
* Do CPU frequency and temperature values rise under stress?

### Visualization Task

* Open the generated CSV files in Excel, Python (Pandas/Matplotlib), or use the official [chart.ipynb](https://github.com/tdurieux/EnergiBridge/blob/main/chart.ipynb).
* Plot CPU usage, memory usage, or power consumption over time.
