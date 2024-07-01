import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# SIRD模型


def sird_model(y, t, beta, gamma, mu):
    S, I, R, D = y
    N = S + I + R + D
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I - mu * I
    dRdt = gamma * I
    dDdt = mu * I
    return [dSdt, dIdt, dRdt, dDdt]


# 定义参数字典

beta = [0.2, 0.3, 0.4]
gamma = [0.05, 0.1, 0.15]
mu = [0.01, 0.015, 0.02]

arg_dict = {
    'β': [(i, 0.1, 0.015) for i in beta],
    'γ': [(0.3, i, 0.015) for i in gamma],
    'μ': [(0.3, 0.1, i  ) for i in mu],
}

arg_indxes = {
    'β': 0,
    'γ': 1,
    'μ': 2,
}



def draw_plot(改变的参数):
    mut_args = arg_dict[改变的参数]

    # 初始条件和时间点
    t = np.linspace(0, 140, 140)  # 时间点
    y0 = [999, 1, 0, 0]  # 初始易感、感染、康复和死亡人数

    # 创建四个subplots,分别显示易感者、感染者、康复者、死亡者在不同 β 下的变化曲线
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), tight_layout=True)

    # 绘制不同参数下的 SIRD 模型曲线

    for arg in mut_args:
        solution = odeint(sird_model, y0, t, args=arg)
        # S, I, R, D = solution.T
        for i, Y in enumerate(solution.T):
            axes[i//2, i % 2].plot(t, Y, label=f'{改变的参数} = {arg[arg_indxes[改变的参数]]:.3f}')

    for ax in axes.flatten():
        ax.set_xlabel('时间', fontsize=12)
        ax.grid(True, axis='y')
        ax.legend(loc='best', fontsize=12)

    # 设置子图标题
    axes[0, 0].set_ylabel('易感者数量', fontsize=14)
    axes[0, 1].set_ylabel('感染者数量', fontsize=14)
    axes[1, 0].set_ylabel('康复者数量', fontsize=14)
    axes[1, 1].set_ylabel('死亡者数量', fontsize=14)

    fig.suptitle('SIRD 模型不同 '+改变的参数+'下的变化曲线', fontsize=16)

    # plt.savefig(f'./figures/prob_2_{改变的参数}.png')
    plt.show()


if __name__ == '__main__':
    for i in ['β', 'γ', 'μ']:
        draw_plot(i)
