import numpy as np
import matplotlib.pyplot as plt


def sum_df(self):
    return np.array(
        [
            self.df[col].sum() if col in self.numericals else None
            for col in self.column_names
        ]
    )


def median_df(self):
    return np.array(
        [
            np.median(self.df[col]) if col in self.numericals else None
            for col in self.column_names
        ]
    )


def min_df(self):
    return np.array(
        [
            self.df[col].min() if col in self.numericals else None
            for col in self.column_names
        ]
    )


def max_df(self):
    return np.array(
        [
            self.df[col].max() if col in self.numericals else None
            for col in self.column_names
        ]
    )


def _hist(self, cols=[], bins=None, histtype="bar", color=None, rwidth=0.9):
    """
    bins : int or sequence or str, optional
    histtype : {'bar', 'barstacked', 'step', 'stepfilled'}, optional
    color : color or array_like of colors or None, optional
    rwidth : scalar or None, optional
    """
    if not isinstance(cols, (list,)):
        raise ValueError("The argument cols must be empty or a list")

    def draw_hist(nums):
        fig1, ax1 = plt.subplots()
        ax1.set_title(nums)
        ax1.hist(
            self.df[nums], bins=bins, histtype=histtype, color=color, rwidth=rwidth
        )

    if not cols:
        for nums in self.numericals:
            draw_hist(nums)

    else:
        for nums in cols:
            if nums in self.numericals:
                draw_hist(nums)
            else:
                print(
                    f"Not able to plot the column: {nums} because it's not a numerical feature."
                )


def _boxplot(self, cols=[], vert=True, meanline=False):
    """
    vert : bool, optional (True)
    meanline : bool, optional (False)
    """
    if not isinstance(cols, (list,)):
        raise ValueError("The argument cols must be empty or a list")

    def draw_box(nums):
        fig1, ax1 = plt.subplots()
        ax1.set_title(nums)
        ax1.boxplot(self.df[nums], vert=vert, meanline=meanline)

    if not cols:
        for nums in self.numericals:
            draw_box(nums)

    else:
        for nums in cols:
            if nums in self.numericals:
                draw_box(nums)
            else:
                print(
                    f"Not able to plot the column: {nums} because it's not a numerical feature."
                )
