# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:35:17 2020

@author: schrodt@physik.uni-kassel.de
"""
import matplotlib.pyplot as plt


def ageify_axis(ax: plt.Axes):
    """
    Change the look of a given axis to match the AGE group standard.

    The axis will have ticks inside and outside on the lower and left axis.
    The top and right axis will get ticks on the inside only.
    Additionally, the text font will be switched to serif (for publiactions) both in
    normal text mode and math mode.

    Parameters
    ----------
    ax : plt.Axes
        Given axis that should be changed.

    Returns
    -------
    ax : TYPE
        Original axis object.
    ax_top : TYPE
        Created axis object representing the top axis.
    ax_right : TYPE
        Created axis object representing the right axis.
    """
    ax.spines["top"].set_visible(True)
    ax.spines["bottom"].set_visible(True)
    ax.spines["left"].set_visible(True)
    ax.spines["right"].set_visible(True)

    ax_right = ax.twinx()
    ax_top = ax.twiny()

    ax.tick_params(
        # axis="both",
        direction="inout",
        labeltop=False,
        labelright=False,
        bottom=True,
        left=True,
        )

    ax_right.tick_params(
        right=True,
        direction="in",
        labelright=False,
        )

    ax_right.set_ylim(ax.get_ylim())

    ax_top.tick_params(
        top=True,
        direction="in",
        labeltop=False,
        )

    ax_top.set_xlim(ax.get_xlim())

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['mathtext.fontset'] = 'dejavuserif'

    return (ax, ax_top, ax_right)
