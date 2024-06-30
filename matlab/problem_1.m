function problem_1(beta, gamma, mu, N, ~)
% 杜文霸 2024 选拔考试 题目 1
% 基于 SIR 模型的疫情传播模型

% close all;

% 定义参数

% N = 1000; % 总人口数
% beta = 0.3; % 传染率
% gamma = 0.1; % 康复率
% mu = 0.01; % 死亡率

% 初始化状态

S_0 = N - 1; % 易感人群数
I_0 = 1; % 感染人群数
R_0 = 0; % 康复人群数
D_0 = 0; % 死亡人群数

% 时间范围

t = 0:0.01:150;

% 定义方程

f = @(t, y) [
             -beta * y(1) * y(2) / N; % 易感人数变化
             beta * y(1) * y(2) / N - gamma * y(2) - mu * y(2); % 感染人数变化
             gamma * y(2); % 康复人数变化
             mu * y(2) % 死亡人数变化
             ];

% 解方程

[t, y] = ode45(f, [t(1), t(end)], [S_0, I_0, R_0, D_0]);

% 绘图

% figure;
hold on;

plot(t, y(:, 1),  ...
    'LineWidth', 1.5, 'Color', [0, 114/255, 189/255]);

plot(t, y(:, 2),  ...
    'LineWidth', 1.5, 'Color', [217/255, 83/255, 2/255]);

plot(t, y(:, 3), ...
    'LineWidth', 1.5, 'Color',  [237/255, 177/255, 32/255]);

plot(t, y(:, 4), ...
    'LineWidth', 1.5,'Color', [126/255, 47/255, 14/255]);

% 标注坐标轴

xlabel('时间');
ylabel('人数');
legend('易感人数 S', '感染人数 I', '康复人数 R', '死亡人数 D', ...
    'Location', 'Best');



% 找出感染人数最高的时刻
max_I = max(y(:, 2));
max_I_index = find(y(:, 2) == max_I); % 找到感染人数最高的时刻的索引
max_line = xline(t(max_I_index), 'r--', 'LineWidth', 1.5);
max_line.Annotation.LegendInformation.IconDisplayStyle = 'off'; % 关闭图例中的图标

% 找出感染人数归零的时刻
% zero_I_index = find(y(:, 2) <= 1); % 找到感染人数归零的时刻的索引
% if length(zero_I_index) >= 2
%     zero_line = xline(t(zero_I_index(2)), 'r--', 'LineWidth', 1.5);
%     zero_line.Annotation.LegendInformation.IconDisplayStyle = 'off'; % 关闭图例中的图标
% end

% 标注 beta, gamma, mu 值, 排列整齐
text_x = t(max_I_index);
text_y = max_I;
text(text_x, text_y, ...
    {['\beta = ', num2str(beta)], ...
     ['\gamma = ', num2str(gamma)], ...
     ['\mu = ', num2str(mu)]}, ...
    "FontSize", 12, "FontWeight", "normal", "FontName", "math");

% 更新刻度

currentTicks = xticks;
updatedTicks = sort([currentTicks, floor(t(max_I_index)), ...
                    %  floor(t(zero_I_index(2)))
                     ]...
                     ); 
xticks(updatedTicks);
xticklabels(arrayfun(@num2str, updatedTicks, 'UniformOutput', false));

hold off;

% end