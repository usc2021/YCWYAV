def ramp_arc(n, ds, dsd):
    nn = np.arange(-n/2,n/2)
    h = np.zeros(nn.shape)
    h[int(n/2+1)] = 1/(4*ds**2)
    odd = (nn%2 == 1)
    h[odd] = -1 / (np.pi*dsd*np.sin((nn[odd]*ds/dsd).astype(np.float64)))**2
    #for i in range(1, n+1, 2):
        #h[i] = -1 / (np.pi*dsd*np.sin((nn[i]*ds/dsd).astype(np.float32)))**2
        #h[i]=-1
    return h, nn


def ramLakFilter(sino, ds, dsd, window, extra, npad):
    na, nb = sino.shape
    if not npad:
        npad = 2 ** np.ceil(np.log2(2 * nb - 1))
    npad = npad.astype(int)

    # padding
    tmp = np.zeros([na, npad])
    tmp[:na, :nb] = sino
    sino = tmp

    hn, nn = ramp_arc(npad, ds, dsd)
    Hk = np.real(np.fft.fft(np.fft.fftshift(hn)))
    window = np.ones(npad)
    window = np.fft.fftshift(window)
    Hk *= np.squeeze(window * ds.astype(np.float32))

    sino = np.real(np.fft.ifft(np.fft.fft(sino) * np.tile(Hk, [na, 1])))
    sino = sino[:, :nb + extra]
    sino[:, nb:nb + extra] = 0
    sino = np.expand_dims(sino, axis=0)

    return sino


import numpy as np

n=10
ds=1
dsd=1

h, nn=ramp_arc(n,ds,dsd)
