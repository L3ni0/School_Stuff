import matplotlib.pyplot as plt
import numpy as np

def fft(X):
	N = len(X)
	if N == 1:
		return X


	even = fft(np.array(X[0::2]))
	odd = fft(np.array(X[1::2]))


	Y = np.zeros(N, dtype=complex)
	for k in range(0, N//2):
		Y[k] = even[k] + np.exp( -2* 1j * np.pi * k / N) * odd[k]
		Y[N//2 + k] = even[k] - np.exp( -2 * 1j * np.pi * k / N) * odd[k]
	return Y

def mixed_sinus_signal(N, fs , hz, ampl):
	N = np.arange(N)
	Y = np.sum([a*np.sin(2*np.pi * N * freq / fs) for a,freq in zip(ampl,hz)], axis=0)

	return Y

def signal_linspace(fs,n):
	return np.array([(fs/n)*i for i in range(n)])


sygnal = mixed_sinus_signal(2048,48000, [100, 300, 500], [0.5,0.3,0.2])
plt.plot((signal_linspace(48000,2048)),sygnal)
plt.show()

trasformowany = np.fft.fft(sygnal)
plt.plot(signal_linspace(48000,2048),np.abs(trasformowany))

plt.show()
trasformowany = [trasformowany[i] if len(trasformowany)-10 > i > 10 else 0 for i in range(len(trasformowany))]
plt.plot(signal_linspace(48000,2048),np.abs(trasformowany))
plt.show()

trasformowany = np.fft.ifft(trasformowany)
plt.plot((signal_linspace(48000,2048)),np.real(trasformowany))
plt.show()