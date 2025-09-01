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
    sem0start = '2024-04-01'  # pilot course first-and-only semester
    sem0end = '2024-09-30'
    sem1start = '2025-04-01'  # first regular course first semester
    sem1end = '2025-09-30'
    sem2end = '2026-03-31'
    # plt.axhline(y=400, color='darkgreen', linestyle='dotted', linewidth=2, label='Good')
    # plt.axhline(y=300, color='darkblue', linestyle='dotted', linewidth=2, label='OK')
    plt.plot(pd.to_datetime([sem1start, sem2end]), [400, 400],
                color='darkgreen', linestyle='dotted', linewidth=2, label='Good')
    plt.plot(pd.to_datetime([sem0start, sem2end]), [300, 300],
                color='darkblue', linestyle='dotted', linewidth=2, label='OK')
    plt.plot(pd.to_datetime([sem0start, sem1end]), [150, 150],
                color='darkred', linestyle='dotted', linewidth=2, label='Failure')
    plt.plot(pd.to_datetime(['2024-01-01', '2024-04-01']), [0, 400], 
             color='black', linestyle='dashed', linewidth=2)
    # plt.plot(pd.to_datetime(['2024-04-01', '2024-09-30']), [400, 400], 
    #          color='black', linestyle='dashed', linewidth=2)
    # ----- decoration:
    plt.xlabel('date')
    plt.ylabel('timevalue')
    plt.legend()
    plt.grid(True)


inputfile = sys.argv[1]
outputfile = sys.argv[2]  # we do no checking 
df = pd.read_csv(inputfile)
df['released'] = df['beta'] + df['done']
df['total'] = df['alpha'] + df['released']
pdf = mbbp.PdfPages(outputfile)
plt.figure(figsize=(15, 6))  # Landscape orientation

plot_progress(df, ["alpha", "beta", "done", "released"])

pdf.savefig()
plt.close()
pdf.close()
