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

# 初始条件和时间点
y0 = [999, 1, 0, 0]  # 初始易感、感染、康复和死亡人数
t = np.linspace(0, 140, 140)  # 时间点

# 分析不同传染率 β 的影响
beta_values = [0.2, 0.3, 0.4]
gamma, mu = 0.1, 0.015

plt.figure()
for beta in beta_values:
    solution = odeint(sird_model, y0, t, args=(beta, gamma, mu))
    S, I, R, D = solution.T
    plt.plot(t, I, label=f'β={beta}')

plt.legend(loc='best')
plt.xlabel('时间', fontsize=12)
plt.ylabel('感染人数 I', fontsize=12)
plt.title('不同传染率 β 对感染人数的影响', fontsize=14)
plt.grid(True)
plt.show()

# 分析不同康复率 γ 的影响
beta, mu = 0.3, 0.015
gamma_values = [0.05, 0.1, 0.15]

plt.figure()
for gamma in gamma_values:
    solution = odeint(sird_model, y0, t, args=(beta, gamma, mu))
    S, I, R, D = solution.T
    plt.plot(t, I, label=f'γ={gamma}')

plt.legend(loc='best')
plt.xlabel('时间', fontsize=12)
plt.ylabel('感染人数 I', fontsize=12)
plt.title('不同康复率 γ 对感染人数的影响', fontsize=14)
plt.grid(True)
plt.show()

# 分析不同死亡率 μ 的影响
beta, gamma = 0.3, 0.1
mu_values = [0.01, 0.015, 0.02]

plt.figure()
for mu in mu_values:
    solution = odeint(sird_model, y0, t, args=(beta, gamma, mu))
    S, I, R, D = solution.T
    plt.plot(t, I, label=f'μ={mu}')

plt.legend(loc='best')
plt.xlabel('时间', fontsize=12)
plt.ylabel('感染人数 I', fontsize=12)
plt.title('不同死亡率 μ 对感染人数的影响', fontsize=14)
plt.grid(True)
plt.show()
