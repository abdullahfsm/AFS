import sys
import io
import pickle
import matplotlib.pyplot as plt

colors = ['royalblue', 'red', 'orange']

def plot_show(fig, axes):
    ax_act, ax_qlen, ax_msoj, ax_util = axes
    ax_act.set_ylabel('ACT (hour)')
    ax_act.set_xlabel('Time (day)')
    ax_qlen.set_ylabel('Queue Length')
    ax_qlen.set_xlabel('Time (day)')
    ax_msoj.set_ylabel('Max Sojourn Time (hour)')
    ax_msoj.set_xlabel('Time (day)')
    ax_util.set_ylabel('Cusum of Base CT (hour)')
    ax_util.set_xlabel('Time (day)')

    ax_act.set_ylim(0, 10)
    ax_qlen.set_ylim(0, 40)
    ax_msoj.set_ylim(0, 250)
    # ax_util.set_ylim(0, 100)

    for ax in [ax_act, ax_qlen, ax_msoj]:
        ax.grid(alpha=.3, linestyle='--')
        ax.set_xlim(0, ax.lines[0].get_xdata()[-1])
        for line in ax.lines:
            line.set_linewidth(0.75)
        for i, l in enumerate(ax.lines):
            l.set_color(colors[i])
    for ax in [ax_util]:
        ax.grid(alpha=.3, linestyle='--')
        ax.set_xlim(0, ax.lines[0].get_xdata()[-1])
        for line in ax.lines:
            line.set_linewidth(0.5)
            # line.set_linestyle('-')
            # line.set_marker('.')
            # line.set_markersize(0.7)
        for i, l in enumerate(ax.lines):
            l.set_color(colors[i])
            # l.set_drawstyle('steps-post')
    # ax_act.legend(loc='lower left')
    fig.set_size_inches(9, 2.5)
    plt.subplots_adjust(left=0.06, right=0.99, bottom=0.2, top=0.93, hspace=0.4, wspace=0.37)
    plt.show()

if __name__ == '__main__':
    with io.open(sys.argv[1], 'rb') as f:
        axa, axq, axm, axu = pickle.load(f)

    fig, [ax_act, ax_qlen, ax_msoj, ax_util] = plt.subplots(1, 4, sharex=False)
    for line in axa.lines:
        ax_act.plot(line.get_xydata()[:,0], line.get_xydata()[:,1],
            label=line.get_label())
    for line in axq.lines:
        ax_qlen.plot(line.get_xydata()[:,0], line.get_xydata()[:,1],
            label=line.get_label())
    for line in axm.lines:
        ax_msoj.plot(line.get_xydata()[:,0], line.get_xydata()[:,1],
            label=line.get_label())
    for line in axu.lines:
        ax_util.plot(line.get_xydata()[:,0], line.get_xydata()[:,1],
            label=line.get_label())

    plot_show(fig, (ax_act, ax_qlen, ax_msoj, ax_util))