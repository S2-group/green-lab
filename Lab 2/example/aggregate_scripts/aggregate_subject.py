from AndroidRunner.Plugins.perfetto.trace_wrapper import PerfettoTrace
from perfetto.trace_processor import TraceProcessor
import os

def main(dummy, path):
    for perfetto_trace_file in os.listdir(path):
        tp = TraceProcessor(trace=os.path.join(path, perfetto_trace_file))
        
        # The basic perfetto tables are: slices, counters, and tracks
        data = tp.query("SELECT * FROM counters").as_pandas_dataframe()
        data.to_csv(os.path.join(path, f"{perfetto_trace_file.split(".")[0]}_aggregated.csv"))
