import sys
import io
import pickle
import matplotlib.pyplot as plt

def plot_show(fig, axes):
    ax_act, ax_qlen, ax_msoj = axes
    ax_act.set_ylabel('ACT (hour)')
    ax_qlen.set_ylabel('Queue Length')
    ax_msoj.set_ylabel('Max Sojourn Time\n(hour)')
    ax_act.set_ylim(0, 0.4)
    for ax in axes:
        ax.grid(alpha=.3, linestyle='--')
        ax.set_xlim(0, ax.lines[0].get_xdata()[-1])
        for line in ax.lines:
            line.set_linewidth(0.75)
    plt.xlabel('Time (day)')
    ax_act.legend(loc='upper left')
    fig.set_size_inches(3, 4.5)
    plt.subplots_adjust(left=0.23, right=0.99, bottom=0.11, top=0.99, hspace=0.15)
    plt.show()

if __name__ == '__main__':
    with io.open(sys.argv[1], 'rb') as f:
        axa, axq, axm = pickle.load(f)

    fig, [ax_act, ax_qlen, ax_msoj] = plt.subplots(3, 1, sharex=True)
    for line in axa.lines:
        ax_act.plot(line.get_xydata()[:,0], line.get_xydata()[:,1],
            label=line.get_label())
    for line in axq.lines:
        ax_qlen.plot(line.get_xydata()[:,0], line.get_xydata()[:,1],
            label=line.get_label())
    for line in axm.lines:
        ax_msoj.plot(line.get_xydata()[:,0], line.get_xydata()[:,1],
            label=line.get_label())

    plot_show(fig, (ax_act, ax_qlen, ax_msoj))