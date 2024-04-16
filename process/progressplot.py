"""python process/progressplot.py process/progress.csv process/progressplot.pdf"""
import sys

# pandas and matplotlib are not in sedrila's requirements-dev.txt, install them manually
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as mbbp

def plot_progress(df: pd.DataFrame, columns: list[str]):
    # ----- x data:
    x = pd.to_datetime(df.iloc[:, 0])  # The date is in the first column
    # ----- y data series:
    for col in columns:
        plt.plot(x, df.loc[:, col], label=col)
    # ----- helper lines:
    plt.axhline(y=400, color='darkgreen', linestyle='dotted', linewidth=2, label='Good')
    plt.axhline(y=300, color='darkblue', linestyle='dotted', linewidth=2, label='OK')
    plt.axhline(y=150, color='darkred', linestyle='dotted', linewidth=2, label='Failure')
    plt.plot(pd.to_datetime(['2024-01-01', '2024-04-01']), [0, 400], color='black', linestyle='dashed', linewidth=2)
    plt.plot(pd.to_datetime(['2024-04-01', '2024-05-31']), [400, 400], color='black', linestyle='dashed', linewidth=2)
    # ----- decoration:
    plt.xlabel('date')
    plt.ylabel('timevalue')
    plt.legend()
    plt.grid(True)


inputfile = sys.argv[1]
outputfile = sys.argv[2]  # we do no checking 
df = pd.read_csv(inputfile)
df['total'] = df['alpha'] + df['beta'] + df['done']
pdf = mbbp.PdfPages(outputfile)
plt.figure(figsize=(15, 6))  # Landscape orientation

plot_progress(df, ["alpha", "beta", "done", "total"])

pdf.savefig()
plt.close()
pdf.close()
