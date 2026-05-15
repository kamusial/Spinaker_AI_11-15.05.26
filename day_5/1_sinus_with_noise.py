import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import random

x = np.arange(-4 * np.pi, 4 * np.pi, 0.2)
y = np.array([np.sin(number) * random.uniform(0.7, 1.3) + random.uniform(-0.1, 0.1) for number in x])

# plt.figure(figsize=(10, 5))
# plt.scatter(x, y, label='sin(x)', color='blue', linewidth=2)
# plt.title('Chart sinus')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)
# plt.xticks(
#     ticks=[-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
#     labels=['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
# )
# plt.show()

# build neural network like yesterday - 10 minutes
model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))
model.add(Dense(20, activation='linear'))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='linear'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(20, activation='linear'))
model.add(Dense(1, activation='linear'))

model.compile(optimizer='rmsprop', loss='mse')
result = model.fit(x, y, epochs=3000)

y_pred = model.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, c='r')
plt.title('Chart sinus')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)  # Oś X
plt.axvline(0, color='black', linewidth=0.5)  # Oś Y
plt.xticks(
    ticks=[-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    labels=['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
)
plt.show()