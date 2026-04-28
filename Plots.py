import matplotlib.pyplot as plt

error_Q1_7 = [-0.001229, 0.000724, 0.006381, -0.003233, 0.006515, -0.000692, 0.001052, 0.006930]
error_Q1_11 = [0.000236, 0.000236, 0.000034, 0.000673, 0.000655, -0.000204, 0.000564, 0.000583]
error_Q1_15 = [-0.000008, 0.000022, 0.000034, 0.000002, 0.000014, 0.000010, 0.000015, 0.000003]

MSE_Q1_7 = 1.82e-05
MSE_Q1_11 = 2.12e-07
MSE_Q1_15 = 2.76e-10

bits = [7, 11, 15]
mse_values = [MSE_Q1_7, MSE_Q1_11, MSE_Q1_15]
samples = list(range(8))

fig1, ax1 = plt.subplots()

# MSE vs wordlength
ax1.plot(bits, mse_values, marker='o', linestyle='--', color='crimson')
ax1.set_yscale('log')
ax1.set_xlabel('Fractional Bits')
ax1.set_ylabel('MSE (log scale)')
ax1.set_title('MSE vs Wordlength')
ax1.set_xticks(bits)
ax1.grid(True)
plt.tight_layout()

fig2, ax2 = plt.subplots()
# per-sample error
ax2.plot(samples, error_Q1_7,  marker='o', linestyle='-', label='Q1.7', color='steelblue')
ax2.plot(samples, error_Q1_11, marker='s', linestyle='-', label='Q1.11', color='red')
ax2.plot(samples, error_Q1_15, marker='^', linestyle='-', label='Q1.15', color='gold')
ax2.set_xlabel('Sample index')
ax2.set_ylabel('Error')
ax2.set_title('Per-sample Error vs Format')
ax2.legend()
ax2.grid(True)
plt.tight_layout()

plt.show()
