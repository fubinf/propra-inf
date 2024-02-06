import sys

# pandas and matplotlib are not in sedrila's requirements-dev.txt, install them manually
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as mbbp

def plot_progress(df: pd.DataFrame):
    # ----- x data:
    x = pd.to_datetime(df.iloc[:, 0])  # The date is in the first column
    # ----- y data series:
    for i in range(1, len(df.columns)):
        plt.plot(x, df.iloc[:, i], label=df.columns[i])
    # ----- helper lines:
    plt.axhline(y=400, color='darkgreen', linestyle='dotted', linewidth=2, label='Good')
    plt.axhline(y=300, color='darkblue', linestyle='dotted', linewidth=2, label='OK')
    plt.axhline(y=150, color='darkred', linestyle='dotted', linewidth=2, label='Failure')
    plt.plot(pd.to_datetime(['2024-01-01', '2024-03-31']), [0, 400], color='black', linestyle='dashed', linewidth=2)
    # ----- decoration:
    plt.xlabel('date')
    plt.ylabel('timevalue')
    plt.legend()
    plt.grid(True)


inputfile = sys.argv[1]
outputfile = sys.argv[2]  # we do no checking 
df = pd.read_csv(inputfile)
pdf = mbbp.PdfPages(outputfile)
plt.figure(figsize=(15, 6))  # Landscape orientation

plot_progress(df)

pdf.savefig()
plt.close()
pdf.close()